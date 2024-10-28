import weakref

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

# Реализация очереди
class LinkedListQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.node_map = weakref.WeakValueDictionary()  # Слабые ссылки на узлы
    
    def is_empty(self):
        return self.head is None
    
    def enqueue(self, item):
        new_node = Node(item)
        self.node_map[item.pk] = new_node  # Используем pk как ключ
        if self.tail:
            self.tail.next = new_node
            new_node.prev = self.tail
        self.tail = new_node
        if not self.head:
            self.head = new_node
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        node = self.head
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        del self.node_map[node.value.pk]  # Удаляем узел по pk
        return node.value
    
    def front(self):
        if self.is_empty():
            raise IndexError("front from empty queue")
        return self.head.value
    
    def size(self):
        return len(self.node_map)  # Возвращаем размер по числу узлов в node_map

    def get_node(self, pk):
        if pk in self.node_map:
            return self.node_map[pk]
        else:
            raise ValueError("Item not found in the queue")
    
    def update_node(self, old_pk, new_item):
        node = self.get_node(old_pk)
        node.value = new_item
        self.node_map[new_item.pk] = node
        del self.node_map[old_pk]