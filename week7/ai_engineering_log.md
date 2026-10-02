# Stage 4 – AI Engineering Log

**Tool:** Microsoft 365 Copilot (UC approved), 03/10/2026
**Prompt:** see screenshots/partD_copilot_1.png
**Raw output:** copilot_appointment.md

## Part E – Review of generated code

| Check | Finding | Decision |
|---|---|---|
| Model consistency (matches UML?) | Yes – attributes and the methods cancel() and complete() match the approved UML | Accept |
| Unsupported features | Copilot re-defines AppointmentStatus on lines 9–12, but it already exists in smartcare_v04.py | Reject – delete the duplicate and use the existing AppointmentStatus already in the file |
| Public state mutation | self.status is a public attribute, so outside code can set it directly and skip the checks in cancel() and complete() | Modify – rename to self._status and add a read-only status property |
| Unnecessary inheritance | Appointment has no parent class; the custom exception inherits from Exception, which Python needs for raise to work | Accept – this inheritance is needed |
| Invented dependencies | No imports or classes from outside the project are used | Accept |
| Error handling | Illegal status changes raise an error, but an empty date, an empty time or a None patient are not checked | Modify – add checks in __init__ that raise ValueError for these |