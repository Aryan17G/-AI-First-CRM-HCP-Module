from sqlalchemy import create_engine, Column, Integer, String, Text, Date, Time
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()
engine = create_engine("sqlite:///./hcp_crm.db", connect_args={"check_same_thread": False}) # Using SQLite for quick setup, easily swap to Postgres
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class HCPInteraction(Base):
    __tablename__ = "hcp_interactions"
    
    id = Column(Integer, primary_key=True, index=True)
    hcp_name = Column(String(255), index=True)
    interaction_type = Column(String(50))
    date = Column(String(20))
    time = Column(String(20))
    attendees = Column(Text)
    topics_discussed = Column(Text)
    sentiment = Column(String(20))
    outcomes = Column(Text)
    follow_ups = Column(Text)

Base.metadata.create_all(bind=engine)