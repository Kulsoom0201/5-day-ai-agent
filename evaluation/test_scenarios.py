# evaluation/test_scenarios.py
"""
Basic test harness for the CareFlow Healthcare Appointment Assistant.

This script simulates user interactions without needing manual input.
It verifies:
- Booking a new appointment
- Rescheduling an appointment
- Canceling an appointment

Run with:
    python -m evaluation.test_scenarios
"""

from agents.orchestrator_agent import OrchestratorAgent


def run_test(test_name, orchestrator, user_id, message):
    print(f"\n---------------------")
    print(f"TEST: {test_name}")
    print(f"USER: {message}")
    response = orchestrator.handle_user_message(user_id, message)
    print(f"AGENT: {response}")


def main():
    orchestrator = OrchestratorAgent()
    user_id = "test_user"

    # 1. Test new appointment booking
    run_test(
        test_name="Book appointment",
        orchestrator=orchestrator,
        user_id=user_id,
        message="I need a cardiology appointment in the evening",
    )

    # 2. Test rescheduling
    run_test(
        test_name="Reschedule appointment",
        orchestrator=orchestrator,
        user_id=user_id,
        message="Please reschedule my appointment to the morning",
    )

    # 3. Test cancellation
    run_test(
        test_name="Cancel appointment",
        orchestrator=orchestrator,
        user_id=user_id,
        message="Cancel my appointment",
    )

    print("\n---------------------")
    print("All test scenarios executed.")
    print("---------------------\n")


if __name__ == "__main__":
    main()

