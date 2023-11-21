import pygame
import sys
import random
import time

# Initialize Pygame
pygame.init()

# Initialize Music,
pygame.mixer.init()
pygame.mixer.music.load(r"C:\Users\user\Downloads\bgmusic.mp3")
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1)

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Words and Clues
word_clue_pairs = [
    ("apple", ["Fruit", "Red", "Juicy", "Healthy"]),
    ("tiger", ["Animal", "Striped", "Roar", "Wild"]),
    ("violin", ["Instrument", "Strings", "Bowed", "Classical"]),
    ("france", ["Country", "Eiffel Tower", "Baguette", "European"]),
    ("bicycle", ["Vehicle", "Two Wheels", "Pedals", "Transport"]),
    ("mars", ["Planet", "Red", "Martian", "Space"]),
    ("computer", ["Digital", "Electronic", "Games", "Coding"]),
    ("happy", ["Joyful", "Cheerful", "Content", "Smiling"]),
    ("cat", ["Pet", "Furry", "Meow", "Whiskers"]),
    ("garden", ["Plants", "Flowers", "Outdoors", "Green"]),
    ("ocean", ["Water", "Blue", "Wave", "Fish"]),
    ("book", ["Reading", "Pages", "Story", "Library"]),
    ("sleep", ["Rest", "Night", "Dream", "Bed"]),
    ("friend", ["Companion", "Pal", "Buddy", "Company"]),
    ("sun", ["Sky", "Daylight", "Warmth", "Brightness"]),
    ("cake", ["Dessert", "Sweet", "Celebration", "Yummy"]),
    ("tree", ["Wood", "Leaves", "Branches", "Nature"]),
    ("color", ["Hue", "Paint", "Rainbow", "Palette"]),
    ("music", ["Sound", "Melody", "Rhythm", "Instrument"]),
    ("flower", ["Blossom", "Petals", "Garden", "Fragrant"]),
    ("star", ["Sky", "Night", "Twinkle", "Celestial"]),
    ("rainbow", ["Colors", "Arc", "Sky", "Spectrum"]),
    ("laugh", ["Joy", "Happiness", "Giggle", "Humor"]),
    ("mountain", ["Peak", "Climb", "Summit", "Hike"]),
    ("butterfly", ["Insect", "Wings", "Flutter", "Metamorphosis"]),
    ("adventure", ["Exciting", "Journey", "Explore", "Quest"]),
    ("puzzle", ["Game", "Problem", "Challenge", "Solution"]),
    ("sunset", ["Evening", "Sun", "Horizon", "Dusk"]),
    ("candle", ["Flame", "Light", "Wax", "Aroma"]),
    ("oxygen", ["Gas", "Breath", "Air", "Life"]),
    ("serenade", ["Music", "Romantic", "Singing", "Love"]),
    # Add more word and clue pairs here
]

# Define the score-task dictionary
score_tasks = {
    0: "Chat with your crush",
    10: "Dance a silly dance",
    20: "Sing a song in a funny voice",
    30: "Tell a joke to a friend",
    40: "Sing your favorite song",
    50: "Tell your parents you love them",
    60: "Hug someone special to you",
    70: "Draw a funny doodle",
    80: "Share a fun fact with someone",
    90: "Do 10 jumping jacks",
    100: "Take a selfie doing a funny pose",
    110: "Write a short poem",
    120: "Send a virtual hug to a friend",
    130: "Do a random act of kindness",
    140: "Create a funny meme and share it",
    150: "Tell a short story using three words at a time with a friend",
    160: "Learn a simple magic trick and perform it",
    170: "Cook a new recipe and share a picture",
    180: "Make up a funny song about the last thing you did",
    190: "Create a fictional superhero with a silly power",
    200: "Do a 5-minute stand-up comedy routine for someone",
    210: "Make a list of 10 things that make you laugh",
    220: "Share a favorite childhood memory with a friend",
    230: "Do a one-minute interpretive dance",
    240: "Send a virtual high-five to someone",
    250: "Write a short comedy skit and perform it",
    260: "Compose a funny limerick",
    270: "Do your best impression of a famous person",
    280: "Send a funny GIF to a friend",
    290: "Create a funny nickname for yourself and use it for a day",
    300: "Record a short video of yourself doing a funny talent",
    # Add more score-task pairs as needed
}

# Pygame setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("4 Clues, 1 Word Game")

# Logo
game_logo = pygame.image.load(r"C:\Users\user\Downloads\logo.png")
game_logo = pygame.transform.scale(game_logo, (WIDTH, HEIGHT))
game_logo_rect = game_logo.get_rect(topleft=(0, 0))

# Background
game_bg = pygame.image.load(r"C:\Users\user\Downloads\background.png")
game_bg = pygame.transform.scale(game_bg, (WIDTH, HEIGHT))
game_bg_rect = game_bg.get_rect(topleft=(0, 0))

# Finish
finish_bg = pygame.image.load(r"C:\Users\user\Downloads\FINISH.png")
finish_bg = pygame.transform.scale(finish_bg, (WIDTH, HEIGHT))
finish_bg_rect = finish_bg.get_rect(topleft=(0, 0))

#Wrong
wrong = pygame.image.load(r"C:\Users\user\Downloads\wrong.png")
wrong = pygame.transform.scale(wrong, (WIDTH, HEIGHT))
wrong_rect = wrong.get_rect(topleft=(0, 0))

# Fonts
font = pygame.font.Font(None, 36)
input_font = pygame.font.Font(None, 32)

# Variables
word_clue_pairs_copy = word_clue_pairs.copy()  # Make a copy of the original word_clue_pairs to later remove it once it appears to not repeat the question again
current_word, current_clues = "", []
attempts = 3
current_guess = ""
score = 0

#Randomize and Display Word and Clue Pairs
def generate_word():
    global current_word, current_clues, word_clue_pairs_copy

    if not word_clue_pairs_copy:
        word_clue_pairs_copy = word_clue_pairs.copy()  # If the copy is empty, reset it

    word_clue_pair = random.choice(word_clue_pairs_copy)
    current_word, current_clues = word_clue_pair
    word_clue_pairs_copy.remove(word_clue_pair)  # Remove the chosen word_clue_pair from the copy

#Introductory Screen
def draw_intro_screen():
    screen.fill(WHITE)

    screen.blit(game_logo, game_logo_rect)

    pygame.display.flip()

#Displays and get the player's details
def draw_screen():
    screen.fill(WHITE)

    screen.blit(game_bg, game_bg_rect)

    clue_y = 160
    for clue in current_clues:
        text = font.render(clue, True, BLACK)
        text_rect = text.get_rect(center=(WIDTH // 2, clue_y))
        screen.blit(text, text_rect)
        clue_y += 40

    guess_text = input_font.render("Your Guess: " + current_guess, True, BLACK)
    guess_text_rect = guess_text.get_rect(center=(WIDTH // 2, 370))  # Adjusted the Y-position
    screen.blit(guess_text, guess_text_rect)

    attempts_text = font.render(f"Attempts left: {attempts}", True, BLACK)
    attempts_text_rect = attempts_text.get_rect(center=(WIDTH // 2, 470))  # Adjusted the Y-position
    screen.blit(attempts_text, attempts_text_rect)

    score_text = font.render(f"Score: {score}", True, BLACK)
    score_text_rect = score_text.get_rect(center=(WIDTH // 2, 520))  # Adjusted the Y-position
    screen.blit(score_text, score_text_rect)

    pygame.display.flip()

#Display a message when they got the correct answer
def show_message(message, delay=2000):
    screen.fill(WHITE)
    screen.blit(game_bg, game_bg_rect)
    text = font.render(message, True, BLACK)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.delay(delay)

#Display the correct answer if the player didn't got the right answer
def reveal_answer():
    delay = 10000
    screen.fill(WHITE)
    screen.blit(wrong, wrong_rect)
    
    answer_text = font.render(f"The correct answer is: {current_word}", True, BLACK)
    answer_text_rect = answer_text.get_rect(center=(WIDTH // 2, HEIGHT // 5.3))  # Adjusted the Y-position
    screen.blit(answer_text, answer_text_rect)
    end = font.render('YOU LOSE!', True, BLACK)
    end_rect = end.get_rect(center=(WIDTH // 2, HEIGHT // 10))  # Adjusted the Y-position
    screen.blit(end, end_rect)
    
    score_text = font.render(f"Your Score: {score}", True, BLACK)
    score_text_rect = score_text.get_rect(center=(WIDTH // 2, HEIGHT // 3.5))
    screen.blit(score_text, score_text_rect)
    task = score_tasks.get(score, "No task for this score")
    task_text = font.render(f"TASK: {task}", True, BLACK)
    task_text_rect = task_text.get_rect(center=(WIDTH // 2, HEIGHT // 1.2))
    screen.blit(task_text, task_text_rect)
    
    pygame.display.flip()
    time.sleep(delay / 1000)  # Wait for the specified delay
    pygame.quit()
    sys.exit()

#Displays ending screen
def end_game():
    delay = 10000
    screen.fill(WHITE)
    
    # Display the background image
    screen.blit(finish_bg, finish_bg_rect)

    # Display the message
    text = font.render("You finished the GAME!", True, BLACK)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 5))
    screen.blit(text, text_rect)

    # Display the score and associated task
    score_text = font.render(f"Your Score: {score}", True, BLACK)
    score_text_rect = score_text.get_rect(center=(WIDTH // 2, HEIGHT // 3.3))
    screen.blit(score_text, score_text_rect)

    task = score_tasks.get(score, "No task for this score")
    task_text = font.render(f"TASK: {task}", True, BLACK)
    task_text_rect = task_text.get_rect(center=(WIDTH // 2, HEIGHT // 1.2))
    screen.blit(task_text, task_text_rect)

    pygame.display.flip()

    time.sleep(delay / 1000)  # Wait for the specified delay
    pygame.quit()
    sys.exit()

draw_intro_screen()
pygame.display.flip()

# Wait for Enter key press to start the game
play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            play = False
    pygame.time.delay(100)

generate_word()
draw_screen()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_BACKSPACE:
                current_guess = current_guess[:-1]
            elif event.key == pygame.K_RETURN:
                if current_guess.lower() == current_word:
                    show_message("Correct answer!", delay=1000)
                    generate_word()
                    attempts = 3
                    score += 10
                    if not word_clue_pairs_copy:
                        end_game()  
                        pygame.display.flip()
                    if score >= 300:
                        end_game()
                else:
                    attempts -= 1
                    if attempts == 0:
                        reveal_answer()
                        current_guess = ""
                if attempts != 0:
                    current_guess = ""
                draw_screen()
            else:
                current_guess += event.unicode

    draw_screen()

# Quit Pygame
pygame.mixer.music.stop()
pygame.quit()
sys.exit()
