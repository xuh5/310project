const dbConnection = require('./database.js')

exports.unlike_review = async (req, res) => {

    console.log("call to /unlike_review...");

    try {
        const { userid, reviewid } = req.body;

        var delete_sql = "delete from Likes where UserID = ? and ReviewID = ?";
        var delete_params = [userid, reviewid];
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