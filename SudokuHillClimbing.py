import random                           
from collections import defaultdict    
from collections import Counter       

SHC_conflicts_puzzle = [[0 for _ in range(9)] for _ in range(9)]  
# puzzle = [   
#         [0, 9, 6, 1, 5, 7, 0, 3, 0],
#         [0, 1, 8, 0, 0, 6, 7, 0, 0],
#         [0, 0, 3, 2, 0, 0, 1, 0, 0],
#         [5, 3, 1, 6, 0, 0, 0, 0, 4],
#         [6, 0, 0, 8, 0, 0, 0, 5, 0],
#         [0, 0, 0, 5, 0, 9, 0, 0, 3],
#         [9, 0, 0, 0, 1, 0, 3, 0, 8],
#         [0, 8, 5, 7, 6, 0, 0, 2, 0],
#         [0, 7, 0, 9, 0, 8, 5, 6, 0]
#     ]

def SHC_generate_initial_solution(puzzle):
    initial_solution = [row[:] for row in puzzle]   
    occurrences = Counter(num for row in puzzle for num in row if num != 0)   

    for i in range(9):
        for j in range(9):
            if initial_solution[i][j] == 0:   
                available_numbers = [num for num in range(1, 10) if occurrences[num] < 9]   
                num = random.choice(available_numbers)   
                initial_solution[i][j] = num   
                occurrences[num] += 1   

    return initial_solution   

# def SHC_print_puzzle(puzzle):
#     for row in puzzle:
#         print(" ".join(str(num) for num in row))   


def SHC_count_conflicts(puzzle):
    for row in range(9):
        for col in range(9):
            num = 0  
                
            for i in range(9):
                if puzzle[row][i] == puzzle[row][col] and i != col:
                    num += 1
                
            for j in range(9):
                if puzzle[j][col] == puzzle[row][col] and j != row:
                    num += 1
                
            start_row, start_col = 3 * (row // 3), 3 * (col // 3)  
            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    if puzzle[i][j] == puzzle[row][col] and (i != row or j != col):
                        num += 1

            SHC_conflicts_puzzle[row][col] = num
    
    return SHC_conflicts_puzzle  


def SHC_hill_climbing(puzzle):

    initial_puzzle = SHC_generate_initial_solution(puzzle)   
    #SHC_print_puzzle(initialPuzzle)

    max_iterations = 500000   
    current_puzzle = [row[:] for row in initial_puzzle]   
    conflicts_puzzle = SHC_count_conflicts(current_puzzle)  
    
    tabu_list = defaultdict(int)  
    restart_counter = 0
    
    for iteration in range(max_iterations):
        max_conflicts = 0   
        max_conflicts_cells = []   
        
        for i in range(9):
            for j in range(9):
                conflicts = conflicts_puzzle[i][j]   
                
                if conflicts > max_conflicts and (i, j) not in tabu_list:
                    max_conflicts = conflicts   
                    max_conflicts_cells = [(i, j)]   
                elif conflicts == max_conflicts and (i, j) not in tabu_list:
                    max_conflicts_cells.append((i, j))   
        
        if len(max_conflicts_cells) < 2:
            continue
        
        first_cell, second_cell = random.sample(max_conflicts_cells, 2)
        row1, col1 = first_cell
        row2, col2 = second_cell
        
        current_puzzle[row1][col1], current_puzzle[row2][col2] = current_puzzle[row2][col2], current_puzzle[row1][col1]
        
        tabu_list[first_cell] += 1
        tabu_list[second_cell] += 1
        
        total_conflicts = sum(sum(row) for row in conflicts_puzzle)
        if total_conflicts == 0:
            return current_puzzle  
        
        # Restart after every 2500 iterations
        restart_counter += 1
        if restart_counter == 2500:
            #print("Restart puzzle \n")
            initial_puzzle = SHC_generate_initial_solution(puzzle)
            current_puzzle = [row[:] for row in puzzle]
            conflicts_puzzle = SHC_count_conflicts(current_puzzle)
            tabu_list = defaultdict(int)
            restart_counter = 0
    
    return None  


def SHC_run(puzzle):
    #print("Initial Sudoku puzzle:")   
    #SHC_print_puzzle(puzzle)
    #print("\n")   

    solved_puzzle = SHC_hill_climbing(puzzle)   

    if solved_puzzle is not None:
        print("\nSolved Sudoku puzzle:")   
        #SHC_print_puzzle(solved_puzzle)
    else:
        print("\nFailed to solve")   

#SHC_run()
