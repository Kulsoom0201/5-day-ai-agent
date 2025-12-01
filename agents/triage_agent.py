# agents/triage_agent.py
"""
TriageAgent:
- Extracts high-level intent (book / reschedule / cancel)
- Produces a minimal structured request_data dict
This is a simple placeholder, not a real NLP/LLM model.
"""

from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class TriageResult:
    intent: str  # "book", "reschedule", "cancel", "unknown"
    request_data: Dict[str, Any]


class TriageAgent:
    """
    Naive triage agent using keyword-based heuristics.
    Replace with an LLM call in a real system.
    """

    def triage(self, message: str, session: Dict[str, Any]) -> TriageResult:
        lower_msg = message.lower()

        # 1. Detect intent
        if any(word in lower_msg for word in ["book", "appointment", "schedule", "see a doctor"]):
            intent = "book"
        elif "reschedule" in lower_msg or "change" in lower_msg:
            intent = "reschedule"
        elif "cancel" in lower_msg:
            intent = "cancel"
        else:
            intent = "unknown"

        # 2. Crude specialty detection
        if "cardio" in lower_msg or "heart" in lower_msg:
            department = "Cardiology"
        elif "skin" in lower_msg or "derma" in lower_msg:
            department = "Dermatology"
        elif "ent" in lower_msg or "ear" in lower_msg or "nose" in lower_msg or "throat" in lower_msg:
            department = "ENT"
        else:
            department = "General"

        # 3. Very basic time preference detection
        if "morning" in lower_msg:
            time_of_day = "morning"
        elif "afternoon" in lower_msg:
            time_of_day = "afternoon"
        elif "evening" in lower_msg or "after 5" in lower_msg:
            time_of_day = "evening"
        else:
            time_of_day = "any"

        request_data = {
            "department": department,
            "time_of_day": time_of_day,
            # In a real system you'd parse date ranges, urgency, etc.
        }

        return TriageResult(intent=intent, request_data=request_data)

