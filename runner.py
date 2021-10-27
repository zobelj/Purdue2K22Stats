from randomize import getRandTeams
from updateSQL import update_sql

def printTeam(side, team):
    print(f"\n{side}:")
    for user in team.keys():
        print(f"{user} : {team[user][0]}")

ringers, ballerz, users = getRandTeams(None)
printTeam("Ringers", ringers)
printTeam("Ballerz", ballerz)

# rerandomize teams until user says no
reRandom = input("\nRe-randomize teams? (y/n/exit) ")

while reRandom.lower() != "n":
    if(reRandom == "exit" or reRandom == "e"):
        exit()

    ringers, ballerz, users = getRandTeams(users)
    printTeam("Ringers", ringers)
    printTeam("Ballerz", ballerz)
    reRandom = input("\nRe-randomize teams? (y/n/exit) ")

# ask if the user wants to upload to the database
upload = input("\nUpload to database? (y/n) ")

if(upload.lower() == "y"):
    ringersScore = int(input("\nRingers score: "))
    ballerzScore = int(input("Ballerz score: "))

    update_sql(ringers, ballerz, ringersScore, ballerzScore)
