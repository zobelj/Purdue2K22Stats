import random
from updateSQL import update_sql

guards = [("Eric Hunter Jr.", 2), ("Brandon Newman", 5), ("Isaiah Thompson", 11), ("Jaden Ivey", 23), ("Ethan Morton", 25), ("Sasha Stefanovic", 55)]
forwards = [("Mason Gillis", 0), ("Brian Wadell", 1), ("Caleb Furst", 3), ("Trey Kaufman-Renn", 4)]
centers = [("Zach Edey", 15), ("Trevion Williams", 50)]

def getSettings():
    print("Choose user set: ")
    print("1. Roommates\n[Brant, Jeremy, Joe, Nick]")
    print("2. Complete database\n[Brant, Jeremy, Joe, Nick, Jake, Lucas]")
    print("3. Custom database\nEnter names separated by space")
    userSet = input("> ")

    validInput = False
    while not validInput:
        if(userSet == "1"):
            users = ["Brant", "Jeremy", "Joe", "Nick"]
            validInput = True
        elif(userSet == "2"):
            users = ["Brant", "Jeremy", "Joe", "Nick", "Jake", "Lucas"]
            validInput = True
        elif(userSet == "3"):
            users = input("> ").split()
            validInput = True
        else:
            print("Invalid input, try again.")
            userSet = input("> ")

    return users

def getUsers(usersParam):
    if(usersParam == None):
        users = getSettings()
    else:
        users = usersParam
    random.shuffle(users)
    team1_users = users[:2]
    team2_users = users[2:4]

    return team1_users, team2_users,

def getPlayers():
    selected_players = random.sample(guards + forwards + centers, 4)
    team1_players = selected_players[:2]
    team2_players = selected_players[2:]

    return team1_players, team2_players

def getRandTeams(users):
    team1_users, team2_users, = getUsers(users)
    team1_players, team2_players = getPlayers()

    team1 = {user : player for user, player in zip(team1_users, team1_players)}
    team2 = {user : player for user, player in zip(team2_users, team2_players)}

    return team1, team2, users

def htmlRandomize():
    team1, team2 = getRandTeams(["Joe", "Brant", "Jeremy", "Nick"])[:2]

    json_data = {"team1_user1" : list(team1.keys())[0],
                "team1_user2" : list(team1.keys())[1],
                "team2_user1" : list(team2.keys())[0],
                "team2_user2" : list(team2.keys())[1],
                "team1_player1" : team1[list(team1.keys())[0]],
                "team1_player2" : team1[list(team1.keys())[1]],
                "team2_player1" : team2[list(team2.keys())[0]],
                "team2_player2" : team2[list(team2.keys())[1]]}

    print(json_data)
    return json_data

def htmlUploadScores(json_data):
    ringers_score = json_data['team1_score']
    ballerz_score = json_data['team2_score']

    t1_user1 = json_data['team1_user1']
    t1_user2 = json_data['team1_user2']
    t2_user1 = json_data['team2_user1']
    t2_user2 = json_data['team2_user2']

    # split player name/number into two elements
    t1_p1 = json_data['team1_player1'].split(',')
    t1_p2 = json_data['team1_player2'].split(',')
    t2_p1 = json_data['team2_player1'].split(',')
    t2_p2 = json_data['team2_player2'].split(',')

    # remove # from player number
    t1_p1_name = t1_p1[0]
    t1_p1_num = t1_p1[1][1:].replace('#', '')
    t1_p2_name = t1_p2[0]
    t1_p2_num = t1_p2[1][1:].replace('#', '')
    t2_p1_name = t2_p1[0]
    t2_p1_num = t2_p1[1][1:].replace('#', '')
    t2_p2_name = t2_p2[0]
    t2_p2_num = t2_p2[1][1:].replace('#', '')

    ringers_dict = {t1_user1 : (t1_p1_name, t1_p1_num), t1_user2 : (t1_p2_name, t1_p2_num)}
    ballerz_dict = {t2_user1 : (t2_p1_name, t2_p1_num), t2_user2 : (t2_p2_name, t2_p2_num)}

    update_sql(ringers_dict, ballerz_dict, ringers_score, ballerz_score)
    return "Success"

def printTeams():
    team1, team2 = getRandTeams()

    print("Team 1:\n", team1)
    print("Team 2:\n", team2)

if __name__ == "__main__":
    printTeams()
