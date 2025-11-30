# 🌍 AI-Powered Travel Planner

**Track:** Concierge Agents  
**Kaggle AI Agents Intensive - Capstone Project**

## 📝 Problem Statement

**The Challenge:**  
Planning a trip is overwhelming and time-consuming. Travelers must:
- Compare hundreds of flight options across multiple websites
- Research destinations, attractions, and local customs
- Find suitable hotels and restaurants that match their preferences
- Create day-by-day itineraries that optimize time and budget
- Coordinate all this information into a coherent travel plan

This process typically takes 10-15 hours per trip and often results in suboptimal choices due to information overload.

**Why This Matters:**  
With over 1.4 billion international trips taken annually, inefficient travel planning wastes billions of collective hours and leads to disappointing vacations due to poor planning.

---

## 💡 Solution

An **AI-powered multi-agent system** that automates the entire travel planning process in minutes instead of hours. The system uses specialized AI agents that work together to:

1. **Search and compare flights** in real-time across multiple airlines
2. **Research destinations** with AI-powered insights on attractions, culture, and safety
3. **Find hotels and restaurants** tailored to traveler preferences and budget
4. **Generate personalized itineraries** with optimal scheduling and cost estimates

**Why Agents?**  
Multi-agent architecture is ideal for travel planning because:
- **Specialization**: Each agent focuses on one domain (flights, research, accommodations, planning)
- **Parallel Processing**: Multiple agents can work simultaneously to reduce wait time
- **Modularity**: Easy to update or replace individual agents without affecting the system
- **Scalability**: Can add new agents (e.g., visa checker, weather forecaster) without rewriting existing code

---

## 🏗️ Architecture

### **Multi-Agent System Design**

```
┌─────────────────────────────────────────────────────────────┐
│                     User Interface (Streamlit)               │
│  - Input: Dates, Destinations, Preferences, Budget          │
│  - Output: Comprehensive Travel Plan                        │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                    Orchestration Layer                       │
│              (Main Application Controller)                   │
└──┬────────────┬────────────┬────────────┬──────────────────┘
   │            │            │            │
   ▼            ▼            ▼            ▼
┌──────┐   ┌──────────┐  ┌────────┐  ┌──────────┐
│Flight│   │ Research │  │ Finder │  │ Planner  │
│Service   │  Agent   │  │ Agent  │  │  Agent   │
└──┬───┘   └────┬─────┘  └───┬────┘  └────┬─────┘
   │            │            │            │
   │            │            │            │
   ▼            ▼            ▼            ▼
┌─────────────────────────────────────────────────┐
│            External APIs & Tools                 │
│  - SerpAPI (Google Flights)                     │
│  - Google Gemini (AI Models)                    │
│  - SerpAPI Search (Web Research)                │
└─────────────────────────────────────────────────┘
```

### **Agent Descriptions**

#### 1. **Flight Service** (Tool-based Agent)
- **Purpose**: Real-time flight search and price comparison
- **Tools**: SerpAPI Google Flights integration
- **Output**: Top 3 cheapest flight options with booking links
- **Features**: 
  - Real-time pricing
  - Multiple airline comparison
  - Direct booking link generation

#### 2. **Research Agent** (LLM-powered Agent)
- **Model**: Google Gemini 1.5 Flash
- **Purpose**: Destination research and attraction discovery
- **Tools**: SerpAPI web search
- **Output**: Comprehensive destination guide including:
  - Climate and best visiting times
  - Cultural insights and customs
  - Safety tips and travel advisories
  - Top attractions and hidden gems
  - Activity recommendations based on preferences

#### 3. **Finder Agent** (LLM-powered Agent)
- **Model**: Google Gemini 1.5 Flash
- **Purpose**: Hotel and restaurant recommendations
- **Tools**: SerpAPI web search
- **Output**: Curated list of:
  - 3-5 hotels matching budget and rating preferences
  - 5-7 restaurants with diverse cuisine options
  - Location-based recommendations near attractions

#### 4. **Planner Agent** (LLM-powered Agent)
- **Model**: Google Gemini 1.5 Pro
- **Purpose**: Itinerary creation and optimization
- **Input**: Research data, hotel data, user preferences
- **Output**: Day-by-day itinerary with:
  - Morning, afternoon, evening activities
  - Transportation suggestions
  - Time allocation and cost estimates
  - Rest periods and flexible time

---

## 🎯 Key Features Implemented

### ✅ **Course Concepts Applied** (3+ Required)

1. **Multi-Agent System** ✓
   - 4 specialized agents (Flight Service, Research, Finder, Planner)
   - Sequential agent execution with data passing
   - Orchestrated by main application controller

2. **Tools Integration** ✓
   - **MCP-like pattern**: Structured service interfaces
   - **Custom Tools**: FlightService with booking link generation
   - **Built-in Tools**: SerpAPI for web search and Google Flights
   - **LLM Tools**: Google Gemini integration via Phi framework

3. **Sessions & State Management** ✓
   - Streamlit session state for caching API results
   - User preference persistence across interactions
   - Form state management for multi-step input

4. **Context Engineering** ✓
   - Structured prompts with clear instructions for each agent
   - Context passing between agents (research → planner)
   - Prompt optimization for token efficiency

5. **Observability** ✓
   - Real-time status indicators (spinners) for each agent
   - Error handling and user-friendly error messages
   - Progress tracking through multi-step process

---

## 🚀 Setup Instructions

### **Prerequisites**
- Python 3.8 or higher
- pip (Python package manager)
- API Keys:
  - [SerpAPI Key](https://serpapi.com/) (for flight search and web research)
  - [Google AI Studio API Key](https://aistudio.google.com/app/apikey) (for Gemini models)

### **Installation**

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/ai-travel-planner.git
cd ai-travel-planner
```

2. **Create virtual environment** (recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure API Keys**

Create `.streamlit/secrets.toml`:
```toml
SERPAPI_KEY = "your_serpapi_key_here"
GOOGLE_API_KEY = "your_google_api_key_here"
```

**⚠️ IMPORTANT**: Never commit API keys to Git. The `.gitignore` file already excludes this file.

5. **Run the application**
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

---

## 📊 Project Structure

```
ai-travel-planner/
├── .streamlit/
│   └── secrets.toml              # API keys (not in Git)
├── src/
│   ├── __init__.py
│   ├── config/
│   │   ├── __init__.py
│   │   └── settings.py           # Configuration management
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── researcher.py         # Research Agent
│   │   ├── planner.py            # Planner Agent
│   │   └── finder.py             # Finder Agent
│   ├── services/
│   │   ├── __init__.py
│   │   └── flight_service.py     # Flight search service
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── formatters.py         # Data formatting utilities
│   │   ├── validators.py         # Input validation
│   │   └── cache_helper.py       # API response caching
│   └── ui/
│       ├── __init__.py
│       ├── styles.py             # CSS styling
│       ├── components.py         # Reusable UI components
│       └── sidebar.py            # Sidebar configuration
├── app.py                        # Main application
├── requirements.txt              # Python dependencies
├── .gitignore                    # Git ignore rules
└── README.md                     # This file
```

---

## 💻 Usage Guide

### **Step 1: Enter Travel Details**
- Departure city (IATA code, e.g., BOM for Mumbai)
- Destination city (IATA code, e.g., DEL for Delhi)
- Trip duration (1-14 days)
- Travel theme (Couple, Family, Adventure, Solo)
- Departure and return dates
- Activity preferences

### **Step 2: Customize Preferences (Sidebar)**
- Budget level (Economy, Standard, Luxury)
- Flight class (Economy, Business, First Class)
- Hotel rating preference
- Travel essentials checklist

### **Step 3: Generate Plan**
Click "🚀 Generate Travel Plan" and wait 30-60 seconds while agents work.

### **Step 4: Review Results**
- **Flights**: Top 3 cheapest options with booking links
- **Destination Research**: Comprehensive guide with attractions
- **Hotels & Restaurants**: Curated recommendations
- **Itinerary**: Day-by-day schedule with activities and costs

### **Step 5: Download**
Click "📥 Download Complete Travel Plan" to save as text file.

---

## 🎥 Demo

### **Demo Scenario**
- **Route**: Mumbai (BOM) → Delhi (DEL)
- **Duration**: 5 days
- **Theme**: Couple Getaway
- **Budget**: Standard
- **Result**: Complete travel plan generated in 45 seconds

---

## 🧪 Technical Implementation Details

### **Agent Communication Pattern**
```python
# Sequential agent execution with data passing
flights = flight_service.search_and_extract(...)
research = researcher.research_destination(...)
hotels = finder.find_accommodations(...)
itinerary = planner.create_itinerary(
    research_data=research,
    hotel_data=hotels
)
```

### **Error Handling**
- Input validation before API calls
- Graceful degradation if agents fail
- User-friendly error messages
- Fallback options for missing data

### **Performance Optimization**
- Session-based caching to reduce API calls
- Parallel-ready architecture (can be extended)
- Lightweight UI with efficient rendering
- Token-optimized prompts

---

## 📈 Impact & Value

### **Time Savings**
- **Traditional Planning**: 10-15 hours per trip
- **With AI Travel Planner**: 2-3 minutes
- **Time Saved**: ~97% reduction in planning time

### **Cost Optimization**
- Real-time flight price comparison
- Budget-aware recommendations
- Optimal itinerary scheduling reduces waste

### **User Experience**
- Single interface for all planning needs
- Personalized recommendations
- Professional-quality itineraries
- Downloadable plans for offline reference

---

## 🔮 Future Enhancements

1. **Additional Agents**
   - Visa requirement checker
   - Weather forecaster
   - Currency exchange advisor
   - Travel insurance recommender

2. **Enhanced Features**
   - Multi-city trip support
   - Group travel coordination
   - Real-time price alerts
   - Booking integration

3. **Deployment**
   - Cloud deployment (Vertex AI Agent Engine)
   - Mobile app version
   - API for third-party integration

4. **Advanced Capabilities**
   - A2A protocol for agent-to-agent communication
   - Long-running operations with pause/resume
   - Memory banks for returning users
   - Advanced evaluation metrics

---

## 🛠️ Technologies Used

- **Frontend**: Streamlit
- **Backend**: Python 3.8+
- **AI Framework**: Phi Data (phidata)
- **LLM**: Google Gemini (1.5 Flash, 1.5 Pro)
- **APIs**: SerpAPI (Google Flights, Web Search)
- **Architecture**: Multi-agent system with orchestration layer

---

## 🙏 Acknowledgments

- Google AI Agents Intensive Course
- Kaggle for hosting the competition
- Phi Data framework developers
- Streamlit community

---

## 📞 Contact

- GitHub: 
- Email: sofiyasavanur3@gmail.com
- LinkedIn: 

---

**Built with ❤️ for the Kaggle AI Agents Intensive Capstone Project**
