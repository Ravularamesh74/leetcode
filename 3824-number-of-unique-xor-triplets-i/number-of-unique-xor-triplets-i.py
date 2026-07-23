class Solution(object):

  def uniqueXorTriplets(self, nums):
    """:type nums: List[int]

    :rtype: int
    """
    n = len(nums)

    if n <= 2:
      return n

    # For n >= 3, all numbers in [0, 2^(bit_length) - 1] can be formed
    return 1 << n.bit_length()