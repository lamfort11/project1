class CornersProblem(search.SearchProblem):
  

    def __init__(self, startingGameState):
        """
        Khởi tạo bài toán với trạng thái game ban đầu.
        """
        self.walls = startingGameState.getWalls()
        self.startingPosition = startingGameState.getPacmanPosition()
        top, right = self.walls.height-2, self.walls.width-2
        self.corners = ((1,1), (1,top), (right, 1), (right, top))
        for u, v in self.corners:
            if not startingGameState.hasFood(u, v):
                print('Warning: no food in corner {}, {}'.format(u, v))
        self.startingGameState = startingGameState


    def getStartState(self):
        """
        Trả về trạng thái bắt đầu. Trạng thái bao gồm:
        - Vị trí hiện tại (x, y)
        - Tuple 4 giá trị boolean đại diện cho 4 góc (đã thăm hay chưa)
        """
        # Kiểm tra xem ngay tại lúc bắt đầu Pac-Man có đang đứng ở một góc nào không
        visited_corners = tuple(self.startingPosition == corner for corner in self.corners)
        
        # Trạng thái là tuple: ( (x, y), (bool, bool, bool, bool) )
        return (self.startingPosition, visited_corners)

    def isGoalState(self, state):
        """
        Kiểm tra xem trạng thái truyền vào có phải là đích không.
        Đích là khi tất cả các góc đều đã được thăm (tất cả giá trị trong tuple đều là True).
        """
        visited_corners = state[1]
        
        return all(visited_corners)

    def getSuccessors(self, state):
        """
        Trả về các trạng thái kế tiếp, hành động tương ứng và chi phí.
        """
        successors = []
        x, y = state[0]
        visited_corners = state[1]


        for action in [Directions.NORTH, Directions.SOUTH, Directions.EAST, Directions.WEST]:
            
            dx, dy = Actions.directionToVector(action)
            nextx, nexty = int(x + dx), int(y + dy)
            
            hitsWall = self.walls[nextx][nexty]
            
            if not hitsWall:
                next_pos = (nextx, nexty)
                
         
                next_visited = list(visited_corners)
                for i in range(4):
                    if next_pos == self.corners[i]:
                        next_visited[i] = True
                        
                next_state = (next_pos, tuple(next_visited))
                
                
                successors.append((next_state, action, 1))

        return successors

    def getCostOfActions(self, actions):
        """
        Trả về chi phí của một chuỗi hành động (đã được viết sẵn, thường không cần sửa).
        """
        if actions == None: return 999999
        x,y= self.startingPosition
        for action in actions:
            dx, dy = Actions.directionToVector(action)
            x, y = int(x + dx), int(y + dy)
            if self.walls[x][y]: return 999999
        return len(actions)
