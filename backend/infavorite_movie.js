const dbConnection = require('./database.js')

exports.infavorite_movie = async (req, res) => {

    console.log("call to /infavorite_movie...");

    try {
        const { userid, movieid } = req.body;

        var delete_sql = "delete from FavoriteMovies where UserID = ? and MovieID = ?";
        var delete_params = [userid, movieid];
        dbConnection.query(delete_sql, delete_params, (err, rows) => {
            if (err) {
                res.status(400).json({
                    "message": err
                });
                return;
            }
            // send response in JSON format:
            console.log("sending response");
            res.json({
                "message": "success"
            });
        });
        return;

    }//try
    catch (err) {
        console.log("**ERROR:", err.message);

        res.status(400).json({
            "message": err.message
        });
    }//catch

}//put