# Stage 3 - Model-Code Consistency Check

| UML element | In code? | Notes |
|---|---|---|
| AppointmentStatus enum (Booked, Cancelled, Completed) | Yes | Matches UML - 3 values, lines 4-7 |
| Patient: 5 attributes | Yes | All 5 set in `__init__` with `self.` |
| Patient.update_contact() | Yes | Implemented - updates phone and address (FR-07) |
| Practitioner: practitioner_id, name | Yes | Both set in `__init__` |
| Appointment: patient, practitioner, date, time, status | Yes | First 4 are parameters; status is not a parameter, it starts as `AppointmentStatus.BOOKED` (line 35) |
| Appointment.cancel(), set_status() | Yes | Methods exist but are still `pass` |
| AppointmentManager: appointments list | Yes | Starts as an empty list `[]` in `__init__` |
| AppointmentManager: book(), has_clash(), get_schedule() | Yes | Names and parameters match UML; all still `pass` |
| Multiplicity: Patient 1 — 0..* Appointment | Yes | Each Appointment stores one patient (`self.patient`); the many appointments live in `AppointmentManager.appointments` |

## Not implemented yet (by design)
- `Appointment.cancel()`, `Appointment.set_status()`, `AppointmentManager.book()`, `has_clash()` and `get_schedule()` are still `pass`, because the handout says not to implement full behaviour until the next stage. This stage only checks that the code structure matches the UML.