from sqlalchemy import create_engine
import pymysql
import pandas as pd


def update_user_gamelogs(csv_name):
    data = pd.read_csv(csv_name)
    engine = create_engine('mysql+pymysql://sql5447048:muZwPef3av@sql5.freemysqlhosting.net/sql5447048')
    data.to_sql(name = 'user_gamelogs', con = engine, if_exists = 'replace')
