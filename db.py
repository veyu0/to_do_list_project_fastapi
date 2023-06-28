from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import create_engine
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker
import os

load_dotenv()

try:
    url = f'postgresql://{os.getenv("user")}:{os.getenv("password")}@{os.getenv("host")}:{os.getenv("port")}/{os.getenv("db_name")}'
    if not database_exists(url):
        create_database(url)

    engine = create_engine(url, pool_size=50, echo=True)

    Session = sessionmaker(bind=engine)
    session = Session()

except Exception as ex:
    print('Something gone wrong with PostgreSQL', ex)

finally:
    print('PostgreSQL connection closed')