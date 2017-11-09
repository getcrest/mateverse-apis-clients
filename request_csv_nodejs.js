/**
* NodeJS code
*/

// Load 'request' module
var request = require("request");

// Specify options like method, url and form data like model_id, api_secret and values
// Values should be a valid json string. Use JSON.stringify() to convert a javascript object to a string
//
var options = {
    method: 'POST',
    url: 'https://mateverse.com/v1/predict/',

    form:
        { model_id: ****, // integer
          api_secret: '****************************', // string
          values: JSON.stringify([{
                    "column_name": "******", // string
                    "column_value": **** // integer/string/boolean/float
                    },
                    {
                    "column_name": "******", // string
                    "column_value": **** // integer/string/boolean/float
                    },
                    {
                    "column_name": "******", // string
                    "column_value": **** // integer/string/boolean/float
                    },
                    {
                    "column_name": "******", // string
                    "column_value": **** // integer/string/boolean/float
                    },
                    ..... // Add more columns
          ])
        }
};

// Make a request and print the output in the console
request(options, function (error, response, body) {
    if (error) throw new Error(error);
    console.log(body);
});