from collections import defaultdict
from functools import reduce
from typing import List, Dict, Set


logs = [
    {"user": "24012", "action": "YouTube", "duration": 1.5},
    {"user": "24013", "action": "Instagram", "duration": 2.0},
    {"user": "24016", "action": "WhatsApp", "duration": 0.8},
    {"user": "24014", "action": "YouTube", "duration": 1.2},
    {"user": "24017", "action": "Chrome", "duration": 1.7},
    {"user": "24015", "action": "Instagram", "duration": 2.5},
    {"user": "24019", "action": "Chrome", "duration": 1.0},
]


#
def total_time_per_user(logs: List[Dict]) -> Dict[str, float]:

    result = defaultdict(float)

    for log in logs:
        result[log["user"]] += log["duration"]

    return dict(result)



def most_active_users(logs: List[Dict], k: int) -> List[str]:

    totals = total_time_per_user(logs)

    return [
        user for user, _ in
        sorted(totals.items(), key=lambda x: x[1], reverse=True)[:k]
    ]



def unique_actions(logs: List[Dict]) -> Set[str]:

    return {log["action"] for log in logs}



def total_activity_time(logs: List[Dict]) -> float:

    return reduce(lambda acc, log: acc + log["duration"], logs, 0.0)



print("Total time per user:")
print(total_time_per_user(logs))

print("\nMost active users:")
print(most_active_users(logs, 2))

print("\nUnique actions:")
print(unique_actions(logs))

print("\nTotal activity time:")
print(total_activity_time(logs))