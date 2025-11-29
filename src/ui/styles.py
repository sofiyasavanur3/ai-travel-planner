"""
CSS styles for the Travel Planner UI.
"""


def get_custom_css():
    """
    Return custom CSS styles for the application.
    
    Returns:
        CSS string to be injected into Streamlit
    """
    return """
    <style>
        /* Main title styling */
        .title {
            text-align: center;
            font-size: 36px;
            font-weight: bold;
            color: #ff5733;
            margin-bottom: 10px;
        }
        
        /* Subtitle styling */
        .subtitle {
            text-align: center;
            font-size: 20px;
            color: #555;
            margin-bottom: 30px;
        }
        
        /* Slider styling */
        .stSlider > div {
            background-color: #f9f9f9;
            padding: 10px;
            border-radius: 10px;
        }
        
        /* Flight card container */
        .flight-card {
            border: 2px solid #ddd;
            border-radius: 10px;
            padding: 15px;
            text-align: center;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
            background-color: #f9f9f9;
            margin-bottom: 20px;
            transition: transform 0.2s;
        }
        
        .flight-card:hover {
            transform: translateY(-5px);
            box-shadow: 4px 4px 15px rgba(0, 0, 0, 0.2);
        }
        
        /* Airline logo */
        .airline-logo {
            width: 80px;
            height: 80px;
            object-fit: contain;
            margin-bottom: 10px;
        }
        
        /* Price styling */
        .price {
            color: #008000;
            font-size: 24px;
            font-weight: bold;
            margin: 15px 0;
        }
        
        /* Book button */
        .book-button {
            display: inline-block;
            padding: 10px 20px;
            font-size: 16px;
            font-weight: bold;
            color: #fff;
            background-color: #007bff;
            text-decoration: none;
            border-radius: 5px;
            margin-top: 10px;
            transition: background-color 0.3s;
        }
        
        .book-button:hover {
            background-color: #0056b3;
        }
        
        /* Welcome banner */
        .welcome-banner {
            text-align: center;
            padding: 15px;
            background-color: #ffecd1;
            border-radius: 10px;
            margin-top: 20px;
            margin-bottom: 30px;
        }
        
        /* Section headers */
        .section-header {
            font-size: 24px;
            font-weight: bold;
            color: #333;
            margin-top: 30px;
            margin-bottom: 15px;
            border-bottom: 2px solid #ff5733;
            padding-bottom: 10px;
        }
        
        /* Info box */
        .info-box {
            background-color: #e7f3ff;
            border-left: 4px solid #2196F3;
            padding: 15px;
            margin: 15px 0;
            border-radius: 5px;
        }
        
        /* Warning box */
        .warning-box {
            background-color: #fff3cd;
            border-left: 4px solid #ffc107;
            padding: 15px;
            margin: 15px 0;
            border-radius: 5px;
        }
        
        /* Success box */
        .success-box {
            background-color: #d4edda;
            border-left: 4px solid #28a745;
            padding: 15px;
            margin: 15px 0;
            border-radius: 5px;
        }
        
        /* Hide Streamlit branding */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        
        /* Custom scrollbar */
        ::-webkit-scrollbar {
            width: 10px;
        }
        
        ::-webkit-scrollbar-track {
            background: #f1f1f1;
        }
        
        ::-webkit-scrollbar-thumb {
            background: #888;
            border-radius: 5px;
        }
        
        ::-webkit-scrollbar-thumb:hover {
            background: #555;
        }
    </style>
    """


def get_welcome_banner(travel_theme, destination):
    """
    Create a welcome banner HTML.
    
    Args:
        travel_theme: Selected travel theme
        destination: Destination code/name
        
    Returns:
        HTML string for welcome banner
    """
    return f"""
    <div class="welcome-banner">
        <h3>🌟 Your {travel_theme} to {destination} is about to begin! 🌟</h3>
        <p>Let's find the best flights, stays, and experiences for your unforgettable journey.</p>
    </div>
    """