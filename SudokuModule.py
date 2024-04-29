import time
import random
import math
import statistics
from collections import defaultdict    
from collections import Counter  
import SudokuSimulatedAnnealing as SSA
import SudokuBacktracking as SBT
import SudokuHillClimbing as SHC 

easy_sudoku = [[   
    [0, 9, 6, 1, 5, 7, 0, 3, 0],
    [0, 1, 8, 0, 0, 6, 7, 0, 0],
    [0, 0, 3, 2, 0, 0, 1, 0, 0],
    [5, 3, 1, 6, 0, 0, 0, 0, 4],
    [6, 0, 0, 8, 0, 0, 0, 5, 0],
    [0, 0, 0, 5, 0, 9, 0, 0, 3],
    [9, 0, 0, 0, 1, 0, 3, 0, 8],
    [0, 8, 5, 7, 6, 0, 0, 2, 0],
    [0, 7, 0, 9, 0, 8, 5, 6, 0]
],
[
    [0, 0, 2, 0, 0, 0, 0, 5, 0],
    [0, 0, 0, 4, 0, 3, 0, 0, 8],
    [8, 0, 3, 0, 0, 0, 0, 7, 0],
    [0, 2, 0, 0, 9, 0, 6, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 6, 0, 5, 0, 0, 3, 0],
    [0, 1, 0, 0, 0, 0, 9, 0, 7],
    [0, 0, 0, 2, 0, 7, 0, 0, 0],
    [4, 0, 0, 0, 0, 0, 2, 0, 0]
],
[
    [0, 0, 2, 0, 0, 0, 0, 5, 0],
    [0, 0, 0, 4, 0, 3, 0, 0, 8],
    [8, 0, 3, 0, 0, 0, 0, 7, 0],
    [0, 2, 0, 0, 9, 0, 6, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 6, 0, 5, 0, 0, 3, 0],
    [0, 1, 0, 0, 0, 0, 9, 0, 7],
    [0, 0, 0, 2, 0, 7, 0, 0, 0],
    [4, 0, 0, 0, 0, 0, 2, 0, 0]
],
[
    [0, 0, 2, 0, 0, 0, 0, 5, 0],
    [0, 0, 0, 4, 0, 3, 0, 0, 8],
    [8, 0, 3, 0, 0, 0, 0, 7, 0],
    [0, 2, 0, 0, 9, 0, 6, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 6, 0, 5, 0, 0, 3, 0],
    [0, 1, 0, 0, 0, 0, 9, 0, 7],
    [0, 0, 0, 2, 0, 7, 0, 0, 0],
    [4, 0, 0, 0, 0, 0, 2, 0, 0]
],
[
    [0, 0, 2, 0, 0, 0, 0, 5, 0],
    [0, 0, 0, 4, 0, 3, 0, 0, 8],
    [8, 0, 3, 0, 0, 0, 0, 7, 0],
    [0, 2, 0, 0, 9, 0, 6, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 6, 0, 5, 0, 0, 3, 0],
    [0, 1, 0, 0, 0, 0, 9, 0, 7],
    [0, 0, 0, 2, 0, 7, 0, 0, 0],
    [4, 0, 0, 0, 0, 0, 2, 0, 0]
]]

medium_sudoku = [[
    [0, 7, 3, 2, 0, 4, 6, 9, 1],
    [0, 2, 8, 0, 0, 6, 0, 0, 7],
    [0, 0, 6, 1, 0, 7, 0, 0, 8],
    [0, 1, 5, 7, 6, 3, 0, 2, 4],
    [6, 0, 0, 0, 0, 0, 8, 7, 0],
    [7, 0, 0, 9, 0, 0, 0, 0, 0],
    [3, 0, 1, 6, 0, 0, 0, 0, 0],
    [2, 8, 0, 5, 4, 9, 3, 0, 0],
    [0, 6, 0, 8, 0, 0, 0, 0, 0]
    ],
    [
    [0, 0, 0, 0, 4, 0, 0, 7, 0],
    [0, 8, 0, 0, 0, 3, 4, 0, 0],
    [0, 7, 0, 0, 9, 8, 5, 6, 0],
    [4, 9, 6, 0, 0, 0, 8, 0, 2],
    [7, 0, 0, 0, 0, 4, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [5, 0, 1, 7, 0, 2, 9, 8, 0],
    [0, 0, 0, 3, 8, 1, 2, 0, 0],
    [0, 0, 0, 4, 0, 0, 6, 0, 3]
    ],
    [
    [4, 8, 0, 0, 0, 0, 0, 6, 3],
    [0, 0, 0, 0, 3, 0, 4, 2, 0],
    [0, 0, 2, 0, 0, 1, 0, 0, 0],
    [0, 5, 4, 0, 8, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 4, 0, 0, 6],
    [2, 1, 0, 0, 0, 3, 9, 0, 0],
    [0, 0, 0, 5, 1, 0, 0, 8, 0],
    [0, 4, 3, 2, 7, 0, 6, 9, 1],
    [1, 7, 8, 3, 9, 0, 5, 4, 0]
    ],
    [
    [4, 0, 0, 1, 5, 7, 0, 3, 2],
    [2, 0, 0, 0, 0, 0, 0, 0, 5],
    [0, 0, 3, 0, 0, 0, 1, 9, 0],
    [5, 0, 0, 0, 0, 0, 1, 9, 0],
    [0, 0, 9, 0, 3, 1, 2, 5, 7],
    [8, 0, 0, 5, 4, 0, 0, 1, 0],
    [0, 0, 2, 4, 1, 5, 0, 0, 8],
    [0, 8, 0, 7, 6, 3, 4, 0, 9],
    [0, 0, 0, 9, 2, 8, 0, 6, 0]
    ],
    [
    [0, 0, 8, 0, 0, 0, 0, 6, 0],
    [0, 0, 0, 0, 2, 8, 7, 0, 0],
    [5, 2, 0, 7, 0, 1, 0, 0, 0],
    [2, 0, 7, 6, 1, 4, 3, 0, 8],
    [3, 6, 5, 0, 9, 2, 4, 0, 7],
    [0, 0, 0, 5, 0, 0, 6, 0, 9],
    [9, 0, 2, 0, 0, 0, 5, 4, 0],
    [0, 0, 0, 1, 0, 0, 2, 0, 0],
    [6, 8, 0, 0, 0, 4, 0, 7, 0]
    ],
]

hard_sudoku = [
    [
    [1, 7, 0, 0, 0, 0, 0, 0, 6],
    [3, 6, 0, 0, 0, 0, 1, 0, 0],
    [2, 0, 0, 1, 0, 9, 0, 7, 0],
    [0, 3, 6, 0, 0, 0, 8, 1, 0],
    [4, 5, 0, 3, 0, 7, 0, 0, 0],
    [0, 8, 0, 5, 0, 0, 7, 0, 0],
    [0, 0, 4, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 2, 0, 0, 4, 0, 0],
    [0, 2, 0, 9, 0, 8, 0, 5, 0]
    ],
    [
    [0, 8, 0, 7, 0, 0, 0, 0, 6],
    [0, 0, 0, 2, 0, 0, 0, 4, 0],
    [7, 5, 1, 4, 9, 0, 0, 3, 0],
    [0, 0, 4, 0, 6, 0, 3, 0, 8],
    [3, 0, 0, 1, 0, 5, 4, 0, 0],
    [0, 0, 0, 0, 0, 4, 5, 6, 0],
    [0, 7, 0, 0, 0, 0, 0, 0, 0],
    [0, 3, 8, 0, 4, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 7, 6, 1, 0]
    ],
    [
    [5, 0, 0, 0, 0, 9, 1, 0, 0],
    [0, 0, 0, 0, 6, 2, 5, 0, 8],
    [0, 1, 0, 0, 0, 8, 7, 6, 4],
    [0, 6, 5, 0, 1, 3, 0, 2, 0],
    [2, 4, 0, 0, 0, 7, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 7, 0, 0, 0, 0, 0, 5, 6],
    [0, 5, 8, 7, 0, 0, 3, 0, 0],
    [0, 0, 0, 0, 4, 0, 8, 0, 0]
    ],
    [
    [0, 0, 0, 0, 6, 8, 9, 0, 3],
    [0, 1, 0, 3, 0, 2, 0, 8, 0],
    [0, 0, 0, 0, 0, 0, 0, 5, 0],
    [8, 0, 0, 9, 0, 0, 0, 4, 0],
    [3, 0, 0, 8, 0, 0, 7, 0, 0],
    [2, 5, 6, 4, 7, 3, 8, 9, 0],
    [1, 3, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 6, 0],
    [7, 0, 4, 0, 1, 9, 0, 0, 0]
    ],
    [
    [9, 0, 0, 1, 7, 5, 0, 0, 0],
    [1, 0, 0, 3, 0, 9, 0, 0, 0],
    [5, 7, 3, 0, 0, 8, 0, 0, 0],
    [0, 9, 0, 0, 5, 1, 3, 7, 0],
    [0, 1, 0, 0, 3, 6, 4, 0, 9],
    [0, 0, 0, 0, 0, 0, 5, 0, 1],
    [0, 0, 0, 6, 2, 0, 0, 8, 0],
    [0, 0, 7, 0, 9, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 0, 5, 0]
    ]
]

expert_sudoku = [
    [
    [0, 0, 0, 0, 0, 2, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 1, 0, 0],
    [2, 0, 0, 0, 0, 4, 0, 3, 0],
    [0, 6, 8, 0, 0, 0, 9, 0, 0],
    [3, 0, 0, 0, 1, 0, 6, 8, 0],
    [0, 0, 0, 0, 0, 3, 0, 5, 0],
    [0, 5, 0, 0, 0, 9, 7, 0, 6],
    [0, 2, 0, 0, 7, 0, 0, 0, 0],
    [0, 0, 3, 0, 0, 0, 0, 9, 0]
    ],
    [
    [0, 0, 6, 0, 0, 0, 0, 7, 0],
    [8, 0, 0, 0, 0, 0, 0, 4, 6],
    [0, 0, 5, 3, 9, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 3, 0, 1],
    [2, 0, 7, 0, 0, 0, 0, 6, 9],
    [0, 0, 0, 5, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 9, 7, 0, 0, 0, 1, 5],
    [0, 6, 0, 0, 2, 8, 0, 0, 0]
    ],
    [
    [0, 0, 0, 2, 0, 0, 0, 0, 1],
    [0, 2, 8, 0, 0, 0, 9, 0, 0],
    [0, 0, 0, 0, 5, 0, 3, 0, 0],
    [4, 0, 0, 3, 0, 0, 0, 5, 0],
    [7, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 4, 7],
    [0, 0, 0, 5, 7, 4, 0, 0, 0],
    [9, 0, 6, 0, 0, 3, 0, 0, 0],
    [0, 0, 6, 0, 0, 1, 0, 0, 0]
    ],
    [
    [5, 0, 8, 4, 2, 7, 0, 0, 0],
    [0, 4, 0, 0, 1, 0, 7, 0, 0],
    [1, 9, 0, 0, 0, 3, 0, 0, 2],
    [0, 0, 0, 0, 6, 0, 0, 0, 5],
    [7, 0, 0, 0, 0, 0, 2, 0, 0],
    [6, 0, 5, 1, 3, 0, 9, 0, 0],
    [9, 0, 0, 0, 0, 0, 1, 5, 0],
    [0, 0, 0, 0, 4, 0, 0, 2, 0],
    [0, 7, 0, 0, 0, 0, 0, 0, 8]
    ],
    [
    [2, 0, 0, 0, 0, 7, 0, 4, 0],
    [9, 0, 0, 0, 0, 8, 0, 0, 0],
    [0, 0, 3, 0, 0, 6, 7, 8, 0],
    [0, 0, 9, 4, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 9, 0, 8],
    [1, 0, 0, 5, 0, 0, 0, 3, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [3, 0, 0, 2, 0, 0, 0, 7, 0],
    [0, 6, 0, 0, 0, 4, 0, 1, 0]
    ]
]


# """ SBT """
# SBT_easy_start_time = time.time()
# for puzzle in easy_sudoku:
#     print("run")
#     SBT.SBT_run(puzzle)
# SBT_easy_end_time = time.time()

# SBT_medium_start_time = time.time()
# for puzzle in medium_sudoku:
#     print("run")
#     SBT.SBT_run(puzzle)
# SBT_medium_end_time = time.time()

# SBT_hard_start_time = time.time()
# for puzzle in hard_sudoku:
#     print("run")
#     SBT.SBT_run(puzzle)
# SBT_hard_end_time = time.time()

# SBT_expert_start_time = time.time()
# for puzzle in expert_sudoku:
#     print("run")
#     SBT.SBT_run(puzzle)
# SBT_expert_end_time = time.time()
# print("\n\n\n")


# """ SHC """
# SHC_easy_start_time = time.time()
# for puzzle in easy_sudoku:
#     print("run")
#     SHC.SHC_run(puzzle)
# SHC_easy_end_time = time.time()

# SHC_medium_start_time = time.time()
# for puzzle in medium_sudoku:
#     print("run")
#     SHC.SHC_run(puzzle)
# SHC_medium_end_time = time.time()

# SHC_hard_start_time = time.time()
# for puzzle in hard_sudoku:
#     print("run")
#     SHC.SHC_run(puzzle)
# SHC_hard_end_time = time.time()

# SHC_expert_start_time = time.time()
# for puzzle in expert_sudoku:
#     print("run")
#     SHC.SHC_run(puzzle)
# SHC_expert_end_time = time.time()
# print("\n\n\n")


""" SSA"""
SSA_easy_start_time = time.time()
for puzzle in easy_sudoku:
    print("run")
    SSA.SSA_run(puzzle)
SSA_easy_end_time = time.time()

SSA_medium_start_time = time.time()
for puzzle in medium_sudoku:
    print("run")
    SSA.SSA_run(puzzle)
SSA_medium_end_time = time.time()

SSA_hard_start_time = time.time()
for puzzle in hard_sudoku:
    print("run")
    SSA.SSA_run(puzzle)
SSA_hard_end_time = time.time()

SSA_expert_start_time = time.time()
for puzzle in expert_sudoku:
    print("run")
    SSA.SSA_run(puzzle)
SSA_expert_end_time = time.time()
print("\n\n\n")

# SBT_easy_elapsed_time = SBT_easy_end_time - SBT_easy_start_time
# SBT_medium_elapsed_time = SBT_medium_end_time - SBT_medium_start_time
# SBT_hard_elapsed_time = SBT_hard_end_time - SBT_hard_start_time
# SBT_expert_elapsed_time = SBT_expert_end_time - SBT_expert_start_time

# SHC_easy_elapsed_time = SHC_easy_end_time - SHC_easy_start_time
# SHC_medium_elapsed_time = SHC_medium_end_time - SHC_medium_start_time
# SHC_hard_elapsed_time = SHC_hard_end_time - SHC_hard_start_time
# SHC_expert_elapsed_time = SHC_expert_end_time - SHC_expert_start_time

SSA_easy_elapsed_time = SSA_easy_end_time - SSA_easy_start_time
SSA_medium_elapsed_time = SSA_medium_end_time - SSA_medium_start_time
SSA_hard_elapsed_time = SSA_hard_end_time - SSA_hard_start_time
SSA_expert_elapsed_time = SSA_expert_end_time - SSA_expert_start_time

# print("SBT Easy Elapsed Time", SBT_easy_elapsed_time, "SBT Medium Elapsed Time", SBT_medium_elapsed_time, "SBT Hard Elapsed Time", SBT_hard_elapsed_time, "SBT Expert Elapsed Time", SBT_expert_elapsed_time,)
# print("SHC Easy Elapsed Time", SHC_easy_elapsed_time, "SHC Medium Elapsed Time", SHC_medium_elapsed_time, "SHC Hard Elapsed Time", SHC_hard_elapsed_time, "SHC Expert Elapsed Time", SHC_expert_elapsed_time,)
print("SSA Easy Elapsed Time", SSA_easy_elapsed_time, "SSA Medium Elapsed Time", SSA_medium_elapsed_time, "SSA Hard Elapsed Time", SSA_hard_elapsed_time, "SSA Expert Elapsed Time", SSA_expert_elapsed_time,)
