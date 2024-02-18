
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charIndexMap = {}
        
        maxLength = 0
        left = 0
        
        for right in range(len(s)):
            if s[right] in charIndexMap:
                left = max(left, charIndexMap[s[right]] + 1)
            charIndexMap[s[right]] = right
            maxLength = max(maxLength, right - left + 1)

        return maxLength
        
def main(): 
    solution = Solution()
    # print(solution.lengthOfLongestSubstring("abcabcbb")) # 3
    # print(solution.lengthOfLongestSubstring("bbbbb")) # 1
    # print(solution.lengthOfLongestSubstring("pwwkew")) # 3
    # print(solution.lengthOfLongestSubstring("")) # 0
    # print(solution.lengthOfLongestSubstring(" ")) # 1
    # print(solution.lengthOfLongestSubstring("au")) # 2
    # print(solution.lengthOfLongestSubstring("dvdf")) # 3
    # print(solution.lengthOfLongestSubstring("anviaj")) # 5
    print(solution.lengthOfLongestSubstring("aab")) # 2
    # print(solution.lengthOfLongestSubstring("abba")) # 2
    # print(solution.lengthOfLongestSubstring("tmmzuxt")) # 5

if __name__ == "__main__":
    main()
    
