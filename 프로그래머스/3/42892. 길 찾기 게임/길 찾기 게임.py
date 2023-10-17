import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, idx, x):
        self.idx = idx
        self.x = x
        self.left = None
        self.right = None
    
class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, idx, x):
        new_node = Node(idx, x)
        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            while True:
                if x < current.x:
                    if current.left is None:
                        current.left = new_node
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = new_node
                        break
                    else:
                        current = current.right
    
    def preorder(self, node, pre):
        if node is not None:
            pre.append(node.idx)
            self.preorder(node.left, pre)
            self.preorder(node.right, pre)
    
    def postorder(self, node, post):
        if node is not None:
            self.postorder(node.left, post)
            self.postorder(node.right, post)
            post.append(node.idx)

def solution(nodeinfo):
    nls = [[i+1, nodeinfo[i][0], nodeinfo[i][1]] for i in range(len(nodeinfo))]
    nls.sort(key=lambda x: (-x[2], x[1]))
    
    bt = BinaryTree()
    for i in range(len(nls)):
        bt.insert(nls[i][0], nls[i][1])
        
    pre, post = [], []
    bt.preorder(bt.root, pre)
    bt.postorder(bt.root, post)
    
    return [pre, post]
