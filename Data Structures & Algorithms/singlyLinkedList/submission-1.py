class LinkedList:
    
    def __init__(self):
        self.linked_list = []
        self.head_counter = 0
        self.tail_counter = 0

    
    def get(self, index: int) -> int:
        try:
            node = self.linked_list[index]
            return node
        except IndexError:
            return -1

    def insertHead(self, val: int) -> None:
        self.linked_list.insert(0, val)

    def insertTail(self, val: int) -> None:
        self.linked_list.append(val)

    def remove(self, index: int) -> bool:
        try:
            self.linked_list.pop(index)
            return True
        except IndexError:
            return False
        

    def getValues(self) -> List[int]:
        return self.linked_list
