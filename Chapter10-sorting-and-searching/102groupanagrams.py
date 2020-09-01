
#leetcode 49
import collections
def groupanagrams(input):
    ans = collections.defaultdict(list)
    for string in input:
        count = [0]*26
        for s in string:
            count[ord(s)-ord("a")]+=1
        ans[tuple(count)].append(string)
    return ans.values()
   


strs = ["eat","tea","tan","ate","nat","bat"]
print(groupanagrams(strs))
#[["bat"],["nat","tan"],["ate","eat","tea"]]
strs2 = [""]
print(groupanagrams(strs2))
#[[""]]
strs3 = ["a"]
print(groupanagrams(strs3))
#[["a"]]
        
