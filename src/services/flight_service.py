"""
Flight service for searching and managing flight data.
"""

from serpapi import GoogleSearch
from typing import Dict, List, Optional
import streamlit as st


class FlightService:
    """Service for handling flight searches and data"""
    
    def __init__(self, api_key: str):
        """
        Initialize flight service.
        
        Args:
            api_key: SerpAPI key
        """
        self.api_key = api_key
    
    def search_flights(
        self,
        source: str,
        destination: str,
        departure_date: str,
        return_date: str,
        currency: str = "INR",
        language: str = "en"
    ) -> Dict:
        """
        Search for flights using Google Flights via SerpAPI.
        
        Args:
            source: Departure airport IATA code
            destination: Arrival airport IATA code
            departure_date: Departure date (YYYY-MM-DD)
            return_date: Return date (YYYY-MM-DD)
            currency: Currency code (default: INR)
            language: Language code (default: en)
            
        Returns:
            Dictionary containing flight search results
        """
        try:
            params = {
                "engine": "google_flights",
                "departure_id": source.upper(),
                "arrival_id": destination.upper(),
                "outbound_date": str(departure_date),
                "return_date": str(return_date),
                "currency": currency,
                "hl": language,
                "api_key": self.api_key
            }
            
            search = GoogleSearch(params)
            results = search.get_dict()
            
            return results
            
        except Exception as e:
            st.error(f"Error fetching flights: {str(e)}")
            return {}
    
    def extract_best_flights(self, flight_data: Dict, limit: int = 3) -> List[Dict]:
        """
        Extract the best (cheapest) flights from search results.
        
        Args:
            flight_data: Flight search results
            limit: Maximum number of flights to return
            
        Returns:
            List of best flight options
        """
        try:
            best_flights = flight_data.get("best_flights", [])
            
            if not best_flights:
                return []
            
            # Sort by price and get top N
            sorted_flights = sorted(
                best_flights,
                key=lambda x: x.get("price", float("inf"))
            )[:limit]
            
            return sorted_flights
            
        except Exception as e:
            st.error(f"Error extracting flights: {str(e)}")
            return []
    
    def get_flight_details(self, flight: Dict) -> Dict:
        """
        Extract detailed information from a flight object.
        
        Args:
            flight: Flight object from search results
            
        Returns:
            Dictionary with formatted flight details
        """
        try:
            flights_info = flight.get("flights", [{}])
            
            # Get first and last flight for departure and arrival info
            first_flight = flights_info[0] if flights_info else {}
            last_flight = flights_info[-1] if flights_info else {}
            
            departure_airport = first_flight.get("departure_airport", {})
            arrival_airport = last_flight.get("arrival_airport", {})
            
            details = {
                "airline": first_flight.get("airline", "Unknown Airline"),
                "airline_logo": flight.get("airline_logo", ""),
                "price": flight.get("price", "Not Available"),
                "total_duration": flight.get("total_duration", "N/A"),
                "departure_time": departure_airport.get("time", "N/A"),
                "departure_airport": departure_airport.get("id", "N/A"),
                "departure_airport_name": departure_airport.get("name", "N/A"),
                "arrival_time": arrival_airport.get("time", "N/A"),
                "arrival_airport": arrival_airport.get("id", "N/A"),
                "arrival_airport_name": arrival_airport.get("name", "N/A"),
                "layovers": len(flights_info) - 1 if len(flights_info) > 1 else 0,
                "departure_token": flight.get("departure_token", ""),
                "booking_token": flight.get("booking_token", "")
            }
            
            return details
            
        except Exception as e:
            st.error(f"Error getting flight details: {str(e)}")
            return {}
    
    def get_booking_link(
        self,
        flight: Dict,
        source: str,
        destination: str,
        departure_date: str,
        return_date: str
    ) -> str:
        """
        Get booking link for a specific flight.
        
        Args:
            flight: Flight object
            source: Departure airport code
            destination: Arrival airport code
            departure_date: Departure date
            return_date: Return date
            
        Returns:
            Booking URL or "#" if not available
        """
        try:
            departure_token = flight.get("departure_token", "")
            
            if not departure_token:
                return "#"
            
            # Make another API call with departure token to get booking link
            params = {
                "engine": "google_flights",
                "departure_id": source.upper(),
                "arrival_id": destination.upper(),
                "outbound_date": str(departure_date),
                "return_date": str(return_date),
                "currency": "INR",
                "hl": "en",
                "api_key": self.api_key,
                "departure_token": departure_token
            }
            
            search = GoogleSearch(params)
            results = search.get_dict()
            
            # Try to get booking token
            best_flights = results.get("best_flights", [])
            if best_flights and len(best_flights) > 0:
                booking_token = best_flights[0].get("booking_token", "")
                if booking_token:
                    return f"https://www.google.com/travel/flights?tfs={booking_token}"
            
            return "#"
            
        except Exception as e:
            st.warning(f"Could not fetch booking link: {str(e)}")
            return "#"
    
    def search_and_extract(
        self,
        source: str,
        destination: str,
        departure_date: str,
        return_date: str,
        limit: int = 3
    ) -> List[Dict]:
        """
        Convenience method to search and extract best flights in one call.
        
        Args:
            source: Departure airport code
            destination: Arrival airport code
            departure_date: Departure date
            return_date: Return date
            limit: Number of flights to return
            
        Returns:
            List of flight details dictionaries
        """
        # Search for flights
        flight_data = self.search_flights(
            source, destination, departure_date, return_date
        )
        
        # Extract best flights
        best_flights = self.extract_best_flights(flight_data, limit)
        
        # Get detailed information for each flight
        detailed_flights = []
        for flight in best_flights:
            details = self.get_flight_details(flight)
            if details:
                detailed_flights.append(details)
        
        return detailed_flights