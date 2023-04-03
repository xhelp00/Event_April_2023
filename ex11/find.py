import requests

BASE_URL = "https://pokeapi.co/api/v2/"

# Define a function to retrieve the abilities of a given Pokemon
def get_pokemon_abilities(name):
	# Build the URL to retrieve information on the specified Pokemon
	url = BASE_URL + "pokemon/" + name.lower()
	response = requests.get(url)

	# If the response is successful, retrieve the Pokemon's abilities and return them
	if response.status_code == 200:
		data = response.json()
		abilities = data["abilities"]
		ability_names = [ability["ability"]["name"] for ability in abilities]
		return ability_names

	# If the response is unsuccessful, raise an error with the status code
	else:
		raise Exception("Error retrieving information. Status code: " + str(response.status_code))

def main():
	# Prompt the user to enter the name of a Pokemon
	pokemon_name = input("Enter the name of a Pokemon: ")
	abilities = get_pokemon_abilities(pokemon_name)
	print("Name: " + pokemon_name.capitalize())
	print("Abilities:")
	for ability in abilities:
		print("- " + ability.capitalize())

if __name__ == "__main__":
	main()
