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


class InvalidAppointmentStatusTransitionError(Exception):
    """Raised when an appointment status transition is not allowed."""


class Appointment:
    def __init__(
        self,
        patient: Patient,
        practitioner: Practitioner,
        date: str,
        time: str,
    ) -> None:
        if patient is None or practitioner is None:
            raise ValueError("Appointment needs a patient and a practitioner")
        if not date or not date.strip():
            raise ValueError("Appointment date cannot be empty")
        if not time or not time.strip():
            raise ValueError("Appointment time cannot be empty")
        self.patient: Patient = patient
        self.practitioner: Practitioner = practitioner
        self.date: str = date
        self.time: str = time

        # FR-01, FR-04: all new appointments start as BOOKED.
        self._status: AppointmentStatus = AppointmentStatus.BOOKED

    @property
    def status(self) -> AppointmentStatus:
        return self._status

    def cancel(self) -> None:
        """
        Cancel a booked appointment.

        Raises:
            InvalidAppointmentStatusTransitionError:
                If the appointment is not currently BOOKED.
        """
        if self.status is not AppointmentStatus.BOOKED:
            raise InvalidAppointmentStatusTransitionError(
                f"Cannot cancel appointment with status "
                f"'{self.status.value}'."
            )

        self._status = AppointmentStatus.CANCELLED

    def complete(self) -> None:
        """
        Mark a booked appointment as completed.

        Raises:
            InvalidAppointmentStatusTransitionError:
                If the appointment is not currently BOOKED.
        """
        if self.status is not AppointmentStatus.BOOKED:
            raise InvalidAppointmentStatusTransitionError(
                f"Cannot complete appointment with status "
                f"'{self.status.value}'."
            )

        self._status = AppointmentStatus.COMPLETED
        

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
    # 1. Valid objects
    p = Patient("P001", "Alice Smith", "1990-05-01", "0400000000", "1 Main St")
    dr = Practitioner("D001", "Dr Smith", "General Practice")
    appt = Appointment(p, dr, "2026-10-05", "10:00")
    print("1. Valid:", appt.patient.name, "with", appt.practitioner.name, "at", appt.time, "-", appt.status.value)

    # 2. Invalid input: patient name is only spaces
    try:
        Patient("P002", "   ", "1990-01-01", "0400000001", "2 Main St")
    except ValueError as error:
        print("2. Blank name rejected:", error)

    # 3. Invalid input: no appointment time
    try:
        Appointment(p, dr, "2026-10-05", None)
    except ValueError as error:
        print("3. Missing time rejected:", error)

    # 4. Cancel a booked appointment
    appt.cancel()
    print("4. After cancel:", appt.status.value)

    # 5. Illegal repeated transition: cancel again
    try:
        appt.cancel()
    except InvalidAppointmentStatusTransitionError as error:
        print("5. Second cancel rejected:", error)

    # 6. Try to change the status directly from outside
    try:
        appt.status = AppointmentStatus.BOOKED
    except AttributeError as error:
        print("6. Direct status change rejected:", error)