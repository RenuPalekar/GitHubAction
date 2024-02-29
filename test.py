import json
import sys
 
def fetch_data(json_file, key):
    with open(json_file, 'r') as f:
        data = json.load(f)
        if key in data:
            return data[key]
        else:
            return f"No data found for key: {key}"
 
if __name__ == "__main__":
    json_file = sys.argv[1]
    key = sys.argv[2]
    result = fetch_data(json_file, key)
    print(result)
FooterHPE: Social coding
Hewlett Packard Enterprise
HPE: Social coding
HPE: Social coding
Hewlett Packard Enterprise
