class MyQueue(object):

    def __init__(self):
        self.s1 = []  # Stack for incoming elements
        self.s2 = []  # Stack for outgoing elements

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.s1.append(x)

    def pop(self):
        """
        :rtype: int
        """
        self.peek()
        return self.s2.pop()

    def peek(self):
        """
        :rtype: int
        """
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.s1 and not self.s2