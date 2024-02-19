import sys
 
def main(url, output_file):
    # Simple message indicating the parameters
    print(f"Downloading file from {url} and saving it to {output_file}")
 
if __name__ == "__main__":
    url = sys.argv[1]
    output_file = sys.argv[2]
    main(url, output_file)
