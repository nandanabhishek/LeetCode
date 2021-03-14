class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        
        squares = []
        
        for rectangle in rectangles:
                squares.append(min(rectangle[0], rectangle[1]))
        
        squares.sort()
        
        count = 1
        length = len(squares) - 1

        
        while length > 0:
            if squares[length] != squares[length-1]:
                break
            count += 1
            length -= 1

        return count
