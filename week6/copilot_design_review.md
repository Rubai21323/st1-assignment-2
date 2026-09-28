Below is a requirements-traceable domain model using only concepts explicitly supported by FR-01 to FR-12. I have not added attributes, operations, classes, or relationships unless they can be linked to a specific requirement.

1. Domain Classes
Patient
Attributes
Attribute	Supporting RequirementpatientID	FR-08 (find patient by patient ID)
name	FR-06, FR-08
dateOfBirth	FR-06
phoneNumber	FR-06, FR-07
address	FR-06, FR-07
Operations
Operation	Supporting RequirementupdatePhoneNumber()	FR-07
updateUsing only the stated requirements, the core domain appears to be Patient, Practitioner, Appointment, with Receptionist included because several system operations are explicitly performed by a receptionist.	
1. Domain Classes
Class: Patient

Supporting requirements: FR-01, FR-06, FR-07, FR-08

Attributes
Attribute	RequirementpatientID	FR-08
name	FR-06, FR-08
dateOfBirth	FR-06
phoneNumber	FR-06, FR-07
address	FR-06, FR-07
Operations
Operation	RequirementupdatePhoneNumber()	FR-07
updateAddress()	FR-07
Class: Practitioner

Supporting requirements: FR-01, FR-03, FR-09, FR-10, FR-11, FR-12

Attributes

No practitioner attributes are explicitly specified in the requirements.

Operations
Operation	RequirementviewTodayAppointments()	FR-10
Class: Appointment

Supporting requirements: FR-01, FR-02, FR-03, FR-04, FR-05, FR-09, FR-10

Attributes
Attribute	Requirementdate	FR-01
time	FR-01
status	FR-04
Operations
Operation	Requirementcancel()	FR-02
changeStatus()	FR-04
Class: Receptionist

Supporting requirements: FR-01, FR-02, FR-06, FR-07, FR-08, FR-09, FR-11

Attributes

No receptionist attributes are explicitly specified in the requirements.

Operations
Operation	RequirementbookAppointment()	FR-01
cancelAppointment()	FR-02
addPatient()	FR-06
updatePatientDetails()	FR-07
findPatient()	FR-08
viewPractitionerSchedule()	FR-09
addPractitioner()	FR-11
2. Enumeration
AppointmentStatus

Supporting requirement: FR-04

Value	RequirementBooked	FR-04
Cancelled	FR-04
Completed	FR-04
3. Relationships and Multiplicities
Patient — Appointment

Relationship: A patient can have appointments and each appointment is for one patient.

End	MultiplicityPatient	1
Appointment	0..*

Supported by: FR-01 (appointment booking requires choosing a patient)

Practitioner — Appointment

Relationship: A practitioner can have appointments and each appointment is with one practitioner.

End	MultiplicityPractitioner	1
Appointment	0..*

Supported by: FR-01, FR-03, FR-09, FR-10

Justification:

Appointment booking requires choosing a practitioner (FR-01).
A practitioner may have multiple appointments (FR-03, FR-09, FR-10).
Each appointment refers to a single practitioner selected during booking (FR-01).
Appointment — AppointmentStatus

Relationship: Each appointment has exactly one status.

End	MultiplicityAppointment	1
AppointmentStatus	1

Supported by: FR-04

4. Constraints Derived from Requirements

These are business rules rather than additional classes.

Constraint	RequirementA practitioner cannot have more than one appointment at the same date/time.	FR-03
Appointment status must be Booked, Cancelled, or Completed.	FR-04
Cancelled appointments must remain stored in appointment history and not be deleted.	FR-05
Patients must be searchable by patientID or name.	FR-08
The system must be able to show booked appointments and free time slots for a practitioner on a selected day.	FR-09
Practitioners can view their own appointments for the day.	FR-10
UML Analysis Summary

Classes

Patient
Practitioner
Appointment
Receptionist
AppointmentStatus (enumeration)

Associations

Patient (1) ↔ Appointment (0..*)
Practitioner (1) ↔ Appointment (0..*)
Appointment (1) ↔ AppointmentStatus (1)

This model stays strictly within the information explicitly supported by FR-01 to FR-12 and does not introduce unsupported attributes such as practitioner name, practitioner ID, availability schedule, clinic details, or appointment notes.