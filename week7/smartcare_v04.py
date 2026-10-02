from enum import Enum


class AppointmentStatus(Enum):
    BOOKED = "Booked"
    CANCELLED = "Cancelled"
    COMPLETED = "Completed"


class Patient:
    def __init__(self, patient_id, name, date_of_birth, phone, address):
        self.patient_id = patient_id
        self.name = name
        self.date_of_birth = date_of_birth
        self.phone = phone
        self.address = address

    def update_contact(self, phone, address):
        self.phone = phone
        self.address = address


class Practitioner:
    def __init__(self, practitioner_id, name):
        self.practitioner_id = practitioner_id
        self.name = name


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
    dr = Practitioner("D001", "Dr Smith")
    appt = Appointment(p, dr, "2026-10-05", "10:00")
    print(appt.patient.name, "with", appt.practitioner.name, "at", appt.time, "-", appt.status.value)