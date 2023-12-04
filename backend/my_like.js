const dbConnection = require('./database.js')

exports.my_like = async (req, res) => {

    console.log("call to /my_like...");

    try {

        var userid = parseInt(req.query.userid);
        var params = [userid];

        var rds_response = new Promise((resolve, reject) => {
            try {
                console.log("/stats: calling RDS...");
                var sql = "Select * from Likes join Review on Likes.ReviewID = Review.ReviewID where Likes.UserID = ?;";
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
                "message": "no review yet",
                "data": []
            });
            return;
        } else {
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