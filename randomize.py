import random

users = ["Brant", "Nick", "Jake", "Lucas"]
nameNumberTuples = [("Mason Gillis", 0), ("Brian Wadell", 1), ("Eric Hunter Jr.", 2), ("Caleb Furst", 3), ("Trey Kaufman-Renn", 4), ("Brandon Newman", 5), ("Isaiah Thompson", 11), ("Zach Edey", 15), ("Jaden Ivey", 23), ("Ethan Morton", 25), ("Trevion Williams", 50), ("Sasha Stefanovic", 55)]

def getUsers():
    random.shuffle(users)
    team1_users = users[:2]
    team2_users = users[2:4]

    return team1_users, team2_users

def getPlayers():
    selected_players = random.sample(nameNumberTuples, 4)
    team1_players = selected_players[:2]
    team2_players = selected_players[2:]

    return team1_players, team2_players

def getRandTeams():

    team1_users, team2_users = getUsers()
    team1_players, team2_players = getPlayers()

    team1 = {user : player for user, player in zip(team1_users, team1_players)}
    team2 = {user : player for user, player in zip(team2_users, team2_players)}

    return team1, team2

def printTeams():
    team1, team2 = getRandTeams()

    print("Team 1:\n", team1)
    print("Team 2:\n", team2)

if __name__ == "__main__":
    printTeams()
