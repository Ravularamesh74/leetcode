class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        
        # Convert 12 → 0
        hour = hour % 12
        
        # Calculate angles
        minute_angle = 6 * minutes
        hour_angle = 30 * hour + 0.5 * minutes
        
        # Find absolute difference
        angle = abs(hour_angle - minute_angle)
        
        # Return smaller angle
        return min(angle, 360 - angle)