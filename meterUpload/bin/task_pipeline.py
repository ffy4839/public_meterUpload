import redis

class tasks_pipeline():
    def __init__(self):
        self.task = {}

    def push(self, data):
        pass

    def pop(self, data):
        pass

    def check_type(self, data):
        pass

    def isEmpty(self):
        pass

    def isFull(self):
        pass

class queue():
    def __init__(self, size):
        self.item = []
        self.size = size

    def push(self, data):
        pass

    def pop(self):
        pass

    def isEmpty(self):
        pass

    def isFull(self):
        pass

