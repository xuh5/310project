const dbConnection = require('./database.js')

exports.my_favorite = async (req, res) => {

    console.log("call to /my_favorite...");

    try {


    }//try
    catch (err) {
        console.log("**ERROR:", err.message);

        res.status(400).json({
            "message": "some sort of error message",
            "data": -1
        });
    }//catch

}//put