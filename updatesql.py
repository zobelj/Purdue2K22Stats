from sqlalchemy import create_engine
import pymysql

engine = create_engine('mysql+pymysql://root:hello123@localhost/kenpom')
all_years.to_sql(name = 'teams', con = engine, if_exists = 'replace')