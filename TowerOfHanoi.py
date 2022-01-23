# Hayden Michael
# 10/31/19
# CSC 310
# Uses array stacks to simulate the tower of hanoi problem with a given size


# uses the ArrayStack class to hold the disks
class ArrayStack:

    def __init__(self):
        self._data = []  # nonpublic list instance

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)  # new item stored at end of list

    def top(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return self._data[-1]  # the last item in the list

    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return self._data.pop()  # remove last item from list


# initializes all of the stacks
A = ArrayStack()
B = ArrayStack()
C = ArrayStack()


# recursive method simulating tower of hanoi with given size n
def TowerOfHanoi(n, from_peg, aux_peg, to_peg):
    if n == 1:  # base case
        # There are many if conditions to work with the stacks
        if from_peg == "A" and to_peg == "C":
            print("Move disk " + str(A.top()) + " from peg", from_peg, "to peg", to_peg)
            C.push(A.pop())
        elif from_peg == "A" and to_peg == "B":
            print("Move disk " + str(A.top()) + " from peg", from_peg, "to peg", to_peg)
            B.push(A.pop())
        elif from_peg == "B" and to_peg == "A":
            print("Move disk " + str(B.top()) + " from peg", from_peg, "to peg", to_peg)
            A.push(B.pop())
        elif from_peg == "B" and to_peg == "C":
            print("Move disk " + str(B.top()) + " from peg", from_peg, "to peg", to_peg)
            C.push(B.pop())
        elif from_peg == "C" and to_peg == "A":
            print("Move disk " + str(C.top()) + " from peg", from_peg, "to peg", to_peg)
            A.push(C.pop())
        elif from_peg == "C" and to_peg == "B":
            print("Move disk " + str(C.top()) + " from peg", from_peg, "to peg", to_peg)
            B.push(C.pop())
        return
    TowerOfHanoi(n - 1, from_peg, to_peg, aux_peg)
    if from_peg == "A" and to_peg == "C":
        print("Move disk " + str(A.top()) + " from peg", from_peg, "to peg", to_peg)
        C.push(A.pop())
    elif from_peg == "A" and to_peg == "B":
        print("Move disk " + str(A.top()) + " from peg", from_peg, "to peg", to_peg)
        B.push(A.pop())
    elif from_peg == "B" and to_peg == "A":
        print("Move disk " + str(B.top()) + " from peg", from_peg, "to peg", to_peg)
        A.push(B.pop())
    elif from_peg == "B" and to_peg == "C":
        print("Move disk " + str(B.top()) + " from peg", from_peg, "to peg", to_peg)
        C.push(B.pop())
    elif from_peg == "C" and to_peg == "A":
        print("Move disk " + str(C.top()) + " from peg", from_peg, "to peg", to_peg)
        A.push(C.pop())
    elif from_peg == "C" and to_peg == "B":
        print("Move disk " + str(C.top()) + " from peg", from_peg, "to peg", to_peg)
        B.push(C.pop())
    TowerOfHanoi(n - 1, aux_peg, from_peg, to_peg)


# Allows the user to enter the amount of disks to try.
# Then the disks will be pushed onto the first stack.
# Finally, the tower of hanoi method is called with the number of disks.
print("Enter the amount of disks: ")
disks = int(input())
i = disks  # need i variable to decrement current disk
while i > 0:
    A.push(i)
    i -= 1
TowerOfHanoi(disks, 'A', 'B', 'C')
