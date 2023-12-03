const dbConnection = require('./database.js')

exports.add_user = async (req, res) => {

  console.log("call to /add_user...");

  try {


  }//try
  catch (err) {
    console.log("**ERROR:", err.message);

    res.status(400).json({
      "message": "some sort of error message",
      "userid": -1
    });
  }//catch

}//put