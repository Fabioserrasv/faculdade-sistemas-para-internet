class ShowTree:
    def __height(self, node):
        if node is None:
            return 0

        left_height = self.__height(node.left)
        right_height = self.__height(node.right)

        return max(left_height, right_height) + 1


    def display_tree(self, root, compact=False):
        # Calculate the height of the tree
        h = self.__height(root)

        # Queue to store nodes at each level

        matrix = [[' '] * (2 ** h) * 2 for _ in range(h * 2)]
        col_idx = 2 ** h
        levels = [[(root, col_idx)]]
        for l in range(h):
            curr_lvl = levels[l]
            next_lvl = []
            for node, col_idx in curr_lvl:
                matrix[l * 2][col_idx] = str(node.value)
                conn_row = matrix[l * 2 + 1]
                if node.left:
                    lft_idx = col_idx - 2 ** (h - l - 1)
                    next_lvl.append((node.left, lft_idx))
                    # connector row for children
                    conn_row[col_idx] = "┘"
                    conn_row[lft_idx] = "┌"
                    for j in range(lft_idx + 1, col_idx):
                        conn_row[j] = "─"
                if node.right:
                    rt_idx = col_idx + 2 ** (h - l - 1)
                    next_lvl.append((node.right, rt_idx))
                    conn_row[col_idx] = "└"
                    conn_row[rt_idx] = "┐"
                    for j in range(col_idx + 1, rt_idx):
                        conn_row[j] = "─"
                if node.left and node.right:
                    conn_row[col_idx] = "┴"
            levels.append(next_lvl)

        self.__left_align(matrix, compact)
        for row in matrix:
            print(''.join(row))


    def __left_align(self, matrix, compact=False):
        # Find the index of the first non-empty column
        empty_columns = []
        for col_idx in range(len(matrix[0])):
            for row_idx in range(len(matrix)):
                symbol = matrix[row_idx][col_idx]
                if symbol == ' ' or (symbol == '─' if compact else False):
                    continue
                else:
                    break
            else:
                empty_columns.append(col_idx)

        # Replace space characters with empty strings in empty columns
        for row_idx in range(len(matrix)):
            for col_idx in empty_columns:
                matrix[row_idx][col_idx] = ''

        return matrix