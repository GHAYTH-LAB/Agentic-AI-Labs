from langchain.messages import SystemMessage,AIMessage,HumanMessage
from langchain_ollama import ChatOllama

conversation=[
    SystemMessage("You are a Helpful Ai Assistant,You will help me find the best places to visit in a city for a tourist")
    ,HumanMessage("HELLO I WANNA VISIT SPAIN NEXT YEAR EXACTLY BARCELONA ORDER ME SOME GOOD PLACES TO VISIT ?")
        ,AIMessage("""Barcelona is an amazing city! I'd be happy to help you plan your trip. Here are some must-visit places to add to your itinerary:"
        "**Landmarks and Iconic Sites:**

    1. **La Sagrada Familia**: Antoni Gaudí's iconic cathedral, a UNESCO World Heritage Site.
    2. **Park Güell**: Another iconic Gaudí landmark, featuring stunning architecture and city views.
    3. **La Rambla**: A famous pedestrian street lined with street performers, cafes, and shops.
    4. **Casa Batlló**: A house designed by Gaudí, known for its colorful and quirky architecture.
    5. **Barceloneta Beach**: A popular beach with clear waters and a lively promenade.

    **Museums and Galleries:**

    1. **Museu Picasso**: A museum showcasing an extensive collection of Picasso's artwork.
    2. **Museu Nacional d'Art de Catalunya**: A museum featuring an impressive collection of Catalan art.
    3. **Museu de la Xocolata**: A museum dedicated to the history of chocolate (yes, you read that right!).

    **Neighborhoods and Markets:**

    1. **El Born**: A charming neighborhood with narrow streets, boutique shops, and restaurants.
    2. **La Boqueria Market**: A world-famous market offering a wide variety of fresh produce, cheeses, and local specialties.
    3. **Gothic Quarter**: A historic neighborhood with narrow streets, charming squares, and plenty of restaurants and bars.

    **Other Recommendations:**

    1. **Camp Nou Stadium**: Home of FC Barcelona, one of the world's most famous football clubs.
    2. **Barcelona Aquarium**: A large aquarium featuring a variety of marine life.
    3. **Montjuïc Hill**: A hill with stunning views of the city, featuring the Olympic Stadium and the Joan Miro Museum.

    **Tips and Tricks:**

    * Consider purchasing a **Hola BCN** card, which grants you free public transportation and discounts on attractions.
    * Try some traditional Catalan cuisine, such as **pa amb tomàquet** (bread with fresh tomato) or **esqueixada** (a salad made with salted cod).
    * Don't miss the **La Mercè** festival, which takes place in September and features music, dance, and fireworks.

    I hope this helps you plan your trip to Barcelona! What type of activities or experiences are you most interested in?")
    """)
    ,AIMessage("Ok after Barcelona where To get?")
]
LLM=ChatOllama(
    model="llama3.1"
    ,temperature=0
)
response=LLM.invoke(conversation)
print(response.content)