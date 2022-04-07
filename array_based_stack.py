class ArrayBasedStack():
    def __init__(self):
        size = 4
        self.array = [None] * size

    def __repr__(self):
        return "%s" % (self.array)

    def push(self, data):
        index = 0
        while self.array[index] is not None:
            index += 1
            if index > len(self.array) - 1:
                new_array = [None] * (len(self.array) // 2)
                new_array = self.array + new_array
                self.array = new_array
        if self.array[index] is None:
            if index > len(self.array) - 1:
                new_array = [None] * (len(self.array) // 2)
                new_array = self.array + new_array
                self.array = new_array
            self.array[index] = data
        return self.array

    def pop(self):
        index = len(self.array) - 1
        empty = self.is_empty()
        if empty == True:
            return self.array
        else:
            while self.array[index] is None:
                index -= 1
            if self.array[index] is not None:
                data = self.array[index]
                self.array[index] = None
            return data

    def top(self):
        index = len(self.array) - 1
        empty = self.is_empty()
        if empty == True:
            return None
        else:
            while self.array[index] is None:
                index -= 1
            if self.array[index] is not None:
                return self.array[index]

    def is_empty(self):
        index = 0
        while index <= len(self.array) - 1:
            if self.array[index] is not None:
                return False
            else:
                index += 1
        return True

    def len(self):
        length = 0
        for data in self.array:
            if data is not None:
                length += 1
            else:
                pass
        return length

def main():
    array = ArrayBasedStack()
    print(array.is_empty())
    array.push(1)
    array.push(3)
    array.push(6)
    array.push(7)
    print(array)
    print(array.pop())
    print(array)
    array.push(9)
    print(array)
    array.push(11)
    print(array)
    array.push(12)
    array.push(14)
    array.push(18)
    print(array)
    print(array.top())
    print(array.len())
    print(array.is_empty())


    def tests():
        def test_push1():
            array = ArrayBasedStack()
            expected = [1, None, None, None]
            result = array.push(1)

            assert expected == result

        def test_push2():
            array = ArrayBasedStack()
            expected = [None, None, None, None]
            result = array.push(None)

            assert expected == result

        def test_push3():
            array = ArrayBasedStack()
            array.push(1)
            array.push(2)
            array.push(3)
            array.push(4)
            expected = [1, 2, 3, 4, 5, None]
            result = array.push(5)

            assert expected == result

        def test_pop1():
            array = ArrayBasedStack()
            expeceted = [None, None, None, None]
            result = array.pop()

            assert expeceted == result

        def test_pop2():
            array = ArrayBasedStack()
            array.push(1)
            array.push(2)
            array.push(3)
            array.push(4)
            expected_data = 4
            result_data = array.pop()

            assert expected_data == result_data

        def test_pop3():
            array = ArrayBasedStack()
            array.push(1)
            array.push(2)
            array.push(3)
            array.push(4)
            array.pop()
            expected_stack = [1, 2, 3, None]
            result_stack = array.array

            assert expected_stack == result_stack

        def test_top1():
            array = ArrayBasedStack()
            expected = None
            result = array.top()

            assert expected == result

        def test_top2():
            array = ArrayBasedStack()
            array.push(1)
            array.push(4)
            array.push(9)
            array.push(10)
            expected = 10
            result = array.top()

            assert expected == result

        def test_top3():
            array = ArrayBasedStack()
            array.push(1)
            array.push(4)
            array.push(9)
            # [1,4,9,None]
            expected = 9
            result = array.top()

            assert expected == result

        def test_is_empty1():
            array = ArrayBasedStack()
            expected = True
            result = array.is_empty()

            assert expected == result

        def test_is_empty2():
            array = ArrayBasedStack()
            array.push(1)
            expected = False
            result = array.is_empty()

            assert expected == result

        def test_len1():
            array = ArrayBasedStack()
            # [None,None,None,None]
            expected = 0
            result = array.len()

            assert expected == result

        def test_len2():
            array = ArrayBasedStack()
            array.push(2)
            array.push(5)
            expected = 2
            result = array.len()

            assert expected == result

        test_push1()
        test_push2()
        test_push3()
        test_pop1()
        test_pop2()
        test_pop3()
        test_top1()
        test_top2()
        test_top3()
        test_is_empty1()
        test_is_empty2()
        test_len1()
        test_len2()
    tests()
main()
