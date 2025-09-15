# Ai_travel_planner
An intelligent travel planning system powered by AI/ML. It helps users generate personalized trip itineraries based on budget, preferences (food, adventure, culture, relaxation), duration, and location. The planner integrates NLP for understanding user queries, recommends destinations, suggests activities, and provides optimized travel routes.
## Problem
Travel planning is time-consuming. People struggle to create optimized itineraries within their budget.

## Solution
AI-powered planner that generates a personalized itinerary based on destination, budget, and trip duration.

## Features
- Takes destination, budget, and days as input
- Generates day-by-day itinerary
- Budget-aware recommendations
- Future: API integration for real data

## Tech Stack
Python, Streamlit, (APIs in next version)

## Demo
https://ai-travel-guide.streamlit.app

## Screenshots


## code
def generate_itinerary(destination, budget, days):
    activities = ["Sightseeing", "Local Food", "Adventure", "Relaxation", "Cultural Experience"]
    itinerary = {}
    for day in range(1, days + 1):
        activity = activities[day % len(activities)]
        itinerary[f"Day {day}"] = f"{activity} in {destination}"
    return itinerary

# Button to generate plan
if st.button("Generate Itinerary"):
    if destination and budget and days:
        st.subheader(f"Your {days}-Day Itinerary for {destination} 🗺️")
        itinerary = generate_itinerary(destination, budget, days)
        for day, plan in itinerary.items():
            st.write(f"**{day}:** {plan}")
    else:
        st.warning("Please fill all inputs.")


