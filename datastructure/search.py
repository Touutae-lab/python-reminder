class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid
        return - 1
    


def main():
    value = Solution()
    print(value.search([1, 2, 3, 4, 5, 6, 7, 8, 9], 5)) # 4
    print(value.search([1, 2, 3, 4, 5, 6, 7, 8, 9], 9)) # 8
    print(value.search([1, 2, 3, 4, 5, 6, 7, 8, 9], 1)) # 0
    print(value.search([1, 2, 3, 4, 5, 6, 7, 8, 9], 10)) # -1
    print(value.search([-1,0,3,5,9,12], 2)) # -1
    


if __name__ == "__main__":
    main()