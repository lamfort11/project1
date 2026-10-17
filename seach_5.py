def getStartState(self):
        """
        Returns the start state (in your state space, not the full Pacman state
        space)
        """
        
        return (self.startingPosition, (False, False, False, False))

    def isGoalState(self, state: Any):
        """
        Returns whether this search state is a goal state of the problem.
        """
        position, visited_corners = state
       
        return all(visited_corners)

    def getSuccessors(self, state: Any):
        """
        Returns successor states, the actions they require, and a cost of 1.
        """
        successors = []
        position, visited_corners = state
        x, y = position

        for action in [Directions.NORTH, Directions.SOUTH, Directions.EAST, Directions.WEST]:
            dx, dy = Actions.directionToVector(action)
            nextx, nexty = int(x + dx), int(y + dy)
            hitsWall = self.walls[nextx][nexty]

        
            if not hitsWall:
                next_pos = (nextx, nexty)
                visited_list = list(visited_corners)
                
                
                for i, corner in enumerate(self.corners):
                    if next_pos == corner:
                        visited_list[i] = True
                        
                next_state = (next_pos, tuple(visited_list))
                successors.append((next_state, action, 1))

        self._expanded += 1
        return successors
