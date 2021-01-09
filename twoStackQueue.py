class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def fillStack2(self):
        if len(self.stack2) == 0 and len(self.stack1) > 0:
            while len(self.stack1) > 0:
                tmp = self.stack1.pop()
                self.stack2.append(tmp)

    def enqueue(self, item):
        self.stack1.append(item)
        self.fillStack2()

    def dequeue(self):
        if len(self.stack2) > 0:
            tmp = self.stack2.pop()
            return tmp
        else:
            self.fillStack2()
            if len(self.stack2) > 0:
                tmp = self.stack2.pop()
                return tmp
            else:
                return None

    def print(self):
        if len(self.stack2) > 0:
            print(self.stack2[len(self.stack2)-1])
        else:
            self.fillStack2()
            if len(self.stack2) > 0:
                print(self.stack2[len(self.stack2) - 1])


if __name__ == "__main__":
    q = Queue()
    f = open("input02.txt", "r")
    lines = f.readlines()
    #n = int(input())
    for line in lines:
        userInput = line.rstrip('\n')
        answer = userInput.split(" ")
        if answer[0] == "1":
            q.enqueue(answer[1])
        elif answer[0] == "2":
            q.dequeue()
        elif answer[0] == "3":
            #print(str(q.stack1) + " " + str(q.stack2))
            q.print()
        #n = n -1