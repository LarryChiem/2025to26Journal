class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        if not s or length == 1:
            return s

        def expand_from_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1

        longest_left, longest_right = 0, 0
        for i in range(length):
            # Check odd length (one center)
            odd_left, odd_right = expand_from_center(i, i)

            # Check even length (two center)
            even_left, even_right = expand_from_center(i, i + 1)
        
            if odd_right - odd_left > longest_right - longest_left:
                longest_left, longest_right = odd_left, odd_right

            if even_right - even_left > longest_right - longest_left:
                longest_left, longest_right = even_left, even_right
            
        return s[longest_left:longest_right + 1]
