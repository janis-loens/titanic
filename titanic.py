from load_data import load_data

all_data = load_data()

# List of all the commands
list_of_commands= ["help", "show_countries", "top_countries <num_countries>"]

# Create a set of the countries to have no duplicates.
countries = set()

for ship in all_data["data"]:
    countries.add(ship["COUNTRY"])

sorted_countries = sorted(list(countries))

# Create a dictionary "country name" = number of ships.
countries_number_dict = {}
for country in sorted_countries:
  countries_number_dict[country] = 0

for country in sorted_countries:
  for ship in all_data["data"]:
    if country == ship["COUNTRY"]:
        countries_number_dict[country] += 1

# Create list of tuples(country, number of ships) sorted by number of ships
sorted_countries_numbers_list = sorted(countries_number_dict.items(), key=lambda item: item[1], reverse=True)

def help(list_of_commands) -> None:
    """
    Print every viable command.
    Args:
        list_of_commands:

    Returns:
        None
    """
    print("Available commands:")
    for command in list_of_commands:
        print(command)
    print()


def show_countries(sorted_countries) -> None:
    """
    Print every country in the list.
    Args:
        sorted_countries(list): list of countries sorted alphabetically

    Returns:
        None
    """
    for country in sorted_countries:
        print(country)
    print()


def top_countries(sorted_countries_numbers_list: list, num_countries) -> None:
    """
    Print the top "n" countries in the list and the number of ships they have.
    Args:
        sorted_countries_numbers_list(list): list of countries sorted by their number of ships.
        num_countries(int): number of countries to be printed

    Returns:
        None
    """
    for count in range(num_countries):
        country, number_of_ships = sorted_countries_numbers_list[count]
        print(f"{country}: {number_of_ships}")
    print()




function_pointer = {
    "help": lambda: help(list_of_commands),
    "show_countries": lambda: show_countries(sorted_countries),
    "top_countries":    lambda n: top_countries(sorted_countries_numbers_list, int(n)),
}

def main():
    print("Welcome to the Ships CLI! Enter 'help' to view available commands.")
    while True:
        parts = input("> ").split()
        if not parts:
            continue

        cmd, *args = parts
        handler = function_pointer.get(cmd)
        if handler is None:
            print("Unknown command:", cmd)
            continue

        try:
            handler(*args)
        except TypeError:
            print(f"Usage for {cmd!r}: …")  # you can show a helpful usage message here

if __name__ == "__main__":
    main()
