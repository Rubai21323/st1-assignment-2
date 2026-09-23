# Stage 1 – AI Usage Log

**Tool used:** Microsoft 365 Copilot (UC approved, protected mode)
**Date:** 23/09/2026
**Evidence:** screenshots/partC_copilot_1.png – partC_copilot_4.png

## Part C – AI as tutor

### Before AI – what I already knew
(Summarise in 1–2 lines what you found yourself in Part B before asking Copilot.)

### Prompt I used
Act as a Python tutor. I am learning introductory software technology.
Here is a small appointment-booking function.
1. Explain what the code does. 2. Identify three limitations.
3. Suggest improvements. 4. Do not rewrite the whole application.
5. Ask me two questions to test my understanding.
(+ the book_appointment function)

### Summary of Copilot's explanation
- Explained the list, the function's three inputs, the empty-name check, the dictionary and append.
- Gave an example showing what the list looks like after one booking.

### Evaluation of Copilot's suggestions
| Copilot suggestion | Useful / Unclear / Incorrect / Out of scope | Decision (Accept / Modify / Reject / Keep unverified) | Why (my reasoning) |
|---|---|---|---|
| Limitation 1: only patient name is validated | Useful | Accept | The code checks the patient name, but the practitioner name and appointment time are not checked, so the system accepts invalid data in those fields. |
| Limitation 2: no check for duplicate bookings | Useful | Accept | This is a real functional flaw because the system would allow double-booking the same practitioner at the same time. |
| Limitation 3: appointment time is plain text | Useful | Accept | It correctly notes that "10:00 AM" is just a string, so there is no protection against invalid inputs like "banana". |
| Improvement: validate all inputs | Useful | Accept | Implementing proper validation is essential to prevent bad data from entering the system. |
| Improvement: use datetime module | Useful | Reject | datetime is built into Python, so it is a good long-term solution, but it adds too much complexity for this simple starter code. |
| Improvement: prevent conflicting appointments | Useful | Accept | This is a vital safety feature for a clinic booking system to avoid scheduling two patients with the same doctor. |
| Design note: global `appointments` list → use a class later | Out of scope | Reject | Using classes and OOP is likely not covered in Week 4, and the handout implies keeping the system simple for now. |

### What Copilot missed
- Copilot didn't point out that there is no way to cancel, search, or change an existing appointment once it is booked.
- When I tested a patient name with only spaces the program accepted it as a valid name, which means the original check only works for truly empty strings, not blank-looking names.
- Copilot also did not mention that the system does not validate if the practitioner name is a real doctor or if they work at the clinic.
- Copilot also did not mention that all bookings are lost when the program closes, because the data is only stored in a temporary list in memory.

### Copilot's questions and my answers
1. Q: What happens with `book_appointment("", "Dr Smith", "10:00 AM")`?
   A: The function checks if patient_name is empty (falsy). Since "" is empty, it will trigger the error check, print a message like "Error: Patient name cannot be empty", and will not add the appointment to the list.
   Verified by running it? Yes – I predicted it would print an error message, but when I ran it the program stopped with a ValueError Traceback. This means  the whole program stops, so the receptionist can't book any more appointments until they fix the code.
2. Q: Why is booking Alice and Bob with Dr Smith at 10:00 a problem?
   A: It is a problem because the book_appointment function does not check if the practitioner is already booked at that time. It will simply add both appointments to the list, resulting in a double-booking conflict for Dr. Smith. The code needs a loop to check for overlapping times before adding a new appointment.