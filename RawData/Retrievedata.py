import requests
import json
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from config import API_KEYS

API_BASE_URL = "https://api.polygon.io/v3/reference/exchanges"
REQUEST_DELAY = 1  # seconds between requests

def fetch_exchange_data(api_key, start_time, end_time, page=1):
    """Fetch data from the Polygon.io exchanges endpoint using a specific API key with pagination."""
    request_url = f"{API_BASE_URL}?apiKey={api_key}&start_date={start_time}&end_date={end_time}&page={page}"
    try:
        response = requests.get(request_url)

        if response.status_code == 200:
            data = response.json().get("results", [])
            next_page = response.json().get("next_page", None)
            return data, next_page
        elif response.status_code == 429:
            print("Rate limit reached. Pausing for cooldown...")
            time.sleep(60)
            return fetch_exchange_data(api_key, start_time, end_time, page)
        else:
            print(f"Unexpected Error {response.status_code}: {response.text}")
            return [], None
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return [], None

def collect_exchange_data(start_time, end_time):
    """Retrieve exchange data using multiple API keys with parallel requests."""
    all_exchange_data = []
    key_index = 0
    total_records = 0
    page = 1

    # Use a ThreadPoolExecutor to parallelize the fetch calls
    with ThreadPoolExecutor(max_workers=10) as executor:
        future_to_api_key = {}

        while total_records < 100000:
            current_api_key = API_KEYS[key_index]
            print(f"\nFetching with API key {key_index + 1}/{len(API_KEYS)}...")

            # Submit the fetch task to the executor
            future = executor.submit(fetch_exchange_data, current_api_key, start_time, end_time, page)
            future_to_api_key[future] = current_api_key

            # Increment API key index
            key_index = (key_index + 1) % len(API_KEYS)

            # Check results as they are completed
            for future in as_completed(future_to_api_key):
                data, next_page = future.result()

                if data:
                    all_exchange_data.extend(data)
                    total_records += len(data)
                    print(f"Retrieved {len(data)} records using API key {future_to_api_key[future]} (Total: {total_records})")

                    # Update page number if necessary
                    if next_page:
                        page = next_page
                    else:
                        page = 1  # Reset page when no more pages

            # Delay between requests to avoid hitting rate limits
            time.sleep(REQUEST_DELAY)

    return all_exchange_data

def save_to_file(data, filename="exchange_data.json"):
    """Save the retrieved exchange data to a JSON file."""
    with open(filename, "w") as output_file:
        json.dump(data, output_file, indent=4)
    print(f"Data successfully saved to {filename}")

if __name__ == "__main__":
    start_time = input("Enter the start date (YYYY-MM-DD): ")
    end_time = input("Enter the end date (YYYY-MM-DD): ")

    print("Starting data collection for exchanges...")
    exchange_data = collect_exchange_data(start_time, end_time)
    save_to_file(exchange_data)
    print("Exchange data collection completed.")
