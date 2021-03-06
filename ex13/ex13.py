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
        the_end = self.end

        while self.begin:
            self.end = self.end and self.end.next or None
            self.begin = self.begin.next

        self.begin = SLLNode(obj, None, None)

        if self.end:
            self.end.next = self.begin
            self.end = the_end
        else:
            self.end = self.begin
            self.begin = None

    def unshift(self):
        the_end = self.end
        the_begin = the_end and the_end.next or None

        if the_begin:
            
            while self.begin and self.begin.next:
                self.end = self.end and self.end.next or None
                self.begin = self.begin.next

            self.end.next = None
            result = self.begin and self.begin.value
            self.end = the_end
            self.begin = the_end and the_end.next or None
        elif the_end:
            result = self.end.value
            self.end = None
        else:
            result = None

        return result

    def first(self):
        un_shift = self.unshift()

        if un_shift:
            result = un_shift
            self.shift(un_shift)
        else:
            result = None

        return result


    def last(self):
        the_pop = self.pop()

        if the_pop:
            result = the_pop
            self.push(result)
        else:
            result = None

        return result

    def dump(self, text='Dump'):
        silence = False

        if text == '--silence':
            silence = True

        if not silence:
            print(f'=={text}==')

        a = self.begin
        b = self.end
        i = 0
        the_list = []

        while self.end:
            if not silence:
                print(f'{i}===>', self.end)

            the_list.append(self.end.value)
            self.end = self.end and self.end.next or None
            self.begin = self.begin and self.begin.next or None
            i += 1
        
        if not silence:
            print("==That's all.==")

        self.begin = a
        self.end = b
        return the_list[::-1]

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

    def remove(self, obj):
        the_list = self.dump('--silence')
        the_range = self.count() - 1

        if not(obj in the_list):
            print('Not exist!')
            return None

        if self.end.value == obj:
            self.pop()
            return the_range

        the_end = self.end
        i = 1

        while self.begin.value != obj:
            i += 1
            self.end = self.end and self.end.next or None
            self.begin = self.begin and self.begin.next or None

        self.end.next = self.begin.next
        self.end = the_end

        return the_range - i
        

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
     