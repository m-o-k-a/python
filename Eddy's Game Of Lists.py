# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 15:30:25 2018
Version 1.0 on Fri Dec 14 16:29:58 2018
Version 1.1 on Fri Dec 14 18:07:10 2018 - seed update
@author: Eddy
"""
#Eddy's Game of lists
#STEP 0: DEPENDENCIES AND EXPLAIN
from random import randint
import os
stop_simulation = True
print("Eddy's Game of lists is a simple edit of Conway's Game of life where the world isn't infinite but finite and round. You can show your own survive or birth rate and see the evolution of your world.")
while stop_simulation:
    generation = 0

#STEP 1: SIZE
    generation_max = int(input("Max Generation: \n>>"))
    grid_rows = int(input("Rows of the grid: \n>>"))
    grid_columns = int(input("Columns of the grid: \n>>"))
    survive_rate = int(input("[SURIVVE RATE]\nHow Many 1 need to be near the cell to survive: \n>> "))
    survive_type = int(input("[SURVIVE TYPE]\n(0)Same neighbour as survive_rate\n(1)Minimum neighbour as survive_rate\n(2)Maximum neighbour as survive_rate\n>> "))
    survive_type = survive_type%3
            
#STEP 2: CREATING
    grid = []
    for r in range(0, grid_rows):
        next_row = []
        for c in range(0, grid_columns):
           next_row.append(0)
        grid.append(next_row)
            
#STEP 3: SETTING POSITION 
    to_fill = True
    while to_fill:
        print("Setting Generation 0:\n")
        for g in range(0, grid_rows):
            print(grid[g], end="\n")
        grid_fill = str(input("Filling:\n(c)clear\n(r)random\n(m)manual\n(s)seed\n(b)begin\n>>"))
        #CLEAR FILL
        if grid_fill == "c" or grid_fill == "C":
            for r in range(0, grid_rows):
                for c in range(0, grid_columns):
                    grid[r][c] = 0
        #RANDOM FILL
        if grid_fill == "r" or grid_fill == "R":
            seed = ""
            grid = []
            for r in range(0, grid_rows):
                next_row = []
                for c in range(0, grid_columns):
                    random_value = randint(0, 1)
                    seed += str(random_value)
                    next_row.append(random_value)
                grid.append(next_row)
            print("Seed: ", seed)
        #SEED FILL
        if grid_fill == "s"  or grid_fill == "S":
            seed = input("Seed work columns by columns, ex: 010000 will, on a 3*3 world, only had the cell on the first row second columns living.\nWrite your seed here (if the seed is too long it will only use the part in the range of the size of the world): \n>>")
            position = 0
            for r in range(0, grid_rows):
                for c in range(0, grid_columns):
                    grid[r][c] = int(seed[position])
                    position += 1
        #MANUAL
        if grid_fill == "m"  or grid_fill == "M":
            fill_row = int(input("Rows of the grid to fill: \n>>"))
            fill_column = int(input("Columns of the grid to fill: \n>>"))
            grid[fill_row][fill_column] = 1
        #BEGIN
        if grid_fill == "b"  or grid_fill == "B":
            gen0_life = 0
            gen0_death = 0
            to_fill = False
            for r in range(0, grid_rows):
                for c in range(0, grid_columns):
                    if grid[r][c] == 1:
                        gen0_life += 1;
                    if grid[r][c] == 0:
                        gen0_death += 1;
#STEP 4: CREATING NEXT LIST
    next_grid = []
    for r in range(0, grid_rows):
        next_row = []
        for c in range(0, grid_columns):
            next_row.append(0)
        next_grid.append(next_row)
            
#STEP5: RUNNING
    to_run = True
    while to_run:
        generation += 1
        print("Generation " + str(generation) + " :\n")
    #STEP 5.1: UPDATE
        for r in range(0, grid_rows):
            survive = 0
            for c in range(0, grid_columns):
                survive = 0
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        try: # left columns
                            if grid[r+x][c+y] == 1:
                                survive += 1
                        except:
                            1+1
                survive -= 1 #*because it count himself
                #check survive
                if survive == survive_rate and grid[r][c] == 0 and survive_type != 2: #come alive
                    next_grid[r][c] = 1
                elif (survive == survive_rate) and grid[r][c] == 1: #survive
                    next_grid[r][c] = 1
                elif survive > survive_rate and grid[r][c] == 1 and survive_type != 1: #die
                    next_grid[r][c] = 0
                elif survive > survive_rate and grid[r][c] == 1 and survive_type == 1: #live
                    next_grid[r][c] = 1
                if survive <= survive_rate and survive_type == 2: #come alive
                    next_grid[r][c] = 1
                else: #die
                    next_grid[r][c] = 0
                
        if generation >= generation_max:
            to_run = False
        grid = next_grid
        for g in range(0, grid_rows):
            print(grid[g], end="\n")
        os.system("pause")
    genX_life = 0
    genX_death = 0
    to_fill = False
    for r in range(0, grid_rows):
        for c in range(0, grid_columns):
            if grid[r][c] == 1:
                genX_life += 1;
            if grid[r][c] == 0:
                genX_death += 1;
    #print value
    if gen0_death == 0:
        print("END OF SIMULATION\n", "Generation 0 population was:\n", "Living Cells:", str(gen0_life), "Dead Cells:", str(gen0_death),"\n")
    else:
        print("END OF SIMULATION\n", "Generation 0 population was:\n", "Living Cells:", str(gen0_life), "Dead Cells:", str(gen0_death),"\n life per dead:", str(gen0_life/gen0_death))
    if genX_death == 0:
        print("Generation", str(generation_max), "population is:\n", "Living Cells:", str(genX_life), "Dead Cells:", str(genX_death),"\n")
    else:
        print("Generation", str(generation_max), "population is:\n", "Living Cells:", str(genX_life), "Dead Cells:", str(genX_death),"\n life per dead:", str(genX_life/genX_death))
    
#STEP 6: reload
    reload = str(input("Generation Succesfully ended.\n Want to start a new one(Any Key) or stop(F) ?\n>>"))
    if reload == "F" or reload == "f":
        stop_simulation = False
print("Thanks for using Eddy's Game of Lists!")
