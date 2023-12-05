const dbConnection = require('./database.js')

exports.add_user = async (req, res) => {

  console.log("call to /add_user...");

  try {
    // Extract data from the request body
    const { username, email, password } = req.body;

    console.log(username);
    console.log(email);
    console.log(password);
    let profilePictureURL = "";

    // Validate the required fields
    if (!username || !email || !password) {
      return res.status(400).json({
        message: "Missing required fields (username, email, password).",
        userid: -1,
      });
    }

    // Check if the user already exists based on email
    let query = "SELECT userid FROM User WHERE email = ?";
    dbConnection.query(query, [email], (err, result) => {
      if (err) {
        console.log("**ERROR:", err.message);
        return res.status(500).json({
          message: err.message,
          userid: -1,
        });
      }

      if (result.length > 0) { // User exists
        return res.status(409).json({
          message: "User already exists with the given email.",
          userid: -1,
        });
      } else { // User doesn't exist, insert new user
        query = "INSERT INTO User (Username, Email, Password, DateJoined, ProfilePictureURL) VALUES (?, ?, ?, NOW(), ?)";
        dbConnection.query(query, [username, email, password, profilePictureURL], (err, insertResult) => {
          if (err) {
            console.log("**ERROR:", err.message);
            return res.status(500).json({
              message: err.message,
              userid: -1,
            });
          }

          if (insertResult.affectedRows == 1) {
            return res.json({
              message: "User successfully added.",
              userid: insertResult.insertId,
            });
          } else {
            return res.status(400).json({
              message: "Failed to insert new user.",
              userid: -1,
            });
          }
        });
      }
    });


  }//try
  catch (err) {
    console.log("**ERROR:", err.message);

    res.status(400).json({
      "message": "some sort of error message",
      "userid": -1
    });
  }//catch

}//put