class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded += string + "\0"
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = s.split("\0")
        return decoded[:len(decoded) - 1]