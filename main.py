import streamlit as st
from agents import TripCrew
from dotenv import load_dotenv
import os
load_dotenv()

def main():
    st.set_page_config(
        page_title="TripMind AI",
        page_icon="✈️",
        layout="wide"
    )

    st.title("TripMind AI ")
    st.markdown("**Plan your perfect trip with AI-powered agents!**")

    with st.sidebar:
        st.header("Trip Details")
        travel_type = st.selectbox("Travel Type", ["Leisure", "Adventure", "Cultural", "Nature"])
        interests = st.multiselect("Interests", ["History", "Food", "Outdoor Activities", "Art", "Nightlife", "Shopping", "Music"])
        season = st.selectbox("Season", ["Spring", "Summer", "Fall", "Winter"])
        duration = st.selectbox("Duration", ["3-5 days", "1 week", "2 weeks", "1 month"])
        budget = st.selectbox("Budget (USD)", ["Under $1000", "$1000-$3000", "$3000-$5000", "Over $5000"])

        st.markdown("---")
        st.markdown("###  AI Agents:")
        st.markdown("1. City Selector")
        st.markdown("2. Local Expert")
        st.markdown("3. Travel Planner")
        st.markdown("4. Budget Manager")
        st.markdown("5. Weather Expert")
        st.markdown("6. Safety Expert")
        st.markdown("7. Language Guide")
        st.markdown("8. Hotel Expert")
        st.markdown("9. Flight Expert")

    if st.button("Plan My Trip", type="primary"):
        if not interests:
            st.warning("Please select at least one interest!")
            return

        user_input = {
            "travel_type": travel_type,
            "interests": interests,
            "season": season,
            "duration": duration,
            "budget": budget,
        }

        with st.spinner("🤖 AI Agents working on your trip plan... Please wait 1-2 minutes..."):
            try:
                result = TripCrew(user_input).result

                st.success("Trip planning completed!")
                st.markdown("---")

                # Tabs mein results dikhao
                tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs([
                    "Cities",
                    "City Info",
                    "Itinerary",
                    "Budget",
                    "Weather",
                    "Safety",
                    "Language",
                    "Hotels",
                    "Flights"
                ])

                with tab1:
                    st.subheader("Recommended Cities")
                    st.markdown(result.get("city_selection", "No data"))

                with tab2:
                    st.subheader("City Research")
                    st.markdown(result.get("city_research", "No data"))

                with tab3:
                    st.subheader("Trip Itinerary")
                    st.markdown(result.get("itinerary_creation", "No data"))

                with tab4:
                    st.subheader("Budget Plan")
                    st.markdown(result.get("budget_planning", "No data"))

                with tab5:
                    st.subheader("Weather Guide")
                    st.markdown(result.get("weather_guide", "No data"))

                with tab6:
                    st.subheader("Safety & Emergency")
                    st.markdown(result.get("safety_emergency", "No data"))

                with tab7:
                    st.subheader("Language Guide")
                    st.markdown(result.get("language_guide", "No data"))

                with tab8:
                    st.subheader("Hotel Suggestions")
                    st.markdown(result.get("hotel_suggestions", "No data"))

                with tab9:
                    st.subheader("Flight Information")
                    st.markdown(result.get("flight_info", "No data"))

            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()