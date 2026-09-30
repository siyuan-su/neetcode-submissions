class Solution:
    def isValid(self, s: str) -> bool:
        map = {"(":")", "{":"}", "[": "]"}
        result = []
        for c in s:
            if len(result) != 0 and (result[-1], c) in map.items():
                result.pop()
            else:
                result.append(c)
            print(result)
        if result == []:
            return True
        else:
            return False