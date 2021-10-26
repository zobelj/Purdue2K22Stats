import random

users = ['Joe', 'Nick', 'Brant', 'Jeremy']
purdue_players = ['Zach Edey', 'Jaden Ivey', 'Trevion Williams', 'Eric Hunter Jr.', 'Brandon Newman', 'Sasha Stefanovic', 'Trey Kauffman-Renn', 'Caleb Furst', 'Mason Gillis', 'Ethan Morton', 'Isaiah Thompson', 'Brian Wadell']

rand_teams = input("Randomize users? Y/n: ").lower()
player_lock = input("Player lock? Y/n: ").lower()

if(rand_teams == "y"):
    random.shuffle(users)
    team1_names = users[:2]
    team2_names = users[2:]

else:
    team1_names = input("Enter team1 users: ").split(" ")
    team2_names = input("Enter team2 users: ").split(" ")

if(rand_teams == "y" and player_lock == "y"):
    ppt = 2
else:
    ppt = int(input("Players per team: "))

selected_players = random.sample(purdue_players, ppt*2)

if(player_lock == "y"):
    team1 = dict(zip(team1_names, selected_players[:ppt]))
    team2 = dict(zip(team2_names, selected_players[ppt:]))

else:
    team1_names = ' '.join(team1_names)
    team2_names = ' '.join(team2_names)
    team1 = {team1_names : selected_players[:ppt]}
    team2 = {team2_names : selected_players[ppt:]}

print(team1)
print(team2)
