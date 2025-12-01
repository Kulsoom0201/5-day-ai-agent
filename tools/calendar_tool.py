# tools/calendar_tool.py
"""
CalendarTool:
A simple per-user calendar that tracks appointments to avoid conflicts.
This is in-memory and purely illustrative.
"""

from typing import Dict, Any, List


class CalendarTool:
    def __init__(self) -> None:
        # user_id -> list of slots
        self._user_appointments: Dict[str, List[Dict[str, Any]]] = {}

    def has_conflict(self, user_id: str, slot: Dict[str, Any]) -> bool:
        """
        Simple conflict check: same date & time considered a conflict.
        """
        user_slots = self._user_appointments.get(user_id, [])
        for existing in user_slots:
            if (
                existing.get("date") == slot.get("date")
                and existing.get("time") == slot.get("time")
            ):
                return True
        return False

    def add_appointment(self, user_id: str, appointment_slot: Dict[str, Any]) -> None:
        """
        Store a new appointment slot for the user.
        """
        self._user_appointments.setdefault(user_id, []).append(appointment_slot)

    def update_appointment(self, user_id: str, appointment_slot: Dict[str, Any]) -> None:
        """
        For simplicity, just replace any slot with same date/time.
        In a real system, we'd store an appointment_id and update by id.
        """
        user_slots = self._user_appointments.get(user_id, [])
        new_slots: List[Dict[str, Any]] = []

        for existing in user_slots:
            if (
                existing.get("date") == appointment_slot.get("date")
                and existing.get("time") == appointment_slot.get("time")
            ):
                # skip old version of this slot
                continue
            new_slots.append(existing)

        new_slots.append(appointment_slot)
        self._user_appointments[user_id] = new_slots

    def remove_appointment(self, user_id: str, appointment_id: str) -> None:
        """
        In this simple demo, we don't track appointment IDs in the calendar.
        We'll just clear all appointments for simplicity.
        """
        # For a real implementation, you'd match against appointment_id.
        self._user_appointments.pop(user_id, None)

