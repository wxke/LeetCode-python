钥匙和房间
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        list1 = [1 for i in range(len(rooms))]
        
        def dp(i):
            if list1[i] == 0:
                return
            list1[i] = 0
            # print(list1)
            for j in range(len(rooms[i])):
                dp(rooms[i][j])
                
                
        for i in range(len(rooms[0])):
            dp(rooms[0][i])
        
        
        if sum(list1) - list1[0] == 0:
            return True
        else:
            return False
            
