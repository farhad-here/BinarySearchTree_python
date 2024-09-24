import pydot
from binarytree import build
# SALAM
# PROJECT DARMORDE
# BST NODE CLASS 
# BA PYTHON 
# :)

#BST IN PYTHON


class Node: 
  
    # Constructor to create a new node 
    def __init__(self, key): 
        self.key = key  
        self.left = None
        self.right = None
        
        
class BinarySearchTree:

    def __init__(self):
        self.root = None  
        
    def insert(self, data): 
        if self.root is None: 
            self.root = Node(data) 
        else: 
            if self.root.key < data: 
                if self.root.right is None: 
                    self.root.right = Node(data) 
                else: 
                    self.insertNode(self.root.right, data) 
            else: 
                if self.root.left is None: 
                    self.root.left = Node(data) 
                else: 
                    self.insertNode(self.root.left, data)  

    def insertNode(self, currentNode, val):
        if(val <= currentNode.key):
            if(currentNode.left):
                self.insertNode(currentNode.left, val)
            else:
                currentNode.left = Node(val)
        elif(val > currentNode.key):
            if(currentNode.right):
                self.insertNode(currentNode.right, val)
            else:
                currentNode.right = Node(val)
                    
    def search(self, root, key): 
        # Base Cases: root is null or key is present at root 
        if root is None or root.key == key: 
            return root 
      
        # Key is greater than root's key 
        if root.key < key: 
            return self.search(root.right, key) 
        
        # Key is smaller than root's key 
        return self.search(root.left, key) 
      
    # This code is contributed by Bhavya Jain                
    
    def inorder(self, root): 
        if root is not None: 
            self.inorder(root.left) 
            print(root.key) 
            self.inorder(root.right) 
    
    def findsuccessor(self, current_node):
        while current_node.left != None:
            current_node = current_node.left
        return current_node
    
    def deleteNode(self, root, key): 
  
        # Base Case 
        if root is None: 
            return root  
      
        # If the key to be deleted is smaller than the root's 
        # key then it lies in  left subtree 
        if key < root.key: 
            root.left = self.deleteNode(root.left, key) 
      
        # If the kye to be delete is greater than the root's key 
        # then it lies in right subtree 
        elif(key > root.key): 
            root.right = self.deleteNode(root.right, key) 
      
        # If key is same as root's key, then this is the node 
        # to be deleted 
        else: 
              
            # Node with only one child or no child 
            if root.left is None : 
                return root.right  
                  
            elif root.right is None : 
                return root.left 
      
            # Node with two children: Get the inorder successor 
            # (smallest in the right subtree) 
            temp = self.findsuccessor(root.right) 
      
            # Copy the inorder successor's content to this node 
            root.key = temp.key 
      
            # Delete the inorder successor 
            root.right = self.deleteNode(root.right , temp.key) 
      
        return root  
    
    def delete(self, key): 
        return self.deleteNode(self.root, key)

    def treeMinimum(self, node):
        while node.left is not None:
            node = node.left
        return node
    def treeMaximum(self, node):
        while node.right is not None:
            node = node.right
        return node
    
    
if __name__ == '__main__':
    bst = BinarySearchTree()
    y = []
    zzz = []
    print("insert 50 30 20 40 70 60 80 ya hrchi mad nazareton hst:")
    bst.insert(x:=int(input(('INPUT FOR INSERT 1=> '))))
    y.append(x)
    bst.insert(x:=int(input(('INPUT FOR INSERT 2=> ')))) 
    y.append(x)
    bst.insert(x:=int(input(('INPUT FOR INSERT 3=> ')))) 
    y.append(x)
    bst.insert(x:=int(input(('INPUT FOR INSERT 4=> ')))) 
    y.append(x)
    bst.insert(x:=int(input(('INPUT FOR INSERT 5=> ')))) 
    y.append(x)
    bst.insert(x:=int(input(('INPUT FOR INSERT 6=> ')))) 
    y.append(x)
    bst.insert(x:=int(input(('INPUT FOR INSERT 7=> '))))
    y.append(x)
    print("inorder Permutation:")
    bst.inorder(bst.root)
    search = int(input(('INPUT FOR SEARCH, just put 80 or everything you want base on inputs in tree=> ')))
    print(f'search for {search} Node:')
    if bst.search(bst.root, search) is None:
        print(search, ' is not exist in tree')
    else:
        print(search, ' is in tree')
    bst.delete(m:=int(input(('INPUT FOR DELETE, put it 80 or everything you want base on input in tree=> '))))
    print("your number node deleted from Tree sucessfully")   
    print("Print Tree after Delete number node to user:")
    bst.inorder(bst.root)
    y.remove(m)
    zzz.extend(y)

    





values = y

tree = build(values)

print(tree)

print(tree.values)

graph = pydot.Dot(graph_type='graph')

for i in tree.values:

    edge = pydot.Edge(i, i+1)

    graph.add_edge(edge)
values = zzz

tree = build(values)

print(tree)

print(tree.values)

graph = pydot.Dot(graph_type='graph')

for i in tree.values:

    edge = pydot.Edge(i, i+1)

    graph.add_edge(edge)


