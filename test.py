import requests
import json

CODEFILE = "key.txt"
#load the Access Code

with open(CODEFILE, "r") as file:
    ACCESSSCODE = file.readline()


TRIPNAMES = ["405tp01370"]
# Define the endpoint URL
url = "http://wsdot.wa.gov/Traffic/api/TollRates/TollRatesREST.svc/GetTollRatesAsJson?AccessCode={ACCESSCODE}"

try:
    # Send the GET request
    response = requests.get(url)
    
    # Throw an error if the request failed (e.g., 404, 500)
    response.raise_for_status()
    
    # Parse the response body as JSON
    data = response.json()
    
    print("Status Code:", response.status_code)
    #print("Response Data:", data)

except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")
except Exception as err:
    print(f"An error occurred: {err}")

for item in data:
    if item["TripName"] in TRIPNAMES:
        if item["CurrentToll"] == 0: item["CurrentToll"] = "Free"
        print("Found a trip, current Toll is: $",item["CurrentToll"])