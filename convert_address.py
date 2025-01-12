import pandas as pd
import requests
import time

def get_coordinates(address, api_key):
    base_url = "https://api.opencagedata.com/geocode/v1/json"
    params = {
        'q': address,
        'key': api_key,
        'limit': 1,
        'countrycode': 'us'
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    
    if response.status_code == 200 and data['results']:
        coordinates = data['results'][0]['geometry']
        return f"{coordinates['lat']}, {coordinates['lng']}"
    else:
        return "Error: Unable to fetch coordinates"

def update_csv_with_coordinates(input_file, output_file, api_key):
    df = pd.read_csv(input_file)
    
    if 'Address' not in df.columns:
        raise ValueError("The CSV file does not have an 'Address' column.")
    
    # df['Coordinates'] = ''
    
    for i, address in enumerate(df['Address']):
        try:
            print(f"Processing address {i + 1}/{len(df)}: {address}")
            if df.at[i, 'Coordinates'] == 'Error: Unable to fetch coordinates': 
                df.at[i, 'Coordinates'] = get_coordinates(address, api_key)
                time.sleep(1)  # To avoid hitting API rate limits
        except Exception as e:
            print(f"Error processing address '{address}': {e}")
    
    df.to_csv(output_file, index=False)
    print(f"Updated CSV saved as: {output_file}")

if __name__ == "__main__":
    input_file = "fuel-prices-with-coordinate.csv" 
    output_file = "fuel-prices-with-coordinates.csv"
    api_key = "e88bb37d1b9d4512b4a671f02f0e1ff4"
    
    update_csv_with_coordinates(input_file, output_file, api_key)
