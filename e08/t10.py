import json

def load_data(file_name):
    with open(file_name) as file:
        return json.load(file)

def print_player(player):
    points = player["goals"] + player["assists"]
    print(f"{player['name']:20} {player['team']:>3} {player['goals']:>3} + {player['assists']:>2} = {points:>3}")

def list_teams(data):
    teams = sorted(set(player["team"] for player in data))
    print("".join(teams))

def list_countries(data):
    countries = sorted(set(player["nationality"] for player in data))
    print("".join(countries))

def search_player(data, name):
    for player in data:
        if player["name"].lower() == name.lower():
            print_player(player)

def players_in_team(data, team):
    players = [p for p in data if p["team"] == team]
    players.sort(key=lambda x: x["goals"] + x["assists"], reverse=True)
    for player in players:
        print_player(player)

def players_from_country(data, country):
    players = [p for p in data if p["nationality"] == country]
    players.sort(key=lambda x: x["goals"] + x["assists"], reverse=True)
    for player in players:
        print_player(player)

def most_points(data, n):
    data.sort(key=lambda x: (x["goals"] + x["assists"], x["goals"]), reverse=True)
    for player in data[:n]:
        print_player(player)

def most_goals(data, n):
    data.sort(key=lambda x: (x["goals"], -x["games"]), reverse=True)
    for player in data[:n]:
        print_player(player)

def main():
    file_name = input("file name: ")
    data = load_data(file_name)
    print(f"read the data of {len(data)} players")
    print("commands:")
    print("0 quit\n1 search for player\n2 teams\n3 countries\n4 players in team")
    print("5 players from country\n6 most points\n7 most goals")
    
    while True:
        command = input("command: ")
        if command == "0":
            break
        elif command == "1":
            name = input("name: ")
            search_player(data, name)
        elif command == "2":
            list_teams(data)
        elif command == "3":
            list_countries(data)
        elif command == "4":
            team = input("team: ")
            players_in_team(data, team)
        elif command == "5":
            country = input("country: ")
            players_from_country(data, country)
        elif command == "6":
            n = int(input("how many: "))
            most_points(data, n)
        elif command == "7":
            n = int(input("how many: "))
            most_goals(data, n)

main()
