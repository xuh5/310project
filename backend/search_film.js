const dbConnection = require('./database.js')

exports.search_film = async (req, res) => {

    console.log("call to /search_film...");

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