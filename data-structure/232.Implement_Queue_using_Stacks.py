# Example 1:


# Input
e1 = ["MyQueue", "push", "push", "peek", "pop", "empty"]
q1 = [[], [1], [2], [], [], []]
# Output
# [null, null, null, 1, 1, false]


# Explanation
# MyQueue myQueue = new MyQueue();
# myQueue.push(1); // queue is: [1]
# myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
# myQueue.peek(); // return 1
# myQueue.pop(); // return 1, queue is [2]
# myQueue.empty(); // return false

class MyQueue:

    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output.pop()

    def peek(self) -> int:
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self) -> bool:
        return not (self.input or self.output)


# Your MyQueue object will be instantiated and called as such:
obj = None
print("[", end=" ")
for i in range(len(e1)):
    cmd = e1[i]
    element = q1[i]
    if cmd == "MyQueue":
        obj = MyQueue()
        print("None", end = " ")
    elif cmd == "push":
        obj.push(element[0])
        print("None", end = " ")
    elif cmd == "peek":
       print(obj.peek(), end = " ")
    elif cmd == "pop":
        print(obj.pop(), end = " ")
    elif cmd == "empty":
        print(obj.empty(), end = " ")

print("]")