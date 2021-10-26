import pandas as pd
from csv import writer

def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)

def update_csv(csv_name, RingersDict, BallerzDict, RingersScore, BallerzScore):
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
        append_list_as_row(csv_name, addList)
    
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
        append_list_as_row(csv_name, addList)
    




