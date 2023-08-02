def height(root):
    if root is None:
        return 0
    return max(height(root.left), height(root.right))+1
 
 
def getcol(h):
    if h == 1:
        return 1
    return getcol(h-1) + getcol(h-1) + 1
 
 
def printTree(M, root, col, row, height):
    if root is None:
        return
    M[row][col] = root.value
    printTree(M, root.left, col-pow(2, height-2), row+1, height-1)
    printTree(M, root.right, col+pow(2, height-2), row+1, height-1)
 
 
def tree_printer(myTree):
    h = height(myTree.root)
    col = getcol(h)
    M = [[0 for _ in range(col)] for __ in range(h)]
    printTree(M, myTree.root, col//2, 0, h)
    for i in M:
        for j in i:
            if j == 0:
                print(" ", end=" ")
            else:
                print(j, end=" ")
        print("")
