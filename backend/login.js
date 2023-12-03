const dbConnection = require('./database.js')

exports.login = async (req, res) => {

    console.log("call to /login...");

    try {


    }//try
    catch (err) {
        console.log("**ERROR:", err.message);

        res.status(400).json({
            "message": "some sort of error message",
            "status": -1
        });
    }//catch

}//put