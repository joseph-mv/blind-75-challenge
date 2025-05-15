class Solution:
    def encode(self, strs: list[str]) -> str:
        """
        Encodes a list of strings to a single string.

        Args:
            strs: A list of strings to encode.

        Returns:
            The encoded single string.
        """
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> list[str]:
        """Decodes a single string to a list of strings.

        Args:
            s: The encoded single string.

        Returns:
            The decoded list of strings.
        """
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length

        return res
