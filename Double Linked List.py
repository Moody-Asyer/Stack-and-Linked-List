double_linked_list = {"head": None}


def add_first(list, data):
    current_head = list["head"]
    new_node = {"data": data,
                "prev": None,
                "next": None
                }
    if current_head == None:
        list["head"] = new_node
    while current_head != None:
        new_node["next"] = current_head
        current_head["prev"] = new_node
        list["head"] = new_node
        break
    return list


def add_last(list, data):
    current_head = list["head"]
    new_node = {"data": data,
                "prev": None,
                "next": None
                }
    if current_head == None:
        list["head"] = new_node
    while current_head != None:
        if current_head["next"] == None:
            new_node["prev"] = current_head
            current_head["next"] = new_node
            break
        else:
            current_head = current_head["next"]
    return list


def add_item_at(list, data, index):
    current_head = list["head"]
    new_node = {"data": data,
                "prev": None,
                "next": None
                }
    count = 0
    if index == 0:
        add_first(list, data)
    else:
        while count != index - 1:
            current_head = current_head["next"]
            count += 1
        if count == index - 1:
            new_node["next"] = current_head["next"]
            new_node["prev"] = current_head
            current_head["next"]["prev"] = new_node
            current_head["next"] = new_node
    return list


def remove_first(list):
    current_head = list["head"]
    list["head"] = current_head["next"]
    list["head"]["prev"] = None
    return list


def remove_last(list):
    current_head = list["head"]
    prev = None
    while current_head != None:
        if current_head["next"] == None:
            prev["next"] = None
            break
        else:
            prev = current_head
            current_head = current_head["next"]
    return list


def remove_item_at(list, index):
    current_head = list["head"]
    prev = None
    count = 0
    if index == 0:
        remove_first(list)
    while count != index:
        prev = current_head
        current_head = current_head["next"]
        count += 1
    if count == index:
        prev["next"] = current_head["next"]
        current_head["next"]["prev"] = current_head["prev"]
    return list


def get_first(list):
    return list["head"]


def get_last(list):
    current_head = list["head"]
    while current_head["next"] != None:
        current_head = current_head["next"]
    return current_head


def get_item_at(list, index):
    current_head = list["head"]
    count = 0
    while count != index:
        current_head = current_head["next"]
        count += 1
    if count == index:
        return current_head


def after(node):
    return node["next"]


def prev(node):
    return node["prev"]


def print_double_linked_list(list):
    current_head = list["head"]
    print = ""
    while current_head != None:
        data = current_head["data"]
        print = print + ("%s<=>") % data
        current_head = current_head["next"]
    print = print + "None"
    return print


def size(linked_list):
    current_head = linked_list["head"]
    length = 0
    if current_head == None:
        return length
    while current_head is not None:
        length += 1
        current_head = current_head["next"]
    return length


add_first(double_linked_list, 5)
add_first(double_linked_list, 3)
add_first(double_linked_list, 1)
add_last(double_linked_list, 7)
add_last(double_linked_list, 9)
add_last(double_linked_list, 10)
add_item_at(double_linked_list, 6, 3)
remove_first(double_linked_list)
remove_last(double_linked_list)
remove_item_at(double_linked_list, 2)
p = print_double_linked_list(double_linked_list)
print(p)
print(double_linked_list)
x = get_first(double_linked_list)
print(x)
y = get_last(double_linked_list)
print(y)
z = get_item_at(double_linked_list, 2)
print(z)
print(after(z))
print(prev(z))
a = size(double_linked_list)
print(a)


def test():
    def test_add_item_at1():
        test_list = {"head": None}
        add_first(test_list, 10)
        add_first(test_list, 6)
        add_first(test_list, 2)

        test_list2 = {"head": None}
        add_first(test_list2, 10)
        add_first(test_list2, 6)
        add_first(test_list2, 4)
        add_first(test_list2, 2)

        expected = test_list2
        result = add_item_at(test_list, 4, 1)

        assert size(expected) == size(result)

    test_add_item_at1()

    def test_add_item_at2():
        test_list = {"head": None}
        add_first(test_list, 1)

        expected = test_list
        result = add_item_at(test_list, 1, 0)

        assert expected == result

    test_add_item_at2()

    def test_add_last():
        test_list = {"head": None}
        add_first(test_list, 9)
        add_first(test_list, 6)
        add_first(test_list, 4)
        add_first(test_list, 1)

        test_list2 = {"head": None}
        add_first(test_list2, 12)
        add_first(test_list2, 9)
        add_first(test_list2, 6)
        add_first(test_list2, 4)
        add_first(test_list2, 1)

        expected = test_list2
        result = add_last(test_list, 12)

        assert size(expected) == size(result)

    test_add_last()

    def test_add_last2():
        test_list = {"head": None}
        add_first(test_list, 1)

        expected = test_list
        result = add_last(test_list, 1)

        assert expected == result

    test_add_last2()

    def test_add_last3():
        test_list = {"head": None}

        expected = test_list
        result = add_last(test_list, None)

        assert expected == result

    test_add_last3()

    def test_after():
        test_list = {"head": None}
        add_first(test_list, 10)
        add_first(test_list, 6)
        add_first(test_list, 5)
        add_first(test_list, 4)
        add_first(test_list, 2)
        test_node = get_item_at(test_list, 2)
        test_node2 = get_item_at(test_list, 3)
        expected = test_node2
        result = after(test_node)
        assert expected == result

    test_after()

    def test_after2():
        test_list = {"head": None}
        add_first(test_list, 10)
        test_node = get_first(test_list)
        expected = None
        result = after(test_node)
        assert expected == result

    test_after2()

    def test_after3():
        test_list = {"head": None}
        add_first(test_list, None)
        test_node = get_first(test_list)
        expected = None
        result = after(test_node)
        assert expected == result

    test_after3()

    def test_prev():
        test_list = {"head": None}
        add_first(test_list, 11)
        add_first(test_list, 9)
        add_first(test_list, 6)
        add_first(test_list, 4)
        add_first(test_list, 1)
        test_node = get_item_at(test_list, 3)
        test_node2 = get_item_at(test_list, 2)
        expected = test_node2
        result = prev(test_node)
        assert expected == result

    test_prev()

    def test_prev2():
        test_list = {"head": None}
        add_first(test_list, 2)
        test_node = get_first(test_list)
        expected = None
        result = prev(test_node)
        assert expected == result

    test_prev2()

    def test_prev3():
        test_list = {"head": None}
        add_first(test_list, None)
        test_node = get_first(test_list)
        expected = None
        result = prev(test_node)
        assert expected == result

    test_prev3()


test()
