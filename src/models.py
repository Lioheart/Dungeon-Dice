"""Modele tablic w bazie dla D&D 3.5"""
import datetime

from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base

from config import DATABASE_URI

engine = create_engine(DATABASE_URI)
Base = declarative_base()


class Spells(Base):
    __tablename__ = 'spells'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)   # Nazwa
    source_book = Column(String)            # Podręcznik źródłowy
    source_page = Column(String)            # Strona
    school = Column(String)                 # Szkoła
    sub_school = Column(String)             # Podszkoła
    descriptor = Column(String)             # Określnik
    class_lvl = Column(String)              # Poziom i klasa (JSON)
    components = Column(String)             # Komponenty
    casting_time = Column(String)           # Czas rzucania
    range = Column(String)                  # Zasięg
    magic_targeting = Column(String)        # Celowanie czarem  (JSON)
    duration = Column(String)               # Czas działania
    saving_throw = Column(String)           # Rzut obronny
    resistance = Column(String)             # Odporność na czary
    descriptor_short = Column(String)       # Opis (krótki)
    descriptor_long = Column(String)        # Opis (długi)
    timestamp = Column(DateTime, onupdate=datetime.datetime.now)

    def __repr__(self):
        return '<Zaklęcie {}>'.format(self.name)

# Base.metadata.create_all(engine)