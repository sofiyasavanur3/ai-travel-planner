"""
Utility functions for formatting data like dates, times, prices, etc.
"""

from datetime import datetime


def format_datetime(iso_string):
    """
    Format datetime string to readable format.
    
    Args:
        iso_string: ISO formatted datetime string
        
    Returns:
        Formatted datetime string (e.g., "Mar-06, 2025 | 6:20 PM")
    """
    if not iso_string or iso_string == "N/A":
        return "N/A"
    
    try:
        # Try multiple datetime formats
        formats = [
            "%Y-%m-%d %H:%M",
            "%Y-%m-%dT%H:%M:%S",
            "%Y-%m-%d %H:%M:%S",
            "%Y-%m-%dT%H:%M:%S.%fZ",
            "%Y-%m-%dT%H:%M:%S%z"
        ]
        
        for fmt in formats:
            try:
                dt = datetime.strptime(iso_string, fmt)
                return dt.strftime("%b-%d, %Y | %I:%M %p")
            except ValueError:
                continue
        
        # If no format matches, return the original string
        return iso_string
        
    except Exception:
        return "N/A"


def format_duration(minutes):
    """
    Convert minutes to hours and minutes format.
    
    Args:
        minutes: Duration in minutes
        
    Returns:
        Formatted duration string (e.g., "2h 30m")
    """
    if not minutes or minutes == "N/A":
        return "N/A"
    
    try:
        minutes = int(minutes)
        hours = minutes // 60
        mins = minutes % 60
        
        if hours > 0 and mins > 0:
            return f"{hours}h {mins}m"
        elif hours > 0:
            return f"{hours}h"
        else:
            return f"{mins}m"
            
    except (ValueError, TypeError):
        return str(minutes)


def format_price(price):
    """
    Format price with currency symbol.
    
    Args:
        price: Price value (can be int, float, or string)
        
    Returns:
        Formatted price string (e.g., "₹12,500")
    """
    if not price or price == "Not Available":
        return "Not Available"
    
    try:
        # Remove any existing currency symbols and commas
        if isinstance(price, str):
            price = price.replace("₹", "").replace(",", "").strip()
        
        price_float = float(price)
        return f"₹{price_float:,.0f}"
        
    except (ValueError, TypeError):
        return str(price)


def format_airport_code(code, name=None):
    """
    Format airport code with optional name.
    
    Args:
        code: Airport IATA code
        name: Airport name (optional)
        
    Returns:
        Formatted airport string
    """
    if not code:
        return "Unknown"
    
    if name:
        return f"{code} ({name})"
    
    return code


def truncate_text(text, max_length=100):
    """
    Truncate text to specified length with ellipsis.
    
    Args:
        text: Text to truncate
        max_length: Maximum length
        
    Returns:
        Truncated text
    """
    if not text:
        return ""
    
    if len(text) <= max_length:
        return text
    
    return text[:max_length-3] + "..."