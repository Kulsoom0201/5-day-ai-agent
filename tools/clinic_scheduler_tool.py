# tools/clinic_scheduler_tool.py
"""
ClinicSchedulerTool:
A mock scheduling backend storing doctors and appointments in memory.

In a real system this would wrap a database or external API.
"""

from typing import List, Dict, Any
import uuid


class ClinicSchedulerTool:
    def __init__(self) -> None:
        # In-memory "database"
        self._doctors = [
            {"id": "doc-1", "name": "Dr. Mehta", "department": "Cardiology"},
            {"id": "doc-2", "name": "Dr. Rao", "department": "Dermatology"},
            {"id": "doc-3", "name": "Dr. Shah", "department": "ENT"},
            {"id": "doc-4", "name": "Dr. Kumar", "department": "General"},
        ]

        # Mock slots for simplicity
        # In a real system, slots would include real datetimes & capacity
        self._slots = [
            {
                "slot_id": "slot-1",
                "doctor_id": "doc-1",
                "doctor_name": "Dr. Mehta",
                "department": "Cardiology",
                "date": "2025-12-05",
                "time": "18:30",
                "time_of_day": "evening",
                "location": "Sunrise Clinic",
                "booked": False,
            },
            {
                "slot_id": "slot-2",
                "doctor_id": "doc-2",
                "doctor_name": "Dr. Rao",
                "department": "Dermatology",
                "date": "2025-12-05",
                "time": "10:00",
                "time_of_day": "morning",
                "location": "Downtown Medical Center",
                "booked": False,
            },
            {
                "slot_id": "slot-3",
                "doctor_id": "doc-4",
                "doctor_name": "Dr. Kumar",
                "department": "General",
                "date": "2025-12-06",
                "time": "15:00",
                "time_of_day": "afternoon",
                "location": "Sunrise Clinic",
                "booked": False,
            },
        ]

        self._appointments: Dict[str, Dict[str, Any]] = {}

    def find_available_slots(self, department: str, time_of_day: str) -> List[Dict[str, Any]]:
        """
        Return a list of slots matching department and time_of_day that are not booked.
        """
        results: List[Dict[str, Any]] = []
        for slot in self._slots:
            if slot["booked"]:
                continue
            if department != "General" and slot["department"] != department:
                continue
            if time_of_day != "any" and slot["time_of_day"] != time_of_day:
                continue
            results.append(slot)
        return results

    def book_slot(self, user_id: str, slot: Dict[str, Any]) -> str:
        """
        Mark a slot as booked and create an appointment record.
        """
        appointment_id = str(uuid.uuid4())
        slot["booked"] = True

        self._appointments[appointment_id] = {
            "id": appointment_id,
            "user_id": user_id,
            "slot": slot,
            "status": "booked",
        }
        return appointment_id

    def reschedule_appointment(self, appointment_id: str, new_slot: Dict[str, Any]) -> bool:
        """
        Reschedule an existing appointment to a new slot.
        """
        appointment = self._appointments.get(appointment_id)
        if not appointment:
            return False

        # Free old slot
        old_slot = appointment["slot"]
        old_slot["booked"] = False

        # Book new slot
        new_slot["booked"] = True
        appointment["slot"] = new_slot
        appointment["status"] = "booked"
        return True

    def cancel_appointment(self, appointment_id: str) -> bool:
        """
        Cancel an existing appointment.
        """
        appointment = self._appointments.get(appointment_id)
        if not appointment:
            return False

        slot = appointment["slot"]
        slot["booked"] = False
        appointment["status"] = "canceled"
        return True
