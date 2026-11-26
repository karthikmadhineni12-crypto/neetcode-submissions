class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmap={}
        for x in t:
            if x in hashmap:
                hashmap[x]=hashmap[x]+1
            else:
                hashmap[x]=1
        for x in s:
            if x in hashmap:
                hashmap[x]=hashmap[x]-1 
            else:
                return False 

        for x in hashmap:
            if hashmap[x]!=0:
                return False
        return True