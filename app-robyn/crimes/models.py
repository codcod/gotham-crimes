from sqlalchemy import Column, DateTime, Float, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = 'sqlite:///./gotham_crime_data.db'

engine = create_engine(
    DATABASE_URL,
    echo=False,
    # connect_args={'detect_types': sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES},
    # native_datetime=True,
)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


Base = declarative_base()


class Crime(Base):
    __tablename__ = 'crimes'

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, index=True)
    description = Column(String)
    location = Column(String)
    suspect_name = Column(String)
    date_time = Column(DateTime)
    latitude = Column(Float)
    longitude = Column(Float)

    def to_dict(self):
        return dict(
            id=self.id,
            type=self.type,
            description=self.description,
            location=self.location,
            suspect_name=self.suspect_name,
            date_time=self.date_time,
            latitude=self.latitude,
            longitude=self.longitude,
        )


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
