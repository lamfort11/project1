def cornersHeuristic(state, problem):
    """
    A heuristic for the CornersProblem that you defined.

      state:   The current search state
               (a data structure you chose in your search problem)

      problem: The CornersProblem instance for this layout.

    This function should always return a number that is a lower bound on the
    shortest path from the state to a goal of the problem; i.e.  it should be
    admissible as well as consistent.
    """
    corners = problem.corners
    walls = problem.walls 

    "*** YOUR CODE HERE ***"
    current_position = state[0]
    visited_corners = state[1]
    
    unvisited_corners = []
    for i in range(4):
        if not visited_corners[i]:
            unvisited_corners.append(corners[i])
            
    if not unvisited_corners:
        return 0

    import itertools
    
    min_distance = float('inf')
    
    for path in itertools.permutations(unvisited_corners):
        current = current_position
        path_distance = 0
        
        for corner in path:
            path_distance += util.manhattanDistance(current, corner)
            current = corner 
            
        if path_distance < min_distance:
            min_distance = path_distance

    return min_distance
