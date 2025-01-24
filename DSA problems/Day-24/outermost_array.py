#leetcode
# 1021. Remove Outermost Parentheses

# solved an easy to medium problem just to componsate for the previous day's problem
# solved it myself, but can be improved.

class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        counter=0
        arr = []
        newArr=[]
        for idx,i in enumerate(s):
            if i == "(":
                if counter!=0:
                    newArr.append(i)
                counter+=1
            elif i == ")":
                counter-=1
                if counter!=0:
                    newArr.append(i)
        s = ''.join(str(x) for x in newArr)
        return s