# CRITERION HOSPITAL.

#### By **{List of contributors}**
This project was created and is sole property of Annglorious mueni.

### Project overview
This CLI manages the hospitals operations which include the patients ,doctors and appointment records.
The application leverages SQLAlchemy for database operations and provides a user-friendly interface for managing healthcare data.


### Features implemented.
#### Minimum Viable Product (MVP) 
1. Core Features
- patient management
- Doctor management
- Appointment management

2. User Interface
- Command-Line Interface
- Simple text-based menu for user interaction.
- Clear prompts for user input.
3. Database Setup
- SQLite Database
- Use SQLite to store data for patients, doctors, and appointments.
- Tables: Patients, Doctors, Appointments.

4. Key Functions
* CRUD Operations
- Implement Create, Read, Update, Delete (CRUD) for:
Patients
Doctors
Appointments

5. Basic Validation
- Ensure input data is validated (e.g., age must be a positive integer, gender must be valid).

6. Data Seeding
- Include a simple script to seed the database with sample data to facilitate testing and demonstration.

7. Code Structure
* Modular Code
- Organize code into functions for readability and maintainability.
- Utilize classes for data models (Patient, Doctor, Appointment).


## Setup/Installation Requirements
* One would need either linux or wsl for window users
* A copy of visual basic code installed
* A github account

1. Open your terminal and go to the directory you wish to work from.
2. Go to the following url using ur github account https://github.com/ANNGLORIOUS/criterion-hospital
3. Go to the code tab and clone the ssh key
4. Go back to the terminal and type git clone <-followed by the ssh key you copied /cloned ->
5. Enter your new cloned repository and type in code .
6. On the visual studio code that has now opened, then install the dependancies:
    - pipenv install
    - pipenv shell
    - pip install sqlalchemy
    - pip install alchemy
7. Then run the following commands:
    - python lib/cli.py
## Technologies Used
This program is built purely with python using the visual code environment.

## Support and contact details
For any issues please email me at annglorious.mueni@student.moringaschool.com
### License
Apache License 2.0

