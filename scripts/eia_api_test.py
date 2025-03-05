import requests
import pandas as pd
import os
from dotenv import load_dotenv

# Load API key from environment variables
load_dotenv()
API_KEY = os.getenv("EIA_API_KEY")

# Base URL
base_url = "https://api.eia.gov/v2/electricity/electric-power-operational-data/data/"

# Parameters
params = {
    "api_key": API_KEY,
    "frequency": "monthly",
    "data[0]": "generation",
    "facets[fueltypeid][]": "SUN",
    "sort[0][column]": "period",
    "sort[0][direction]": "desc",
    "sort[1][column]": "location",
    "sort[1][direction]": "asc",
    "offset": "0",
    "length": "20" 
}

# Make the request
response = requests.get(base_url, params=params)

# Check if the request was successful
if response.status_code == 200:
    print("nice, that worked.")

else:
    print(f"Error: {response.status_code}")
    print(response.text)