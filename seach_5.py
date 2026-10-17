class CornersProblem(search.SearchProblem):
   
    def __init__(self, startingGameState):
   
        self.walls = startingGameState.getWalls()
        self.startingPosition = startingGameState.getPacmanPosition()
        top, right = self.walls.height-2, self.walls.width-2
        self.corners = ((1,1), (1,top), (right, 1), (right, top))
        for corner in self.corners:
            if not startingGameState.hasFood(*corner):
                print('Warning: no food in corner ' + str(corner))
        self._expanded = 0 

      
    def getStartState(self):
        """
        Returns the start state (in your state space, not the full Pacman state space)
        """
        "*** YOUR CODE HERE ***"
       
        visited_corners = tuple(self.startingPosition == corner for corner in self.corners)
        
        return (self.startingPosition, visited_corners)

    def isGoalState(self, state):
        """
        Returns whether this search state is a goal state of the problem.
        """
        "*** YOUR CODE HERE ***"
        visited_corners = state[1]

        return all(visited_corners)

    def getSuccessors(self, state):
        """
        Returns successor states, the actions they require, and a cost of 1.
        """
        successors = []
        current_position = state[0]
        visited_corners = state[1]
        
        for action in [Directions.NORTH, Directions.SOUTH, Directions.EAST, Directions.WEST]:
          
            x, y = current_position
            dx, dy = Actions.directionToVector(action)
            next_x, next_y = int(x + dx), int(y + dy)
            
            if not self.walls[next_x][next_y]:
                next_position = (next_x, next_y)
                
                next_visited_corners = list(visited_corners)
                for i in range(4):
                    if next_position == self.corners[i]:
                        next_visited_corners[i] = True
                
                next_state = (next_position, tuple(next_visited_corners))
                cost = 1 
                
                successors.append((next_state, action, cost))

        self._expanded += 1 
        return successors
