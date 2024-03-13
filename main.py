import pygame, random,time
pygame.init()
WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# text font
font = pygame.font.SysFont('times', 32)
# button
button_X = 0
button_X = 0
count = 0
box_color = [255,255,255]
menue = False
# cool down update
cool = 0
# number
orig_number = 0
number = 0
# print pos
x = random.randint(0, WIDTH - 32), random.randint(0, HEIGHT - 32)
y = random.randint(0, WIDTH - 32), random.randint(0, HEIGHT - 32)
position = x,y
# number color
color = (255,255,255)
# end game
win = False
end_game = random.randint(0,1800)
# game
running = True
while running:
    # time
    time.sleep(0.1)
    end_game -= 1
    # update
    menue = False
    pygame.display.flip()
    mouse = pygame.mouse.get_pos()
    cool = cool
    # quit game
    for event in pygame.event.get():
        # quit
        if event.type == pygame.QUIT:
            running = False
    # display numbers
    number_string = str(number)
    display_number = font.render(number_string, 1, color)
    screen.blit(display_number, (position))
    #color changing text
    if number == 0:
        color = (255, 255, 255)
    if number > 124 and number <= 249:
        color = (random.randint(0, 200), 255, 255)
    if number >= 250 and number <= 298:
        color = (255, random.randint(0, 200), 255)
    if number >= 299 and number <= 747:
        color = (255, 255, random.randint(0, 200))
    if number >= 748 and number <= 999:
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    # if the number is grader than it's past self
    if number > orig_number:
        # changing position
        orig_number += 1
        x = random.randint(0, WIDTH - 32), random.randint(0, HEIGHT - 32)
        y = random.randint(0, WIDTH - 32), random.randint(0, HEIGHT - 32)
        position = (x, y)
        screen.blit(display_number, (position))
        # update
        screen.fill((0, 0, 0))
        pygame.display.update()
    # display button
    button = pygame.Rect((button_X,button_X, 50, 50))
    pygame.draw.rect(screen, box_color, button)
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = event.pos
        if button.collidepoint(mouse_pos):
            count += 1
            if count == 1:
                menue = True
            else:
                menue = False
                count = 0
        else:
            menue = False
    if menue == True:
        number += 1
        menue = False
    # cool down update
    if menue != True:
        cool = random.randint(0,100)
        distroy = random.randint(0,1000000)
        if distroy == 0:
            font = pygame.font.SysFont('times', 100)
            end_string = 'bonus'.upper()
            display = font.render(end_string, 1,(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            screen.blit(display, (WIDTH // 2 - 395, HEIGHT // 2))
            number *= number
            end_game -= number
            pygame.display.update()
        if distroy == 1000000:
            number = -1
        if cool == 50:
            number -= 1
            orig_number -= 1
            screen.fill((0,0,0))
            pygame.display.update()
    # change location and color of button
    R = random.randint(0,1)
    if R == 0:
        color_b = random.randint(0, 100)
        if color_b == 50:
            box_color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
    if R == 1:
        move = random.randint(0, 100)
        if move == 50:
            button_X = random.randint(0,WIDTH - 50)
            button_Y = random.randint(0, HEIGHT - 50)
            screen.fill((0, 0, 0))
            pygame.display.update()
    # win game
    if number > 999 and end_game == 0:
        win = True
        menue = False
        font = pygame.font.SysFont('times', 100)
        end_string = 'you have won'.upper()
        display = font.render(end_string, 1, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        screen.blit(display, (WIDTH // 2 - 395, HEIGHT // 2))
        if number == number:
            running = False
    elif win == False:
        end_game = random.randint(0, 1800) - 1
    # loose game
    if number < 0:
        menue = False
        font = pygame.font.SysFont('times', 100)
        end_string = 'you have lost the game'.upper()
        display = font.render(end_string, 1, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        screen.blit(display, (WIDTH // 2 - 395, HEIGHT // 2))
        if number < -1:
            running = False
    pygame.display.update()