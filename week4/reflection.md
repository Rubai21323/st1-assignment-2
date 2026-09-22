# Stage 1 – Reflection

## Part A – Understanding the problem (AI OFF)

### What data must be stored?
- Patient name
- Patient date of birth or unique ID (to tell apart patients with the same name like "Rubai Max")
- Patient contact details (phone number or address)
- Practitioner name
- Appointment time (date and time)

### What functions might be useful?
- Book a new appointment
- View the schedule for a practitioner or day
- Cancel or reschedule an existing appointment

### What could go wrong?
- Double-booking a practitioner for the same time slot.
- Booking the wrong patient because two people have the same name.
- Booking an appointment outside of clinic working hours.

### What requirements are unclear?
- How long is a standard appointment slot (e.g., 15 mins, 30 mins)?
- What are the clinic's operating hours?
- Do different types of appointments require different lengths of time?
