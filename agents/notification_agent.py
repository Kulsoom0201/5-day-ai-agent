# agents/notification_agent.py
"""
NotificationAgent:
- Builds user-facing messages from triage and scheduler results.
"""

from agents.triage_agent import TriageResult
from agents.scheduler_agent import SchedulerResult


class NotificationAgent:
    """
    Converts internal results into friendly, human-readable text responses.
    """

    def build_user_message(
        self,
        intent: str,
        triage_result: TriageResult,
        scheduler_result: SchedulerResult,
    ) -> str:
        if not scheduler_result.success:
            return scheduler_result.message

        slot = scheduler_result.slot or {}
        department = triage_result.request_data.get("department", "the doctor")

        date = slot.get("date", "an upcoming day")
        time = slot.get("time", "a convenient time")
        doctor = slot.get("doctor_name", "a specialist")
        location = slot.get("location", "the clinic")

        if intent == "book":
            return (
                f"Your appointment with {doctor} ({department}) is booked for "
                f"{date} at {time} at {location}. "
                "If you’d like, I can help you reschedule or cancel later."
            )
        elif intent == "reschedule":
            return (
                f"Your appointment has been rescheduled to {date} at {time} "
                f"with {doctor} at {location}."
            )
        elif intent == "cancel":
            return "Your appointment has been canceled. Let me know if you want to book a new one."
        else:
            return scheduler_result.message

