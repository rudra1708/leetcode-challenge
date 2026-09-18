class Solution(object):
    def sumEvenGrandparent(self, root):
        if not root:
            return 0
        ans=0
        q = deque([(root, None, None)])
        while q:
            node, parent,grandparent=q.popleft()
            if grandparent is not None and grandparent.val %2==0:
                ans=ans+node.val
            if node.left:
                q.append((node.left,node,parent))
            if node.right:
                q.append((node.right,node,parent))
        return ans



        