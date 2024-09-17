from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Patient
from models import Doctor
from models import Appointment
from datetime import datetime

DATABASE_URL = 'sqlite:///hospital.db'
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def create_patient():
    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))
    gender = input("Enter patient gender: ")
    patient = Patient.create(name, age, gender)
    session.add(patient)
    session.commit()
    print("Patient created.")

def delete_patient():
    patient_id = int(input("Enter patient ID to delete: "))
    patient = Patient.delete(session, patient_id)
    if patient:
        print("Patient deleted.")
    else:
        print("Patient not found.")

def list_patients():
    patients = Patient.get_all(session)
    for patient in patients:
        print(patient)

def view_patient():
    patient_id = int(input("Enter patient ID to view: "))
    patient = Patient.find_by_id(session, patient_id)
    if patient:
        print(patient)
    else:
        print("Patient not found.")

def create_doctor():
    name = input("Enter doctor name: ")
    specialty = input("Enter doctor specialty: ")
    doctor = Doctor.create(name, specialty)
    session.add(doctor)
    session.commit()
    print("Doctor created.")

def delete_doctor():
    doctor_id = int(input("Enter doctor ID to delete: "))
    doctor = Doctor.delete(session, doctor_id)
    if doctor:
        print("Doctor deleted.")
    else:
        print("Doctor not found.")

def list_doctors():
    doctors = Doctor.get_all(session)
    for doctor in doctors:
        print(doctor)

def view_doctor():
    doctor_id = int(input("Enter doctor ID to view: "))
    doctor = Doctor.find_by_id(session, doctor_id)
    if doctor:
        print(doctor)
    else:
        print("Doctor not found.")

def create_appointment():
    patient_id = int(input("Enter patient ID: "))
    doctor_id = int(input("Enter doctor ID: "))
    date = input("Enter appointment date (YYYY-MM-DD HH:MM:SS): ")
    date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    appointment = Appointment.create(patient_id, doctor_id, date)
    session.add(appointment)
    session.commit()
    print("Appointment created.")

def delete_appointment():
    appointment_id = int(input("Enter appointment ID to delete: "))
    appointment = Appointment.delete(session, appointment_id)
    if appointment:
        print("Appointment deleted.")
    else:
        print("Appointment not found.")

def list_appointments():
    appointments = Appointment.get_all(session)
    for appointment in appointments:
        print(appointment)

def view_appointment():
    appointment_id = int(input("Enter appointment ID to view: "))
    appointment = Appointment.find_by_id(session, appointment_id)
    if appointment:
        print(appointment)
    else:
        print("Appointment not found.")