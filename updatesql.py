from sqlalchemy import create_engine
import pymysql
import pandas as pd

data = pd.read_csv('NBA 2K Blacktop.csv')

engine = create_engine('mysql+pymysql://sql5447048:muZwPef3av@sql5.freemysqlhosting.net/sql5447048')
data.to_sql(name = 'user_gamelogs', con = engine, if_exists = 'replace')
