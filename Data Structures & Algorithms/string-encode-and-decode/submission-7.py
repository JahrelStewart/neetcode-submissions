class Solution:
    def encode(self, strs: List[str]) -> str:
        out = ""
        for _str in strs:
            out += str(len(_str)) + "#" + _str
        
        return out

    def decode(self, s: str) -> List[str]:
        out = []
        i = 0        
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            width = int(s[i:j])
            start = j+1
            end = start + width
            out.append(s[start:end])
            i = end
        
        return out


        

