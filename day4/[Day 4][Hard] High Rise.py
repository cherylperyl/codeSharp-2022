# Question:
# In a 7x7 grid, we want to place buildings in each square given some clues.

# Below are some requirements to solving the 7x7 puzzle.
# - The height of a building is between 1 and 7
# - No two buildings in a row or a column may have the same number of floors
# - Taller buldings block the view of shorter buildings located behind them


clues1 = [3, 1, 5, 5, 4, 2, 3, 3, 2, 1, 2, 3, 3, 5, 3, 4, 2, 2, 2, 2, 1, 1, 2, 3, 4, 4, 5, 2]
clues2 = [6, 4, 0, 2, 0, 0, 3, 0, 3, 3, 3, 0, 0, 4, 0, 5, 0, 5, 0, 2, 0, 0, 0, 0, 4, 0, 0, 3]

clues2_sol = "2 1 6 4 3 7 5 \
                3 2 5 7 4 6 1 \
                4 6 7 5 1 2 3 \
                1 3 2 6 7 5 4 \
                5 7 1 3 2 4 6 \
                6 4 3 2 5 1 7 \
                7 5 4 1 6 3 2"