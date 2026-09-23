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
| Runs successfully? | No - It crashes on blank names or None values. | Yes - It does not crash, but it saves bad data instead. |
| Uses only required features? | Yes - It sticks to the basic handout requirements. | Yes - It only uses a list and dictionary. |
| Adds assumptions? | No - It follows the handout structure. | Yes - It assumes all input will be valid text. |
| Handles errors? | Partly - It checks for empty names, but crashes on other bad inputs. | No - It does not check for anything, so it saves bad data. |
| Could I explain it? | Yes - I understand the logic and where it fails. | Yes - The code is simple enough to explain. |