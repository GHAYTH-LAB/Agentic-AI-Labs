import requests
from dotenv import load_dotenv 
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
import os
load_dotenv()
key=os.getenv("CURRENCY_API_KEY")
gemini_model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)
@tool("currency_converter",description="Convert currency from Dollars to Tunisia Dinars",return_direct=False)
def convert_currency():
    API_URL="https://api.freecurrencyapi.com/v1/latest"
    params={
        "apikey":key
        ,"base_currency":"USD"
        ,"currencies":"TND"
    }
    response=requests.get(url=API_URL
                          ,params=params
                          )
    return response.json()
agent=create_agent(
    model=gemini_model
    ,tools=[convert_currency]
    ,system_prompt="You are a helpful AI Assistant and your role is to give me the rate of converstion Be precise and remain helpful"
)
response=agent.invoke({
    "messages":[
        {
            "role":"user"
            ,"content":"What is 100 dollars in TND"
        }
    ]
})