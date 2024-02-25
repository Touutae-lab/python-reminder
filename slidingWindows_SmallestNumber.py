

class Solution:
    def smallestNumberAtK(self, s: list[int], k: int) -> int:
        if not s or k <= 0 or k > len(s):
            return 0

        currentSum = sum(s[:k])
        minSum = currentSum

        for i in range(k, len(s)):
            currentSum += s[i] - s[i - k] 
            minSum = min(minSum, currentSum)
        return minSum


def main():
    solution = Solution()
    print(solution.smallestNumberAtK([2, 1, 3, 4, 1, 2, 1, 5, 4], 5)) # 11
    print(solution.smallestNumberAtK([2, 1, 3, 4, 1, 2, 1, 5, 4], 4)) # 8
    print(solution.smallestNumberAtK([2, 1, 3, 4, 1, 2, 1, 5, 4], 3)) # 4
    print(solution.smallestNumberAtK([2, 1, 3, 4, 1, 2, 1, 5, 4], 2)) # 3
    print(solution.smallestNumberAtK([2, 1, 3, 4, 1, 2, 1, 5, 4], 1)) # 1
    print(solution.smallestNumberAtK([2, 1, 3, 4, 1, 2, 1, 5, 4], 0)) # 0



if __name__ == "__main__":
    main()
        
        