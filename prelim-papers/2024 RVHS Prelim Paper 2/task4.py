import csv

#Task 4.1
class Contestant():
    def __init__(self, name, time):
        self.name = name
        self.time = float(time)

    def __str__(self, start="S"):
        temp_name = self.name.replace(" ", "")
        if len(temp_name)<8:
            return start+"-"+(temp_name).upper()+(8-len(temp_name))*"_"+"("+str(round(self.time, 2))+"s)"
        else:
            return start+"-"+(temp_name[:8]).upper()+"("+str(round(self.time, 2))+"s)"

class Beginner(Contestant):
    def __init__(self, name, time, practice_hour):
        super().__init__(name, time)
        self.practice_hour = practice_hour

    def __str__(self):
            return super().__str__("B")

class Professional(Contestant):
    def __init__(self, name, time, competitions_won):
        super().__init__(name, time)
        self.practice_hour = competitions_won

    def __str__(self):
            return super().__str__("P")

print(str(Contestant("ChanChan Chan",35.01)))
print(str(Beginner("Li uLi uLi u",55.54, 300)))
print(str(Professional("OhOhOh",6.34, 60))) 

#Task 4.2
def readfile(filename: str):
    array = []
    with open(filename, "r") as f:
        s = list(csv.reader(f))
        for row in s:
            if row[0][0] == "P":
                array.append(Professional(row[1], row[2], row[3]))
            elif row[0][0] == "B":
                array.append(Beginner(row[1], row[2], row[3]))

    return array

print(readfile("rubik.txt"))

#Task 4.3
class Node:
    def __init__(self, new_player):
        self.player = new_player
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def Insert(self, player):
        node = Node(player)
        if self.root == None:
            self.root = node
        else:
            curr = self.root
            while True:
                if node.player.time < curr.player.time:
                    if curr.player.left == None:
                        curr.player.left = node
                        break
                    else:
                        curr = curr.player.left
                else:
                    if curr.player.right == None:
                        curr.player.right = node
                        break
                    else:
                        curr = curr.player.right

    def inorder(self, curr=None):
        if curr == None:
            if self.root == None:
                return "There are no nodes in the tree"
            else:
                curr=self.root
        if curr is not None:
            print(self.inorder(curr.player.left))
            print(str(curr.player))
            print(self.inorder(curr.player.right))

    def count_professtional(self, curr=None):
        if curr == None:
            if self.root == None:
                return "There are no nodes in the tree"
            else:
                curr=self.root
        if curr is not None:
            if str(curr.player)[0] == "P":
                value = self.count_professtional(curr.player.left)+1
                return value + self.count_professtional(curr.player.right)
            else:
                value = self.count_professtional(curr.player.left)
                return value + self.count_professtional(curr.player.right)

    def find_best_beginner(self):
        