class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
            output=[]
            for i in range(len(candies)):
                if extraCandies+candies[i]>=max(candies):
                    output.append(True)
                else:
                    output.append(False)
            return output        