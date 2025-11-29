"""
Finder agent for discovering hotels and restaurants.
"""

from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.serpapi_tools import SerpApiTools


class FinderAgent:
    """Agent for finding hotels and restaurants"""
    
    def __init__(self, gemini_model: str, serpapi_key: str):
        """
        Initialize finder agent.
        
        Args:
            gemini_model: Gemini model ID
            serpapi_key: SerpAPI key
        """
        self.agent = Agent(
            name="Hotel & Restaurant Finder",
            instructions=[
                "You are an expert at finding the best hotels and restaurants.",
                "Identify key locations from the user's travel plans.",
                "Search for highly-rated hotels in convenient locations.",
                "Consider proximity to main attractions and transportation.",
                "Search for top-rated restaurants offering diverse cuisines.",
                "Prioritize results based on user preferences, ratings, and reviews.",
                "Include a range of options for different budgets.",
                "Provide specific names, locations, and brief descriptions.",
                "Mention approximate price ranges.",
                "Include any special features or highlights.",
                "Provide direct booking links or reservation information when available.",
                "Organize recommendations by location or day of itinerary."
            ],
            model=Gemini(id=gemini_model),
            tools=[SerpApiTools(api_key=serpapi_key)],
            add_datetime_to_instructions=True,
            markdown=True
        )
    
    def find_accommodations(
        self,
        destination: str,
        travel_theme: str,
        budget: str,
        hotel_rating: str,
        activity_preferences: str
    ) -> str:
        """
        Find hotels and restaurants for the destination.
        
        Args:
            destination: Destination city/location
            travel_theme: Type of trip
            budget: Budget preference
            hotel_rating: Preferred hotel rating
            activity_preferences: User's preferences
            
        Returns:
            Hotel and restaurant recommendations as text
        """
        prompt = f"""
Find the best hotels and restaurants in {destination} for a {travel_theme.lower()} trip.

Preferences:
- Budget: {budget}
- Hotel Rating: {hotel_rating}
- Activities interested in: {activity_preferences}

Please provide:

**Hotels** (3-5 recommendations):
For each hotel include:
- Name and location
- Star rating and guest rating
- Brief description and highlights
- Approximate price range per night
- Proximity to main attractions
- Special amenities

**Restaurants** (5-7 recommendations):
For each restaurant include:
- Name and location
- Cuisine type
- Brief description
- Approximate price range
- Specialties or must-try dishes
- Atmosphere (casual, fine dining, etc.)

Organize by area/neighborhood if helpful, and include options for different budgets within the {budget} range.
"""
        
        try:
            response = self.agent.run(prompt, stream=False)
            return response.content if hasattr(response, 'content') else str(response)
        except Exception as e:
            return f"Error finding accommodations: {str(e)}"