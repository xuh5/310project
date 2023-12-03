const dbConnection = require('./database.js')

exports.add_review = async (req, res) => {

    console.log("call to /add_review...");

    try {


    }//try
    catch (err) {
        console.log("**ERROR:", err.message);

        res.status(400).json({
            "message": "some sort of error message",
            "rateId": -1,
            "reviewId": -1,
            "imageId": -1,
            "newRate": -1,
            "newReview": -1
        });
    }//catch

}//put