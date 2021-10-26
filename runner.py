from randomize import getRandTeams
from updatecsv import update_csv

team1, team2 = getRandTeams()

update_csv(team1, team2, 21, 9)
