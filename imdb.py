import json

def hent_filmliste():
    fil = open("imdb.json")
    filmer = json.load(fil)
    fil.close()
    return filmer
