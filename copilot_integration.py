# GHW Integration Task
challenges_done = ["Identity Lab", "Health-Tech", "Copilot Setup", "Simple App"]

def check_rank(count):
    if count >= 7:
        return "Top Tier Participant"
    return "Hacker"

print(f"Status: {check_rank(len(challenges_done) + 3)}")
