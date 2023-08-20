import sys
import random
import pygame

# Initialize pygame
pygame.init()

window_width, window_height = 640, 480
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Slots by Vuk')

# Make changes to the lists so that they contain the right amount of specific symbols
# 1st list should contain 21 symbols
# 2nd list should contain 24 symbols
# 3rd list should contain 23 symbols 
"""
    There will be 7 different symbols that can be drawn from the lists:
    7 - Seven
    B - Bar
    W - Watermellon
    R - Ring(bell)
    P - Plum
    L - Lemon
    C - Cherry
    Each of the lists should contain a combination of these symbols in the next order:
    Column_A = [(7 x 1), (B x 3), (W x 2), (R x 1), (P x 7) (L x 5), (C x 2)]
    Column_B = [(7 x 1), (B x 2), (W x 2), (R x 5), (P x 3), (L x 5), (C x 6)]
    Column_C = [(7 x 1), (B x 1), (W x 2), (R x 8), (P x 3), (L x 4), (C x 0)]
"""


# Column_A after changes
column_A = ['7', 'B', 'B', 'B', 'W', 'W', 'R', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'L', 'L', 'L', 'L', 'L', 'C', 'C'] # 21 Characters
# Column_B after changes
column_B = ['7', 'B', 'B', 'W', 'W', 'R', 'R', 'R', 'R', 'R', 'P', 'P', 'P', 'L', 'L', 'L', 'L', 'L', 'C', 'C', 'C', 'C', 'C', 'C'] # 24 Characters
# Column_C after changes
column_C = ['7', 'B', 'W', 'W', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'P', 'P', 'P', 'L', 'L', 'L', 'L', 'C', 'C', 'C', 'C'] # 23 characters

# Game over boolean
game_over = False

# Credit
credit = 1

# Bet
bet = 3

# Add font to the game
font = pygame.font.Font(None, 36)
font_big = pygame.font.Font(None, 72)
font_medium = pygame.font.Font(None, 52)

# Mouse
mouse = pygame.mouse.get_pos()

# Cost of a spin
cost_to_play = 1

padding = 30

# Basic colors
black = (0, 0, 0)
background_color = (244, 242, 222)
fields_color = (31, 110, 140)
white = (255, 255, 255)
game_over_color = (255, 0, 0)

clock = pygame.time.Clock()

# Write a function that will display a button while the game is running which will influence the amount of BET user shooses, 1,3 or 5
def bet_amount():
    global bet
    # Every time the user clicks on the button the bet should move one step up: from 1 to 3, from 3 to 5, from 5 to 1
    for event in pygame.event.get():
          
        if event.type == pygame.QUIT:
            pygame.quit()
              
        #checks if a mouse is clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
              
            #if the mouse is clicked on the
            # button the game is terminated
            if window_width/2 <= mouse[0] <= window_width/2+140 and window_height/2 <= mouse[1] <= window_height/2+40:
                pygame.quit()



# Create a new function that will check the combination that the random generators got and adjust the prize accordingly
def combination_check(combination):
    global credit, bet
    # If the bet BET amount is 1
    if bet == 1:
        if combination[0] == '7' and combination[1] == '7' and combination[2] == '7':
            credit += 200
            print('jackpot')
        elif combination[0] == 'B' and combination[1] == 'B' and combination[2] == 'B':
            credit += 100
            print('jackpot')
        elif combination[0] == 'W' and combination[1] == 'W' and combination[2] == 'W':
            credit += 100
            print('jackpot')
        elif combination[0] == 'W' and combination[1] == 'W' and combination[2] == 'B':
            credit += 100
            print('jackpot')
        elif combination[0] == 'R' and combination[1] == 'R' and combination[2] == 'R':
            credit += 18
        elif combination[0] == 'R' and combination[1] == 'R' and combination[2] == 'B':
            credit += 18
        elif combination[0] == 'P' and combination[1] == 'P' and combination[2] == 'P':
            credit += 14
        elif combination[0] == 'P' and combination[1] == 'P' and combination[2] == 'B':
            credit += 14
        elif combination[0] == 'L' and combination[1] == 'L' and combination[2] == 'L':
            credit += 10
        elif combination[0] == 'L' and combination[1] == 'L' and combination[2] == 'B':
            credit += 10
        elif combination[0] == 'C' and combination[1] == 'C' and combination[2] == 'C':
            credit += 5
        elif combination[0] == 'C' and combination[1] in column_B and combination[2] in column_C:
            credit += 2
    elif bet == 3:
        if combination[0] == '7' and combination[1] == '7' and combination[2] == '7':
            credit += 600
            print('jackpot')
        elif combination[0] == 'B' and combination[1] == 'B' and combination[2] == 'B':
            credit += 300
            print('jackpot')
        elif combination[0] == 'W' and combination[1] == 'W' and combination[2] == 'W':
            credit += 300
            print('jackpot')
        elif combination[0] == 'W' and combination[1] == 'W' and combination[2] == 'B':
            credit += 300
            print('jackpot')
        elif combination[0] == 'R' and combination[1] == 'R' and combination[2] == 'R':
            credit += 54
        elif combination[0] == 'R' and combination[1] == 'R' and combination[2] == 'B':
            credit += 54
        elif combination[0] == 'P' and combination[1] == 'P' and combination[2] == 'P':
            credit += 42
        elif combination[0] == 'P' and combination[1] == 'P' and combination[2] == 'B':
            credit += 42
        elif combination[0] == 'L' and combination[1] == 'L' and combination[2] == 'L':
            credit += 30
        elif combination[0] == 'L' and combination[1] == 'L' and combination[2] == 'B':
            credit += 30
        elif combination[0] == 'C' and combination[1] == 'C' and combination[2] == 'C':
            credit += 15
        elif combination[0] == 'C' and combination[1] in column_B and combination[2] in column_C:
            credit += 6

    elif bet == 5:
        if combination[0] == '7' and combination[1] == '7' and combination[2] == '7':
            credit += 1000
            print('jackpot')
        elif combination[0] == 'B' and combination[1] == 'B' and combination[2] == 'B':
            credit += 500
            print('jackpot')
        elif combination[0] == 'W' and combination[1] == 'W' and combination[2] == 'W':
            credit += 500
            print('jackpot')
        elif combination[0] == 'W' and combination[1] == 'W' and combination[2] == 'B':
            credit += 500
            print('jackpot')
        elif combination[0] == 'R' and combination[1] == 'R' and combination[2] == 'R':
            credit += 90
        elif combination[0] == 'R' and combination[1] == 'R' and combination[2] == 'B':
            credit += 90
        elif combination[0] == 'P' and combination[1] == 'P' and combination[2] == 'P':
            credit += 60
        elif combination[0] == 'P' and combination[1] == 'P' and combination[2] == 'B':
            credit += 60
        elif combination[0] == 'L' and combination[1] == 'L' and combination[2] == 'L':
            credit += 50
        elif combination[0] == 'L' and combination[1] == 'L' and combination[2] == 'B':
            credit += 50
        elif combination[0] == 'C' and combination[1] == 'C' and combination[2] == 'C':
            credit += 25
        elif combination[0] == 'C' and combination[1] in column_B and combination[2] in column_C:
            credit += 10


# Function that runs before the main loop, asking the user for the amount of credit they will risk
def ask_for_credit():
    global credit, padding, bet
    # Values for the bottom rect that will ask for the amount of credit
    user_input = ''
    input_rect_y = window_height / 2 - 60
    input_rect_x = window_width / 2 - 100
    input_rect = pygame.Rect(input_rect_x, input_rect_y, 200, 120)
    
    while credit <= 1 and credit >= 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                # Check for backspace
                if event.key == pygame.K_BACKSPACE:
                    # get text input from 0 to -1 i.e. end.
                    user_input = user_input[:-1]
                # Unicode standard is used for string
                # formation
                else:
                    user_input += event.unicode
                if event.key == pygame.K_RETURN:  # Check for ENTER key
                        try:
                            credit = int(user_input)
                            return credit  # Convert user_input to an integer
                        except ValueError:
                            # Handle invalid input (e.g., non-integer values)
                            pass
                        
        window.fill(background_color)
        # Draw the first rect that displays the message
        user_message = font_medium.render("Input the amount of credit", True, fields_color)
        user_message_rect = user_message.get_rect(center=(window_width // 2, user_message.get_height() // 2))
        user_message_rect.y += padding
        

        window.blit(user_message, user_message_rect)
        pygame.display.update()
        
        # Draw the second rect that takes the input
        pygame.draw.rect(window, fields_color, input_rect)
        text_surface = font_big.render(user_input, True, white)
        window.blit(text_surface, ((input_rect.x + (input_rect.width - text_surface.get_width()) // 2), input_rect.y + (input_rect.height - text_surface.get_height()) // 2))

        pygame.display.update()
        clock.tick(60)
        
# A function that will display the values from the spin to the screen
def display_values(value_text, border_size):
    # Add padding and a border
    global padding
    window.fill(background_color)
    # Changed from the original code font.render(value_text, True, white)
    slot_text = font_big.render(value_text, True, white)
    # Create a larger surface to generate the combination
    slot_width = 200
    slot_height = 120
    slot_text_with_borders = pygame.Surface((slot_width, slot_height), pygame.SRCALPHA)
    slot_text_with_borders.fill(fields_color)

    pygame.draw.rect(slot_text_with_borders, fields_color, slot_text_with_borders.get_rect(), border_size)
    
    slot_text_with_borders.blit(slot_text, ((slot_width / 2 - slot_text.get_width() / 2), (slot_height / 2 - slot_text.get_height() / 2)))

    slot_text_rect = slot_text_with_borders.get_rect(center=(window_width // 2, window_height // 2))
    window.blit(slot_text_with_borders, slot_text_rect)

# A function that displays the users remeindeing credit
def credit_left(credit):
    global cost_to_play, padding
    current_credit = str(credit)
    credit_text = font.render("Credit: " + current_credit + " $", True, fields_color)

    credit_text_rect = credit_text.get_rect(center=(window_width // 2, window_height - credit_text.get_height() // 2))
    credit_text_rect.y -= padding
    
    window.blit(credit_text, credit_text_rect)
    pygame.display.update()

# A function that that returns true if the player choses to spin one more time
def another_spin():
    global game_over, padding
    # Update the screen to show the message 'Another spin?'
    message = font.render('Press SPACE to spin again', True, fields_color)
    message_rect = message.get_rect(center=(window_width // 2, message.get_height() // 2))
    message_rect.y += padding
    window.blit(message, message_rect)
    pygame.display.update()
    
    # Set a timer for the duration of the message
    message_duration = 60000 #miliseconds
    start_time = pygame.time.get_ticks()
    while pygame.time.get_ticks() - start_time < message_duration:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True
    return False

# Main loop
def main_loop():
    global column_A, column_B, column_C, credit, game_over 
    border_size = 0

    while not game_over:
        ask_for_credit()
        while credit > cost_to_play:
            # The ability to quit the game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    sys.exit()
            # Draw a button that will trigger the bet_amount() function
            button_wodth = 100
            button_height = 70
            
            
            # New values for the random numbers from each of the lists
            first_num = random.randint(0, len(column_A) - 1)
            second_num = random.randint(0, len(column_B) - 1)
            third_num = random.randint(0, len(column_C) - 1)
            # 1 / 1000 probability of winning
            combination = column_A[first_num] + column_B[second_num] + column_C[third_num]
            if len(combination) > 3:
                print(combination)
            
            display_values(combination, border_size)
            credit_left(credit)

            """
                Introduce the new reward system of the game, the symbols drawn should be paying the next amounts of credit:
                Bet = 1:
                7-7-7 = 200
                B-B-B = 100
                W-W-W = 100
                W-W-B = 100
                R-R-R = 18
                R-R-B = 18
                F-F-F = 14
                F-F-B = 14
                L-L-L = 10
                L-L-B = 10
                C-C-ANY = 5
                C-ANY-ANY = 2
                The values above will change depending on the amount of BET the player has selected, there will be 3 levels of the BET amount:
                1, 3, 5
                Each of the bet amount multiplies the winnings by the amount of reward based on BET 1:
                BET 1: 7-7-7 = 200; BET 3: 7-7-7 = 600; BET 5: 7-7-7 = 1000
            """
            # Invoke the combination_check function
            combination_check(combination)
                
            # Invoke the another_spin() function that will determine the next spin
            if not another_spin():
                break
            # Reduce the amount of credit acording to the amount of BET
            if bet == 1:
                credit -= 1
            elif bet == 3:
                credit -= 3
            elif bet == 5:
                credit -= 5
        
        game_over = True

if __name__ == '__main__':
    main_loop()



    




