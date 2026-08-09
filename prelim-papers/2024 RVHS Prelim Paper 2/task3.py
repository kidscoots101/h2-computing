import random
import time
import copy

#Task 3.1
def create_puzzle(n):
    array = [[None for x in range(n)] for _ in range(n)]
    numbers = [x for x in range((n**2))]
    random.shuffle(numbers) #Shuffle numbers
    for i in range(0, n): #Inserts shuffled numbers 
        for k in range(0, n):
            array[i][k] = numbers[(n*i)+k]
            if numbers[(n*i)+k] == 0:
                zero = [i, k]
            
    return array, zero[0], zero[1]

#Task 3.2
def display_puzzle(puzzle):
    display_puzzle = copy.deepcopy(puzzle)
    indexes = "   ".join([str(x) for x in range(len(display_puzzle))])
    indexes = "    " + indexes
    print(indexes)
    for v in range(len(display_puzzle)):
        if 0 in display_puzzle[v]:
            display_puzzle[v][display_puzzle[v].index(0)] = "#"
        row = [str(v)] + list(map(lambda x: str(x), display_puzzle[v]))
        print("   ".join(row))

#Task 3.3
def find_available_move(puzzle, r, c):
    n = len(puzzle)
    if r == 0:
        return(['R', 'D', 'L'])
    elif r == (n-1):
        return(['U', 'R', 'L'])
    elif c == 0:
        return(['U', 'R', 'D'])
    elif c == (n-1):
        return(['U', 'D', 'L'])
    else:
        return(['U', 'R', 'D', 'L'])

#Task 3.4
def make_move(move, puzzle, r, c):
    if move == "U":
        puzzle[r][c], puzzle[r-1][c] = puzzle[r-1][c], puzzle[r][c]
        return puzzle, r-1, c
    elif move == "R":
        print(puzzle[r])
        puzzle[r][c], puzzle[r][c+1] = puzzle[r][c+1], puzzle[r][c]
        return puzzle, r, c+1
    elif move == "D":
            puzzle[r][c], puzzle[r+1][c] = puzzle[r+1][c], puzzle[r][c]
            return puzzle, r+1, c
    elif move == "L":
            puzzle[r][c], puzzle[r][c-1] = puzzle[r][c-1], puzzle[r][c]
            return puzzle, r, c-1

#Task 3.5
def win(puzzle):
    for i in puzzle:
        print("here", puzzle)
        if 0 in i:
            i = copy.deepcopy(i)
            i[i.index(0)] = 99999999999
        if sorted(i) != i:
            return False

    return True

def game_menu():
    puzzle = [[2,3,5],[1,0,4],[7,8,6]]
    r, c = 1, 1
    time_start = time.time()
    while True:
        print(display_puzzle(puzzle))
        
        print("Menu Options: [1] New game, [2] Make one move, [3] Make many moves, [3] Quit")
        option = int(input("Choose an option: "))
        while option not in [1, 2, 3, 4]:
            print("Invalid")
            option = int(input("Choose an option: "))
            
        if option == 1:
            n = int(input("Choose a puzzle size from 3 to 5"))
            puzzle, r, c = create_puzzle(n)
            time_start = time.time()
            
        elif option == 2:
            print(find_available_move(puzzle, r, c))
            move = input("Choose your move: ")
            puzzle, r, c = make_move(move, puzzle, r, c)
            if win(puzzle):
                return f"You took {time.time() - time_start}s to win"
            
        elif option == 3:
            print(find_available_move(puzzle, r, c))
            move = input("Choose your moves: ")
            moves = list(move)
            og_puzzle = copy.deepcopy(puzzle)
            for j in moves:
                avail_moves = find_available_move(puzzle, r, c)
                print(avail_moves, "there")
                if j not in avail_moves:
                    puzzle = og_puzzle
                    break
                else:
                    puzzle, r, c = make_move(j, puzzle, r, c)
                    if win(puzzle):
                        return f"You took {time.time() - time_start}s to win"

        else:
            return f"You took {time.time() - time_start}s to give up"

print(game_menu())
    