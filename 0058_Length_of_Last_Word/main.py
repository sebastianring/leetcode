class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        letter_hit = False
        end = -1
        start = -1

        for i in range(len(s)-1, -1, -1):
            if letter_hit == False:
                if s[i] != ' ':
                    end = i
                    letter_hit = True
            else:
                if s[i] == ' ':
                    start = i
                    break
        
        return (end-start)




p = Solution()
print(f'{p.lengthOfLastWord(s = "Hello World")} expected: 5')
print(f'{p.lengthOfLastWord(s = "   fly me   to   the moon  ")} expected: 4')
print(f'{p.lengthOfLastWord(s = "day")} expected: 3')