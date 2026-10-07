class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        # Combine position and speed into pairs and sort by position in descending order
        cars = sorted(zip(position, speed), reverse=True)
        
        stack = []
        for pos, spd in cars:
            # Calculate the time needed to reach the target destination
            time = float(target - pos) / spd
            
            # If stack is empty or this car takes more time than the fleet ahead of it,
            # it forms a new, slower fleet.
            if not stack or time > stack[-1]:
                stack.append(time)
                
        # The number of fleets is the number of distinct arrival times remaining in the stack
        return len(stack)
