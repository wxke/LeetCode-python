有序矩阵中第K小的元素
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        def Build_heap(data,low,high):
            i = low
            tmp = data[i]
            j = 2*i +1
            while j <= high:
                if j < high and data[j] > data[j+1]:
                    j = j + 1
                if tmp > data[j]:
                    data[i] = data[j]
                    i = j
                    j = 2 * i + 1
                else:
                    break
            data[i] = tmp
        
        
        
        def heap(data,k):
            n = len(data)
            for i in range((n//2)-1 , -1, -1):
                Build_heap(data,i,n-1)
            for i in range(k):
                data[0] ,data[n-1-i] = data[n-1-i],data[0]
                Build_heap(data,0,n-i-2)
            
        
        data = []
        for i in matrix:
            data.extend(i)
        
        heap(data,k)
        return data[-k]
