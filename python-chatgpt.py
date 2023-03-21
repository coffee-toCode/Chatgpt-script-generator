#command line template: python .\python-chatgpt.py "" ".py"

# Import the required libraries
import requests
import argparse
from dotenv import load_dotenv
import os

# Load the environment variables from the .env file
load_dotenv()

# Define the command line arguments that the script accepts
parser = argparse.ArgumentParser()
parser.add_argument("prompt", help="The prompt to send to the OpenAI API")
parser.add_argument("file_name", help="Name the file")
args = parser.parse_args()


# Set the API endpoint URL and get the OpenAI API key from the environment variable
api_endpoint = "https://api.openai.com/v1/completions"
api_key = os.getenv("OPENAI_API_KEY")


# Set the request headers to include content type and authorization token
request_headers = {
   "Content-Type": "application/json", 
   "Authorization": "Bearer " + api_key
   }



# Set the request data to include the OpenAI model(which can be changed based on use case), the prompt, and other generation parameters
request_data = {
   "model": "text-davinci-003",
   "prompt": f"write python script to {args.prompt}. Provide only the code, no text.",
   "max_tokens": 100,
   "temperature": 0.2
   }
   


# Send a POST request to the OpenAI API with the request headers and data, and store the response within this variable.
response = requests.post(api_endpoint, headers= request_headers, json = request_data)




# If the response status code is OK (200), save the generated code in a file
if response.status_code == 200:
   response_text = response.json()["choices"][0]["text"]
   with open(args.file_name, "w") as file:
      file.write(response_text)

# Otherwise, print an error message with the status code
else:
   print("request failed with status code: " + str(response.status_code))
