# agents/scheduler_agent.py
"""
SchedulerAgent:
- Wraps interaction with scheduler and calendar tools.
- Decides which slots to offer and returns a simple result object.
"""

from dataclasses import dataclass
from typing import Dict, Any, Optional

from tools.clinic_scheduler_tool import ClinicSchedulerTool
from tools.calendar_tool import CalendarTool


@dataclass
class SchedulerResult:
    success: bool
    message: str
    appointment_id: Optional[str] = None
    slot: Optional[Dict[str, Any]] = None


class SchedulerAgent:
    """
    Handles booking, rescheduling, and canceling appointments
    by calling the underlying tools.
    """

    def __init__(self) -> None:
        self._scheduler_tool = ClinicSchedulerTool()
        self._calendar_tool = CalendarTool()

    def book_appointment(
        self,
        user_id: str,
        request_data: Dict[str, Any],
        session: Dict[str, Any],
    ) -> SchedulerResult:
        department = request_data.get("department", "General")
        time_of_day = request_data.get("time_of_day", "any")

        # 1. Find doctor slots based on department/time
        slots = self._scheduler_tool.find_available_slots(department=department, time_of_day=time_of_day)

        if not slots:
            return SchedulerResult(
                success=False,
                message=f"No available slots found for {department} in the {time_of_day}.",
            )

        # 2. Pick the first slot that does not conflict with user's calendar
        for slot in slots:
            if not self._calendar_tool.has_conflict(user_id=user_id, slot=slot):
                # 3. Book it
                appointment_id = self._scheduler_tool.book_slot(user_id=user_id, slot=slot)
                self._calendar_tool.add_appointment(user_id=user_id, appointment_slot=slot)

                return SchedulerResult(
                    success=True,
                    message="Appointment booked successfully.",
                    appointment_id=appointment_id,
                    slot=slot,
                )

        return SchedulerResult(
            success=False,
            message="Found slots, but they all conflict with your existing schedule.",
        )

    def reschedule_appointment(
        self,
        user_id: str,
        request_data: Dict[str, Any],
        session: Dict[str, Any],
    ) -> SchedulerResult:
        last_appointment_id = session.get("last_appointment_id")
        if not last_appointment_id:
            return SchedulerResult(
                success=False,
                message="I couldn't find a previous appointment to reschedule.",
            )

        department = request_data.get("department", "General")
        time_of_day = request_data.get("time_of_day", "any")

        slots = self._scheduler_tool.find_available_slots(department=department, time_of_day=time_of_day)
        if not slots:
            return SchedulerResult(
                success=False,
                message=f"No alternative slots available for {department} in the {time_of_day}.",
            )

        new_slot = slots[0]  # naive choice for demo
        success = self._scheduler_tool.reschedule_appointment(last_appointment_id, new_slot)
        if not success:
            return SchedulerResult(
                success=False,
                message="Unable to reschedule the appointment due to an internal error.",
            )

        self._calendar_tool.update_appointment(user_id=user_id, appointment_slot=new_slot)

        return SchedulerResult(
            success=True,
            message="Appointment rescheduled successfully.",
            appointment_id=last_appointment_id,
            slot=new_slot,
        )

    def cancel_appointment(
        self,
        user_id: str,
        request_data: Dict[str, Any],
        session: Dict[str, Any],
    ) -> SchedulerResult:
        last_appointment_id = session.get("last_appointment_id")
        if not last_appointment_id:
            return SchedulerResult(
                success=False,
                message="I couldn't find a previous appointment to cancel.",
            )

        success = self._scheduler_tool.cancel_appointment(last_appointment_id)
        if not success:
            return SchedulerResult(
                success=False,
                message="Unable to cancel the appointment due to an internal error.",
            )

        self._calendar_tool.remove_appointment(user_id=user_id, appointment_id=last_appointment_id)

        return SchedulerResult(
            success=True,
            message="Your appointment has been canceled.",
            appointment_id=last_appointment_id,
        )

