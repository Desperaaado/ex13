class SLLNode(object):
    def __init__(self, value, nxt, prev):
        self.value = value
        self.next = nxt

    def __repr__(self):
        nxt = self.next and self.next.value or None
        return f"=={self.value}: {repr(nxt)}=="

class SLList(object):
    def __init__(self):
        self.begin = None
        self.end = None

    def push(self, obj):
        self.begin = self.end
        self.end = SLLNode(obj, self.begin, None)
    
    def pop(self):
        result = self.end and self.end.value or None
        self.end = self.end and self.end.next or None
        self.begin = self.begin and self.begin.next or None
        return result
    
    def shift(self, obj):
        a = self.begin
        b = self.end

        while self.begin:
            self.end = self.end and self.end.next or None
            self.begin = self.begin.next

        self.begin = SLLNode(obj, None, None)

        if self.end:
            self.end.next = self.begin
            self.begin = a
            self.end = b
        else:
            self.end = self.begin
            self.begin = None

    def unshift(self):
        the_end = self.end
        the_begin = the_end and the_end.next or None

        if the_begin:
            
            while self.begin.next:
                self.end = self.end and self.end.next or None
                self.begin = self.begin.next

            self.end.next = None
            result = self.begin.value
            self.end = the_end
            self.begin = the_end and the_end.next or None
        elif the_end:
            result = self.end.value
            self.end = None
        else:
            result = None

        return result

    def first(self):
        pass

    def last(self):
        pass

    def dump(self):
        a = self.begin
        b = self.end
        i = 0
        
        while self.end:
            print(f'{i}===>', self.end)
            self.end = self.end and self.end.next or None
            self.begin = self.begin and self.begin.next or None
            i += 1
        
        print("==That's all.==")
        self.begin = a
        self.end = b

    def count(self):
        a = self.begin
        b = self.end

        if b:
            i = 1
        else:
            i = 0

        while self.end:
            # print(f'{i}===>', self.end)
            self.end = self.end and self.end.next or None
            self.begin = self.begin and self.begin.next or None
            i += 1
        
        i -= 1
        self.begin = a
        self.end = b

        # for empty list
        if i < 0:
            i += 1

        return i

    def remove(self):
        pass

    def get(self, index):
        max_range = self.count() - 1
        
        if index > max_range or max_range < 0:
            print('Out of range!')
            return None

        the_end = self.end

        for i in range(max_range - index):
            self.end = self.end and self.end.next or None
            self.begin = self.begin and self.begin.next or None


        result = self.end and self.end.value or None
        self.end = the_end
        self.begin = self.end and self.end.next or None
        return result
     