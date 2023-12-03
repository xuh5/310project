const dbConnection = require('./database.js')

exports.like_review = async (req, res) => {

    console.log("call to /like_review...");

    try {


    }//try
    catch (err) {
        console.log("**ERROR:", err.message);

        res.status(400).json({
            "message": "some sort of error message",
            "likeId": -1
        });
    }//catch

}//put