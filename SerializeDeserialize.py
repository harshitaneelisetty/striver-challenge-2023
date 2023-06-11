#https://www.codingninjas.com/codestudio/problems/serialize-and-deserialize-binary-tree_8230748?challengeSlug=striver-sde-challenge

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __del__(self):
        if self.left:
            del self.left
        if self.right:
            del self.right


def serializeTree(root):
    serialized = ""
    level = [root]
    while len(level) != 0:
        curr = level[0]
        level.pop(0)
        if curr != None:
            serialized += str(curr.data)
            serialized += ','
            level.append(curr.left)
            level.append(curr.right)
        else:
            serialized += "-1,"
    return serialized
  
def deserializeTree(serialized):
    ptr = 0
    firstVal = ""
    while ptr < len(serialized) and serialized[ptr] != ',':
        firstVal += serialized[ptr]
        ptr += 1
    ptr += 1
    val = int(firstVal)
    if val == -1:
        return None
    root = TreeNode(val)
    level = [root]
    while len(level) != 0:
        curr = level[0]
        level.pop(0)
        leftChild = ""
        while ptr < len(serialized) and serialized[ptr] != ',':
            leftChild += serialized[ptr]
            ptr += 1
        ptr += 1
        rightChild = ""
        while ptr < len(serialized) and serialized[ptr] != ',':
            rightChild += serialized[ptr]
            ptr += 1
        ptr += 1
        leftChildValue = int(leftChild)
        rightChildValue = int(rightChild)
        if leftChildValue != -1:
            leftNode = TreeNode(leftChildValue)
            curr.left = leftNode
            level.append(curr.left)
        if rightChildValue != -1:
            rightNode = TreeNode(rightChildValue)
            curr.right = rightNode
            level.append(curr.right)
    return root
