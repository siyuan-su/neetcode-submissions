class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = [0]*26
        map = {}
        for i in strs:
            for j in i:
                count[ord(j) - 97] += 1
            count = tuple(count)
            if count in map.keys():
                map[count] += [i]
            else:
                map[count] = [i]
            count = [0]*26
        return list(map.values())

       