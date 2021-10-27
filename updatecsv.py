import pandas as pd
from csv import writer
from sqlalchemy import create_engine



def update_csv(csv_name, RingersDict, BallerzDict, RingersScore, BallerzScore):
    my_conn = create_engine('mysql+pymysql://sql5447048:muZwPef3av@sql5.freemysqlhosting.net/sql5447048')
    data = pd.read_csv(csv_name)
    GameID = max(data['GameID']) + 1

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
        addList = [GameID, 'Ringers', UserID, PF, PA, PlayerID, TeammateID, OppPlayer1, OppPlayer2]
        id=my_conn.execute("INSERT INTO  `sql5447048`.`user_gamelogs` (`GameID` ,`TeamID` ,`UserID` ,`PF`,`PA`,`PlayerID`,`TeammateID`,`OppPlayer1`,`OppPlayer2`) \
                  VALUES (GameID, 'Ringers', UserID, PF, PA, PlayerID, TeammateID, OppPlayer1, OppPlayer2)")
    
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
        addList = [GameID, 'Ballerz', UserID, PF, PA, PlayerID, TeammateID, OppPlayer1, OppPlayer2]
        id=my_conn.execute("INSERT INTO  `sql5447048`.`user_gamelogs` (`GameID` ,`TeamID` ,`UserID` ,`PF`,`PA`,`PlayerID`,`TeammateID`,`OppPlayer1`,`OppPlayer2`) \
                  VALUES (GameID, 'Ballerz', UserID, PF, PA, PlayerID, TeammateID, OppPlayer1, OppPlayer2)")
    




