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
"C:\Users\Asus\OneDrive\Pictures\Screenshots\Screenshot 2025-09-16 005628.png"

## code starts from here
import streamlit as st

# Title
st.title("AI Travel Planner ✈️")

# User Inputs
destination = st.text_input("Enter your destination:")
budget = st.number_input("Enter your budget (in USD):", min_value=100, step=50)
days = st.number_input("Number of days:", min_value=1, step=1)

# Travel Style Selection
style = st.selectbox(
    "Choose your travel style:",
    ["Adventure", "Relaxation", "Culture", "Foodie", "Mixed"]
)

# Activity presets for each style
activities_dict = {
    "Adventure": ["Hiking", "Rafting", "Wildlife Safari", "Camping", "Zipline"],
    "Relaxation": ["Beach Day", "Spa", "Resort Stay", "Leisure Walk", "Sunset View"],
    "Culture": ["Museum Visit", "Temple Tour", "Historical Walk", "Art Gallery", "Local Market"],
    "Foodie": ["Street Food Tour", "Fine Dining", "Local Cafe", "Cooking Class", "Winery Visit"],
    "Mixed": ["Sightseeing", "Local Food", "Adventure", "Relaxation", "Cultural Experience"]
}

# Generate itinerary
def generate_itinerary(destination, budget, days, style):
    activities = activities_dict[style]
    itinerary = {}
    for day in range(1, days + 1):
        activity = activities[(day - 1) % len(activities)]
        itinerary[f"Day {day}"] = f"{activity} in {destination}"
    return itinerary

# Button to generate plan
if st.button("Generate Itinerary"):
    if destination and budget and days:
        st.subheader(f"Your {days}-Day {style} Trip to {destination} 🗺️")
        itinerary = generate_itinerary(destination, budget, days, style)
        for day, plan in itinerary.items():
            st.write(f"**{day}:** {plan}")
    else:
        st.warning("Please fill all inputs.")

