import os
import sys
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey,  DateTime
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
    
class Doctor(Base):
    __tablename__ = 'doctors'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    specialty = Column(String)
    appointments = relationship("Appointment", back_populates="doctor")

    def __repr__(self):
        return f"<Doctor(id={self.id}, name='{self.name}', specialty='{self.specialty}')>"

    @staticmethod
    def create(name, specialty):
        return Doctor(name=name, specialty=specialty)

    @staticmethod
    def delete(session, doctor_id):
        doctor = session.query(Doctor).get(doctor_id)
        if doctor:
            session.delete(doctor)
            session.commit()
        return doctor

    @staticmethod
    def get_all(session):
        return session.query(Doctor).all()

    @staticmethod
    def find_by_id(session, doctor_id):
        return session.query(Doctor).get(doctor_id)

class Appointment(Base):
    __tablename__ = 'appointments'

    id = Column(Integer, primary_key=True, autoincrement=True)
    patient_id = Column(Integer, ForeignKey('patients.id'), nullable=False)
    doctor_id = Column(Integer, ForeignKey('doctors.id'), nullable=False)
    date = Column(DateTime, nullable=False)
    patient = relationship("Patient", back_populates="appointments")
    doctor = relationship("Doctor", back_populates="appointments")

    def __repr__(self):
        return (f"<Appointment(id={self.id}, patient_id={self.patient_id}, "
                f"doctor_id={self.doctor_id}, date={self.date})>")

    @staticmethod
    def create(patient_id, doctor_id, date):
        return Appointment(patient_id=patient_id, doctor_id=doctor_id, date=date)

    @staticmethod
    def delete(session, appointment_id):
        appointment = session.query(Appointment).get(appointment_id)
        if appointment:
            session.delete(appointment)
            session.commit()
        return appointment

    @staticmethod
    def get_all(session):
        return session.query(Appointment).all()

    @staticmethod
    def find_by_id(session, appointment_id):
        return session.query(Appointment).get(appointment_id)  
