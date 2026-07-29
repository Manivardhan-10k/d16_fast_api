# from sqlalchemy import create_engine
# #to create connection with database
# from sqlalchemy.orm import sessionmaker, declarative_base

# # DATABASE_URL = "mysql+pymysql://root:1234@localhost:3306/employees_db"
# DATABASE_URL = "mysql+pymysql://:AVNS_rW3layz6yj4ljHGw-po@test-deployment-manivardhan-b2b5.i.aivencloud.com:28723/defaultdb"

# engine = create_engine(DATABASE_URL)

# SessionLocal = sessionmaker(
#     autocommit=False,
#     autoflush=False,
#     bind=engine
# )

# Base = declarative_base()



from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+pymysql://avnadmin:AVNS_rW3layz6yj4ljHGw-po@test-deployment-manivardhan-b2b5.i.aivencloud.com:28723/defaultdb"

engine = create_engine(
    DATABASE_URL,
    connect_args={
        "ssl": {}
    }
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
