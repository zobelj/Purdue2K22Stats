import pandas as pd
from csv import writer
from sqlalchemy import create_engine
from sqlalchemy.sql import text

def update_sql(RingersDict, BallerzDict, RingersScore, BallerzScore):
    # read database url from file
    with open('db_url.txt', 'r') as f:
        db_url = f.read()
    my_conn = create_engine(db_url)
  
    ID = my_conn.execute("SELECT max(GameID) FROM user_gamelogs")
    for row in ID:
        GameID = row[0] + 1

    for player in RingersDict:
        UserID = player
        PF = RingersScore
        PA = BallerzScore
        PlayerID = RingersDict[player][1]
        for teammate in RingersDict:
            if teammate != player:
                TeammateID = RingersDict[teammate][1]
        oppList = []
        for opponent in BallerzDict:
            oppList.append(BallerzDict[opponent][1])
        OppPlayer1 = oppList[0]
        OppPlayer2 = oppList[1]
        query = text("INSERT INTO  `sql5447048`.`user_gamelogs` (`GameID` ,`TeamID` ,`UserID` ,`PF`,`PA`,`PlayerID`,`TeammateID`,`OppPlayer1`,`OppPlayer2`) \
                  VALUES (:GameID, 'Ballerz', :UserID, :PF, :PA, :PlayerID, :TeammateID, :OppPlayer1, :OppPlayer2)")
        id=my_conn.execute(query, GameID=GameID, TeamID='Ballerz', UserID=UserID, PF=PF, PA=PA, PlayerID=PlayerID, TeammateID=TeammateID, OppPlayer1=OppPlayer1, OppPlayer2=OppPlayer2)
    
    for player in BallerzDict:
        UserID = player
        PF = BallerzScore
        PA = RingersScore
        PlayerID = BallerzDict[player][1]
        for teammate in BallerzDict:
            if teammate != player:
                TeammateID = BallerzDict[teammate][1]
        oppList = []
        for opponent in RingersDict:
            oppList.append(RingersDict[opponent][1])
        OppPlayer1 = oppList[0]
        OppPlayer2 = oppList[1]
        query = text("INSERT INTO  `sql5447048`.`user_gamelogs` (`GameID` ,`TeamID` ,`UserID` ,`PF`,`PA`,`PlayerID`,`TeammateID`,`OppPlayer1`,`OppPlayer2`) \
                  VALUES (:GameID, 'Ballerz', :UserID, :PF, :PA, :PlayerID, :TeammateID, :OppPlayer1, :OppPlayer2)")
        id=my_conn.execute(query, GameID=GameID, TeamID='Ringers', UserID=UserID, PF=PF, PA=PA, PlayerID=PlayerID, TeammateID=TeammateID, OppPlayer1=OppPlayer1, OppPlayer2=OppPlayer2)
