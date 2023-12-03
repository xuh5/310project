const dbConnection = require('./database.js')

exports.infavorite_movie = async (req, res) => {

    console.log("call to /infavorite_movie...");

    try {


    }//try
    catch (err) {
        console.log("**ERROR:", err.message);

        res.status(400).json({
            "message": "some sort of error message"
        });
    }//catch

}//put