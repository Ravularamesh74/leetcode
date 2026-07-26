class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """

        if numerator == 0:
            return "0"

        res = []

        # Handle sign
        if (numerator < 0) ^ (denominator < 0):
            res.append("-")

        numerator = abs(numerator)
        denominator = abs(denominator)

        # Integer part
        res.append(str(numerator // denominator))
        remainder = numerator % denominator

        if remainder == 0:
            return "".join(res)

        res.append(".")

        # Store remainder -> index
        seen = {}

        while remainder:
            if remainder in seen:
                idx = seen[remainder]
                res.insert(idx, "(")
                res.append(")")
                break

            seen[remainder] = len(res)

            remainder *= 10
            res.append(str(remainder // denominator))
            remainder %= denominator

        return "".join(res)