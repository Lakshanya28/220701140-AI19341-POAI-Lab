def dfs_water_jug(jug1_capacity, jug2_capacity, target):
    visited = set()  # To track visited states
    solution = []  # To store the solution steps

    def dfs(jug1, jug2):
        # If the state is already visited, skip it
        if (jug1, jug2) in visited:
            return False

        # Mark the state as visited
        visited.add((jug1, jug2))
        solution.append((jug1, jug2))  # Add the current state to the solution

        # If the target is achieved in either jug, return True
        if jug1 == target or jug2 == target:
            return True

        # Explore all possible next states:
        next_states = [
            (jug1_capacity, jug2),  # Fill Jug1
            (jug1, jug2_capacity),  # Fill Jug2
            (0, jug2),              # Empty Jug1
            (jug1, 0),              # Empty Jug2
            # Pour Jug1 -> Jug2
            (max(0, jug1 - (jug2_capacity - jug2)), min(jug2_capacity, jug2 + jug1)),
            # Pour Jug2 -> Jug1
            (min(jug1_capacity, jug1 + jug2), max(0, jug2 - (jug1_capacity - jug1)))
        ]

        # Recursively explore each next state
        for state in next_states:
            if dfs(state[0], state[1]):
                return True

        # Backtrack if no solution is found
        solution.pop()
        return False

    # Start DFS from the initial state (0, 0)
    if dfs(0, 0):
        return solution
    else:
        return "No solution found"

# Example usage
steps = dfs_water_jug(4, 3, 2)
print("Steps to achieve the target:")
for i, step in enumerate(steps):
    #print(f"Step {i + 1}: Jug1 = {step[0]}, Jug2 = {step[1]}")
    print("step:",i+1,"j1-",step[0],"j2-",step[1])
