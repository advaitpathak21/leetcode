class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        flag = 0
        
        for i in range(len(intervals) - 1):
            curr = []
            curr1 = []
            if flag == 0:
                first = intervals[i]
                second  = intervals[i+1]
                
                if second[0] == second[-1] and second[0] <= first[0]:
                    curr.append(second[0])
                    curr.append(second[-1])
                    curr1.append(min(first[0], first[-1]))
                    curr1.append(max(first[0], first[-1]))
                    flag = 2
                elif second[0] <= first[-1]:
                    curr.append(min(first[0], second[0]))
                    curr.append(max(first[-1], second[-1]))
                    flag = 1
                else:
                    curr.append(first[0])
                    curr.append(first[-1])
                    
                res.append(curr)
                if flag == 2: res.append(curr1)
            else:
                flag = 0
                
        if flag == 0:
            curr = []
            curr.append(intervals[-1][0])
            curr.append(intervals[-1][1])
            res.append(curr)
        
        return res