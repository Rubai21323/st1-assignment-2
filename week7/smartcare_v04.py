from enum import Enum


class AppointmentStatus(Enum):
    BOOKED = "Booked"
    CANCELLED = "Cancelled"
    COMPLETED = "Completed"


class Patient:
    def __init__(self, patient_id: str, name: str, date_of_birth: str, phone: str, address: str):
        if not patient_id or not patient_id.strip():
            raise ValueError("Patient ID cannot be empty")
        if not name or not name.strip():
            raise ValueError("Patient name cannot be empty")
        self.patient_id = patient_id
        self.name = name
        self.date_of_birth = date_of_birth
        self.phone = phone
        self.address = address

    def update_contact(self, phone: str, address: str):
        self.phone = phone
        self.address = address


class Practitioner:
    def __init__(self, practitioner_id: str, name: str, specialty: str):
        if not practitioner_id or not practitioner_id.strip():
            raise ValueError("Practitioner ID cannot be empty")
        if not name or not name.strip():
            raise ValueError("Practitioner name cannot be empty")
        self.practitioner_id = practitioner_id
        self.name = name
        self.specialty = specialty


class Appointment:
    def __init__(self, patient, practitioner, date, time):
        self.patient = patient
        self.practitioner = practitioner
        self.date = date
        self.time = time
        self.status = AppointmentStatus.BOOKED

    def cancel(self):
        pass

    def set_status(self, status):
        pass


class AppointmentManager:
    def __init__(self):
        self.appointments = []

    def book(self, patient, practitioner, date, time):
        pass

    def has_clash(self, practitioner, date, time):
        pass

    def get_schedule(self, practitioner):
        pass


if __name__ == "__main__":
    p = Patient("P001", "Alice Smith", "1990-05-01", "0400000000", "1 Main St")
    dr = Practitioner("D001", "Dr Smith", "General Practice")
    appt = Appointment(p, dr, "2026-10-05", "10:00")
    print(appt.patient.name, "with", appt.practitioner.name, "at", appt.time, "-", appt.status.value)