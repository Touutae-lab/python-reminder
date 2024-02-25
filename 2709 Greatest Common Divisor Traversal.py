from typing import List
from collections import defaultdict

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.root[rootY] = rootX

    def connected(self):
        root_set = set([self.find(x) for x in range(len(self.root))])
        return len(root_set) == 1
    
class Solution:
    def SieveOfEratosthenes(self, n = 100000):
        prime = [True for i in range(n+1)]
        p = 2
        result = defaultdict(list)
        while (p <= n):
            if (prime[p] == True):
                for i in range(p, n+1, p):
                    prime[i] = False
                    result[i].append(p)
            p += 1
        return result

    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        max_num = max(nums)
        sieve = self.SieveOfEratosthenes(max_num)
        uf = UnionFind(len(nums))

        primeIdx = {}
        for i, num in enumerate(nums):
            for prime in sieve[num]:
                if prime in primeIdx:
                    uf.union(i, primeIdx[prime])
                primeIdx[prime] = i

        return uf.connected()

solution = Solution()
# Example usage
nums = [2, 3, 6]
print(solution.canTraverseAllPairs(nums))  # Output: True

nums = [3, 9, 5]
print(solution.canTraverseAllPairs(nums))  # Output: False

nums = [4, 3, 12, 8]
print(solution.canTraverseAllPairs(nums))  # Output: True