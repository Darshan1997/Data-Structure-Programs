class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

def levelOrder(root):
    levelQueue = []
    levelQueue.append({'0':root})
    while len(levelQueue) > 0:
        tmpDict = levelQueue[0]
        dictTuple = iter(tmpDict.items())
        key,tmpnode = next(dictTuple)
        val = key
        root = tmpnode
        print(root.info,end=" ")
        levelQueue.remove(tmpDict)
        
        if not root.left == None:
            print('in the left ',root.left.info)
            levelQueue.append({str(int(val) + 1):root.left})
        
        if not root.right == None:
            print('in the right ',root.right.info)
            levelQueue.append({str(int(val) + 1):root.right})
        



tree = BinarySearchTree()
t = int(6)

#arr = list(map(int, input().split()))
arr = [1,2,3,4,5,6]

for i in range(t):
    tree.create(arr[i])

root = tree.root

levelQueue = []
tmpset = []
levelQueue.append({'0':root})
while len(levelQueue) > 0:
    tmpDict = levelQueue[0]
    dictTuple = iter(tmpDict.items())
    key,tmpnode = next(dictTuple)
    val = key
    root = tmpnode
    tmpset.append(root.info)
    levelQueue.remove(tmpDict)
    
    if not root.left == None:
        print('in the left ',root.left.info)
        levelQueue.append({str(int(val) + 1):root.left})
    
    if not root.right == None:
        print('in the right ',root.right.info)
        levelQueue.append({str(int(val) + 1):root.right})