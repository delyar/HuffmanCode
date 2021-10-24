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
        self.C = {}
        
        
        # Creating empty heap
        heap = []
        heapify(heap)
        for char in F:
            leaf_node = LeafNode(char,F[char])
            heappush(heap, leaf_node)
            
        while len(heap) >1:
            min1 = heappop(heap)
            min2 = heappop(heap)
            
            children = [min1,min2]
            count = min1.count + min2.count
            
            u = Node(count, children)
            heappush(heap, u)
            
        self.T = heappop(heap)
        self.dfs(self.T,'')
        
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
        
     
    def dfs(self, node, code):
        if node.is_leaf():
            self.C[node.symbol] = code    
        else:
            self.dfs(node.children[0], code + '0')
            self.dfs(node.children[1], code + '1')
                    
        
        
def get_frequencies(s):
    F = dict()
    
    for char in s:
        if char in F:
            F[char] += 1
        else:
            F[char] = 1
     
    print('freq:', F)      
    return F
    
    
f = get_frequencies('abbass')

hc = HuffmanCode()

print('Dict', hc.C)
print('\nencode:', hc.encode('oregon state rules'))
print('decode:', hc.decode('0001001'))

print('-----')