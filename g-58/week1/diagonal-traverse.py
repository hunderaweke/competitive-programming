class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        container= defaultdict(list)
        for col in range(len(mat)):
            for row in range(len(mat[0])):
                container[col+row].append(mat[col][row])
        print(container)
        ans = []
        for index in container:
            if index %2:
                [ans.append(x) for x in container[index]]
            else:
                [ans.append(x) for x in container[index][::-1]]
        return ans