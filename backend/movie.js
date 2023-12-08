const dbConnection = require('./database.js');

exports.movie = async (req, res) => {
    console.log("call to /movie...");

    try {
        const { movieid, userid } = req.query;

        if (!movieid || !userid) {
            return res.status(400).json({
                message: "Missing required fields: movieid, userid.",
                data: -1
            });
        }

        // Query to get movie information
        const movieQuery = "SELECT * FROM Movie WHERE MovieID = ?";
        dbConnection.query(movieQuery, [movieid], async (err, movieResult) => {
            if (err) {
                console.log("**ERROR:", err.message);
                return res.status(500).json({
                    message: "Error querying movie information.",
                    data: -1
                });
            }

            if (movieResult.length === 0) {
                return res.status(404).json({
                    message: "Movie not found.",
                    data: -1
                });
            }

            // Query to get top ten reviews for the movie, including usernames and movie titles
            const reviewsQuery = `
                SELECT R.*, U.Username, M.Title
                FROM Review R
                JOIN User U ON R.UserID = U.UserID
                JOIN Movie M ON R.MovieID = M.MovieID
                WHERE R.MovieID = ? 
                ORDER BY R.Rating DESC 
                LIMIT 10;
            `;
            const reviews = await new Promise((resolve, reject) => {
                dbConnection.query(reviewsQuery, [movieid], (err, reviewsResult) => {
                    if (err) {
                        reject(err);
                    } else {
                        resolve(reviewsResult);
                    }
                });
            });

            // Check if the movie is a favorite of the user
            const favoriteQuery = "SELECT * FROM FavoriteMovies WHERE UserID = ? AND MovieID = ?";
            const isFavorite = await new Promise((resolve, reject) => {
                dbConnection.query(favoriteQuery, [userid, movieid], (err, favoriteResult) => {
                    if (err) {
                        reject(err);
                    } else {
                        resolve(favoriteResult.length > 0);
                    }
                });
            });

            // Check if the user has liked any of the reviews
            let likedReviews = new Set();
            for (let review of reviews) {
                const likeQuery = "SELECT * FROM Likes WHERE UserID = ? AND ReviewID = ?";
                const liked = await new Promise((resolve, reject) => {
                    dbConnection.query(likeQuery, [userid, review.ReviewID], (err, likeResult) => {
                        if (err) {
                            reject(err);
                        } else {
                            resolve(likeResult.length > 0);
                        }
                    });
                });

                if (liked) {
                    likedReviews.add(review.ReviewID);
                }
            }

            // Respond with movie info, reviews (including usernames and movie titles), favorite status, and liked reviews
            return res.json({
                message: "Movie data retrieved successfully.",
                data: {
                    movieInfo: movieResult[0],
                    reviews: reviews,
                    isFavorite: isFavorite,
                    likedReviews: Array.from(likedReviews)
                }
            });
        });
    } catch (err) {
        console.log("**ERROR:", err.message);
        res.status(500).json({
            message: "Internal server error",
            data: -1
        });
    }
};
