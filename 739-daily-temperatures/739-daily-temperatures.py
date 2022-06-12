from queue import PriorityQueue


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for _ in range(len(temperatures))]
        unvisited = [0]
        for i in range(1,len(temperatures)):
            t = temperatures[i]
            while len(unvisited) > 0 and t > temperatures[unvisited[-1]]:
                nxt_idx = unvisited.pop()
                res[nxt_idx] = i-nxt_idx
            unvisited.append(i)
        return res
                