# Endpoint for api.example-weather-app/location

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

### Disclaimer

I'm now affiliated with OpenAI.