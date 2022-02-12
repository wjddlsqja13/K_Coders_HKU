""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def check_binary_search_tree_(root):
    if root == None:
        return True
    return search(root.left, -1, root.data) and search(root.right, root.data, 10001)

def search(root, minV, maxV):
    if root == None: return True
    if minV < root.data < maxV:
        return search(root.left, minV, root.data) and search(root.right, root.data, maxV)
    else: return False