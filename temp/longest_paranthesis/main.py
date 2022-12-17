class Solution:
    def longestValidParentheses(self, s: str) -> int:
        open = 0
        closed = 0
        record = 0
        cur = 0

        for i in range(len(s)):
            if s[i] == '(':
                open += 1
            else:
                #print(i)
                if open > 0:
                    open -= 1
                    closed += 1
                    cur += 1
                    
                    if open == 0:
                        record += closed
                        closed = 0
                else:
                    cur = 0
        
        return record * 2


        pass



p = Solution()
print(p.longestValidParentheses(s = "(()"))
print(p.longestValidParentheses(s = ")()())"))
print(p.longestValidParentheses(s = ")("))
print(p.longestValidParentheses(s = "()(()"))


