class BSTNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.left = BSTNode(value)
            else: 
                self.right.insert(value)

    def contains(self, value):
        if value == self.value:
            return True
        elif value < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(value)
        elif value > self.value:
            if not self.right:
                return False
            else:
                return self.right.contains(value)