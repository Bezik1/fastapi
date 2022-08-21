from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:1011fajeruw@localhost:3306/sql-kurs")

meta = MetaData()

db = engine.connect()