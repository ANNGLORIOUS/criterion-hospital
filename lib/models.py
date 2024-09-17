import os
import sys
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import func
sys.path.append(os.getcwd)


engine = create_engine('sqlite:///lib/hospital.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Patient(Base):
    __tablename__ = 'patients'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    gender = Column(String)
    appointments = relationship("Appointment", back_populates="patient")

    def __repr__(self):
        return f"<Patient(id={self.id}, name='{self.name}', age={self.age}, gender='{self.gender}')>"

    @staticmethod
    def create(name, age, gender):
        return Patient(name=name, age=age, gender=gender)

    @staticmethod
    def delete(session, patient_id):
        patient = session.query(Patient).get(patient_id)
        if patient:
            session.delete(patient)
            session.commit()
        return patient

    @staticmethod
    def get_all(session):
        return session.query(Patient).all()

    @staticmethod
    def find_by_id(session, patient_id):
        return session.query(Patient).get(patient_id)
    
