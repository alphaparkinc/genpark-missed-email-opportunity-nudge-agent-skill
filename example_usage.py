from client import MissedEmailOpportunityNudgeAgentClient

def main():
    client = MissedEmailOpportunityNudgeAgentClient()
    thread = [{"sender": "prospect@acme.com", "subject": "Proposal details", "hours_ago": 72}]
    res = client.detect_and_nudge(thread, 48)
    print(f"Missed Opportunity: {res['missed_opportunity_detected']} ({res['urgency']})")
    print(f"Suggested Nudge: '{res['suggested_nudge_draft']}'")

if __name__ == "__main__":
    main()
