'''
Good Nodes in binary tree are that node, if in the path form root to that node, there are no nodes  with a value 
greater than that node itself
'''

def goodNodes(root):
    def count(node,v):
        if not node:
            return 0

        mx = max(node.val,v)

        return (node.val>=v)+count(node.left,mx)+count(node.right,mx)

    return count(root,root.val)
