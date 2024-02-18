class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s=s.replace(" ","")
        k = "1234567890abcdefghijklmnopqrstuvwxyz"
        ans=list(filter(lambda x: x in k,s))
        s="".join(ans)
        l,r = 0, len(s)-1
        while l<r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True
N=Solution()
s=input()
print(N.isPalindrome(s))