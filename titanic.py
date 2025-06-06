from load_data import load_data

all_data = load_data()

# number of ships
total_ships = len(all_data["data"])
print(total_ships)

# Ship names
for ship in all_data["data"]:
  print(ship["SHIPNAME"])

def help():
  list_of_commands= ["help", "show_countries", "top_countries <num_countries>"]


def show_countries():
  countries = set()

  for ship in all_data["data"]:
    countries.add(ship["COUNTRY"])

  sorted_countries = sorted(list(countries))
  
  for country in sorted_countries:
    print(country)

countries_number_dict = {}
for country in sorted_countries:
  

def top_countries(num_countries):
