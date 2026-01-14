
def clean_sessions(pool, sessions, dead_servers):
    cleaned = []
    for session in sessions:
        server = session[0]
        if server not in dead_servers:
            cleaned.append(session)
        elif server not in pool:
            cleaned.append(session)
    
    cleaned.sort()
    return cleaned


# Test
pool = ("srv-A", "srv-B", "srv-C", "srv-D")
sessions = [("srv-B", "cli-1"), ("srv-A", "cli-2"), ("srv-C", "cli-3"),
            ("srv-B", "cli-4"), ("srv-D", "cli-5")]
dead = ["srv-B", "srv-D"]

result = clean_sessions(pool, sessions, dead)
print(f"Cleaned Sessions: {result}")
# Expected: [('srv-A', 'cli-2'), ('srv-C', 'cli-3')]
