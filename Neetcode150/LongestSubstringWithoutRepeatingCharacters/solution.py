class Solution:
    def length_of_longest_substring(self, s: str) -> int:
        last_seen = {}
        max_len = 0
        left = 0

        for right, char in enumerate(s):
            # Get the repeated character out of the window
            if char in last_seen and left <= last_seen[char]:
                left = last_seen[char] + 1

            last_seen[char] = right

            current_window_length = right - left + 1
            max_len = max(max_len, current_window_length)
        return max_len
