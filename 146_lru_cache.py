class Node:
    def __init__(self, key=None, value=None, next=None, prev=None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.map = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        
        node = self.map[key]
        self.remove(node)
        self.put(node.key, node.value)
        return node.value


    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.remove(self.map[key])
        elif len(self.map) >= self.capacity:
            self.remove(self.head.next)
        self.add(Node(key, value))            
    
    def remove(self, node: Node) -> None:
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

        del self.map[node.key]
    
    def add(self, node: Node) -> None:
        prevEnd = self.tail.prev
        prevEnd.next = node
        node.next = self.tail
        node.prev = prevEnd
        self.tail.prev = node
        self.map[node.key] = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
