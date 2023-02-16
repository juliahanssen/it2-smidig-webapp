import requests

def hent_temp(lat, lon):
    url = f"https://api.met.no/weatherapi/locationforecast/2.0/complete?lat={lat}&lon={lon}"
    respons = requests.get(url, headers={"User-agent": "Julias mac"})
    data = respons.json()
    temperatur = data["properties"]["timeseries"][0]["data"]["instant"]["details"]["air_temperature"]
    return temperatur
