import sys
import random
import pygame

# Initialize pygame
pygame.init()

window_width, window_height = 450, 330
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
column_B = ['7', 'B', 'B', 'W', 'W', 'R', 'R', 'R', 'R', 'R' 'P', 'P', 'P', 'L', 'L', 'L', 'L', 'L', 'C', 'C', 'C', 'C', 'C', 'C'] # 24 Characters
column_C = ['7', 'B', 'W', 'W', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R' 'P', 'P', 'P', 'L', 'L', 'L', 'L', 'C', 'C', 'C', 'C'] # 23 characters

# Game over boolean
game_over = False

# Credit
credit = 1

# Add font to the game
font = pygame.font.Font(None, 36)

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

# Function that runs before the main loop, asking the user for the amount of credit they will risk
def ask_for_credit():
    global credit, padding
    # Values for the bottom rect that will ask for the amount of credit
    user_input = ''
    input_rect_y = window_height - (window_height // 2)
    input_rect_x = (window_width // 2) - 45
    input_rect = pygame.Rect(input_rect_x, input_rect_y, 100, 32)
    
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
        user_message = font.render("Input the amount of credit", True, fields_color)
        user_message_rect = user_message.get_rect(center=(window_width // 2, user_message.get_height() // 2))
        user_message_rect.y += padding

        window.blit(user_message, user_message_rect)
        pygame.display.update()
        
        # Draw the second rect that takes the input
        pygame.draw.rect(window, fields_color, input_rect)
        text_surface = font.render(user_input, True, white)
        window.blit(text_surface, input_rect)

        pygame.display.update()
        clock.tick(60)
        
# A function that will display the values from the spin to the screen
def display_values(value_text, border_size):
    # Add padding and a border
    global padding
    window.fill(background_color)

    slot_text = font.render(value_text, True, white)

    # Create a larger surface to generate the combination
    slot_width = slot_text.get_width() + 2 * (padding + border_size)
    slot_height = slot_text.get_height() + 2 * (padding + border_size)
    slot_text_with_borders = pygame.Surface((slot_width, slot_height), pygame.SRCALPHA)
    slot_text_with_borders.fill(fields_color)

    pygame.draw.rect(slot_text_with_borders, fields_color, slot_text_with_borders.get_rect(), border_size)
    
    slot_text_with_borders.blit(slot_text, (padding + border_size, padding + border_size))

    slot_text_rect = slot_text_with_borders.get_rect(center=(window_width // 2, window_height // 2))
    window.blit(slot_text_with_borders, slot_text_rect)

# A function that displays the users remeindeing credit
def credit_left(credit):
    global cost_to_play, padding
    current_credit = str(credit)
    credit_text = font.render("Credit: " + current_credit, True, fields_color)

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
            
            first_num = random.randint(0, 9)
            second_num = random.randint(0, 9)
            third_num = random.randint(0, 9)
            # 1 / 1000 probability of winning
            combination = column_A[first_num] + column_B[second_num] + column_C[third_num]
            
            display_values(combination, border_size)
            credit_left(credit)
            
            if first_num == second_num and second_num == third_num:
                
                print("You have won!")
                credit += 300
                
            # Invoke the another_spin() function that will determine the next spin
            if not another_spin():
                break
            credit -= 1
        
        game_over = True

if __name__ == '__main__':
    main_loop()



    




