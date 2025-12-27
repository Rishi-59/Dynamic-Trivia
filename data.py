import requests

endpoint = "https://opentdb.com/api.php"

parameters = {
    "amount" : 10,
    "type" : "boolean" 
}

print("Fetching question data...")
response = requests.get(url=endpoint,params=parameters,timeout=10)
response.raise_for_status()
data = response.json()

question_data = data["results"]
print("Question data fetched successfully.")
# print(question_data)
