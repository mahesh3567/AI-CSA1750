def print_state(state):
    jug1, jug2 = state
    print(f"Jug1: {jug1}, Jug2: {jug2}")
def dfs(jug1_capacity, jug2_capacity, target):
    visited = set()
    stack = [((0, 0), [])]  # Start with both jugs empty and an empty path
    visited.add((0, 0))
    while stack:
        (jug1, jug2), path = stack.pop()
        # Add current state to the path
        current_state = (jug1, jug2)
        path = path + [current_state]
        # Check if we have achieved the target in the first jug
        if jug1 == target and jug2 == 0:
            print("Solution found:")
            for i, state in enumerate(path, 1):
                print(f"{i}. {state}")
            return
        # Possible actions based on constraints
        actions = []
        # Fill the first jug
        if jug1 < jug1_capacity:
            actions.append((jug1_capacity, jug2))
        # Fill the second jug
        if jug2 < jug2_capacity:
            actions.append((jug1, jug2_capacity))
        # Empty the first jug
        if jug1 > 0:
            actions.append((0, jug2))
        # Empty the second jug
        if jug2 > 0:
            actions.append((jug1, 0))
        # Pour from the first jug to the second jug
        if jug1 > 0 and jug2 < jug2_capacity:
            pour_amount = min(jug1, jug2_capacity - jug2)
            actions.append((jug1 - pour_amount, jug2 + pour_amount))
        # Pour from the second jug to the first jug
        if jug2 > 0 and jug1 < jug1_capacity:
            pour_amount = min(jug2, jug1_capacity - jug1)
            actions.append((jug1 + pour_amount, jug2 - pour_amount))
        for action in actions:
            if action not in visited:
                visited.add(action)
                stack.append((action, path))
    print("No solution exists")
# Example usage
jug1_capacity = 4
jug2_capacity = 3
target = 2  # The target amount to measure in the first jug
dfs(jug1_capacity, jug2_capacity, target)