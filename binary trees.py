class TreeNode(object):
    def __init__(self,data):
        self.data = data
        self.leftNode = None;
        self.rightNode= None;
      
    def __str__ (self):
        return str(self.data);
    
    
   
       
class BinaryTree(object):
    def __init__(self):
        self.root = None;
    def __str__(self):
        return "My root node is "+ str(self.root.data);
    def insert(self,data):
        newNode = TreeNode(data);

        if(self.root is None ):
            self.root = newNode;
            print ("inserted new node at root");
        else :
            self.insertBelow(self.root, newNode);
                
        

    def insertBelow(self,subRoot, newNode):

        if (newNode.data < subRoot.data):
            #go left
            if (subRoot.leftNode is None):
                    subRoot.leftNode= newNode;
            else:
                
                self.insertBelow(subRoot.leftNode, newNode);
        elif(newNode.data > subRoot.data):
            #go right
            if (subRoot.rightNode is None):
                    subRoot.rightNode= newNode;
            else:
                
                self.insertBelow(subRoot.rightNode, newNode);
        else:
                #it's equal
                 print ("Can't insert duplicate value" );
    def printInOrder(self):
        if (self.root is None):
            print("The tree is empty");
        else:
            self.printInOrderRecursive(self.root,0);
            
    def printInOrderRecursive(self,subRoot, depthSoFar):
        if(subRoot.leftNode is not None):
            #print("Go left")
            self.printInOrderRecursive(subRoot.leftNode, depthSoFar+ 1);

        for i in range (0, depthSoFar):
            print ('\t', end= ' ')
        print(subRoot);

        if(subRoot.rightNode is not None):
            #print("Go Right")
            self.printInOrderRecursive(subRoot.rightNode, depthSoFar+ 1);
       
        
    def search(self,key):
        if(self.root is None):
            return False;
        else:
            return self.searchRecursive(self.root, key);
           
    def searchRecursive(self, subRoot,key):
        if (key < subRoot.data):
            if(subRoot.leftNode is None):
                return None;
            else:
                return self.searchRecursive(subRoot.leftNode, key);
        elif(key> self.root.data):
            if(subRoot.rightNode is None):
                return None;
            else:
                return self.searchRecursive(subRoot.rightNode, key);
        else:
            return subRoot;
        
    def delete(self, key):
        self.root = self.deleteRecursive(self.root, key);

    def deleteRecursive(self, subRoot, key):
        
        #print('{},{}'.format(subRoot, key));
        if(subRoot is None):
            return subRoot
        
        if(key < subRoot.data):
            # go left
           subRoot.leftNode = self.deleteRecursive(subRoot.leftNode, key);
        elif(key > subRoot.data):
            #go right
           subRoot.rightNode = self.deleteRecursive(subRoot.rightNode, key);
        else:
            #found it
            #print("found it")
            if subRoot.leftNode is None and subRoot.rightNode is None:
                #print("delete a leaf node")
                 #this is a leaf node just delete it
                return None;
            #Case 2: 1 child
            elif subRoot.leftNode is None or subRoot.rightNode is None:
            #Replace this node with its child
                if subRoot.leftNode is not None:
                    temp = subRoot.leftNode
                    subRoot = None
                    return temp;
                elif subRoot.rightNode is not None:
                    temp = subRoot.rightNode
                    subRoot = None
                    return temp;
            #Case 3: 2 children
            else:
                #Replace this node with the inorder successor/ next biggest number in the tree
                inOrderSuccessor = self.inOrderSuccessor(subRoot);
                subRoot.data = inOrderSuccessor.data;
                subRoot.rightNode = self.deleteRecursive(subRoot.rightNode, inOrderSuccessor.data)
        return subRoot;
            
    def inOrderSuccessor(self, subRoot):
        #return the smallest value in the right subtree
        current = subRoot.rightNode;

        while current.leftNode is not None:
            current = current.leftNode;

        return current;
        
    
            
        # find the node
        
        

            
            
        
            

           
        
        
    
        
       

 


def main():
     tree = BinaryTree();
     tree.insert(2);
     tree.insert(5);
     tree.insert(1);
     tree.insert(4);
     tree.insert(6);
     tree.printInOrder();
     #tree.printInOrder();
     tree.delete(6);
     print('\n');
     tree.printInOrder();
     tree.delete(5)
     print('\n');
     tree.printInOrder();
     tree.delete(2)
     print('\n');
     tree.printInOrder();
     
     
     
     #print("Contains 1?", tree.search(1));
     #print("Contains 8?",tree.search(8));
    
if __name__ == "__main__":
    main();
