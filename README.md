# 5-day-ai-agent
I am participating in a capstone project of 5 day ai agent.

🏥 CareFlow — AI Healthcare Appointment Assistant (Agents for Good)

CareFlow is a multi-agent AI assistant that helps patients find, schedule, reschedule, and cancel medical appointments using natural language conversations.
It reduces scheduling friction, avoids calendar conflicts, and remembers patient preferences — supporting both patients and clinic staff.

Submission for Kaggle – Agents Intensive Capstone Project
Track: 🩺 Agents for Good

## Problem

In many clinics — especially in low-resource settings — appointments are still managed through:

- Phone calls  
- Notebooks or spreadsheets  
- Manual calendar checking  


This creates:

Long wait times

Missed or double bookings

Frustration for both patients and staff

Scheduling logistics consume time that could instead be used for care.

💡 Solution

CareFlow automates medical appointment management using AI agents.
Patients can express their needs naturally, e.g.:

“I need a cardiology appointment next week after 5 pm.”

CareFlow will:

Understand the intent

Collect necessary information using questions only if needed

Check doctor/clinic availability

Suggest suitable appointment slots

Finalize booking, reschedule, or cancellation

Send a clear confirmation summary

The system remembers doctor preferences, time preferences, and past appointments for smoother repeat interactions.

🧠 Key Concepts from the Course

CareFlow demonstrates the following course requirements:

Concept	Implementation
Multi-Agent System	Orchestrator, Triage, Scheduler, Notification
Tools	Custom tools for clinic scheduling & calendar conflict checks
Memory	Session memory + long-term patient preference memory
Context Engineering	Conversation compaction to prevent token overload
Observability	Structured logs for agent decisions & tool calls
Evaluation	Script-based test scenarios validating booking flows
🏗 Architecture & Flow
User
 ↓
Orchestrator Agent
 ↓
Triage Agent → extracts structured request from natural language
 ↓
Scheduler Agent → calls tools (clinic scheduler + calendar)
 ↓
Orchestrator Agent → confirms selected slot
 ↓
Notification Agent → sends friendly summary/confirmation
 ↓
User


Agents share session memory and patient profile memory (doctor & time preferences).

📂 Project Structure
agents/
  orchestrator_agent.py
  triage_agent.py
  scheduler_agent.py
  notification_agent.py

tools/
  clinic_scheduler_tool.py
  calendar_tool.py

memory/
  session_service.py
  patient_memory.py

evaluation/
  test_scenarios.py

main.py
requirements.txt
README.md

🛠 Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/Kulsoom0201/5-day-ai-agent.git
cd 5-day-ai-agent

2️⃣ Create a virtual environment (optional but recommended)
python -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt


⚠️ API keys (if any) must be added via environment variables — never committed to the repository.

💬 Usage Example
Start the agent:
python main.py


Then interact with messages like:

I need a dermatology appointment next Tuesday morning
Reschedule my appointment with Dr. Mehta to Friday evening
Cancel my appointment tomorrow at 3pm


The agent will:

Ask follow-up questions if needed

Check availability with scheduling tools

Suggest slots

Book/reschedule/cancel after confirmation

And return a summary such as:

✔ Your appointment with Dr. Mehta (Cardiology) is confirmed for Wednesday 6:30 PM at Sunrise Clinic.
A reminder will be sent 24 hours prior.

🧪 Evaluation / Testing

To run scripted test cases:

python -m evaluation.test_scenarios


This verifies:

Booking flow

Rescheduling flow

Cancellation flow

Logs show each agent call + each tool call step-by-step.

⚠️ Limitations & Future Work
Current Limitations	Planned Improvements
Uses mock scheduling APIs	Integrate real clinic APIs with authentication
No mobile/voice interface	Add WhatsApp / SMS / voice support
English-only	Add multilingual support
Console-only interaction	Deploy as web app / chatbot front-end
No caregiver mode	Add “book for family member” feature
🛡 License & Disclaimer

License: MIT (or any preferred open-source license)

Disclaimer:
CareFlow does not provide medical advice and does not replace professional healthcare judgment. It supports appointment logistics only.

🙌 Acknowledgements

Built as part of the Kaggle + Google Agents Intensive Program.
Inspired by the need to make healthcare more accessible and reduce administrative burden.
