const dbConnection = require('./database.js')

exports.my_review = async (req, res) => {

    console.log("call to /my_review...");

    try {

        var userid = parseInt(req.query.userid);
        console.log(userid)
        var params = [userid];

        var rds_response_1 = new Promise((resolve, reject) => {
            try {
                console.log("/stats: calling RDS...");
                var sql = "Select Review.*, Movie.*, User.Username from Review join Movie join User on Movie.MovieID = Review.MovieID and Review.UserID = User.UserID where Review.UserID = ?;";
                dbConnection.query(sql, params, (err, results, _) => {
                    try {
                        if (err) {
                            reject(err);
                            return;
                        }
                        console.log("/stats query done");
                        resolve(results);
                    } catch (code_err) {
                        reject(code_err);
                    }
                });
            } catch (code_err) {
                reject(code_err);
            }
        });

        var rows = await rds_response_1;

        if (rows.length == 0) {
            res.json({
                "message": "no review yet",
                "data": []
            });
            return;
        } else {
            res.json({
                "message": "success",
                "data": rows
            });
        }
            // for (row of rows){
            //
            //     bucket_key = row.ImageURL;
            //
            //     const command = new GetObjectCommand({
            //         Bucket: s3_bucket_name,
            //         Key: bucket_key,
            //     });
            //
            //     try {
            //         const s3_response = await s3.send(command);
            //         var datastr = await s3_response.Body.transformToString("base64");
            //         // The Body object also has 'transformToByteArray' and 'transformToWebStream' methods.
            //         row[ImageURL] =datastr;
            //
            //     } catch (err) {
            //         console.error(err);
            //     }
            // }






    }//try
    catch (err) {
        console.log("**ERROR:", err.message);

        res.status(400).json({
            "message": err.message,
            "data": -1
        });
    }//catch

}//put