class Solution:
    # find the edges of the current row and return the sublist
    # the sublist won't have the empty sides
    def cutEdges(self, walls: list[int]) -> list[int]:
        # assign the initial left edge and the initial right edge
        length = len(walls)
        startIndex = 0
        endIndex = length - 1

        # loop though the list until we find the left edge
        while startIndex < length:
            if walls[startIndex] == 0:
                startIndex = startIndex + 1
            else: # we found the left edge
                break

        # loop through the list backwards until we find the right edge
        while endIndex > 0:
            if walls[endIndex] == 0:
                endIndex = endIndex - 1
            else: # we found the right edge
                break

        # return the new sublist
        return walls[startIndex:endIndex+1]


    # count how many units of water are on the current row and decrement each index
    def countWater(self, walls: list[int]) -> int:
        length = len(walls)
        if length < 3:
            return 0

        units = 0
        i = 0
        while i < length:
            if walls[i] == 0:
                units = units + 1
            else:
                walls[i] = walls[i] - 1
            i = i + 1
        return units


    # count units of water one "row" at a time
    # decrementing each each column by 1 as we go
    def trap(self, walls: list[int]) -> int:
        unitsOfWater = 0

        # get the max value so we know how many rows we need to compute
        height = max(walls)

        # loop through each row calculating water held by that row
        i = 0
        while i < height:
            # cut off the edges that don't hold anything
            walls = self.cutEdges(walls)
            
            # count the water held and decrement the walls
            unitsOfWater = unitsOfWater + self.countWater(walls)

            # increment row
            i = i + 1

        return unitsOfWater


if __name__ == "__main__":
    test = [5,7,2,3,4,8,3,5,1]
    s = Solution()
    print(str(s.trap(test)))



   