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
        
        self.C = DFS(self.T)
        
    def encode(self, m):
        """
        Uses self.C to encode a binary message.
.    
        Parameters:
            m: A plaintext message.
        
        Returns:
            The binary encoding of the plaintext message obtained using self.C.
        """
        binary_encoding = ''
        for char in m:
            code = self.C[char]
            binary_encoding += code
        return binary_encoding
        
    def decode(self, text):
        return ''
        
     
     
def DFS(root):
    
    dfs_array = []
    stack = []
    
    c = {}
    
    root.discovered = True
    stack.append(root)
    #do something
    
    
    code = ''
    while len(stack) != 0:
        v = stack.pop()
        code = code[:-1]
        #process v
        
        for (index,child) in enumerate(v.children):
            if child.discovered == False:
                child.discovered = True
                stack.append(child)
                
                if index == 0:
                    code +='0'
                else:
                    code+= '1'
                    
                if child.is_leaf():
                    c[child.symbol] = code
            
                
    print('\n \n Huffman Dictionary:', c)
    return c
        
def get_frequencies(s):
    F = dict()
    
    for char in s:
        if char in F:
            F[char] += 1
        else:
            F[char] = 1
     
    print('freq:', F)      
    return F
    
    
f = get_frequencies('Huffman coding is a data compression algorithm.')

hc = HuffmanCode(f)

print('encode:', hc.encode('a'))
print('decode:', hc.decode('0001001'))

print('-----')