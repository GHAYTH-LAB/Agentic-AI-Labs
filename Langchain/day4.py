from langchain.messages import SystemMessage,AIMessage,HumanMessage
from langchain_ollama import ChatOllama

conversation=[
    SystemMessage("You are a Helpful Ai Assistant,You will help me find the best places to visit in a city for a tourist and be my guide for any trip")
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
    ,HumanMessage ("Ok after Barcelona where To get?")
    ,AIMessage("""After exploring the vibrant city of Barcelona, you might want to consider visiting other amazing destinations in Spain. Here are some suggestions for your next stop:

    **Option 1: Madrid**

* Distance from Barcelona: 620 km (385 miles), approximately 1-hour flight or 6-hour train ride
* Must-visit attractions:
        + **Museo del Prado**: One of the world's greatest art museums, featuring works by Goya, Velázquez, and El Greco.
        + **Royal Palace of Madrid**: A grand palace with stunning architecture and beautiful gardens.
        + **Retiro Park**: A beautiful urban park with a lake, gardens, and sculptures.
* Experience the vibrant nightlife, try some delicious tapas, and visit the famous **Mercado de San Miguel**.

**Option 2: Seville**

* Distance from Barcelona: 760 km (472 miles), approximately 1.5-hour flight or 8-hour train ride
* Must-visit attractions:
        + **Cathedral of Seville**: A stunning Gothic cathedral with a Moorish influence.
        + **Royal Alcázar of Seville**: A beautiful palace with Mudéjar architecture and stunning gardens.
        + **Plaza de España**: A beautiful square with a mix of Moorish and Gothic styles.
* Explore the charming Santa Cruz neighborhood, visit the **Archivo de Indias** (a UNESCO World Heritage Site), and enjoy the city's lively flamenco music scene.

**Option 3: Valencia**

* Distance from Barcelona: 340 km (211 miles), approximately 1-hour flight or 3-hour train ride
* Must-visit attractions:
        + **City of Arts and Sciences**: A complex of modern museums, parks, and aquariums.
        + **Central Market**: A beautiful market with a stunning glass roof and a wide variety of local produce.
        + **Beach of the City of Arts and Sciences**: A beautiful beach with clear waters and a lively promenade.
* Visit the **Turia Gardens**, explore the historic center, and try some delicious **paella**.

**Option 4: Costa Brava**

* Distance from Barcelona: 100 km (62 miles), approximately 1-hour drive or 1.5-hour train ride
* Must-visit attractions:
        + **Cadaqués**: A charming fishing village with stunning beaches and a beautiful church.
        + **Tossa de Mar**: A medieval town with a stunning castle and a beautiful beach.
        + **Girona**: A charming city with a beautiful cathedral, a medieval quarter, and a stunning riverfront.
* Explore the beautiful coastline, visit the **Cap de Creus** natural park, and enjoy the local seafood.

Which of these options sounds most appealing to you?""")
,HumanMessage("What are the other cities in the world that are Like Barcelona")
]
LLM=ChatOllama(
    model="llama3.1"
    ,temperature=0
)
response=LLM.invoke(conversation)
print(response.content)