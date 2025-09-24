
import os
from dotenv import load_dotenv, find_dotenv
from openai import AsyncOpenAI
from agents import OpenAIChatCompletionsModel

# --- Load environment variables ---
load_dotenv(find_dotenv())

# --- API Key ---
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
if not OPENROUTER_API_KEY:
    raise ValueError("❌ OPENROUTER_API_KEY is not set. Please add it to your .env file.")

# --- OpenRouter Client ---
external_client = AsyncOpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)

# --- model Configuration ---
model = OpenAIChatCompletionsModel(model="anthropic/claude-3-haiku:beta", openai_client=external_client)

# --- Agent Defaults ---
AGENT_TEMPERATURE = 0.7
AGENT_MAX_TOKENS = 2000

# --- Travel Defaults ---
DEFAULT_BUDGET = 1000
DEFAULT_TRIP_DURATION = 7  # days
MAX_TRAVELERS = 4
DEFAULT_DEPARTURE_CITY = "New York"
DEFAULT_DESTINATION_CITY = "Paris"
DEFAULT_ACCOMMODATION_TYPE = "hotel"
DEFAULT_TRANSPORTATION_TYPE = "flight"
DEFAULT_ACTIVITY_PREFERENCES = ["sightseeing", "food", "culture"]

# --- External API Endpoints ---
FLIGHT_API_ENDPOINT = "https://api.example.com/flights"
HOTEL_API_ENDPOINT = "https://api.example.com/hotels"
WEATHER_API_ENDPOINT = "https://api.example.com/weather"
