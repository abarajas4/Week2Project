import requests 
import json


API_KEY = ""
url = f"https://api.spoonacular.com/recipes/complexSearch?apiKey={API_KEY}" \
"&number=1&cuisine=American&addRecipeInstructions=True&instructionsRequired=True&addRecipeInformation=True"

response = requests.get(url)
data = response.json()
print(data)

#for recipe in data['results']:
   #print(recipe["title"])

#testing if Yuneydy can push
