"""
Utility functions for validating user inputs.
"""

from datetime import datetime, date


def validate_iata_code(code):
    """
    Validate IATA airport code.
    
    Args:
        code: Airport IATA code
        
    Returns:
        tuple: (is_valid, error_message)
    """
    if not code:
        return False, "Airport code cannot be empty"
    
    code = code.strip().upper()
    
    if len(code) != 3:
        return False, "Airport code must be exactly 3 characters"
    
    if not code.isalpha():
        return False, "Airport code must contain only letters"
    
    return True, None


def validate_dates(departure_date, return_date):
    """
    Validate departure and return dates.
    
    Args:
        departure_date: Departure date
        return_date: Return date
        
    Returns:
        tuple: (is_valid, error_message)
    """
    today = date.today()
    
    # Check if departure date is in the past
    if departure_date < today:
        return False, "Departure date cannot be in the past"
    
    # Check if return date is before departure date
    if return_date < departure_date:
        return False, "Return date must be after departure date"
    
    # Check if trip is too short (at least 1 day)
    if (return_date - departure_date).days < 1:
        return False, "Trip must be at least 1 day long"
    
    # Check if trip is not too far in the future (optional, 1 year limit)
    days_until_departure = (departure_date - today).days
    if days_until_departure > 365:
        return False, "Cannot book flights more than 1 year in advance"
    
    return True, None


def validate_trip_duration(num_days):
    """
    Validate trip duration.
    
    Args:
        num_days: Number of days
        
    Returns:
        tuple: (is_valid, error_message)
    """
    if num_days < 1:
        return False, "Trip duration must be at least 1 day"
    
    if num_days > 30:
        return False, "Trip duration cannot exceed 30 days"
    
    return True, None


def validate_activity_preferences(preferences):
    """
    Validate activity preferences input.
    
    Args:
        preferences: Activity preferences text
        
    Returns:
        tuple: (is_valid, error_message)
    """
    if not preferences or not preferences.strip():
        return False, "Please provide at least one activity preference"
    
    if len(preferences.strip()) < 10:
        return False, "Please provide more details about your activity preferences"
    
    return True, None


def sanitize_input(text):
    """
    Sanitize user input text.
    
    Args:
        text: Input text
        
    Returns:
        Sanitized text
    """
    if not text:
        return ""
    
    # Remove leading/trailing whitespace
    text = text.strip()
    
    # Remove any potentially harmful characters (basic sanitization)
    # In production, use more robust sanitization
    text = text.replace("<", "").replace(">", "")
    
    return text