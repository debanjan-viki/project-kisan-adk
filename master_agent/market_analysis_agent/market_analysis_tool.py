# import requests
import os
import json

def get_market_data():
    # url = "https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070?api-key=579b464db66ec23bdd000001a9bd2679973c4ed84aca051575375f0a&format=json"
    
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, "response.json")
    with open(file_path, 'r') as file:
        response = json.load(file)
    
    if response['status'] == 'ok':
        # response = response.json()
        records = response['records']
        for record in records:
            record['min_price'] = int(record['min_price'])
            record['max_price'] = int(record['max_price'])
            record['modal_price'] = int(record['modal_price'])
        return records
    else:
        raise Exception(f"Error fetching market data: {response.status_code} - {response.text}")
    
def main():
    try:
        market_data = get_market_data()
        print(json.dumps(market_data, indent=4))
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()