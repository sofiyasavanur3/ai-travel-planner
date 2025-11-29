"""
AI Travel Planner - Main Application
A comprehensive travel planning app powered by AI agents.
"""

import streamlit as st
from datetime import date, timedelta

# Import configurations
from src.config.settings import settings

# Import services
from src.services.flight_service import FlightService

# Import agents
from src.agents.researcher import ResearchAgent
from src.agents.planner import PlannerAgent
from src.agents.finder import FinderAgent

# Import UI components
from src.ui.styles import get_custom_css, get_welcome_banner
from src.ui.sidebar import render_sidebar
from src.ui.components import (
    render_flight_card,
    render_section_header,
    render_info_box
)

# Import utilities
from src.utils.validators import (
    validate_iata_code,
    validate_dates,
    validate_activity_preferences
)


def initialize_app():
    """Initialize the Streamlit app with configuration"""
    st.set_page_config(
        page_title=settings.PAGE_TITLE,
        layout=settings.PAGE_LAYOUT,
        initial_sidebar_state="expanded"
    )
    
    # Apply custom CSS
    st.markdown(get_custom_css(), unsafe_allow_html=True)
    
    # Validate API keys
    if not settings.validate_keys():
        st.stop()


def render_header():
    """Render the application header"""
    st.markdown(
        '<h1 class="title">✈️ AI-Powered Travel Planner</h1>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<p class="subtitle">Plan your dream trip with AI! Get personalized recommendations for flights, hotels, and activities.</p>',
        unsafe_allow_html=True
    )


def get_user_inputs():
    """
    Get and validate user inputs from the main form.
    
    Returns:
        Dictionary containing all user inputs
    """
    # Location inputs
    st.markdown("### 🌍 Where are you headed?")
    col1, col2 = st.columns(2)
    
    with col1:
        source = st.text_input(
            "🛫 Departure City (IATA Code):",
            value=settings.DEFAULT_SOURCE,
            max_chars=3,
            help="Enter 3-letter airport code (e.g., BOM for Mumbai)"
        ).upper()
    
    with col2:
        destination = st.text_input(
            "🛬 Destination (IATA Code):",
            value=settings.DEFAULT_DESTINATION,
            max_chars=3,
            help="Enter 3-letter airport code (e.g., DEL for Delhi)"
        ).upper()
    
    # Trip details
    st.markdown("### 📅 Plan Your Adventure")
    col1, col2 = st.columns(2)
    
    with col1:
        num_days = st.slider(
            "🕒 Trip Duration (days):",
            min_value=settings.MIN_TRIP_DAYS,
            max_value=settings.MAX_TRIP_DAYS,
            value=settings.DEFAULT_TRIP_DURATION
        )
    
    with col2:
        travel_theme = st.selectbox(
            "🎭 Select Your Travel Theme:",
            settings.TRAVEL_THEMES
        )
    
    # Date selection
    col1, col2 = st.columns(2)
    
    with col1:
        departure_date = st.date_input(
            "📅 Departure Date",
            value=date.today() + timedelta(days=7),
            min_value=date.today()
        )
    
    with col2:
        return_date = st.date_input(
            "📅 Return Date",
            value=date.today() + timedelta(days=7 + num_days),
            min_value=departure_date
        )
    
    # Activity preferences
    activity_preferences = st.text_area(
        "🌍 What activities do you enjoy?",
        value="Relaxing on the beach, exploring historical sites, trying local cuisine",
        help="Describe your interests and preferred activities",
        height=100
    )
    
    return {
        "source": source,
        "destination": destination,
        "num_days": num_days,
        "travel_theme": travel_theme,
        "departure_date": departure_date,
        "return_date": return_date,
        "activity_preferences": activity_preferences
    }


def validate_inputs(inputs, sidebar_data):
    """
    Validate all user inputs.
    
    Args:
        inputs: User inputs dictionary
        sidebar_data: Sidebar selections dictionary
        
    Returns:
        tuple: (is_valid, error_messages)
    """
    errors = []
    
    # Validate source airport
    is_valid, error = validate_iata_code(inputs["source"])
    if not is_valid:
        errors.append(f"Departure: {error}")
    
    # Validate destination airport
    is_valid, error = validate_iata_code(inputs["destination"])
    if not is_valid:
        errors.append(f"Destination: {error}")
    
    # Check if source and destination are different
    if inputs["source"] == inputs["destination"]:
        errors.append("Departure and destination must be different")
    
    # Validate dates
    is_valid, error = validate_dates(inputs["departure_date"], inputs["return_date"])
    if not is_valid:
        errors.append(error)
    
    # Validate activity preferences
    is_valid, error = validate_activity_preferences(inputs["activity_preferences"])
    if not is_valid:
        errors.append(error)
    
    return len(errors) == 0, errors


def main():
    """Main application logic"""
    
    # Initialize app
    initialize_app()
    
    # Render header
    render_header()
    
    # Get sidebar inputs
    sidebar_data = render_sidebar()
    
    # Get main form inputs
    user_inputs = get_user_inputs()
    
    # Display welcome banner
    st.markdown("---")
    st.markdown(
        get_welcome_banner(
            user_inputs["travel_theme"],
            user_inputs["destination"]
        ),
        unsafe_allow_html=True
    )
    
    # Generate travel plan button
    if st.button("🚀 Generate Travel Plan", type="primary", use_container_width=True):
        
        # Validate inputs
        is_valid, errors = validate_inputs(user_inputs, sidebar_data)
        
        if not is_valid:
            for error in errors:
                st.error(f"❌ {error}")
            st.stop()
        
        # Initialize services and agents with different models
        flight_service = FlightService(settings.SERPAPI_KEY)
        researcher = ResearchAgent(settings.GEMINI_MODEL_RESEARCH, settings.SERPAPI_KEY)
        finder = FinderAgent(settings.GEMINI_MODEL_FINDER, settings.SERPAPI_KEY)
        planner = PlannerAgent(settings.GEMINI_MODEL_PLANNER)
        
        # Step 1: Search for flights
        with st.spinner("✈️ Searching for best flight options..."):
            flights = flight_service.search_and_extract(
                source=user_inputs["source"],
                destination=user_inputs["destination"],
                departure_date=str(user_inputs["departure_date"]),
                return_date=str(user_inputs["return_date"]),
                limit=3
            )
        
        # Step 2: Research destination
        with st.spinner("🔍 Researching destination attractions & activities..."):
            research_results = researcher.research_destination(
                destination=user_inputs["destination"],
                num_days=user_inputs["num_days"],
                travel_theme=user_inputs["travel_theme"],
                activity_preferences=user_inputs["activity_preferences"],
                budget=sidebar_data["budget"]
            )
        
        # Step 3: Find hotels and restaurants
        with st.spinner("🏨 Finding best hotels & restaurants..."):
            hotel_restaurant_results = finder.find_accommodations(
                destination=user_inputs["destination"],
                travel_theme=user_inputs["travel_theme"],
                budget=sidebar_data["budget"],
                hotel_rating=sidebar_data["hotel_rating"],
                activity_preferences=user_inputs["activity_preferences"]
            )
        
        # Step 4: Create itinerary
        with st.spinner("🗺️ Creating your personalized itinerary..."):
            itinerary = planner.create_itinerary(
                destination=user_inputs["destination"],
                num_days=user_inputs["num_days"],
                travel_theme=user_inputs["travel_theme"],
                activity_preferences=user_inputs["activity_preferences"],
                budget=sidebar_data["budget"],
                research_data=research_results,
                hotel_data=hotel_restaurant_results
            )
        
        # Display Results
        st.markdown("---")
        
        # Flight Results
        render_section_header("Cheapest Flight Options", "✈️")
        
        if flights:
            cols = st.columns(len(flights))
            for idx, flight in enumerate(flights):
                with cols[idx]:
                    # Try to get booking link
                    booking_link = "#"
                    try:
                        if flight.get("departure_token"):
                            booking_link = flight_service.get_booking_link(
                                flight,
                                user_inputs["source"],
                                user_inputs["destination"],
                                str(user_inputs["departure_date"]),
                                str(user_inputs["return_date"])
                            )
                    except Exception as e:
                        st.warning(f"Booking link unavailable: {str(e)}")
                    
                    render_flight_card(flight, booking_link)
        else:
            render_info_box(
                "⚠️ No flights found for the selected dates. Please try different dates.",
                "warning"
            )
        
        # Research Results
        render_section_header("Destination Research", "🔍")
        st.markdown(research_results)
        
        # Hotels & Restaurants
        render_section_header("Hotels & Restaurants", "🏨")
        st.markdown(hotel_restaurant_results)
        
        # Itinerary
        render_section_header("Your Personalized Itinerary", "🗺️")
        st.markdown(itinerary)
        
        # Success message
        st.markdown("---")
        render_info_box(
            "✅ <strong>Travel plan generated successfully!</strong><br>"
            "You can now save or share this itinerary. Have a wonderful trip! 🎉",
            "success"
        )
        
        # Download button for itinerary
        full_plan = f"""
# Travel Plan: {user_inputs['source']} to {user_inputs['destination']}

## Trip Details
- Duration: {user_inputs['num_days']} days
- Theme: {user_inputs['travel_theme']}
- Dates: {user_inputs['departure_date']} to {user_inputs['return_date']}

## Flights
{len(flights)} options found

## Destination Research
{research_results}

## Hotels & Restaurants
{hotel_restaurant_results}

## Itinerary
{itinerary}
"""
        
        st.download_button(
            label="📥 Download Complete Travel Plan",
            data=full_plan,
            file_name=f"travel_plan_{user_inputs['destination']}.txt",
            mime="text/plain"
        )


if __name__ == "__main__":
    main()