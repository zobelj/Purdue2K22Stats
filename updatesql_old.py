from sqlalchemy import create_engine
import pandas as pd

def update_user_gamelogs(csv_name):
    data = pd.read_csv(csv_name)
    engine = create_engine(pd.read_csv("./database_url.csv"))
    data.to_sql(name = 'user_gamelogs', con = engine, if_exists = 'replace')

# https://www.plus2net.com/python/mysql-insert-sqlalchemy.php