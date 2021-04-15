class stack:
    def __init__(self):
        self.stack_items = []

    # isEmpty 기능 구현
    def is_empty(self):
        return not self.stack_items

    # pop 기능 구현
    def pop(self):
        item_length = len(self.stack_items)
        # 스택이 비어있을때는 에러메세지 출력
        if self.is_empty():
            print("Stack is empty!")
            return False

        # 가장 위에 있는 item 반환하며 삭제
        result = self.stack_items[item_length - 1]
        del self.stack_items[item_length - 1]
        return result

    # push 기능 구현
    def push(self, x):
        self.stack_items.append(x)


stack = stack()
stack.push(1)
stack.push(2)
stack.pop()
stack.pop()
stack.pop()