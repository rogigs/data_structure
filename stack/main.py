from stack import Stack

if __name__ == "__main__":
    stack = Stack()
    print(len(stack))

    stack.push(3)
    stack.push("python")
    stack.push(2)
    stack.push(1.2)
    print(stack)

    print(stack)
    print(stack.peek())
    stack.pop()
    print(stack.peek())
