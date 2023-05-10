class Solution:
    def spiralOrder(self, matrix):
        """
        :param matrix:
        :return:
        >>> Solution().spiralOrder(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        [1, 2, 3, 6, 9, 8, 7, 4, 5]
        """
        result = []

        while matrix:
            result += matrix.pop(0)
            if matrix:
                for index in range(~-len(matrix)):
                    if len(matrix[index]):
                        result.append(matrix[index].pop())
            if matrix:
                result += matrix.pop()[::-1]
            if matrix:
                for index in range(1, -~len(matrix)):
                    if len(matrix[-index]):
                        result.append(matrix[-index].pop(0))

        return result

if __name__ == '__main__':
    pass
