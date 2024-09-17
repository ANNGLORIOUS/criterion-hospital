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

def seed():
    # Create tables
    from models import Base
    Base.metadata.create_all(engine)
    
    # Add sample data
    if not session.query(Patient).first():
        patient1 = Patient.create("John Mwangi", 30, "Male")
        patient2 = Patient.create("Jane Smith", 25, "Female")
        patient3 = Patient.create("Sicily Mukulu", 36, "Female")
        patient4 = Patient.create("Vincent kaka", 45, "male")
        patient5 = Patient.create("Wilson Smith", 50, "male")
        patient6 = Patient.create("Catherine mwende", 56, "Female")
        patient7 = Patient.create("Celine Resi", 70, "Female")
        session.add_all([patient1, patient2, patient3, patient4, patient5, patient6, patient7])
    
    if not session.query(Doctor).first():
        doctor1 = Doctor.create("Dr. Brown", "Cardiology")
        doctor2 = Doctor.create("Dr. Green", "Neurology")
        doctor3 = Doctor.create("Dr. Blue", "Orthopedics")
        doctor4 = Doctor.create("Dr. Black", "Pediatrics")
        doctor5 = Doctor.create("Dr.White", "Gynacologist")
        doctor6 = Doctor.create("Dr. Yellow", "Dermatology")
        doctor7 = Doctor.create("Dr. Red", "Urology")
        session.add_all([doctor1, doctor2, doctor3, doctor4, doctor5, doctor6, doctor7])
    
    if not session.query(Appointment).first():
        appointment1 = Appointment.create(patient_id=1, doctor_id=1, date=datetime(2024, 9, 15, 10, 0, 0))
        appointment2 = Appointment.create(patient_id=2, doctor_id=2, date=datetime(2024, 9, 20, 14, 30, 0))
        appointment3 = Appointment.create(patient_id=3, doctor_id=3, date=datetime(2024, 9, 25, 16, 0, 0))
        appointment4 = Appointment.create(patient_id=4, doctor_id=4, date=datetime(2024, 9, 30, 8, 45, 0))
        appointment5 = Appointment.create(patient_id=5, doctor_id=5, date=datetime(2024, 10, 5, 12, 15, 0))
        appointment6 = Appointment.create(patient_id=6, doctor_id=6, date=datetime(2024, 10, 10, 18, 0, 0))
        appointment7 = Appointment.create(patient_id=7, doctor_id=7, date=datetime(2024, 10, 15, 10, 30, 0))
    appointments = [appointment1, appointment2, appointment3, appointment4, appointment5, appointment6, appointment7]
    session.add_all(appointments)
    
    session.commit()
    print("Database seeded.")

if __name__ == "__main__":
    seed()