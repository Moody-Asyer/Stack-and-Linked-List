length = 8
array_length = [None] * length


def hash(data):
    nilai_hash = data % 3
    return nilai_hash


def insert(keys, data):
    index = hash(data)
    value = keys[index]
    if value is None:
        keys[index] = data
    else:
        while value is not None:
            if index == 7:
                return "Full"
            elif value == "Deleted":
                value = data
                break
            else:
                index += 1
                value = keys[index]
        keys[index] = data
    return keys


def delete(keys, data):
    index = hash(data)
    value = keys[index]
    if value is None:
        return keys
    while value is not None:
        if value == data:
            keys[index] = "Deleted"
            break
        else:
            index += 1
            if index > 7:
                return keys
            else:
                value = keys[index]
    return keys


def search(keys, data):
    found = False
    if keys is None:
        return found
    else:
        for angka in keys:
            if angka == data:
                found = True
        return found


def vacum(keys):
    length = 8
    temp_array = [None] * length
    for angka in keys:
        if angka != "Deleted":
            if angka == None:
                pass
            else:
                insert(temp_array, angka)
        else:
            pass
    return temp_array


insert(array_length, 4)
insert(array_length, 6)
insert(array_length, 8)
insert(array_length, 12)
insert(array_length, 9)
insert(array_length, 10)
insert(array_length, 7)
insert(array_length, 5)
delete(array_length, 7)
delete(array_length, 12)
delete(array_length, 15)
print(search(array_length, 9))
print(search(array_length, 99))
print(array_length)
insert(array_length,11)
print(array_length)
print(vacum(array_length))


def test():
    assert [None, 4, None, None, None, None, None, None] == insert([None, None, None, None, None, None, None, None], 4)
    assert [3, None, None, None, None, None, None, None] == insert([None, None, None, None, None, None, None, None], 3)
    assert [None, None, 5, None, None, None, None, None] == insert([None, None, None, None, None, None, None, None], 5)
    assert [3, 1, 2, 4, None, None, None, None] == insert([3, 1, 2, None, None, None, None, None], 4)
    assert "Full" == insert([3, 1, 2, 4, 5, 6, 7, 8], 9)
    assert [3, 1, 2, 4, 5, 6, 7, 8] == insert([3, 1, 2, 4, 5, 6, "Deleted", 8], 7)

    assert [3, 1, 2, 4, 5, 6, 7, 8] == delete([3, 1, 2, 4, 5, 6, 7, 8], 12)
    assert [None, None, None, None, None, None, None, None] == delete([None, None, None, None, None, None, None, None],
                                                                      1)
    assert [3, 1, 2, 4, 5, "Deleted", 7, 8] == delete([3, 1, 2, 4, 5, 6, 7, 8], 6)

    assert False == search([None, None, None, None, None, None, None, None], 5)
    assert False == search([3, 1, 2, 4, 5, 6, 7, 8], 11)
    assert True == search([3, 1, 2, 4, 5, 6, 7, 8], 4)

    assert [3, 1, 2, 4, 5, 7, 8, None] == vacum([3, 1, 2, 4, 5, "Deleted", 7, 8])
    assert [None, None, None, None, None, None, None, None] == vacum(
        [None, "Deleted", "Deleted", "Deleted", "Deleted", "Deleted", "Deleted", "Deleted"])
    assert [3, 7, 5, None, None, None, None, None] == vacum([3, "Deleted", "Deleted", "Deleted", 5, 7, "Deleted", None])


test()

# Keuntungan Open addressing dibanding chaining selain dari pada tidak ada array yang kosong adalah:
# 1.Open addressing menggunakan/menyimpan memori data lebih sedikit dibanding dengan chaining yang menggunakan banyak memori.
# 2.Jumlah isi data dalam array dari Open addressing bersifat tetap, tidak seperti chaining yang bisa bertambah terus tapi-
# tidak efisien karena kemungkinan adanya perbedaan isi data pada tiap index array ataupun ada array yang kosong.
# 3.Adanya shadow delete membantu untuk menunjukkan mana index array yang kosong karena telah dihapus dan bisa diisi lagi-
# dengan data baru.
# 4.Ketika mencari data tidak perlu looping berkali-kali.
# 5.Adanya fungsi vacum yang bisa merapikan kembali atau mengurutkan element pada array.