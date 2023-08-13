import math
import random

column_A = ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z']
column_B = ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z']
column_C = ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z']

# Game over boolean
game_over = False

# Credit
credit = 100

# Cost of a spin
cost_to_play = 1

# Main loop
def main_loop():
    global column_A, column_B, column_C, credit, game_over 
    count = 0

    while not game_over and credit > cost_to_play:
        first_num = random.randint(0, 9)
        second_num = random.randint(0, 9)
        third_num = random.randint(0, 9)
        print(column_A[first_num], column_B[second_num], column_C[third_num])
        if first_num == second_num and second_num == third_num:
            game_over = True
            print("You have won!")
        credit -= 1
        count += 1
        print(count)
    
    game_over = True



if __name__ == '__main__':
    main_loop()



    




