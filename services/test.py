class Stack:
    top = None

    def push(self, obj):
        if not Stack.top:
            Stack.top = obj
        else:
            cur_obj = Stack.top
            while cur_obj.next:
                cur_obj = cur_obj.next
            cur_obj.set_next(obj)

    def pop(self):
        if not Stack.top:
            print('Список пуст')
        else:
            if not Stack.top.next:
                Stack.top = None
            else:
                cur_obj = Stack.top
                while cur_obj.next:
                    if not cur_obj.next.next:
                        cur_obj.set_next(None)
                    else:
                        cur_obj = cur_obj.next

    def get_data(self):
        data_list = []
        if not Stack.top:
            print('Список пуст')
        else:
            cur_obj = Stack.top
            data_list.append(cur_obj.data)
            while cur_obj.next:
                cur_obj = cur_obj.next
                data_list.append(cur_obj.data)
            print(data_list)


class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data

    def set_next(self, next_obj):
        if isinstance(next_obj, StackObj) or next_obj is None:
            self.__next = next_obj

    def get_next(self):
        return self.__next

    data = property(get_data, set_data)
    next = property(get_next, set_next)


st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st.push(StackObj("obj4"))
st.push(StackObj("obj5"))
st.push(StackObj("obj6"))

st.pop()
st.pop()
st.pop()
st.pop()
st.pop()
st.pop()
st.pop()

st.get_data()