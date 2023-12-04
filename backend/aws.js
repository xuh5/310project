//
// AWS.js
//
// Exports 
// s3: an S3Client object
// s3_bucket_name: our S3 bucket
// s3_region_name: the AWS region where our bucket resides
//

const { S3Client } = require('@aws-sdk/client-s3');
const { fromIni } = require('@aws-sdk/credential-providers');

const fs = require('fs');
const ini = require('ini');

const config = require('./config.js');

const movieapp_config = ini.parse(fs.readFileSync(config.movieapp_config, 'utf-8'));
const s3_region_name = movieapp_config.s3readonly.region_name;
const s3_bucket_name = movieapp_config.s3.bucket_name;

//
// create s3 object for communicating with S3 service, but
// this does not open the connection:
//
let s3 = new S3Client({
  region: s3_region_name,
  credentials: fromIni({ profile: config.movieapp_profile })
});

module.exports = { s3, s3_bucket_name, s3_region_name };
