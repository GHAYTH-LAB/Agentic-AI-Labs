import requests
from dotenv import load_dotenv 
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_ollama import ChatOllama
import os
load_dotenv()
key=os.getenv("CURRENCY_API_KEY")
ollama_model = ChatOllama(
    model="llama3.1"
    ,temperature=0

)
@tool("currency_converter",description="Convert currency from Dollars to EURO",return_direct=False)
def convert_currency(amount:float)->str:
    try:
        API_URL="https://api.freecurrencyapi.com/v1/latest"
        params={
            "apikey":key
            ,"base_currency":"USD"
            ,"currencies":"EUR"
        }
        response=requests.get(url=API_URL
                          ,params=params
                          )
        data=response.json()
        print(data)
        rate=data["data"]["EUR"]
        converted=rate*amount
        return f"{amount} in USD is equivalent to {converted} in EUR"
    except Exception as e:
        return f"Error fetching convertion is {e}"
agent=create_agent(
    model=ollama_model
    ,tools=[convert_currency]
    ,system_prompt="You are a helpful AI Assistant and your role is to give me the rate of converstion Be precise and remain helpful"
)
response=agent.invoke({
    "messages":[
        {
            "role":"user"
            ,"content":"What is 100 dollars in EURO"
        }
    ]

})
print(response["messages"][-1].content)