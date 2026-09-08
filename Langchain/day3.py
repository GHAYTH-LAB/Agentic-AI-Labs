import requests
from langchain.agents import create_agent
from langchain.tools import tool 
from langchain_ollama import ChatOllama
from dotenv import load_dotenv
import os
load_dotenv()
NEWS_API_KEY=os.getenv("NEWS_API_KEY")
@tool("News_finder",description="Find News of any topic the user asks about",return_direct=False)
def get_News(subject:str,timeframe:int,country:str,News_language:str)->str:
    COUNTRY_CODE_MAP = {
        "japan": "jp",
        "france": "fr",
        "united states": "us",
        "usa": "us",
        "united kingdom": "gb",
        "uk": "gb",
        "germany": "de",
        "italy": "it",
        "spain": "es",
        "china": "cn",
        "india": "in",
        "canada": "ca",
        "australia": "au",
        "brazil": "br",
        "south korea": "kr",
        "mexico": "mx",
    }
    country_key =country.strip().lower()
    country = COUNTRY_CODE_MAP.get(country_key, country_key)
    API_URL="https://newsdata.io/api/1/latest"
    params={
        "apikey":NEWS_API_KEY
        ,"q":subject
        ,"country":country
        ,"language":News_language
    }
    response=requests.get(url=API_URL
                          ,params=params)
    data = response.json()
    if data.get("status") != "success":
        return f"News API error: {data.get('results')}"
    results = data.get("results") or []
    if not results:
        return f"No news found for '{subject}'."
    return f"The content is {results[0]['content']} and the url source of this article is {results[0]['source_url']}"
@tool("get weather",description="Get Weather of a city based on its longitude and latitude",return_direct=False)
def get_weather(city:str)->str:
    GET_CORDINATES_API_URL="http://api.openweathermap.org/geo/1.0/direct"
    params={
            "q":city
            ,"appid":os.getenv("GEOCODE_API_KEY")
        }
    response=requests.get(url=GET_CORDINATES_API_URL,
                              params=params)
    data=response.json()
    lon=data[0]["lon"]
    lat=data[0]["lat"]
    get_weather_API_URL="https://api.openweathermap.org/data/4.0/onecall/current"
    params={
        "lat":lat
        ,"lon":lon
        ,"appid":os.getenv("WEATHER_API_KEY")
        ,"units":"metric"
        ,"lang":"en"
    }
    response=requests.get(url=get_weather_API_URL
                          ,params=params)
    response=response.json()
    pressure=response["data"][0]["pressure"]
    humidity=response["data"][0]["humidity"]
    temperature=response["data"][0]["temp"]
    return f"pressure is {pressure} ,humidity is {humidity} and temperature is {temperature}"
@tool("currency_converter",description="convert an amou of money from one currency to another",return_direct=False)
def convert_currency(from_currency:str,to_currency:str,amount:float)->float:
    currency_url="https://api.fastforex.io/convert"
    params={
        "from":from_currency
        ,"to":to_currency
        ,"amount":amount
        ,"api_key":os.getenv("CURRENCY_API_KEY")
    }
    response=requests.get(url=currency_url
                          ,params=params)
    response=response.json()
    amount=response["result"][to_currency]
    return amount
LLM=ChatOllama(
    model="llama3.1"
    ,temperature=0
)
agent=create_agent(
    model=LLM
    ,tools=[ convert_currency,get_weather,get_News]
    ,system_prompt="""
You are a helpful travel assistant.

You have three tools:

1. get_weather(city)
   - Gets the current weather and coordinates of a city.
   - Always use this tool when the user asks for weather or coordinates.
   - Never invent weather or coordinates.

2. get_News(subject, timeframe, country, News_language)
   - Gets recent news.
   - Always use this tool when the user asks for news.
   - Never invent news or URLs.

3. currency_converter(from_currency, to_currency, amount)
   - Converts currencies using the currency API.
   - Always use this tool for currency conversion.
   - Never calculate exchange rates yourself.

Use all necessary tools for the user's request.
After receiving the tool results, give the user a clear natural-language answer.
"""
)
Query=input("I am your trip assistant,I am here to help you with Your trip **** Please Input Your Query")
response=agent.invoke({
    "messages":[{
        "role":"user"
        ,"content":Query
    }]
})
print(response["messages"][-1].content)