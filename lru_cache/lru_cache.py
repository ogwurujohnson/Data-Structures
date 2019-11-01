from doubly_linked_list import ListNode
from doubly_linked_list import DoublyLinkedList


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.dll = DoublyLinkedList()
        self.cache = {}

    def find_node(self, key):
        node = self.dll.head
        if node.value == key:
            return node
        while self.dll.tail is not node:
            node = node.next
            if node.value == key:
                return node
        return None

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        if key not in self.cache:
            return None

        value = self.cache[key]
        node = self.find_node(key)
        self.dll.move_to_front(node)
        return value

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
        if not key in self.cache:
            self.cache[key] = value
            self.dll.add_to_head(key)
        else:
            self.cache[key] = value
            node = ListNode(value)
            self.dll.move_to_front(node)
        if self.dll.length > self.limit:
            del self.cache[self.dll.tail.value]
            self.dll.remove_from_tail()