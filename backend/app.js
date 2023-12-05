//
// Express js (and node.js) web service that interacts with 
// AWS S3 and RDS to provide clients data for building a 
// simple photo application for photo storage and viewing.
//
// Project 02 for CS 310
//
// Authors:
//  Xiaoli Yu
//  Prof. Joe Hummel (initial template)
//  Northwestern University
//  CS 310
//
// References:
// Node.js: 
//   https://nodejs.org/
// Express: 
//   https://expressjs.com/
// MySQL: 
//   https://expressjs.com/en/guide/database-integration.html#mysql
//   https://github.com/mysqljs/mysql
// AWS SDK with JS:
//   https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/index.html
//   https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/getting-started-nodejs.html
//   https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-s3/
//   https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/javascript_s3_code_examples.html
//

const express = require('express');
const app = express();
const config = require('./config.js');

const dbConnection = require('./database.js')
const { HeadBucketCommand, ListObjectsV2Command } = require('@aws-sdk/client-s3');
const { s3, s3_bucket_name, s3_region_name } = require('./aws.js');

app.use(express.json({ strict: false, limit: "50mb"}));

var startTime;

app.listen(config.service_port, () => {
  startTime = Date.now();
  console.log('web service running...');
  //
  // Configure AWS to use our config file:
  //
  process.env.AWS_SHARED_CREDENTIALS_FILE = config.movieapp_config;
});

app.get('/', (req, res) => {

  var uptime = Math.round((Date.now() - startTime) / 1000);

  res.json({
    "status": "running",
    "uptime-in-secs": uptime,
    "dbConnection": dbConnection.state
  });
});

//
// service functions:
//
var stats = require('./api_stats.js');
var user = require('./add_user.js');
var login = require('./login.js')
var search = require('./search_film.js')
var review = require('./add_review.js')
var movie = require('./movie.js')
var like_review = require('./like_review.js')
var unlike_review = require('./unlike_review.js')
var favorite_movie = require('./favorite_movie.js')
var infavorite_movie = require('./infavorite_movie.js')
var my_favorite = require('./my_favorite.js')
var my_like = require('./my_like.js')
var my_review = require('./my_review.js')

app.get('/stats', stats.get_stats);  //app.get('/stats', (req, res) => {...});
app.put('/add_user', user.add_user);  //app.get('/users', (req, res) => {...});
app.get('/login', login.login);
app.get('/search_film', search.search_film);
app.post('/add_review', review.add_review);
app.get('/movie', movie.movie);
app.post('/like_review', like_review.like_review);
app.post('/unlike_review', unlike_review.unlike_review);
app.post('/favorite_movie', favorite_movie.favorite_movie);
app.post('/infavorite_movie', infavorite_movie.infavorite_movie);
app.get('/my_favorite', my_favorite.my_favorite);
app.get('/my_like', my_like.my_like);
app.get('/my_review', my_review.my_review);