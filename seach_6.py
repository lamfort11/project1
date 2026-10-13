def cornersHeuristic(state: Any, problem: CornersProblem):
    position, visited_corners = state
    corners = problem.corners

    max_distance = 0

    for i in range(4):
        if not visited_corners[i]:
            distance = util.manhattanDistance(position, corners[i])

            if distance > max_distance:
                max_distance = distance

    return max_distance
