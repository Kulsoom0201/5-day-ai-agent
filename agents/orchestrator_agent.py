# agents/orchestrator_agent.py
"""
OrchestratorAgent coordinates the overall workflow:
- Understands high-level intent (book / reschedule / cancel / check)
- Delegates to sub-agents (triage, scheduler, notification)
- Manages simple per-user session state (in-memory)
"""

from typing import Dict, Any

from agents.triage_agent import TriageAgent
from agents.scheduler_agent import SchedulerAgent
from agents.notification_agent import NotificationAgent


class OrchestratorAgent:
    """
    High-level coordinator for the CareFlow assistant.
    """

    def __init__(self) -> None:
        # Simple in-memory session state keyed by user_id
        self._sessions: Dict[str, Dict[str, Any]] = {}

        # Sub-agents
        self._triage_agent = TriageAgent()
        self._scheduler_agent = SchedulerAgent()
        self._notification_agent = NotificationAgent()

    def _get_session(self, user_id: str) -> Dict[str, Any]:
        """
        Retrieve or create a session state for a given user.
        """
        if user_id not in self._sessions:
            self._sessions[user_id] = {
                "patient_profile": {},   # could hold preferences, history, etc.
                "last_appointment_id": None,
            }
        return self._sessions[user_id]

    def handle_user_message(self, user_id: str, message: str) -> str:
        """
        Main entry point for handling a user message.

        Steps:
        1. Get session state
        2. Let triage agent extract structured info + intent
        3. Call scheduler agent to interact with tools
        4. Use notification agent to generate final response message
        """
        session = self._get_session(user_id)

        # 1. Triage: extract intent and structured appointment request
        triage_result = self._triage_agent.triage(message, session)

        intent = triage_result.intent  # e.g. "book", "reschedule", "cancel"
        request = triage_result.request_data

        # 2. Call scheduler logic based on intent
        if intent == "book":
            scheduler_result = self._scheduler_agent.book_appointment(
                user_id=user_id,
                request_data=request,
                session=session,
            )
        elif intent == "reschedule":
            scheduler_result = self._scheduler_agent.reschedule_appointment(
                user_id=user_id,
                request_data=request,
                session=session,
            )
        elif intent == "cancel":
            scheduler_result = self._scheduler_agent.cancel_appointment(
                user_id=user_id,
                request_data=request,
                session=session,
            )
        else:
            # Fallback when we don't understand intent well
            return "I’m not sure if you want to book, reschedule, or cancel. Could you please clarify?"

        # Optionally store last appointment id in the session
        if scheduler_result.appointment_id:
            session["last_appointment_id"] = scheduler_result.appointment_id

        # 3. Create user-friendly notification/summary
        response = self._notification_agent.build_user_message(
            intent=intent,
            triage_result=triage_result,
            scheduler_result=scheduler_result,
        )
        return response

