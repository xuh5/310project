const dbConnection = require('./database.js');
const { PutObjectCommand } = require('@aws-sdk/client-s3');
const { s3, s3_bucket_name } = require('./aws.js');
const uuid = require('uuid');

exports.add_review = async (req, res) => {
    console.log("call to /add_review...");

    try {
        const { userid, movieid, rate, reviewContent, image } = req.body;

        if (!userid || !movieid || !rate || !reviewContent) {
            return res.status(400).json({
                message: "Missing required fields (userid, movieid, rate, reviewContent).",
                reviewId: -1,
                newRate: -1,
                newReview: -1
            });
        }

        // If image data is present, process it
        let imageURL = '';
        if (image) {
            // Convert base64 to binary
            const buffer = Buffer.from(image, 'base64');
            const uniqueKey = uuid.v4(); // Generate unique key
            const s3Params = {
                Bucket: s3_bucket_name,
                Key: `reviews/${uniqueKey}.jpg`,
                Body: buffer
            };

            await s3.send(new PutObjectCommand(s3Params));
            imageURL = `https://${s3_bucket_name}.s3.amazonaws.com/reviews/${uniqueKey}.jpg`;
        }

        // Insert review into the database
        const insertReviewQuery = "INSERT INTO Review (UserID, MovieID, Rating, ReviewText, ReviewDate, ImageURL) VALUES (?, ?, ?, ?, NOW(), ?)";
        dbConnection.query(insertReviewQuery, [userid, movieid, rate, reviewContent, imageURL], async (err, insertResult) => {
            if (err) {
                console.log("**ERROR:", err.message);
                return res.status(500).json({
                    message: "Error inserting review.",
                    reviewId: -1,
                    newRate: -1,
                    newReview: -1
                });
            }

            // Update the average rating and review quantity for the movie
            const updateMovieQuery = `
                UPDATE Movie
                SET AverageRate = (SELECT AVG(Rating) FROM Review WHERE MovieID = ?),
                    ReviewQuantity = (SELECT COUNT(*) FROM Review WHERE MovieID = ?)
                WHERE MovieID = ?;
            `;
            dbConnection.query(updateMovieQuery, [movieid, movieid, movieid], (err, updateResult) => {
                if (err) {
                    console.log("**ERROR:", err.message);
                    return res.status(500).json({
                        message: "Error updating movie rating and review quantity.",
                        reviewId: -1,
                        newRate: -1,
                        newReview: -1
                    });
                }

                // Fetch the new average rate and review quantity
                const fetchUpdatedMovieQuery = "SELECT AverageRate, ReviewQuantity FROM Movie WHERE MovieID = ?";
                dbConnection.query(fetchUpdatedMovieQuery, [movieid], (err, movieResult) => {
                    if (err || movieResult.length === 0) {
                        console.log("**ERROR:", err ? err.message : "Movie not found");
                        return res.status(500).json({
                            message: "Error fetching updated movie data.",
                            reviewId: -1,
                            newRate: -1,
                            newReview: -1
                        });
                    }

                    // Respond with the new data
                    return res.json({
                        message: "Review successfully added.",
                        reviewId: insertResult.insertId,
                        newRate: movieResult[0].AverageRate,
                        newReview: movieResult[0].ReviewQuantity
                    });
                });
            });
        });

    } catch (err) {
        console.log("**ERROR:", err.message);
        res.status(500).json({
            message: "Internal server error",
            reviewId: -1,
            newRate: -1,
            newReview: -1
        });
    }
};
