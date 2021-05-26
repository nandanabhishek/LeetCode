class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        output = []
        for i in range(1, target[-1]+1):
            if i in target:
                output.append("Push")
            else:
                output.append("Push")
                output.append("Pop")
        return output
        
