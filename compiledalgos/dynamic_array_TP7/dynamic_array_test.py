from dynamic_array import DynamicArray

def test_append_and_len():
    arr = DynamicArray()
    assert len(arr) == 0
    arr.append(10)
    arr.append(20)
    arr.append(30)
    assert len(arr) == 3
    assert arr[0] == 10
    assert arr[1] == 20
    assert arr[2] == 30

def test_getitem_out_of_bounds():
    arr = DynamicArray()
    arr.append(1)
    try:
        _ = arr[1]
        assert False, "IndexError not raised"
    except IndexError:
        pass

def test_resize():
    arr = DynamicArray()
    for i in range(100):
        arr.append(i)
    assert len(arr) == 100
    for i in range(100):
        assert arr[i] == i


test_append_and_len()
print("test_append_and_len passed")
test_getitem_out_of_bounds()
print("test_getitem_out_of_bounds passed")
test_resize()
print("test_resize passed")