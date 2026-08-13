class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        max_satisfied = 0
        j = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                max_satisfied += customers[i]
            j += 1
        count = 0
        window_sum = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                window_sum += customers[i]

        count = window_sum
        for i in range(minutes, len(customers)):
            if grumpy[i-minutes] == 1:
                window_sum -= customers[i-minutes]
            if grumpy[i] == 1:
                window_sum += customers[i]
            count = max(count, window_sum)

        return max_satisfied + count
            
            

        