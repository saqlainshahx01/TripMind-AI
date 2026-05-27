import os
from groq import Groq
from dotenv import load_dotenv
load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_groq(system_role, prompt):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": system_role},
            {"role": "user", "content": prompt}
        ],
        temperature=0.9
    )
    return response.choices[0].message.content

class TripCrew:
    def __init__(self, input):
        self.input = input

    @property
    def result(self):
        # Agent 1 - City Selector
        city_selection = ask_groq(
            system_role="You are an expert travel consultant with deep knowledge of cities worldwide.",
            prompt=(
                f"Select 3 best cities for a {self.input['travel_type']} trip "
                f"with interests in {self.input['interests']} during {self.input['season']}. "
                f"Budget: {self.input['budget']}. "
                f"Give bullet points with 2 sentence explanation for each city. "
                f"At the end write: RECOMMENDED CITY: [city name]"
            )
        )

        # Selected city extract karo
        city = "Paris"
        if "RECOMMENDED CITY:" in city_selection:
            city = city_selection.split("RECOMMENDED CITY:")[-1].strip().split("\n")[0].strip()

        # Agent 2 - Local Expert
        city_research = ask_groq(
            system_role=f"You are a local resident of {city} with extensive knowledge of its culture and attractions.",
            prompt=(
                f"Give detailed info about {city} including:\n"
                f"- Top 5 attractions with description\n"
                f"- Local cuisine highlights with restaurant names\n"
                f"- Best local dishes to try\n"
                f"- Recommended restaurants for breakfast, lunch and dinner\n"
                f"- Cultural norms and etiquette\n"
                f"- Recommended accommodation areas\n"
                f"- Transportation tips"
            )
        )

        # Agent 3 - Travel Planner
        itinerary = ask_groq(
            system_role="You are an experienced travel planner who creates efficient and enjoyable itineraries.",
            prompt=(
                f"Create a {self.input['duration']} trip itinerary to {city}.\n"
                f"Travel type: {self.input['travel_type']}\n"
                f"Interests: {self.input['interests']}\n"
                f"Make a detailed table with columns: Time, Activity, Transportation, Meals.\n"
                f"IMPORTANT: Every breakfast, lunch and dinner must have a specific restaurant name in Meals column.\n"
                f"Do not leave Meals column empty for any meal time."
            )
        )

        # Agent 4 - Budget Manager
        budget = ask_groq(
            system_role="You are a financial expert with experience in travel budgeting.",
            prompt=(
                f"Create a budget plan for {self.input['budget']} trip to {city}.\n"
                f"Duration: {self.input['duration']}\n"
                f"Based on this itinerary:\n{itinerary[:500]}\n"
                f"Include accommodation, transport, meals, activities and emergency fund in table format."
            )
        )

        # Agent 5 - Weather Expert
        weather = ask_groq(
            system_role="You are a weather and travel preparation expert.",
            prompt=(
                f"What is the weather like in {city} during {self.input['season']}?\n"
                f"Give:\n"
                f"- Average temperature\n"
                f"- Weather conditions\n"
                f"- Packing suggestions with specific clothing items\n"
                f"- Best time to visit outdoor attractions"
            )
        )

        # Agent 6 - Safety Expert
        emergency = ask_groq(
            system_role="You are a travel safety and emergency expert.",
            prompt=(
                f"Give complete safety guide for tourists visiting {city}:\n"
                f"- Emergency numbers (police, ambulance, fire)\n"
                f"- Nearest hospitals\n"
                f"- Tourist police contact\n"
                f"- Common scams to avoid\n"
                f"- Safe and unsafe areas\n"
                f"- Embassy contact information"
            )
        )

        # Agent 7 - Language Expert
        language = ask_groq(
            system_role="You are a language and culture expert.",
            prompt=(
                f"Give a language guide for tourists visiting {city}:\n"
                f"- Local language name\n"
                f"- 20 essential phrases with pronunciation\n"
                f"- Common greetings\n"
                f"- Restaurant ordering phrases\n"
                f"- Emergency phrases\n"
                f"- Shopping phrases"
            )
        )

        # Agent 8 - Hotel Expert
        hotels = ask_groq(
            system_role="You are a hotel and accommodation expert.",
            prompt=(
                f"Suggest best hotels in {city} for a {self.input['travel_type']} trip:\n"
                f"Budget: {self.input['budget']}\n"
                f"- 3 Luxury hotels (with price range per night)\n"
                f"- 3 Mid-range hotels (with price range per night)\n"
                f"- 3 Budget hotels (with price range per night)\n"
                f"- Best areas to stay\n"
                f"- Booking tips"
            )
        )

        # Agent 9 - Flight Expert  
        flights = ask_groq(
            system_role="You are a flight and travel booking expert.",
            prompt=(
                f"Give flight information for visiting {city} during {self.input['season']}:\n"
                f"- Best airlines to use\n"
                f"- Approximate flight prices\n"
                f"- Best time to book\n"
                f"- Nearest airports\n"
                f"- Airport to city transportation options with costs"
            )
        )

        return {
            "city_selection": city_selection,
            "city_research": city_research,
            "itinerary_creation": itinerary,
            "budget_planning": budget,
            "weather_guide": weather,
            "safety_emergency": emergency,
            "language_guide": language,
            "hotel_suggestions": hotels,
            "flight_info": flights
        }