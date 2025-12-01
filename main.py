# main.py
"""
Entry point for the CareFlow Healthcare Appointment Assistant.

This is a simple CLI loop that:
- Creates an OrchestratorAgent
- Accepts user input
- Prints the assistant's response
"""

from agents.orchestrator_agent import OrchestratorAgent


def main() -> None:
    print("🩺 CareFlow - Healthcare Appointment Assistant")
    print("Type 'quit' or 'exit' to stop.\n")

    # In a real system, this could be a logged-in user id
    user_id = "demo_user"

    orchestrator = OrchestratorAgent()

    while True:
        user_message = input("You: ").strip()

        if user_message.lower() in {"quit", "exit"}:
            print("CareFlow: Goodbye! Take care. 💙")
            break

        response = orchestrator.handle_user_message(user_id=user_id, message=user_message)
        print(f"CareFlow: {response}\n")


if __name__ == "__main__":
    main()

