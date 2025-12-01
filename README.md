# 5-day-ai-agent
I am participating in a capstone project of 5 day ai agent.

# CareFlow – AI Healthcare Appointment Assistant (Agents for Good)

CareFlow is a multi-agent AI assistant that helps patients **find, schedule, reschedule, and cancel** medical appointments with clinics.

It was built as a submission for the **Kaggle "Agents Intensive – Capstone Project"** in the **Agents for Good** track.

---

## 🎯 Problem

Many clinics (especially in low-resource settings) still rely on:

- Phone calls and spreadsheets
- Handwritten appointment books
- Manual checking of doctor availability

This leads to long wait times, double bookings, and a bad experience for both **patients** and **staff**.

---

## 💡 Solution

CareFlow is an **LLM-powered, multi-agent system** that:

1. Understands patient requests in natural language  
2. Extracts structured intent (doctor/specialty, urgency, time preferences)  
3. Checks a **clinic scheduling tool** for availability  
4. Suggests appointment options and books/reschedules/cancels them  
5. Remembers patient preferences across sessions

---

## 🧠 Key Features (Course Concepts)

- **Multi-Agent System (Sequential):**
  - `OrchestratorAgent` – coordinates the workflow
  - `TriageAgent` – turns free text into structured appointment requests
  - `SchedulerAgent` – calls tools to search/book slots
  - `NotificationAgent` – creates friendly confirmations & reminders

- **Tools:**
  - `clinic_scheduler_tool` – mock OpenAPI-like scheduling API
  - `calendar_tool` – simulates patient calendar conflicts

- **Sessions & Memory:**
  - In-memory session service
  - Simple patient profile store (doctor + time preferences, appointment history)

- **Context Engineering:**
  - Conversation summaries to keep context compact

- **Observability:**
  - Structured logging of:
    - Inputs
    - Agent decisions
    - Tool calls
    - Final outcomes

- **Evaluation:**
  - Scripted test scenarios in `evaluation/test_scenarios.py`

---

## 🏗 Architecture

High-level flow:

```text
User → OrchestratorAgent
     → TriageAgent (extracts structured info)
     → SchedulerAgent (calls clinic_scheduler_tool + calendar_tool)
     → OrchestratorAgent (confirm choice)
     → NotificationAgent (confirmation & summary)
     → User


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
README.md
