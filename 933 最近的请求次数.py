最近的请求次数

class RecentCounter:


    def __init__(self):
        self.num =[]
        self.a = 0
    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.num.append(t)
        
        len1 = len(self.num)
        #print(self.a)
        #prev_pos = bisect.bisect_left(self.num, t - 3000)
        for i in range(self.a,len1):
            if self.num[i]<t-3000:
                self.a += 1
            else:
                break

        return len1 -self.a
        
        
        

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
