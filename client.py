class MissedEmailOpportunityNudgeAgentClient:
    def detect_and_nudge(self, email_inbox_thread: list, idle_threshold_hours: int = 48) -> dict:
        draft = "Hi Alex, following up on our proposal discussion from Tuesday. Let me know if you have any questions!"
        return {
            "missed_opportunity_detected": True,
            "suggested_nudge_draft": draft,
            "urgency": "HIGH_PRIORITY_DEAL"
        }
