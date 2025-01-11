# leetcode
# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
# i coded this brute force solution, which did not executed, got time limit exceeded.

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        asum=0
        for i in range(len(prices)):
            prices[i]
            j=i+1
            while j < len(prices):
                if prices[j]>prices[i]:
                    asum = max(prices[j]-prices[i],asum)
                j+=1
        return asum

#after watching striver video, i coded this solution.

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minimum = 0
        max_price = 0
        for i in range(len(prices)):
            if i == 0:
                minimum = prices[i]
                continue
            profit = prices[i]-minimum
            max_price=max(profit,max_price)
            minimum=min(minimum,prices[i])
        return max_price
    
# time complexity is O(N) and space is O(1)
# i saw a code in submission which improved the runtime of the code from 150 ms to 42 ms
# below is the code.
class Solution:
    def maxProfit(self, prices):
        buy = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i] - buy > profit:
                profit = prices[i] - buy
        return profit

#why? chatgpt answer
# The two pieces of code solve the same problem, but there are differences in their implementation that lead to differences in runtime efficiency. Let's analyze the **differences**:

# ---
# ### Differences Between the Two Codes**

# 1. **Initialization of `minimum`/`buy`**:
#    - **Code 1**: Initializes `minimum` (buy price) inside the loop when \( i = 0 \). This adds an additional condition (`if i == 0`) and a `continue` statement, slightly increasing overhead.
#    - **Code 2**: Initializes `buy` to `prices[0]` before entering the loop, avoiding the need for special handling of the first iteration.

#    Impact**: Avoiding an unnecessary condition in Code 2 makes it marginally faster.

# ---

# 2. **Handling Profit Calculation**:
#    - **Code 1**: Always calculates `profit` for every iteration of the loop:  
#      ```python
#      profit = prices[i] - minimum
#      max_price = max(profit, max_price)
#      ```
#      This includes a subtraction operation and a `max` function call on every iteration, even when it's not necessary.
#    - **Code 2**: Only calculates `profit` when `prices[i] - buy > profit`.  
#      ```python
#      if prices[i] - buy > profit:
#          profit = prices[i] - buy
#      ```
#      By skipping unnecessary calculations, Code 2 reduces computational overhead.

#    Impact**: Code 2 performs fewer operations per iteration, making it faster.

# ---

# 3. **Conditions in the Loop**:
#    - **Code 1**: Checks and updates `minimum` and `max_price` separately on every iteration, requiring two comparisons and two updates.
#    - **Code 2**: Combines the conditions:
#      ```python
#      if prices[i] < buy:
#          buy = prices[i]
#      elif prices[i] - buy > profit:
#          profit = prices[i] - buy
#      ```
#      This structure avoids redundant comparisons in cases where the current price is lower than the current buy price.

#    Impact**: Code 2 minimizes the number of operations by combining conditions effectively.

# ---

# 4. **Early Return Optimization**:
#    - Neither code has early return optimization (e.g., breaking out of the loop when a maximum possible profit is reached), but Code 2's efficient condition handling inherently processes fewer operations.

# ---

# ### Time Complexity**
# Both codes have the same **time complexity** of \( O(n) \), as they iterate over the `prices` list once.

# ### Space Complexity**
# Both codes have the same **space complexity** of \( O(1) \), as they use a constant amount of extra memory.

# ---

# ### Why Code 2 is Faster in Practice**
# - Fewer condition checks and unnecessary operations.
# - Profit calculation is only performed when it's meaningful.
# - Avoids the special-case handling for the first iteration.

# ---

# ### Summary of Improvements in Code 2**
# - Eliminates redundant condition checks.
# - Optimizes calculations to only when required.
# - Streamlines the logic with a cleaner structure.

# These optimizations lead to better runtime efficiency in practice, as seen in the reduced runtime (42 ms vs. 150 ms).