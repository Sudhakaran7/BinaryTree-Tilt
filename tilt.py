from binarytree import build 
class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def postOrderTraverse(root, tilt):
            if not root:
                return 0, tilt
            left, tilt = postOrderTraverse(root.left, tilt)
            right, tilt = postOrderTraverse(root.right, tilt)
            tilt += abs(left-right)
            return left+right+root.val, tilt

        return postOrderTraverse(root, 0)[1]

n=int(input())
nodes =list(map(int,input().split())) 
binary_tree = build(nodes) 
val=Solution()
print(val.findTilt(binary_tree))
