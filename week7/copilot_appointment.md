Below is an implementation that follows the approved UML and business rules exactly. The only additions beyond the UML are:

AppointmentStatus enum (required by the specification).
InvalidAppointmentStatusTransitionError custom exception (required by the specification for illegal transitions).
Runtime checks inside cancel() and complete() to enforce the status-transition rules.
from enum import Enum


class AppointmentStatus(Enum):
    BOOKED = "Booked"
    CANCELLED = "Cancelled"
    COMPLETED = "Completed"


class InvalidAppointmentStatusTransitionError(Exception):
    """Raised when an appointment status transition is not allowed."""


class Appointment:
    def __init__(
        self,
        patient: "Patient",
        practitioner: "Practitioner",
        date: str,
        time: str,
    ) -> None:
        self.patient: Patient = patient
        self.practitioner: Practitioner = practitioner
        self.date: str = date
        self.time: str = time

        # FR-01, FR-04: all new appointments start as BOOKED.
        self.status: AppointmentStatus = AppointmentStatus.BOOKED

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

        self.status = AppointmentStatus.CANCELLED

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

        self.status = AppointmentStatus.COMPLETED

Design decisions not directly visible in the UML
Status is initialized to BOOKED in the constructor because the business rules state that every new appointment starts as booked (FR-01, FR-04).
Illegal transitions raise InvalidAppointmentStatusTransitionError to satisfy the requirement that actions such as cancelling twice, completing twice, or completing a cancelled appointment are rejected.
Cancelled appointments remain as objects because cancel() only changes the status to CANCELLED; it does not delete or remove the appointment (FR-05).
Forward-reference type hints ("Patient" and "Practitioner") are used so the existing Patient and Practitioner classes can be referenced without redefining them.