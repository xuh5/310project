const dbConnection = require('./database.js')

exports.favorite_movie = async (req, res) => {

    console.log("call to /favorite_movie...");

    try {


    }//try
    catch (err) {
        console.log("**ERROR:", err.message);

        res.status(400).json({
            "message": "some sort of error message",
            "favoriteId": -1
        });
    }//catch

}//put