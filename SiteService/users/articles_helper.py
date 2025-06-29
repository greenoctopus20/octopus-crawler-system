from sqlalchemy import Column, Integer, String, Date, Text, create_engine, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from datetime import datetime

DB_USER = 'doadmin'
DB_PASSWORD = 'AVNS_VQ6ICJAz3PnxBkncK1e'
DB_HOST = 'mysql-database-cluster-do-user-15555854-0.c.db.ondigitalocean.com'
DB_PORT = '25060'
DB_NAME = 'defaultdb'

DATABASE_URL = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
#print(DATABASE_URL)

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

existing_tables = Base.metadata.tables




def count_articles(site_id):
    session = Session()
    count = session.query(articles).filter(articles.site_id == site_id).count()
    session.close()
    return count


def get_date_last_extracted(site_id):
    session = Session()
    last_extracted_date = (
        session.query(func.max(articles.extracted_date))
        .filter(articles.site_id == site_id)
        .scalar()
    )
    session.close()
    return last_extracted_date