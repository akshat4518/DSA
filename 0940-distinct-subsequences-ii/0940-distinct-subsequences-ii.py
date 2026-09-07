class Solution:
    MOD = 10**9 + 7

    def distinctSubseqII(self, s: str) -> int:

        # Total distinct non-empty subsequences
        tot = 0

        # dp[i] = previous contribution associated with character i
        dp = [0] * 26

        for ch in s:

            # Convert character to index 0-25
            c = ord(ch) - ord('a')

            # New subsequences created by this character
            # +1 represents the character itself
            # -dp[c] removes duplicates caused by previous same character
            new = tot + 1 - dp[c]

            # Update total
            tot = (tot + new) % self.MOD

            # Update contribution of this character
            dp[c] = (dp[c] + new) % self.MOD

        return tot