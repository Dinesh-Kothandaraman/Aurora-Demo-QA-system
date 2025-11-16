import requests

BASE = "http://127.0.0.1:8080/ask"
q = "When and where Sophia want to book a private jet?"

try:
    r = requests.get(BASE, params={"q": q})
    r.raise_for_status()
    data = r.json()
except requests.exceptions.RequestException as e:
    print("Request failed:", e)
    data = None
except ValueError:
    print("Server returned non-JSON response")
    data = None

print(q, "->", data)
