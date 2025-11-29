"""
Simple caching helper to reduce API calls.
"""

import streamlit as st
import hashlib
import json


def get_cache_key(*args):
    """
    Generate a cache key from arguments.
    
    Args:
        *args: Arguments to create cache key from
        
    Returns:
        Hash string to use as cache key
    """
    key_string = json.dumps(args, sort_keys=True, default=str)
    return hashlib.md5(key_string.encode()).hexdigest()


def get_cached_result(cache_key):
    """
    Get cached result if available.
    
    Args:
        cache_key: Cache key to lookup
        
    Returns:
        Cached result or None
    """
    if 'api_cache' not in st.session_state:
        st.session_state.api_cache = {}
    
    return st.session_state.api_cache.get(cache_key)


def set_cached_result(cache_key, result):
    """
    Store result in cache.
    
    Args:
        cache_key: Cache key
        result: Result to cache
    """
    if 'api_cache' not in st.session_state:
        st.session_state.api_cache = {}
    
    st.session_state.api_cache[cache_key] = result


def clear_cache():
    """Clear all cached results."""
    if 'api_cache' in st.session_state:
        st.session_state.api_cache = {}