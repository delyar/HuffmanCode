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
        binary_encoding = ''
        for char in m:
            code = self.C[char]
            binary_encoding += code
        return binary_encoding
        
    def decode(self, text):
        final_string = ''
        key_list = list(self.C.keys())
        val_list = list(self.C.values())
        
        code = ''
        for char in text:
            code += char
            if code in self.C.values():
                position = val_list.index(code)
                key = key_list[position]
                final_string += key
                code = ''
            
        return final_string
        
     
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
    
    
f = get_frequencies('string for test')
hc = HuffmanCode(f)

print('\nencode:', hc.encode('string for test'))
print('decode:', hc.decode('100000111100111011010101011101001101000111110000'))


# hc = HuffmanCode({'F': 1, 'o': 92, 'u': 21, 'r': 79, ' ': 275, 's': 43, 'c': 31, 'e': 165, 'a': 102, 'n': 76, 'd': 58, 'v': 24, 'y': 10, 'g': 27, 'f': 26, 't': 124, 'h': 80, 'b': 13, 'i': 65, ',': 22, 'w': 26, 'L': 1, 'p': 15, 'l': 41, 'm': 13, 'q': 1, '.': 10, '\n': 4, 'N': 1, 'W': 2, '-': 15, 'I': 3, 'B': 1, 'T': 2, 'k': 3, 'G': 1})
print('Dict', hc.C)


# print('\nencode:', hc.encode('oregon state rules'))
# print('decode:', hc.decode('11001010010010101110111011101010011010010001'))


print('-----')