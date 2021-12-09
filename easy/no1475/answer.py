# O(n^2) solution

# class Solution:
#     def finalPrices(self, prices: List[int]) -> List[int]:
#         ans = []
#         for i in range(len(prices)):
#             discount_flag = False
#             for j in range(i+1, len(prices)):
#                 if prices[i] >= prices[j]:
#                     ans.append(prices[i] - prices[j])
#                     discount_flag = True
#                     break
#             if not discount_flag:
#                 ans.append(prices[i])
                
#         return ans


# O(n) solution

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        for i, price in enumerate(prices):
            while stack and prices[stack[-1]] >= price:
                prices[stack.pop()] -= price
            stack.append(i)
            
        return prices

