from randomize import getRandTeams
from updatecsv import update_csv

ringers, ballerz = getRandTeams()
ringersScore = int(input("Ringers score: "))
ballerzScore = int(input("Ballerz score: "))

update_csv("./NBA 2K Blacktop.csv", ringers, ballerz, ringersScore, ballerzScore)
