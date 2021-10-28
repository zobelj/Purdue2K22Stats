from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.sql import text

listRows = []
with open('db_url.txt', 'r') as f:
    db_url = f.read()
    my_conn = create_engine(db_url)
r_set=my_conn.execute("SELECT * FROM user_gamelogs");

for row in r_set:
    listRows.append(row)

mainData = pd.DataFrame(listRows, columns=['Index', 'GameID', 'TeamID', 'UserID', "PF", "PA", "PlayerID", "TeammateID", "OppPlayer1", "OppPlayer2"])

listPlayerRecordRows = []

with my_conn.connect() as con:
    file = open("sql_scripts/get_player_records.sql")
    query = text(file.read())
    rows = con.execute(query)
    for row in rows:
        listPlayerRecordRows.append(row)

playerRecords = pd.DataFrame(listPlayerRecordRows, columns = ['PlayerID','Name', 'W','L','wpct','RegW','RegL','PPG','PAPG'])
print(playerRecords)



# X = data[['BA','oppBA','platoon']].to_numpy()
# y = data[['H']].values.flatten()
# clf = LogisticRegression(random_state=0, max_iter = 100000).fit(X, y)
# clf.predict(X)

# print(clf.predict_proba([[.305,.2,1]]))

# print(clf.score(X, y))
# print(clf.coef_, clf.intercept_)
