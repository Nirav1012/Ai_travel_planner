import streamlit as st

# Title
st.title("AI Travel Planner ✈️")

# User Inputs
destination = st.text_input("Enter your destination:")
budget = st.number_input("Enter your budget (in USD):", min_value=100, step=50)
days = st.number_input("Number of days:", min_value=1, step=1)

# Generate dummy itinerary
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

