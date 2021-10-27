from updatesql import update_user_gamelogs
from randomize import getRandTeams
from updatecsv import update_csv

def printTeam(side, team):
    print(f"\n{side}:")
    for user in team.keys():
        print(f"{user} : {team[user][0]}")

ringers, ballerz = getRandTeams()
printTeam("Ringers", ringers)
printTeam("Ballerz", ballerz)

ringersScore = int(input("\nRingers score: "))
ballerzScore = int(input("Ballerz score: "))

update_csv("./NBA 2K Blacktop.csv", ringers, ballerz, ringersScore, ballerzScore)
update_user_gamelogs("./NBA 2K Blacktop.csv")
