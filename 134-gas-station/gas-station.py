class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0      # candidate starting station
        tank = 0       # current tank level for this attempt
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                # this attempt failed at station i —
                # throw it away completely, try fresh from the next station
                start = i + 1
                tank = 0
        return start if sum(gas) >= sum(cost) else -1