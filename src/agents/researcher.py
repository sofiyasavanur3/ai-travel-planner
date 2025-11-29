"""
Research agent for gathering destination information.
"""

from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.serpapi_tools import SerpApiTools


class ResearchAgent:
    """Agent for researching travel destinations"""
    
    def __init__(self, gemini_model: str, serpapi_key: str):
        """
        Initialize research agent.
        
        Args:
            gemini_model: Gemini model ID
            serpapi_key: SerpAPI key
        """
        self.agent = Agent(
            name="Travel Researcher",
            instructions=[
                "You are an expert travel researcher.",
                "Identify the travel destination specified by the user.",
                "Gather detailed information on the destination including:",
                "  - Climate and best time to visit",
                "  - Culture and local customs",
                "  - Safety tips and travel advisories",
                "  - Popular attractions and landmarks",
                "  - Must-visit places and hidden gems",
                "Search for activities that match the user's interests and travel style.",
                "Prioritize information from reliable sources and official travel guides.",
                "Provide well-structured summaries with key insights and recommendations.",
                "Keep responses concise but informative.",
                "Format your response in a readable way with clear sections."
            ],
            model=Gemini(id=gemini_model),
            tools=[SerpApiTools(api_key=serpapi_key)],
            add_datetime_to_instructions=True,
            markdown=True
        )
    
    def research_destination(
        self,
        destination: str,
        num_days: int,
        travel_theme: str,
        activity_preferences: str,
        budget: str
    ) -> str:
        """
        Research a travel destination.
        
        Args:
            destination: Destination city/location
            num_days: Number of days for the trip
            travel_theme: Type of trip (couple, family, adventure, solo)
            activity_preferences: User's activity preferences
            budget: Budget preference (economy, standard, luxury)
            
        Returns:
            Research results as text
        """
        prompt = f"""
Research the best attractions and activities in {destination} for a {num_days}-day {travel_theme.lower()} trip.

Travel Preferences:
- Activities interested in: {activity_preferences}
- Budget: {budget}
- Trip duration: {num_days} days

Please provide:
1. Overview of {destination} (climate, culture, best time to visit)
2. Top 5-7 must-visit attractions suitable for this trip type
3. Recommended activities based on preferences
4. Local dining recommendations
5. Safety tips and travel advice
6. Estimated daily budget for activities

Keep the response well-organized and practical.
"""
        
        try:
            response = self.agent.run(prompt, stream=False)
            return response.content if hasattr(response, 'content') else str(response)
        except Exception as e:
            return f"Error researching destination: {str(e)}"