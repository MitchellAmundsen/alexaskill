import requests

pokemonname = "squirtle"
url = "http://pokeapi.co/api/v2/pokemon/" + pokemonname + "/"
#response = urllib2.urlopen(url)
response = requests.get(url)
data = response.json()

height = data['height']
weight = data['weight']
vartype = ''

typeobj = data['types']
for i in typeobj:
	thetype = i['type']['name']
	vartype = vartype + " " + thetype
    
speech_output = pokemonname + " has a height of " + str(height) + ", a weight of " + str(weight) + ", and is a" + vartype + " type pokemon."

print(speech_output)
