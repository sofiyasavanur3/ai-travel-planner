"""
Configuration settings for the AI Travel Planner application.
Manages API keys and application constants.
"""

import os
import streamlit as st


class Settings:
    """Application settings and configuration"""
    
    def __init__(self):
        """Initialize settings from Streamlit secrets or environment variables"""
        self.load_api_keys()
        self.setup_constants()
    
    def load_api_keys(self):
        """Load API keys from Streamlit secrets or environment variables"""
        try:
            # Try to load from Streamlit secrets first
            self.SERPAPI_KEY = st.secrets["SERPAPI_KEY"]
            self.GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
        except (KeyError, FileNotFoundError):
            # Fallback to environment variables
            self.SERPAPI_KEY = os.getenv("SERPAPI_KEY", "")
            self.GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")
        
        # Set Google API key in environment for google-generativeai
        if self.GOOGLE_API_KEY:
            os.environ["GOOGLE_API_KEY"] = self.GOOGLE_API_KEY
    
    def setup_constants(self):
        """Setup application constants"""
        # Page configuration
        self.PAGE_TITLE = "🌍 AI Travel Planner"
        self.PAGE_LAYOUT = "wide"
        
        # Travel themes
        self.TRAVEL_THEMES = [
            "💑 Couple Getaway",
            "👨‍👩‍👧‍👦 Family Vacation",
            "🏔️ Adventure Trip",
            "🧳 Solo Exploration"
        ]
        
        # Budget options
        self.BUDGET_OPTIONS = ["Economy", "Standard", "Luxury"]
        
        # Flight class options
        self.FLIGHT_CLASS_OPTIONS = ["Economy", "Business", "First Class"]
        
        # Hotel ratings
        self.HOTEL_RATINGS = ["Any", "3⭐", "4⭐", "5⭐"]
        
        # Default values
        self.DEFAULT_SOURCE = "BOM"
        self.DEFAULT_DESTINATION = "DEL"
        self.DEFAULT_TRIP_DURATION = 5
        self.MIN_TRIP_DAYS = 1
        self.MAX_TRIP_DAYS = 14
        
        # API settings
        self.CURRENCY = "INR"
        self.LANGUAGE = "en"
        
        # Gemini models - using multiple models to distribute quota
        self.GEMINI_MODEL_RESEARCH = "gemini-1.5-flash"  # Lighter model for research
        self.GEMINI_MODEL_FINDER = "gemini-1.5-flash"    # Lighter model for finding
        self.GEMINI_MODEL_PLANNER = "gemini-1.5-pro"     # Better model for planning
    
    def validate_keys(self):
        """Validate that required API keys are present"""
        if not self.SERPAPI_KEY:
            st.error("⚠️ SERPAPI_KEY is missing! Please add it to .streamlit/secrets.toml")
            return False
        
        if not self.GOOGLE_API_KEY:
            st.error("⚠️ GOOGLE_API_KEY is missing! Please add it to .streamlit/secrets.toml")
            return False
        
        return True


# Create a global settings instance
settings = Settings()