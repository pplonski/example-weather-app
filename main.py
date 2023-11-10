from fastapi import FastAPI

app = FastAPI()

@app.get("/location")
async def get_weather(location: str = "Lapy, Poland"):
    return {
	"location": location,
	"temperature": "75 F",
  	"condition": "Funny",
  	"humidity": "50%",
  	"wind": "5 mph"
    }


