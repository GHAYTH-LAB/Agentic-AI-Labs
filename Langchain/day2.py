import requests
from langchain.agents import create_agent 
from langchain.tools import tool
from dotenv import load_dotenv 
from langchain_ollama import ChatOllama
import os
load_dotenv()
key=os.getenv("CURRENCY_API_KEY")
country_key=os.getenv("REST_COUNTRY_KEY")
@tool("weather",description="get the weather in celsius for any place giving the latitude and longitude",return_direct=False)
def get_weather(latitude:float,longitude:float)->float:
    weather_API_URL= "https://api.open-meteo.com/v1/forecast"
    params={
        "latitude":latitude
        ,"longitude":longitude
        ,"temperature_unit":"celsius"
        ,"current": "temperature_2m",

    }
    response=requests.get(url=weather_API_URL
                          ,params=params)
    data=response.json()
    temperature=data["current"]["temperature_2m"]
    return temperature
@tool("currency_converter",description="convert the amount from one currency to another",return_direct=False)
def convert_currency(amount:float,from_currency:str,to_currency:str)->float:
    currency_API_URl="https://api.fastforex.io/convert"
    params={
        "api_key":key
        ,"from":from_currency
        ,"to":to_currency
        ,"amount":amount
    }
    response=requests.get(url=currency_API_URl
                          ,params=params)
    data=response.json()
    return data["result"][to_currency]
@tool
def get_tourist_places(city: str):
    """Find tourist attractions and interesting places to visit in a city."""
    geocoding_url = "https://api.geoapify.com/v1/geocode/search"
    geocoding_params = {
        "text": city,
        "apiKey": os.getenv("GEOAPIFY_API_KEY")
    }
    geo_response = requests.get(
        geocoding_url,
        params=geocoding_params
    )
    geo_response.raise_for_status()
    geo_data = geo_response.json()
    if not geo_data.get("features"):
        return f"Could not find the city: {city}"
    coordinates = geo_data["features"][0]["geometry"]["coordinates"]
    longitude = coordinates[0]
    latitude = coordinates[1]
    places_url = "https://api.geoapify.com/v2/places"
    places_params = {
        "categories": "tourism.sights",
        "filter": f"circle:{longitude},{latitude},10000",
        "bias": f"proximity:{longitude},{latitude}",
        "limit": 10,
        "apiKey": os.getenv("GEOAPIFY_API_KEY")
    }
    places_response = requests.get(
        places_url,
        params=places_params
    )
    places_response.raise_for_status()
    places_data = places_response.json()
    places = []
    for place in places_data.get("features", []):
        properties = place.get("properties", {})

        places.append({
            "name": properties.get("name"),
            "address": properties.get("formatted"),
            "latitude": properties.get("lat"),
            "longitude": properties.get("lon")
        })

    return places
llm=ChatOllama(
    model="llama3.1"
    ,temperature=0
)
agent=create_agent(
    model=llm
    ,tools=[get_tourist_places,get_weather,convert_currency]
    ,system_prompt="""You are a helpful AI travel assistant.

Your job is to help users with:

1. Current weather information
2. Currency conversion
3. Tourist attractions and places to visit

You have access to the following tools:

1. get_weather(latitude, longitude)

   * Use this tool when the user asks about the current weather.
   * The tool requires two arguments:

     * latitude: the latitude of the location.
     * longitude: the longitude of the location.
   * If the user provides the latitude and longitude, use those coordinates directly.
   * Make sure latitude and longitude are passed in the correct order:
     get_weather(latitude, longitude)
   * Never invent or guess coordinates.
   * Never invent or guess weather data.

2. convert_currency(from_currency, to_currency, amount)

   * Use this tool when the user asks to convert money.
   * from_currency is the currency the user currently has.
   * to_currency is the currency the user wants.
   * amount is the amount of money to convert.
   * Always use this tool for currency conversion.
   * Never calculate or guess exchange rates yourself.
   * Pass the arguments in this exact order:
     convert_currency(from_currency, to_currency, amount)

3. get_tourist_places(city)

   * Use this tool when the user asks about tourist attractions, monuments, sightseeing, or places to visit.
   * The tool requires a city name.
   * Use the results returned by the tool.
   * Never invent tourist attractions.
   * If the user asks for a specific number of places, such as 5, return that number when enough results are available.

Rules:

* Understand the user's request before selecting a tool.
* Use the appropriate tool for each part of the user's request.
* You can use multiple tools for a single request.
* If the user asks several questions, use all the necessary tools.
* Do not invent information that should come from an API.
* Do not guess weather information or exchange rates.
* Do not invent tourist attractions.
* Respect the exact argument order of every tool.
* After receiving the tool results, combine them into one clear and natural answer.
* Keep the final answer concise but useful.
"""
    )
response=agent.invoke({
    "messages":[{
        "role":"user"
        ,"content":"I'm planning a trip to Paris which cordinates are Latitude: 48.8566 and Longitude= 2.3522. Tell me the current weather,give me 5 interesting places to visit, and tell me how much"
        "500 Dollars in Euros."
}]
})

print(response["messages"][-1].content)