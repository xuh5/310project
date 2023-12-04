const dbConnection = require('./database.js')

exports.favorite_movie = async (req, res) => {

    console.log("call to /favorite_movie...");

    try {

        const { userid, movieid } = req.body;

        var insert_sql = "INSERT INTO FavoriteMovies (UserID, MovieID) VALUES (?, ?)";
        var insert_params = [userid, movieid];
        dbConnection.query(insert_sql, insert_params, (err, rows) => {
            if (err) {
                res.status(400).json({
                    "message": err,
                    "favoriteId": -1
                });
                return;
            }
            // send response in JSON format:
            console.log("sending response");
            var favoriteid = rows.insertId;
            res.json({
                "message": "success",
                "favoriteId": favoriteid
            });
        });
        return;


    }//try
    catch (err) {
        console.log("**ERROR:", err.message);

        res.status(400).json({
            "message": "some sort of error message",
            "favoriteId": -1
        });
    }//catch

}//put