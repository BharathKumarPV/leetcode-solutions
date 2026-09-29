class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:

        row = len(grid)
        col = len(grid[0])

        # Total path length must be even
        if (row + col - 1) % 2 != 0:
            return False

        dp = [[set() for _ in range(col)] for _ in range(row)]

        # Starting cell
        if grid[0][0] == '(':
            dp[0][0].add(1)
        else:
            return False

        for i in range(row):
            for j in range(col):

                # Skip starting cell
                if i == 0 and j == 0:
                    continue

                if grid[i][j] == '(':
                    change = 1
                else:
                    change = -1

                # From above
                if i > 0:
                    for balance in dp[i-1][j]:
                        new_balance = balance + change

                        if new_balance >= 0:
                            dp[i][j].add(new_balance)

                # From left
                if j > 0:
                    for balance in dp[i][j-1]:
                        new_balance = balance + change
                        if new_balance >= 0:
                            dp[i][j].add(new_balance)

        return 0 in dp[row-1][col-1]