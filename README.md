# Endpoint for api.example-weather-app.com/location

REST API endpoint for `api.example-weather-app.com/location` used in OpenAI GPT builder.

The GPT builder was announced during OpenAI DevDay (06/11/23). You can use it to build your customized GTP. One of its features is ability to call REST API. You can add actions that call 3rd party API.

![](/media/add_action.gif)

In the example API, you can select `Get weather data` endpoint. I selected it, and send prompt to GPT `What is weather in New York?`.

![](/media/send_question.png)

I got error response, because no such API exists. Below is screenshot with error response.

![](/media/api_error.png)

What I did? I bought `example-weather-app.com` domain and set simple FastAPI app with hard-coded JSON response. It is available at `https://api.example-weather-app.com/location?location=your+location`.

Now, we got correct response in OpenAI GPT builder.

![](/media/api_response.png)


### OpenAPI schema

Here is OpenAPI schema for this endpoint:

```
{
  "openapi": "3.1.0",
  "info": {
    "title": "Get weather data",
    "description": "Retrieves current weather data for a location.",
    "version": "v1.0.0"
  },
  "servers": [
    {
      "url": "https://api.example-weather-app.com"
    }
  ],
  "paths": {
    "/location": {
      "get": {
        "description": "Get temperature for a specific location",
        "operationId": "GetCurrentWeather",
        "parameters": [
          {
            "name": "location",
            "in": "query",
            "description": "The city and state to retrieve the weather for",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "deprecated": false
      }
    }
  },
  "components": {
    "schemas": {}
  }
}
```

## Disclaimer

I'm now affiliated with OpenAI.


## 👩‍💼🐦 Connect with Us on LinkedIn & Twitter

Stay up-to-date with the latest updates about our projects by following us on Twitter ([MLJAR Twitter](https://twitter.com/MLJAROfficial)) and LinkedIn ([Aleksandra LinkedIn](https://www.linkedin.com/in/aleksandra-p%C5%82o%C5%84ska-42047432/) & [Piotr LinkedIn](https://www.linkedin.com/in/piotr-plonski-mljar/)). 

Feel free to contact us if you need any help with ChatGPT Actions.
