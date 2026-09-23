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

## Part B – Limitations of the starter code (AI OFF)
- Data is not saved permanently; if the program closes, all bookings are lost because it only uses a temporary list in memory.
- The book_appointment function does not check if the practitioner is already booked at that time, which allows double-booking.
- There is no validation for the date and time format, so text like 'banana' would be accepted instead of a real time.
- The code does not support cancelling, searching, or changing an existing appointment.
- The book_appointment function does not check if the practitioner's name is valid or if they even work at the clinic.

## Part H – Reflection

Before using AI, I ran the starter code myself and found five main limitations. The biggest issues were that all bookings are lost when the program closes, and it had no way to stop double-bookings.

Copilot helped me understand what the code was actually doing. It explained how the `book_appointment` function was just adding dictionaries to a simple list.

When I asked Copilot to write its own version, it assumed that all the data typed in would be perfect. When I tested it, that wasn't true. Unlike the human version, it didn't crash, but it quietly saved bad data like an empty name or a `None` time without any warning.

I verified the AI's claims by running the code myself. For example, I thought an empty name would print a friendly error, but it actually crashed with a ValueError. I also found that the code accepted three spaces (`"   "`) as a real name, which Copilot completely missed.

I chose to fix double booking because it is a serious safety problem for a clinic. My check loops through the appointments list and compares the practitioner and time. The remaining engineering work was mine: choosing which one fix mattered most, testing before and after the change, and deciding what was out of scope. The fix still doesn't show a friendly message; it just raises a ValueError.