import requests
import os
 
# URL of the file to download
file_url = 'https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf'
 
# Directory where you want to save the file
save_directory = '.github/workflows/output'
 
# Create the directory if it doesn't exist
if not os.path.exists(save_directory):
    os.makedirs(save_directory)
 
# Get the file name from the URL
file_name = os.path.basename(file_url)
 
# Full path to save the file
file_path = os.path.join(save_directory, file_name)
 
# Send a GET request to the URL
response = requests.get(file_url)
 
# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Open the file in binary write mode and save the content
    with open(file_path, 'wb') as f:
        f.write(response.content)
    print(f"File downloaded successfully and saved as {file_path}")
else:
    print("Failed to download file")

if __name__ == "__main__":
    url = sys.argv[1]
    output_file = sys.argv[2]
