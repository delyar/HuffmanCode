from heapq import heapify, heappush, heappop

class Node:
    def __init__(self, count, children):
        self.count    = count
        self.children = children
        self.discovered = False
        
    def is_leaf(self):
        return False
        
    def __lt__(self, other):
        return self.count < other.count

    def __eq__(self, other):
        return self.count == other.count
        
        
        
class LeafNode(Node):
    def __init__(self, symbol, count):
        super().__init__(count, [])
        self.symbol = symbol
        
    def is_leaf(self):
        return True



class HuffmanCode:
    def __init__(self, F):
        self.C = dict() 
        self.T = None   
        
        
        # Creating empty heap
        heap = []
        heapify(heap)
        for char in F:
            leaf_node = LeafNode(char,F[char])
            heappush(heap, leaf_node)
            
        
        
        while len(heap) >1:
            min1 = heap[0]
            heappop(heap)
            min2 = heap[0]
            heappop(heap)
            children = [min1,min2]
            count = min1.count + min2.count
            u = Node(count,children)
            heappush(heap, u)
            
        self.T = heap[0]
        heappop(heap)
        
        print("The heap elements : ")
        for i in heap:
            print(i.count, end = ' ')
            
        print('T:',self.T)
        
        
        
    def encode(self, m):
        """
        Uses self.C to encode a binary message.
.    
        Parameters:
            m: A plaintext message.
        
        Returns:
            The binary encoding of the plaintext message obtained using self.C.
        """
        return None
        
    def decode(self, c):
        """
        Uses self.T to decode a binary message c = encode(m).
.    
        Parameters:
            c: A message encoded in binary using self.encode.
        
        Returns:
            The original plaintext message m decoded using self.T.
        """
        
        # TODO: Implement this method!
        return None
     
     
     
def DFS(root):
    print('-------')
    print('DFS:')
    dfs_array = []
    stack = []
     
    root.discovered = True
    dfs_array.append(root)
    stack.append(root)
    #do something
    
    
    while len(stack) != 0:
        v = stack.pop()
        #process v
        
        for child in v.children:
            if child.discovered == False:
                child.discovered = True
                dfs_array.append(child)
                stack.append(child)
                
    print('-------')
    return dfs_array
        
def get_frequencies(s):
    F = dict()
    
    for char in s:
        if char in F:
            F[char] += 1
        else:
            F[char] = 1
     
    print('freq:', F)      
    return F
    
    
    
f = get_frequencies('salam')

hc = HuffmanCode(f)

dfs = DFS(hc.T)

print(dfs)