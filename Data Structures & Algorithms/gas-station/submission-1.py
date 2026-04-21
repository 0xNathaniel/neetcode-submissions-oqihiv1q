class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        n = len(gas)

        def isPossible(idx):
            travel = 0
            current_gas = gas[idx]

            while travel < n:
                if current_gas < cost[(idx + travel) % n]:
                    return False

                current_gas -= cost[(idx + travel) % n]
                travel += 1
                current_gas += gas[(idx + travel) % n]

            return True

        for i in range(n):
            if isPossible(i):
                return i

        return -1