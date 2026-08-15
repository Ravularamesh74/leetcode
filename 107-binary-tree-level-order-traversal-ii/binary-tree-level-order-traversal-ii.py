from collections import deque


class Solution(object):

  def levelOrderBottom(self, root):
    """:type root: Optional[TreeNode]

    :rtype: List[List[int]]
    """
    if not root:
      return []

    result = []
    queue = deque([root])

    while queue:
      level_size = len(queue)
      current_level = []

      for _ in range(level_size):
        node = queue.popleft()
        current_level.append(node.val)

        if node.left:
          queue.append(node.left)
        if node.right:
          queue.append(node.right)

      result.append(current_level)

    # Reverse to get bottom-up level order
    return result[::-1]