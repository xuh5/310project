const dbConnection = require('./database.js');

exports.like_review = async (req, res) => {
    console.log("call to /like_review...");

    try {
        const { userid, reviewid } = req.body;

        if (!userid || !reviewid) {
            return res.status(400).json({
                message: "Missing required fields (userid, reviewid).",
                likeId: -1
            });
        }

        const insertQuery = "INSERT INTO Likes (ReviewID, UserID, LikeDate) VALUES (?, ?, NOW())";
        dbConnection.query(insertQuery, [reviewid, userid], (err, result) => {
            if (err) {
                console.log("**ERROR:", err.message);
                return res.status(500).json({
                    message: "Error adding like to review.",
                    likeId: -1
                });
            }

            return res.json({
                message: "Review liked successfully.",
                likeId: result.insertId
            });
        });
    } catch (err) {
        console.log("**ERROR:", err.message);
        res.status(500).json({
            message: "Internal server error",
            likeId: -1
        });
    }
};
