class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {0: 0}
        
        for total in range(1, amount + 1):
            for coin in coins:
                if coin > total:
                    continue
                if (total - coin) in memo:
                    current_count = memo[total - coin] + 1

                    if total in memo:
                        memo[total] = min(memo[total], current_count)
                        continue

                    memo[total] = current_count

        return memo[amount] if amount in memo else -1