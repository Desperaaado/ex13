class SLLNode(object):
    def __init__(self, value, nxt, prev):
        self.value = value
        self.next = nxt

    def __repr__(self):
        nxt = self.next and self.next.value or None
        return f"{self.value}: {repr(nxt)}"

class SLList(object):
    def __init__(self):
        self.bigain = None
        self.end = None

    def push(self, obj):
        nxt = self.bigain
        self.bigain = self.end
        self.end = SLLNode(obj, nxt, None)
    
    def pop(self):
        result = self.end and self.end.value or None
        self.end = self.bigain
        self.bigain = self.bigain and self.bigain.next or None
        return result
    
    def shift(self):
        pass

    def unshift(self):
        pass

    def first(self):
        pass

    def last(self):
        pass

    def dump(self):
        pass

    def count(self):
        pass

    def remove(self):
        pass

    def get(self):
        pass
     