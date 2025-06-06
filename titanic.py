from load_data import load_data

all_data = load_data()

# List of all the commands
list_of_commands= ["help", "show_countries", "top_countries <num_countries>"]

# Create a set of the countries to have no duplicates.
countries = set()

for ship in all_data["data"]:
    countries.add(ship["COUNTRY"])

sorted_countries = sorted(list(countries))

# Create a dictionary with the country name as key and the number of ships they have as value.
countries_number_dict = {}
for country in sorted_countries:
  countries_number_dict[country] = 0

for country in sorted_countries:
  for ship in all_data["data"]:
    if country == ship["COUNTRY"]:
        countries_number_dict[country] += 1

sorted_countries_numbers_list = sorted(countries_number_dict.items(), key=lambda item: item[1], reverse=True)


def show_countries(sorted_countries):
    for country in sorted_countries:
        print(country)
  

def top_countries(countries_shipnumbers: list, num_countries):
    for count in range(num_countries):
        country, number_of_ships = countries_shipnumbers[count]
        print(f"{country}: {number_of_ships}")

def main():
    print("Welcome to the Ships CLI! Enter 'help' to view available commands.")
    while True:
        user_command = input()
        if user_command == "help":
            print("Available commands:")
            for command in list_of_commands:
                print(command)
            print()
        if user_command == "show_countries":
            show_countries(sorted_countries)
            print()
        if "top_countries" in user_command:
            user_command = user_command.split(" ")
            if int(user_command[1]) <= len(sorted_countries_numbers_list):
                top_countries(sorted_countries_numbers_list, int(user_command[1]))
                print()
            else:
                print(f"Sorry, there are only {len(sorted_countries_numbers_list)} countries in this list.")



if __name__ == "__main__":
    main()