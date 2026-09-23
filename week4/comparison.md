# Stage 1 – Human vs AI Comparison

## Part F – Test results

| Test | Input | Human version (smartcare_v01.py) | AI version (ai_version.py) |
|---|---|---|---|
| 1. Normal appointment | "Alice", "Dr Smith", "10:00 AM" | Accepted and displayed | Accepted and displayed |
| 2. Same practitioner/time twice | Alice and Bob, both Dr Smith 10:00 AM | Both booked, no warning | Both booked, no warning |
| 3. Blank patient name | "" | Crashed | Saved empty name |
| 4. None time | "Carol", "Dr Smith", None | Accepted – showed Time: None | Saved None as the time |

## Part E – Human vs AI comparison

| Question | Human version | AI version |
|---|---|---|
| Easy to understand? | Yes - It has clear validation checks. | Yes - It is shorter and simpler. |
| Runs successfully? | Partly - It runs, but crashes on a blank name. | Yes - It does not crash, but it saves bad data instead. |
| Uses only required features? | Yes - It sticks to the basic handout requirements. | Yes - It only uses a list and dictionary. |
| Adds assumptions? | No - It follows the handout structure. | Yes - It assumes all input will be valid text. |
| Handles errors? | Partly - It stops an empty name (but by crashing), and accepts double bookings and a None time. | No - It does not check for anything, so it saves bad data. |
| Could I explain it? | Yes - I understand the logic and where it fails. | Yes - The code is simple enough to explain. |

## Part G – One improvement

**Change:** Added a check in `book_appointment` that blocks a booking if the same practitioner already has an appointment at that time.

**Why this one:** This fixes the double-booking problem from the case study. It is a critical safety feature for a clinic, and it was the exact limitation we found in the starter code.

**Evidence:** Before the fix, Alice and Bob were both booked with Dr Smith at 10:00 AM (partF_human_test1-2.png). After the fix, the second booking was rejected with a ValueError (partG_double_booking_blocked.png).

**Limitation still remaining:** It still crashes with a ValueError instead of showing a friendly error message when a double booking is attempted. It also does not validate if the time is in the correct format (like "10:00 AM" vs "10:00").