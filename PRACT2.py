class Order:
    def __init__(self, qtty, customer):
        self.customer = customer
        self.qtty = qtty

    def print_order(self):
        print(f"     Customer: {self.customer}")
        print(f"     Quantity: {self.qtty}")
        print("     ------------")

class Node:
    def __init__(self, info):
        self.info = info
        self.next = None

class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def enqueue(self, info):
        new_node = Node(info)
        if self.is_empty():
            self.front = new_node
        else:
            self.rear.next = new_node
        self.rear = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            return None
        info = self.front.info
        self.front = self.front.next
        self.size -= 1
        if self.is_empty():
            self.rear = None
        return info

    def queue_dump(self):
        print("********* QUEUE DUMP *********")
        print(f"   Size: {self.size}")
        node = self.front
        index = 1
        while node is not None:
            print(f"   ** Element {index}")
            order = node.info
            order.print_order()
            node = node.next
            index += 1
        print("******************************")

def main():
    queue = LinkedQueue()
    
    queue.enqueue(Order(20, "cust1"))
    queue.enqueue(Order(30, "cust2"))
    queue.enqueue(Order(40, "cust3"))
    queue.enqueue(Order(50, "cust3"))

    queue.queue_dump()

if __name__ == "__main__":
    main()