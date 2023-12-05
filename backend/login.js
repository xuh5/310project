const dbConnection = require('./database.js');

exports.login = async (req, res) => {
    console.log("call to /login...");

    try {
        const { userid, password } = req.query;

        if (!userid || !password) {
            return res.status(400).json({
                message: "Missing required fields: userid and password.",
                status: -1
            });
        }

        const userQuery = "SELECT * FROM User WHERE UserID = ?";
        dbConnection.query(userQuery, [userid], (err, users) => {
            if (err) {
                console.log("**ERROR:", err.message);
                return res.status(500).json({
                    message: "Error querying user.",
                    status: -1
                });
            }

            if (users.length === 0) {
                return res.status(404).json({
                    message: "User not found.",
                    status: -1
                });
            }

            const user = users[0];
            if (password === user.Password) {
                return res.json({
                    message: "Login successful.",
                    status: 1
                });
            } else {
                return res.status(401).json({
                    message: "Incorrect password.",
                    status: -1
                });
            }
        });
    } catch (err) {
        console.log("**ERROR:", err.message);
        res.status(500).json({
            message: "Internal server error",
            status: -1
        });
    }
};
