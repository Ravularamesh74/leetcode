class Solution(object):

  def maxPalindromes(self, s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    ans = 0
    last_end = -1
    n = len(s)

    for i in range(n):
      # Check palindromes of length k or k+1 ending at index i
      for length in (k, k + 1):
        start = i - length + 1
        if start > last_end and self.isPalindrome(s, start, i):
          ans += 1
          last_end = i
          break

    return ans

  def isPalindrome(self, s, left, right):
    while left < right:
      if s[left] != s[right]:
        return False
      left += 1
      right -= 1
    return True