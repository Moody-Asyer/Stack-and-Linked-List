def remove_first(linked_list):
    current_head = linked_list["head"]
    linked_list["head"] = current_head["next"]
    return linked_list


def remove_last(linked_list):
    current_head = linked_list["head"]
    prev = None
    while current_head != None:
        if current_head["next"] == None:
            prev["next"] = None
            current_head = None
        else:
            prev = current_head
            current_head = current_head["next"]
    return linked_list


def remove_item_at(linked_list, index):
    current_head = linked_list["head"]
    count = 0
    prev = None
    while count != index:
        prev = current_head
        current_head = current_head["next"]
        count += 1
    if count == index:
        if current_head["next"] == None:
            remove_first(linked_list)
        else:
            prev["next"] = current_head["next"]
    return linked_list


def add_first(linked_list, data):
    current_head = linked_list["head"]
    new_node = {
        "data": data,
        "next": current_head
    }
    linked_list["head"] = new_node
    return linked_list


def add_last(linked_list, data):
    new_node = {
        "data": data,
        "next": None
    }
    current_head = linked_list["head"]
    if current_head == None:
        add_first(linked_list, data)
    while current_head != None:
        if current_head["next"] == None:
            current_head["next"] = new_node
            current_head = None
        else:
            current_head = current_head["next"]
    return linked_list


def add_item_at(linked_list, data, index):
    current_head = linked_list["head"]
    count = 0
    new_node = {
        "data": data,
        "next": None
    }

    if index == 0:
        add_first(linked_list, data)
    else:
        while count != index - 1:
            current_head = current_head["next"]
            count += 1
        if count == index - 1:
            new_node["next"] = current_head["next"]
            current_head["next"] = new_node
    return linked_list


def get_first(linked_list):
    current_head = linked_list["head"]
    return current_head


def get_last(linked_list):
    current_head = linked_list["head"]
    while current_head["next"] != None:
        current_head = current_head["next"]
    return current_head


def get_item_at(linked_list, index):
    current_head = linked_list["head"]
    count = 0
    while count < index:
        current_head = current_head["next"]
        count += 1
    else:
        return current_head


def print_linked_list(linked_list):
    current_head = linked_list["head"]
    print_list = ""
    while current_head is not None:
        data = current_head["data"]
        print_list = print_list + ("%s-->") % data
        current_head = current_head["next"]

    print_list = print_list + "None"
    return print_list


def prev(linked_list, data):
    current_head = linked_list["head"]
    while current_head is not None:
        if current_head["next"]["data"] == data:
            return current_head
        else:
            current_head = current_head["next"]


def after(linked_list, data):
    current_head = linked_list["head"]
    while current_head is not None:
        if current_head["data"] == data:
            return current_head["next"]
        else:
            current_head = current_head["next"]


def size(linked_list):
    current_head = linked_list["head"]
    length = 0
    if current_head == None:
        return length
    while current_head is not None:
        length += 1
        current_head = current_head["next"]
    return length


list = {
    "head": None
}

add_first(list, 5)
add_first(list, 4)
add_first(list, 3)
add_first(list, 2)
add_last(list, 6)
add_last(list, 7)
add_last(list, 8)
add_last(list, 9)
remove_first(list)
remove_last(list)
remove_item_at(list, 3)
add_item_at(list, 6, 3)
print(print_linked_list(list))
print(list)
print(get_first(list))
print(get_last(list))
print(get_item_at(list, 2))
print(prev(list, 5))
print(after(list, 6))
print(size(list))


def test():
    assert {'head': {'data': 5, 'next': None}} == add_first({'head': None}, 5)
    assert {'head': {'data': 3, 'next': {'data': 5, 'next': None}}} == add_first({'head': {'data': 5, 'next': None}}, 3)
    assert {'head': {'data': None, 'next': None}} == add_first({'head': None}, None)

    assert {'head': {'data': 3, 'next': {'data': 5, 'next': None}}} == add_last({'head': {'data': 3, 'next': None}}, 5)
    assert {'head': {'data': 5, 'next': None}} == add_last({'head': None}, 5)
    assert {'head': {'data': None, 'next': None}} == add_last({'head': None}, None)

    assert {'head': {'data': 2,
                     'next': {'data': 4, 'next': {'data': 5, 'next': {'data': 7, 'next': None}}}}} == add_item_at(
        {'head': {'data': 2, 'next': {'data': 4, 'next': {'data': 7, 'next': None}}}}, 5, 2)
    assert {'head': {'data': 5, 'next': None}} == add_item_at({'head': None}, 5, 0)

    assert {'head': {'data': 5, 'next': None}} == remove_first({'head': {'data': 3, 'next': {'data': 5, 'next': None}}})
    assert {'head': None} == remove_first({'head': {'data': 5, 'next': None}})

    assert {'head': {'data': 2, 'next': {'data': 4, 'next': None}}} == remove_last(
        {'head': {'data': 2, 'next': {'data': 4, 'next': {'data': 5, 'next': None}}}})
    assert {'head': None} == remove_last({'head': None})

    assert {'head': {'data': 2, 'next': {'data': 4, 'next': {'data': 7, 'next': None}}}} == remove_item_at(
        {'head': {'data': 2, 'next': {'data': 4, 'next': {'data': 5, 'next': {'data': 7, 'next': None}}}}}, 2)
    assert {'head': None} == remove_item_at({'head': {'data': 4, 'next': None}}, 0)

    assert None == get_first({'head': None})
    assert {'data': 2, 'next': {'data': 4, 'next': {'data': 7, 'next': None}}} == get_first(
        {'head': {'data': 2, 'next': {'data': 4, 'next': {'data': 7, 'next': None}}}})

    assert {'data': 7, 'next': None} == get_last(
        {'head': {'data': 2, 'next': {'data': 4, 'next': {'data': 7, 'next': None}}}})
    assert {'data': 7, 'next': None} == get_last({'head': {'data': 7, 'next': None}})

    assert {'data': 5, 'next': {'data': 7, 'next': None}} == get_item_at(
        {'head': {'data': 2, 'next': {'data': 4, 'next': {'data': 5, 'next': {'data': 7, 'next': None}}}}}, 2)
    assert None == get_item_at({'head': None}, 0)

    assert {'data': 4, 'next': {'data': 5, 'next': {'data': 7, 'next': None}}} == prev(
        {'head': {'data': 2, 'next': {'data': 4, 'next': {'data': 5, 'next': {'data': 7, 'next': None}}}}}, 5)
    assert None == prev({'head': None}, None)

    assert {'data': 5, 'next': {'data': 7, 'next': None}} == after(
        {'head': {'data': 2, 'next': {'data': 4, 'next': {'data': 5, 'next': {'data': 7, 'next': None}}}}}, 4)
    assert None == after({'head': None}, None)
    assert None == after({'head': {'data': 4, 'next': None}}, 4)

    assert "3-->None" == print_linked_list({"head": {"data": 3, "next": None}})
    assert "2-->4-->5-->6-->None" == print_linked_list(
        {'head': {'data': 2, 'next': {'data': 4, 'next': {'data': 5, 'next': {'data': 6, 'next': None}}}}})
    assert "None" == print_linked_list({"head": None})

    assert 6 == size({'head': {'data': 2, 'next': {'data': 4, 'next': {'data': 5, 'next': {'data': 7,
                                                                                           'next': {'data': 9,
                                                                                                    'next': {'data': 10,
                                                                                                             'next': None}}}}}}})


test()
