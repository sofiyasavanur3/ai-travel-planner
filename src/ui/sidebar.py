"""
Sidebar configuration and components.
"""

import streamlit as st
from src.config.settings import settings


def render_sidebar():
    """
    Render the sidebar with all preferences and options.
    
    Returns:
        Dictionary containing all sidebar selections
    """
    st.sidebar.title("🌎 Travel Assistant")
    st.sidebar.subheader("Personalize Your Trip")
    
    # Budget preference
    budget = st.sidebar.radio(
        "💰 Budget Preference:",
        settings.BUDGET_OPTIONS,
        index=1  # Default to "Standard"
    )
    
    # Flight class
    flight_class = st.sidebar.radio(
        "✈️ Flight Class:",
        settings.FLIGHT_CLASS_OPTIONS,
        index=0  # Default to "Economy"
    )
    
    # Hotel rating
    hotel_rating = st.sidebar.selectbox(
        "🏨 Preferred Hotel Rating:",
        settings.HOTEL_RATINGS,
        index=2  # Default to "4⭐"
    )
    
    st.sidebar.markdown("---")
    
    # Packing Checklist
    st.sidebar.subheader("🎒 Packing Checklist")
    packing_items = {
        "👕 Clothes": st.sidebar.checkbox("👕 Clothes", value=True),
        "🩴 Footwear": st.sidebar.checkbox("🩴 Comfortable Footwear", value=True),
        "🕶️ Sun Protection": st.sidebar.checkbox("🕶️ Sunglasses & Sunscreen"),
        "📖 Guidebook": st.sidebar.checkbox("📖 Travel Guidebook"),
        "💊 Medications": st.sidebar.checkbox("💊 Medications & First-Aid", value=True),
        "📱 Electronics": st.sidebar.checkbox("📱 Chargers & Power Bank"),
    }
    
    st.sidebar.markdown("---")
    
    # Travel Essentials
    st.sidebar.subheader("🛂 Travel Essentials")
    visa_required = st.sidebar.checkbox("🛃 Check Visa Requirements")
    travel_insurance = st.sidebar.checkbox("🛡️ Get Travel Insurance")
    currency_converter = st.sidebar.checkbox("💱 Currency Exchange Rates")
    
    st.sidebar.markdown("---")
    
    # About section
    with st.sidebar.expander("ℹ️ About"):
        st.write("""
        **AI Travel Planner**
        
        This app uses AI to help you plan your perfect trip:
        - 🔍 Research destinations
        - ✈️ Find best flights
        - 🏨 Discover hotels & restaurants
        - 🗺️ Create personalized itineraries
        
        Powered by Google Gemini and SerpAPI.
        """)
    
    return {
        "budget": budget,
        "flight_class": flight_class,
        "hotel_rating": hotel_rating,
        "packing_items": packing_items,
        "visa_required": visa_required,
        "travel_insurance": travel_insurance,
        "currency_converter": currency_converter
    }