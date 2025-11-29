"""
Planner agent for creating travel itineraries.
"""

from phi.agent import Agent
from phi.model.google import Gemini


class PlannerAgent:
    """Agent for creating detailed travel itineraries"""
    
    def __init__(self, gemini_model: str):
        """
        Initialize planner agent.
        
        Args:
            gemini_model: Gemini model ID
        """
        self.agent = Agent(
            name="Travel Planner",
            instructions=[
                "You are an expert travel itinerary planner.",
                "Create detailed, day-by-day itineraries based on user preferences.",
                "Gather details about travel preferences, budget, and interests.",
                "Create realistic schedules with appropriate time allocations.",
                "Include transportation options and estimated travel times between locations.",
                "Suggest optimal timing for activities (morning, afternoon, evening).",
                "Provide estimated costs for activities and meals.",
                "Balance the itinerary - don't overpack the schedule.",
                "Include time for rest and spontaneous exploration.",
                "Consider opening hours and booking requirements.",
                "Present the itinerary in a clear, day-by-day structured format.",
                "Use bullet points and clear formatting for readability."
            ],
            model=Gemini(id=gemini_model),
            add_datetime_to_instructions=True,
            markdown=True
        )
    
    def create_itinerary(
        self,
        destination: str,
        num_days: int,
        travel_theme: str,
        activity_preferences: str,
        budget: str,
        research_data: str,
        hotel_data: str
    ) -> str:
        """
        Create a detailed travel itinerary.
        
        Args:
            destination: Destination city/location
            num_days: Number of days for the trip
            travel_theme: Type of trip
            activity_preferences: User's preferences
            budget: Budget preference
            research_data: Research results from research agent
            hotel_data: Hotel and restaurant data
            
        Returns:
            Detailed itinerary as text
        """
        prompt = f"""
Create a detailed {num_days}-day itinerary for a {travel_theme.lower()} trip to {destination}.

Travel Details:
- Duration: {num_days} days
- Trip Type: {travel_theme}
- Activities preferred: {activity_preferences}
- Budget: {budget}

Research Data:
{research_data}

Hotels & Restaurants:
{hotel_data}

Please create a day-by-day itinerary with:
- Morning, afternoon, and evening activities for each day
- Specific attractions to visit with estimated time needed
- Restaurant recommendations for meals
- Transportation suggestions between locations
- Estimated costs for activities
- Tips for making the most of each day
- One flexible/rest time each day

Format each day clearly with:
**Day X: [Theme/Focus]**
- Morning: [Activity] (Time, Cost, Details)
- Afternoon: [Activity] (Time, Cost, Details)
- Evening: [Activity] (Time, Cost, Details)

Keep it practical, realistic, and exciting!
"""
        
        try:
            response = self.agent.run(prompt, stream=False)
            return response.content if hasattr(response, 'content') else str(response)
        except Exception as e:
            return f"Error creating itinerary: {str(e)}"