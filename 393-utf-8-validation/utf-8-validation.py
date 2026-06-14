class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        

        remaining = 0

        for byte in data:
            if remaining == 0:
                if (byte >> 7) == 0:
                    # 1-byte character
                    continue
                elif (byte >> 5) == 0b110:
                    remaining = 1
                elif (byte >> 4) == 0b1110:
                    remaining = 2
                elif (byte >> 3) == 0b11110:
                    remaining = 3
                else:
                    return False
            else:
                # Continuation byte must start with 10
                if (byte >> 6) != 0b10:
                    return False
                remaining -= 1

        return remaining == 0