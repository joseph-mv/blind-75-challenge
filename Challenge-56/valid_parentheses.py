class Solution:
    def isValid(self, s: str) -> bool:
        """
        Determines if the input string containing brackets is valid.

        Args:
            s: The input string containing only '(', ')', '{', '}', '[' and ']'.

        Returns:
            True if the input string is valid, False otherwise.
        """
        obj={
            ')':'(',
            ']':'[',
            '}':'{'
        }
        stack=[]
        for ch in s:
            if ch in '([{':
                stack.append(ch)
                continue
            if not stack or stack.pop() != obj[ch]:
                return False

        return True
        