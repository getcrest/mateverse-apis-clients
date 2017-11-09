# Mateverse APIs Clients
Mateverse APIs Clients(Python, NodeJS)

https://www.mateverse.com/
http://www.matelabs.in

## Introduction

The Mateverse APIs call will return you the 'confidence score'/'accuracy score' of your 'image files'/text/'text files'/'csv values' that are trained on a particular model of your choice. When you make a prediction through the API, you pass in the 'image file'/url or 'text file'/text or 'csv values' and tell it which model to use, authenticating the API call with your api_secret key and model_id


## Usage

In request.py you need to pass in the following parameters to make the API work:

#### api_secret key
The api_secret key serves as the authentication key to the API call. Just copy-paste your api_secret key in request.py and you are good to go.

#### model_id
The model_id is to tell the API which model to use for your prediction.

#### file_paths - Path to your images/text files
You need to give the path to the images/text files which will go inside a list. You can pass in the path to as much images/text files as you want.

    Examples:

    If using an images model
    ['images/image1.jpg', 'images/image2.jpg']

    If using a text model
    ['text/text1.txt', 'text/text2.txt']

#### image_url(Optional) - Url to a publicly accessible image
Provide an url of a publicly accessible image. This is an optional parameter.

    Example:
    https://c1.staticflickr.com/1/155/354864230_a8fe1fe864.jpg

#### text_sample(Optional) - Sample text. Can be a word or a sentence or a paragraph
Provide a text sample which you want to use for the prediction. This is an optional parameter.

    Example:
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque finibus neque tortor, non lobortis nibh tempor id"

#### values - When you use a csv model
Provide a valid json string containing all column names and column values.

    Example:
    "[{\"column_value\": ***, \"column_name\": \"******\"}, {\"column_value\": ***, \"column_name\": \"******\"}, {\"column_value\": ***, \"column_name\": \"******\"}, {\"column_value\": ***, \"column_name\": \"******\"}]"


## Run
    Take predictions from an images model:
    python request_images.py

    Take predictions from a text model:
    python request_text.py

    Take predictions from a csv model:
    python request_csv.py

## Response
Response will be a JSON object, easily parsable in all programming languages.

    Response from an images model:
    {
       "status":"success",
       "message":"Predictions",
       "predictions":[
          {
             "sample":"image.jpeg",
             "predictions":[
                {
                   "predicted_score":"0.962045",
                   "predicted_label":"predicted label 1"
                },
                {
                   "predicted_score":"0.037955",
                   "predicted_label":"predicted label 2"
                }
             ]
          },
          {
             "sample":"https://www.example.com/image.jpg",
             "predictions":[
                {
                   "predicted_score":"0.932396",
                   "predicted_label":"predicted label 1"
                },
                {
                   "predicted_score":"0.067604",
                   "predicted_label":"pfredicted label 2"
                }
             ]
          }
       ]
    }

    Response from a text model:
    [
      {
        "status": "success",
        "message": "Predictions.",
        "predictions": [
          {
            "sample": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "label": "predicted label(class) or predicted number(integer/float)"
          }
        ]
      }
    ]

    Response from a csv model:
    {
       "status":"success",
       "message":[],
       "predictions":[
          {
             "sample":"[{\"column_value\": ***, \"column_name\": \"******\"}, {\"column_value\": ***, \"column_name\": \"******\"}, {\"column_value\": ***, \"column_name\": \"******\"}, {\"column_value\": ***, \"column_name\": \"******\"}]",
             "label":"predicted label(class) or predicted number(integer/float)"
          }
       ]
    }



## Licensing

MIT License
