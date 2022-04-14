#  INORDER TRAVERSER
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

#  PREORDER TRAVERSER
def preorder(root):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)

#  POSTORDER TRAVERSER
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)

#  LEVELORDER TRAVERSER
def levelorder(root):
    q = [root]
    while len(q) > 0:
        node = q.pop(0)
        print(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

#  TO FIND LEAFNODES
def leafnodes(root):
    if root:
        if not root.left and not root.right:
            print(root.val)
        leafnodes(root.left)
        leafnodes(root.right)