import random

# excuse categories
# "bug" – Excuses for why a bug exists.
# "deadline" – Excuses for missing deadlines.
# "PR" – Excuses for pull request delays.
# "meeting" – Excuses for missing or being late to meetings.
# "deployment" – Excuses for why a deployment failed.

EXCUSES = {
    "bug": [
        "It works on my machine.",
        "We just need to restart the server.",
        "It's probably an edge case we didn't consider.",
        "Must be a caching issue :(",
        "I didn't break it, it was like that before.",

    ],
    "deadline": [
        "We've underestimated the complexity of this project",
        "Testing took longer than expected.",
        "We had some last minute requirement changes.",
        "The deadline was an appoximation.",
        "The timeline was more of a suggestion."
    ],
    "PR": [
        "I was waiting for a review.",
        "I need to refactor before merging.",
        "It was a small change, so I didn't push it yet.",
        "I'm in a merge conflict... with my own code.",
        
    ],
    "meeting": [
        "I was on mute the whole time, whoops.",
        "My inertnet cut out.",
        "Sorry, time zones got confusing.",
        "There was a power outage in my building."

    ],
    "deployment": [
        "It worked in my branch...",
        "There was a merge conflict we havent caught yet.",
        "Looks like a version mismatch issue.",
    ],
}

#functions
def generate_excuse(category: str) ->str:
    if category in EXCUSES:
        return random.choice(EXCUSES[category])
    return "Invalid category. Use list_categories() to see all available categories."

def random_excuse() -> str:
    category = random.choice(list(EXCUSES.keys()))
    return generate_excuse(category)

def add_custom_excuse(category: str, excuse: str):
    if category in EXCUSES:
        EXCUSES[category].append(excuse)
    else:
        EXCUSES[category] = [excuse]

def list_categories() -> list:
    return list(EXCUSES.keys())