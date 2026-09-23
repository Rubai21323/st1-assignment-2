# AI-generated version – Microsoft 365 Copilot, 23/09/2026 (Part D)
# Not written by me. Kept unchanged for comparison in Part E.

appointments = []

def add_appointment(patient_name, practitioner_name, appointment_time):
    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }
    appointments.append(appointment)
    return appointment

# Example usage
add_appointment("John Smith", "Dr Brown", "10:00 AM")
print(appointments)