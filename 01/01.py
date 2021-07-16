# 链表

class linkpoint:
    def __init__(self, data, nextid=None):
        self.nextid = nextid
        self.data = data


class link:

    def __init__(self):
        self.head: linkpoint = None
        self.current: linkpoint = None
        self.last = False
    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):

        if self.current.nextid != None:
            now = self.current
            self.current = self.current.nextid
            return now
        elif self.last == False:
            self.last = True
            return self.current
        else:
            raise StopIteration


a = linkpoint(13)
b = linkpoint(19)
a.nextid = b
linking = link()
linking.head = a
for x in linking:
    print(x.data)
