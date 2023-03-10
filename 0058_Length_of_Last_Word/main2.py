class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s == '':
            return 0
        
        r = len(s.rstrip().split(' ')[-1])
        return r

p = Solution()
print(f'{p.lengthOfLastWord(s = "Hello World")} expected: 5')
print(f'{p.lengthOfLastWord(s = "   fly me   to   the moon  ")} expected: 4')
print(f'{p.lengthOfLastWord(s = "day")} expected: 3')