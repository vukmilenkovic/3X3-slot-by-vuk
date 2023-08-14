import sys
import random
import pygame

# Initialize pygame
pygame.init()

window_width, window_height = 640, 480
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Slots by Vuk')



column_A = ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z']
column_B = ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z']
column_C = ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z']

# Game over boolean
game_over = False

# Credit
credit = 20

# Add font to the game
font = pygame.font.Font(None, 36)

# Cost of a spin
cost_to_play = 1

# Basic colors
black = (0, 0, 0)
white = (255, 255, 255)
game_over_color = (255, 0, 0)

# A function that will display the values from the spin to the screen
def display_values(value_text, border_size):
    # Add padding and a border
    padding = 30
    
    window.fill(black)

    slot_text = font.render(value_text, True, white)

    # Create a larger surface to generate the combination
    slot_width = slot_text.get_width() + 2 * (padding + border_size)
    slot_height = slot_text.get_height() + 2 * (padding + border_size)
    slot_text_with_borders = pygame.Surface((slot_width, slot_height), pygame.SRCALPHA)

    pygame.draw.rect(slot_text_with_borders, white, slot_text_with_borders.get_rect(), border_size)

    slot_text_with_borders.blit(slot_text, (padding + border_size, padding + border_size))

    slot_text_rect = slot_text_with_borders.get_rect(center=(window_width // 2, window_height // 2))
    window.blit(slot_text_with_borders, slot_text_rect)



# A function that that returns true if the player choses to spin one more time
def another_spin():
    global game_over
    # Update the screen to show the message 'Another spin?'
    message = font.render('Another spin?', True, white)
    message_rect = message.get_rect(center=(window_width // 2, window_height - message.get_height() //2))
    window.blit(message, message_rect)
    pygame.display.update()
    
    # Set a timer for the duration of the message, let it be 20 seconds
    message_duration = 20000
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
    count = 0
    border_size = 4
    while not game_over and credit > cost_to_play:
        # The ability to quit the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                sys.exit()

        first_num = random.randint(0, 9)
        second_num = random.randint(0, 9)
        third_num = random.randint(0, 9)

        combination = column_A[first_num] + column_B[second_num] + column_C[third_num]
        display_values(combination, border_size)
        if first_num == second_num and second_num == third_num:
            game_over = True
            print("You have won!")
        
        # Invoke the another_spin() function that will determine the next spin
        if not another_spin():
            break
        credit -= 1
        count += 1
        print(count)
    
    game_over = True



if __name__ == '__main__':
    main_loop()



    




