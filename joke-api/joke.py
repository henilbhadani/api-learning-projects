import requests

url = "https://official-joke-api.appspot.com/random_joke"

try:
    r = requests.get(url)

    if r.status_code == 200:
        data = r.json()
        print("Here's a joke:\n")
        print(data["setup"])
        print(data["punchline"])
    else:
        print("API error")

except Exception as e:
    print("something went wrong:",e)