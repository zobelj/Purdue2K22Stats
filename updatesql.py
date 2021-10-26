from sqlalchemy import create_engine
import pymysql

# https://docs.rackspace.com/support/how-to/install-mysql-server-on-the-ubuntu-operating-system/

engine = create_engine('mysql+pymysql://root:hello123@localhost/kenpom')
all_years.to_sql(name = 'teams', con = engine, if_exists = 'replace')