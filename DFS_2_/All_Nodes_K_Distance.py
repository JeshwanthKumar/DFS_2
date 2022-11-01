# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#Time_Complexity: O(n)
#Spce_Complexity: Recursive stack space - O(n)


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        adj = defaultdict(list) # Initialize adjacency matrix as a list
        self.adjList(root, adj) #Recursive function call for creating the adjacency list
        
        res = [] #Initialize result as an empty array
        self.dfs(target.val, 0, k, res, adj, set()) #Recursive function call of dfs
        return res #Return result
        
    def adjList(self, curr, adj): #Recursive function with curr and adj
        if curr.left:    #If there is a left child
            adj[curr.val].append(curr.left.val) #Append the currnet value as key with its adjacent left value as value
            adj[curr.left.val].append(curr.val) # Append the left value as key with current value as value
            self.adjList(curr.left, adj) #Recursive call
        if curr.right:    #If there is a right child
            adj[curr.val].append(curr.right.val) #Append the currnet value as key with its adjacent right value as value
            adj[curr.right.val].append(curr.val) #Append the right value as key with current value as value
            self.adjList(curr.right, adj) #Recursive call
        return  #Return, which return the adjacency matrix
    
    def dfs(self, curr, currStep, lastStep, res, adj, visited):     #Recursive function
        #Base condition
        if currStep == lastStep:    #If the currStep is equal to lastStep
            res.append(curr)    #Append the curr node into the result
            return  #Return
        visited.add(curr) #Add the curr into visited set
        for nxt in adj[curr]:    #Continue for every next node in adj
            if nxt not in visited: #If the next element is not in visited then add it to the visited
                visited.add(nxt) 
                self.dfs(nxt, currStep+1, lastStep, res, adj, visited) #Recursive call
        return  #Return
        