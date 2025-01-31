#leetcode
#151. Reverse Words in a String
#https://leetcode.com/problems/reverse-words-in-a-string/description/


#need to optimise the code. This is my brute force solution

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        i=0
        a= ""
        b= ""
        while i < len(s):
            if i==len(s)-1 and s[i]!=" ":
                a=a+s[i]
                if b!="":
                    b=a+" "+b
                else:
                    b=a+b
                a=""
            elif s[i] != " ":
                a=a+s[i]
            elif s[i] == " ":
                if a!="":
                    if b!="":
                        b=a+" "+b
                    else:
                        b=a+b
                    a=""
            i+=1
        return b