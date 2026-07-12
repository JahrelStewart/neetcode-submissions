class Solution:
    def encode(self, strs: List[str]) -> str:
        if len(strs) == 1:
            if strs[0] == "":
                return "//////"
        elif len(strs) == 0:
            return ""

        _str = ""
        for i, str in enumerate(strs):
            _str += str + "//////" if i < len(strs) - 1 else str
        
        return _str

    def decode(self, s: str) -> List[str]:
        if s == "//////":
            return [""]
        elif s == "":
            return []

        return s.split("//////")

