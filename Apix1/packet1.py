import requests

def call_x(event=None,context=None):
    r = requests.get("https://www.google.com")
    if r.status_code == 200:
        return " Okyung was here!!"
print ("Okyung was here!!")
