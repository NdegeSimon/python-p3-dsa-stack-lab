class Stack:
    def __init__(self, items=None, limit=100):
        self.limit = limit
        if items is None:
            self.items = []
        else:
            self.items = items[:]  # Create a copy to avoid mutable default argument issues

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
            # Based on test expectations, don't raise exception - just ignore
            pass

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            # Based on test expectations, return None instead of raising exception
            return None

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)

    def empty(self):
        """Returns True if the Stack is empty; False otherwise"""
        return len(self.items) == 0

    def full(self):
        """Returns True if the Stack is full; False otherwise"""
        return len(self.items) >= self.limit

    def search(self, target):
        """Returns distance from top to target element, or -1 if not found"""
        try:
            # Find the index of the target from the end (top of stack)
            for i, item in enumerate(reversed(self.items)):
                if item == target:
                    return i
            return -1
        except:
            return -1


# Example usage and tests:
if __name__ == "__main__":
    # Test empty stack
    print("Testing empty stack:")
    stk = Stack()
    print(f"isEmpty: {stk.isEmpty()}")  # True
    print(f"empty: {stk.empty()}")      # True
    print(f"size: {stk.size()}")        # 0
    print(f"pop on empty: {stk.pop()}")  # None
    
    # Test full stack
    print("\nTesting full stack:")
    stk = Stack([1], 1)  # Stack with one item and limit of 1
    print(f"full: {stk.full()}")        # True
    print(f"size: {stk.size()}")        # 1
    print(f"pop: {stk.pop()}")          # 1
    
    stk.push(1)  # Add item back
    print(f"After push(1), size: {stk.size()}")  # 1
    stk.push(2)  # This should not raise error, just be ignored
    print(f"After push(2), size: {stk.size()}")  # Still 1
    
    # Test search functionality
    print("\nTesting search:")
    stk = Stack()
    stk.push(1)
    stk.push(2)
    stk.push(3)
    
    print(f"Search for 3: {stk.search(3)}")  # 0 (at top)
    print(f"Search for 2: {stk.search(2)}")  # 1 (one position from top)
    print(f"Search for 1: {stk.search(1)}")  # 2 (two positions from top)
    print(f"Search for 5: {stk.search(5)}")  # -1 (not found)