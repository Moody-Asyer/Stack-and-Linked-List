class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "{data:%s,next:%s}"%(self.data,self.next)

class LinkedList():
    def __init__(self):
        self.head = None

    def __repr__(self):
        return "{head:%s}"%(self.head)

    def push(self,data):
        current = self.head
        new_node = Node(data)
        if current == None:
            if data != None:
                self.head = new_node
            else:
                return self.head
        else:
            while current != None:
                if current.next == None:
                    current.next = new_node
                    break
                else:
                    current = current.next
            return self.head

    def pop(self):
        current = self.head
        prev = None
        if current == None:
            return self.head
        while current != None:
            if current.next == None:
                if prev == None:
                    return current.next
                else:
                    prev.next = None
                    break
            else:
                prev = current
                current = current.next
        return self

    def top(self):
        current = self.head
        if current == None:
            return self.head
        while current != None:
            if current.next == None:
                return current
            else:
                current = current.next

    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False

    def len(self):
        current = self.head
        length = 0
        if current == None:
            return length
        else:
            while current != None:
                length += 1
                current = current.next
            return length

def main():
    list = LinkedList()
    print(list.is_empty())
    list.push(1)
    list.push(3)
    list.push(5)
    list.push(6)
    print(list)
    print(list.pop())
    print(list)
    print(list.top())
    print(list.is_empty())
    print(list.len())

    def tests():
        def test_push1():
            list = LinkedList()
            list.push(1)
            expected_data = 1
            expected_next = None
            result_data = list.head.data
            result_next = list.head.next

            assert expected_data == result_data
            assert expected_next == result_next

        def test_push2():
            list = LinkedList()
            list.push(None)
            expected_head = None
            result_head = list.head

            assert expected_head == result_head

        def test_push3():
            list = LinkedList()
            list.push(1)
            list.push(3)
            list.push(5)

            expected_data1 = 1
            expected_data2 = 3
            expected_data3 = 5
            expected_nextdata1 = 3
            expected_nextdata2 = 5
            expected_nextdata3 = None
            result_data1 = list.head.data
            result_data2 = list.head.next.data
            result_data3 = list.head.next.next.data
            result_next1 = list.head.next.data
            result_next2 = list.head.next.next.data
            result_next3 = list.head.next.next.next

            assert expected_data1 == result_data1
            assert expected_data2 == result_data2
            assert expected_data3 == result_data3
            assert expected_nextdata1 == result_next1
            assert expected_nextdata2 == result_next2
            assert expected_nextdata3 == result_next3

        def test_pop1():
            list = LinkedList()

            expected = None
            result = list.pop()

            assert expected == result

        def test_pop2():
            list = LinkedList()
            list.push(2)
            list.push(3)
            list.push(4)
            list.pop()

            expected_data1 = 2
            expected_data2 = 3
            expected_next1 = 3
            expected_next2 = None
            result_data1 = list.head.data
            result_data2 = list.head.next.data
            result_next1 = list.head.next.data
            result_next2 = list.head.next.next

            assert expected_data1 == result_data1
            assert expected_data2 == result_data2
            assert expected_next1 == result_next1
            assert expected_next2 == result_next2

        def test_pop3():
            list = LinkedList()
            list.push(2)
            expected = None
            result = list.pop()

            assert expected == result

        def test_top1():
            list = LinkedList()
            expected = None
            result = list.top()

            assert expected == result

        def test_top2():
            list = LinkedList()
            list.push(1)
            list.push(2)
            top = list.top()
            expected_data = 2
            expected_next = None
            result_data = top.data
            result_next = top.next

            assert expected_data == result_data
            assert expected_next == result_next

        def test_is_empty1():
            list = LinkedList()
            expected = True
            result = list.is_empty()

            assert expected == result

        def test_is_empty2():
            list = LinkedList()
            list.push(1)
            list.push(8)
            expected = False
            result = list.is_empty()

            assert expected == result

        def test_len1():
            list = LinkedList()
            expected = 0
            result = list.len()

            assert expected == result

        def test_len2():
            list = LinkedList()
            list.push(3)
            list.push(9)
            list.push(12)
            expected = 3
            result = list.len()

            assert expected == result

        test_push1()
        test_push2()
        test_push3()
        test_pop1()
        test_pop2()
        test_pop3()
        test_top1()
        test_top2()
        test_is_empty1()
        test_is_empty2()
        test_len1()
        test_len2()
    tests()
main()