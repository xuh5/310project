const dbConnection = require('./database.js');

exports.search_film = async (req, res) => {
    console.log("call to /search_film...");

    try {
        const { name, genre, rate, reviewQuantity, year, language } = req.query;

        let query = "SELECT * FROM Movie WHERE ";
        const conditions = [];
        const params = [];

        if (name) {
            conditions.push("Title LIKE ? ");
            params.push('%${name}%');
        }

        if (genre) {
            conditions.push("Genre = ?");
            params.push(genre);
        }

        if (rate) {
            conditions.push("AverageRate >= ?");
            params.push(rate);
        }

        if (reviewQuantity) {
            conditions.push("ReviewQuantity >= ?");
            params.push(reviewQuantity);
        }

        if (year) {
            conditions.push("ReleaseYear = ?");
            params.push(year);
        }

        if (language) {
            conditions.push("Language = ?");
            params.push(language);
        }

        if (conditions.length === 0) {
            return res.status(400).json({
                message: "No search criteria provided",
                data: -1
            });
        }

        query += conditions.join(" AND ");

        dbConnection.query(query, params, (err, results) => {
            if (err) {
                console.log("**ERROR:", err.message);
                return res.status(500).json({
                    message: "Error executing search query",
                    data: -1
                });
            }

            return res.json({
                message: "success",
                data: results
            });
        });
    } catch (err) {
        console.log("**ERROR:", err.message);
        res.status(500).json({
            message: "Internal server error",
            data: -1
        });
    }
};
