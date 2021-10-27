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

# rerandomize teams until user says no
reRandom = input("\nRe-randomize teams? (y/n/exit) ")

while reRandom.lower() != "n":
    if(reRandom == "exit"):
        exit()
    ringers, ballerz = getRandTeams()
    printTeam("Ringers", ringers)
    printTeam("Ballerz", ballerz)
    reRandom = input("\nRe-randomize teams? (y/n/exit) ")

    

ringersScore = int(input("\nRingers score: "))
ballerzScore = int(input("Ballerz score: "))

update_csv("./NBA 2K Blacktop.csv", ringers, ballerz, ringersScore, ballerzScore)
update_user_gamelogs("./NBA 2K Blacktop.csv")
