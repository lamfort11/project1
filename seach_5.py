def getStartState(self):
        """
        Returns the start state (in your state space, not the full Pacman state
        space)
        """
        # Trạng thái bắt đầu: Vị trí của Pac-Man và 4 góc đều chưa được thăm (False hết)
        return (self.startingPosition, (False, False, False, False))

    def isGoalState(self, state: Any):
        """
        Returns whether this search state is a goal state of the problem.
        """
        position, visited_corners = state
        # Đích đạt được khi BẮT BUỘC TẤT CẢ 4 góc đều đã được thăm (True hết)
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

            # Nếu không phải tường thì là nước đi hợp lệ
            if not hitsWall:
                next_pos = (nextx, nexty)
                visited_list = list(visited_corners)
                
                # Kiểm tra xem vị trí mới có trùng với góc nào không để cập nhật trạng thái
                for i, corner in enumerate(self.corners):
                    if next_pos == corner:
                        visited_list[i] = True
                        
                next_state = (next_pos, tuple(visited_list))
                successors.append((next_state, action, 1))

        self._expanded += 1 # DO NOT CHANGE
        return successors
