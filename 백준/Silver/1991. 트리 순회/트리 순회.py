class Node():
    def __init__(self, data, left, right) -> None:
        self.data = data
        self.left = left
        self.right = right
        
def postorder(node):
    if node.left != None: postorder(tree[node.left])
    if node.right != None: postorder(tree[node.right])
    print(node.data, end='')

def inorder(node):
    if node.left != None: inorder(tree[node.left])
    print(node.data, end='')
    if node.right != None: inorder(tree[node.right])

def preorder(node):
    print(node.data, end='')
    if node.left != None: preorder(tree[node.left])
    if node.right != None: preorder(tree[node.right])

n = int(input())
tree = {}

for i in range(n):
    d, l, r = input().split()
    if l == '.': l = None
    if r == '.': r = None
    tree[d] = Node(d, l, r)
    
preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])