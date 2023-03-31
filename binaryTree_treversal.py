
# Case 1

lis = [1,None,2,3]

# Case2
lis2 = []

# case3
lis3 = [1]


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        Lists = []

        def rec_func(root):
            if not root:
                return
            else:
                Lists.append(root.val)
                rec_func(root.left)
                rec_func(root.right)
        rec_func(root)

        return Lists
    
cls = Solution()
    
print(cls.preorderTraversal(lis))