//
// config.js
//
// Web service configuration parameters, separate
// from our photoapp-config file that contains 
// AWS-specific configuration information.
//

const config = {
  movieapp_config: "movieapp-config.ini",
  movieapp_profile: "s3readwrite",
  service_port: 8080,
  page_size: 12
};

module.exports = config;
