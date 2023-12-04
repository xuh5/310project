const dbConnection = require('./database.js')

exports.my_favorite = async (req, res) => {

    console.log("call to /my_favorite...");

    try {

        var userid = parseInt(req.query.userid);
        var params = [userid];

        var rds_response = new Promise((resolve, reject) => {
            try {
                console.log("/stats: calling RDS...");
                var sql = "Select * from FavoriteMovies join Movie on FavoriteMovies.MovieID = Movie.MovieID where FavoriteMovies.UserID = ?;";
                dbConnection.query(sql, params, (err, results, _) => {
                    try {
                        if (err) {
                            reject(err);
                            return;
                        }
                        console.log("/stats query done");
                        resolve(results);
                    }
                    catch (code_err) {
                        reject(code_err);
                    }
                });
            }
            catch (code_err) {
                reject(code_err);
            }
        });

        var rows = await rds_response;

        if(rows.length == 0){
            res.json({
                "message": "no favorite movies yet",
                "data": []
            });
            return;
        } else {
            res.json({
                "message": "success",
                "data": rows
            });
        }


    }//try
    catch (err) {
        console.log("**ERROR:", err.message);

        res.status(400).json({
            "message": err.message,
            "data": -1
        });
    }//catch

}//put