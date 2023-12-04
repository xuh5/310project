//
// database.js
//
// Exports 
// dbConnection: connection object to our MySQL database in AWS RDS
//

const mysql = require('mysql');
const fs = require('fs');
const ini = require('ini');

const config = require('./config.js');

const movieapp_config = ini.parse(fs.readFileSync(config.movieapp_config, 'utf-8'));
const endpoint = movieapp_config.rds.endpoint;
const port_number = movieapp_config.rds.port_number;
const user_name = movieapp_config.rds.user_name;
const user_pwd = movieapp_config.rds.user_pwd;
const db_name = movieapp_config.rds.db_name;

//
// creates connection object, but doesn't open connnection:
//
let dbConnection = mysql.createConnection(
  {
    host: endpoint,
    port: port_number,
    user: user_name,
    password: user_pwd,
    database: db_name,
    multipleStatements: true  // allow multiple queries in one call
  }
);

module.exports = dbConnection;
