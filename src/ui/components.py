"""
Reusable UI components for the Travel Planner.
"""

import streamlit as st
from src.utils.formatters import format_datetime, format_duration, format_price


def render_flight_card(flight_details, booking_link="#"):
    """
    Render a single flight card.
    
    Args:
        flight_details: Dictionary with flight information
        booking_link: URL for booking (default: "#")
    """
    airline_logo = flight_details.get("airline_logo", "")
    airline_name = flight_details.get("airline", "Unknown Airline")
    price = format_price(flight_details.get("price", "Not Available"))
    total_duration = format_duration(flight_details.get("total_duration", "N/A"))
    
    departure_time = format_datetime(flight_details.get("departure_time", "N/A"))
    arrival_time = format_datetime(flight_details.get("arrival_time", "N/A"))
    
    departure_airport = flight_details.get("departure_airport", "N/A")
    arrival_airport = flight_details.get("arrival_airport", "N/A")
    
    layovers = flight_details.get("layovers", 0)
    layover_text = f"{layovers} stop(s)" if layovers > 0 else "Non-stop"
    
    # Create HTML for flight card
    card_html = f"""
    <div style="
        border: 2px solid #ddd; 
        border-radius: 10px; 
        padding: 15px; 
        text-align: center;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
        background-color: #f9f9f9;
        margin-bottom: 20px;
        transition: transform 0.2s;
    ">
        <img src="{airline_logo}" width="80" alt="{airline_name}" style="margin-bottom: 10px;" />
        <h3 style="margin: 10px 0; color: #333;">{airline_name}</h3>
        <p style="color: #666; margin: 5px 0;"><strong>{departure_airport}</strong> → <strong>{arrival_airport}</strong></p>
        <hr style="border: 0; border-top: 1px solid #ddd; margin: 15px 0;">
        <p style="margin: 8px 0;"><strong>🛫 Departure:</strong> {departure_time}</p>
        <p style="margin: 8px 0;"><strong>🛬 Arrival:</strong> {arrival_time}</p>
        <p style="margin: 8px 0;"><strong>⏱️ Duration:</strong> {total_duration}</p>
        <p style="margin: 8px 0;"><strong>🔄 Stops:</strong> {layover_text}</p>
        <h2 style="color: #008000; margin: 15px 0;">💰 {price}</h2>
        <a href="{booking_link}" target="_blank" style="
            display: inline-block;
            padding: 10px 20px;
            font-size: 16px;
            font-weight: bold;
            color: #fff;
            background-color: #007bff;
            text-decoration: none;
            border-radius: 5px;
            margin-top: 10px;
        ">🔗 Book Now</a>
    </div>
    """
    
    st.markdown(card_html, unsafe_allow_html=True)


def render_section_header(title, icon=""):
    """
    Render a section header with optional icon.
    
    Args:
        title: Section title
        icon: Optional emoji icon
    """
    st.markdown(
        f'<h2 style="color: #333; border-bottom: 2px solid #ff5733; padding-bottom: 10px; margin-top: 30px;">'
        f'{icon} {title}'
        f'</h2>',
        unsafe_allow_html=True
    )


def render_info_box(message, box_type="info"):
    """
    Render an information box.
    
    Args:
        message: Message to display
        box_type: Type of box (info, warning, success)
    """
    colors = {
        "info": {"bg": "#e7f3ff", "border": "#2196F3"},
        "warning": {"bg": "#fff3cd", "border": "#ffc107"},
        "success": {"bg": "#d4edda", "border": "#28a745"}
    }
    
    color = colors.get(box_type, colors["info"])
    
    st.markdown(
        f'''
        <div style="
            background-color: {color["bg"]};
            border-left: 4px solid {color["border"]};
            padding: 15px;
            margin: 15px 0;
            border-radius: 5px;
        ">
            {message}
        </div>
        ''',
        unsafe_allow_html=True
    )


def render_loading_message(message):
    """
    Render a loading message with spinner.
    
    Args:
        message: Loading message to display
    """
    return st.spinner(message)


def render_packing_checklist():
    """Render a packing checklist in the sidebar"""
    st.sidebar.subheader("🎒 Packing Checklist")
    
    items = [
        "👕 Clothes",
        "🩴 Comfortable Footwear",
        "🕶️ Sunglasses & Sunscreen",
        "📖 Travel Guidebook",
        "💊 Medications & First-Aid",
        "📱 Phone Charger & Power Bank",
        "🪪 Passport & ID",
        "💳 Credit Cards & Cash"
    ]
    
    for item in items:
        st.sidebar.checkbox(item, key=f"pack_{item}")


def render_travel_essentials():
    """Render travel essentials checklist"""
    st.sidebar.subheader("🛂 Travel Essentials")
    
    visa = st.sidebar.checkbox("🛃 Check Visa Requirements")
    insurance = st.sidebar.checkbox("🛡️ Get Travel Insurance")
    currency = st.sidebar.checkbox("💱 Currency Exchange Info")
    
    return {
        "visa_required": visa,
        "travel_insurance": insurance,
        "currency_converter": currency
    }