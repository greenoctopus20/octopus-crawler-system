from sqlalchemy import Column, Integer, String, Date, Text, create_engine, inspect, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
""" 
DB_USER = 'user003'
DB_PASSWORD = 'user_password_01//-_'
DB_HOST = '127.0.0.1'
DB_PORT = '3002'
DB_NAME = 'extracted'
 """
DB_USER = 'doadmin'
DB_PASSWORD = 'AVNS_VQ6ICJAz3PnxBkncK1e'
DB_HOST = 'mysql-database-cluster-do-user-15555854-0.c.db.ondigitalocean.com'
DB_PORT = '25060'
DB_NAME = 'defaultdb'

DATABASE_URL = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL, echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)

# Define the articles model
class articles(Base):
    __tablename__ = 'extracted'

    id = Column(Integer, primary_key=True, autoincrement=True)
    site_id = Column(Integer)
    url = Column(String(255))
    extracted_date = Column(DateTime, default=datetime.now) 
    title = Column(String(255))
    author = Column(String(255))
    body = Column(Text) 
    date = Column(String(50))


inspector = inspect(engine)
existing_tables = inspector.get_table_names()

if 'extracted' not in existing_tables:
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    session = Session()
    try:
        all_records = session.query(articles).all()
        print("All articles records:", all_records)

        new_record = articles(
            site_id=1,
            url='https://example.com',
            title='Sample Title',
            author='John Doe',
            body='Sample body text.',
            date='2023-12-14'
        )
        session.add(new_record)
        session.commit()
        print("New record created:", new_record)

    except Exception as e:
        print(f"Exception: {str(e)}")
        session.rollback()

    finally:
        session.close()