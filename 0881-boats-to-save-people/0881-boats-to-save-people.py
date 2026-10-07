class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()

        left = 0
        right = len(people) - 1
        boats = 0

        while left <= right:

            # Try to put the lightest and heaviest together
            if people[left] + people[right] <= limit:
                left += 1

            # Heaviest person always needs a boat
            right -= 1
            boats += 1

        return boats