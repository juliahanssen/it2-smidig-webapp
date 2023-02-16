import requests

def hent_temp(lat, lon):
    url = f"https://api.met.no/weatherapi/locationforecast/2.0/complete?lat={lat}&lon={lon}"
    respons = requests.get(url, headers={"User-agent": "Julias mac"})
    data = respons.json()
    temperatur = data["properties"]["timeseries"][0]["data"]["instant"]["details"]["air_temperature"]
    return temperatur


def hent_vaer(lat, lon):
    url = f"https://api.met.no/weatherapi/locationforecast/2.0/complete?lat={lat}&lon={lon}"
    respons = requests.get(url, headers={"User-agent": "Julias mac"})
    data = respons.json()
    vaer =  data["properties"]["timeseries"][0]["data"]["next_12_hours"]["summary"]["symbol_code"]
    return vaer

def hent_vind(lat, lon):
    url = f"https://api.met.no/weatherapi/locationforecast/2.0/complete?lat={lat}&lon={lon}"
    respons = requests.get(url, headers={"User-agent": "Julias mac"})
    data = respons.json()
    vind = data["properties"]["timeseries"][0]["data"]["instant"]["details"]["wind_speed"]
    return vind


