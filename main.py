import pygame, sys, random
from typing import List

IMG_PATH = "./imgs/"
BG_SIZE = (576, 800)
#BIRD_TYPE =


def draw_floor(screen, floor_x_pos):
    screen.blit(floor_surface, (floor_x_pos, BG_SIZE[1] - int(BG_SIZE[1] / 5)))
    screen.blit(floor_surface, (floor_x_pos + BG_SIZE[0], BG_SIZE[1] - int(BG_SIZE[1] / 5)))


def create_pipe():
    random_pipe_height = random.choice(pipe_heights)
    bottom_pipe = pipe_surface.get_rect(midtop=(int(BG_SIZE[0]*1.1), random_pipe_height))
    top_pipe = pipe_surface.get_rect(midbottom=(int(BG_SIZE[0]*1.1), random_pipe_height - space_btw_pipes))
    return bottom_pipe, top_pipe


def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes


def draw_pipes(pipes, screen1):
    for pipe in pipes:
        screen.blit(pipe_surface, pipe)
        if pipe.bottom >= BG_SIZE[1]:
            screen.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flip_pipe, pipe)


def check_collision(pipes):
    for pipe in pipes:
       if bird_rect.colliderect(pipe):
           death_sound.play()
           return False

    if bird_rect.top <= -int(BG_SIZE[1]*0.2) or bird_rect.bottom >= int(BG_SIZE[1]-BG_SIZE[1]/5):
        death_sound.play()
        return False

    return True


def rotate_bird(bird):
    return pygame.transform.rotozoom(bird, -3*bird_movement, 1)


def score_display(game_active):
    score_surface = game_font.render("Score: " + str(int(score)), True, (255, 255, 255))
    score_rect = score_surface.get_rect(center=(int(BG_SIZE[0]/2), 60))
    screen.blit(score_surface, score_rect)
    if not game_active:
        highscore_surface = game_font.render("Highscore: " + str(int(high_score)), True, (255, 255, 255))
        highscore_surface_rect = highscore_surface.get_rect(center=(int(BG_SIZE[0] / 2), 110))
        screen.blit(highscore_surface, highscore_surface_rect)


def update_highscore(score, high_score):
    if score > high_score:
        high_score = score
    return high_score


# pygame.mixer.pre_init(frequency=44100, size=16, channels=1, buffer=512)
pygame.init()
screen = pygame.display.set_mode(BG_SIZE)
clock = pygame.time.Clock()
game_font = pygame.font.Font("04B_19.ttf", 40)

#Game Variables
gravity = 0.25
bird_movement = 0
space_btw_pipes = int(BG_SIZE[1]/4)
game_active = True
score = 0
high_score = 0

bg_surface = pygame.image.load(IMG_PATH + "background-day.png").convert()
bg_surface = pygame.transform.scale(bg_surface, BG_SIZE)

floor_surface = pygame.image.load(IMG_PATH + "base.png").convert()
floor_surface = pygame.transform.scale(floor_surface, (int(BG_SIZE[0]*1.5), int(BG_SIZE[1]/5)))
floor_x_pos = 0

bird_downflap = pygame.image.load(IMG_PATH + "bluebird-downflap.png").convert_alpha()
bird_downflap = pygame.transform.scale(bird_downflap, (int(BG_SIZE[0]/15), int(BG_SIZE[1]/20)))
bird_midflap = pygame.image.load(IMG_PATH + "bluebird-midflap.png").convert_alpha()
bird_midflap = pygame.transform.scale(bird_midflap, (int(BG_SIZE[0]/15), int(BG_SIZE[1]/20)))
bird_upflap = pygame.image.load(IMG_PATH + "bluebird-upflap.png").convert_alpha()
bird_upflap = pygame.transform.scale(bird_upflap, (int(BG_SIZE[0]/15), int(BG_SIZE[1]/20)))
bird_frames = [bird_downflap, bird_midflap, bird_upflap]
bird_index = 0
bird_surface = bird_frames[bird_index]
bird_rect = bird_surface.get_rect(center=(int(BG_SIZE[0]/4), int(BG_SIZE[1]/4)))

BIRDFLAP = pygame.USEREVENT + 1
pygame.time.set_timer(BIRDFLAP, 200)
# bird_surface = pygame.image.load(IMG_PATH + "bluebird-midflap.png").convert_alpha()
# bird_surface = pygame.transform.scale(bird_surface, (int(BG_SIZE[0]/15), int(BG_SIZE[1]/20)))
# bird_rect = bird_surface.get_rect(center=(int(BG_SIZE[0]/4), int(BG_SIZE[1]/4)))

pipe_surface = pygame.image.load(IMG_PATH + "pipe-green.png")
pipe_surface = pygame.transform.scale(pipe_surface, (int(BG_SIZE[0]/10), int(BG_SIZE[1]/1.5)))
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)
pipe_heights = [int(BG_SIZE[1]*0.4), int(BG_SIZE[1]*0.5), int(BG_SIZE[1]*0.6)] #int(BG_SIZE[1]*0.8) [int(BG_SIZE[1]*0.2),

game_over_surface = pygame.image.load(IMG_PATH + "message.png").convert_alpha()
game_over_surface = pygame.transform.scale(game_over_surface, tuple(int(x/2) for x in BG_SIZE))
game_over_rect = game_over_surface.get_rect(center=(int(BG_SIZE[0]/2), int(BG_SIZE[1]/2)))

flap_sound = pygame.mixer.Sound("sound/sfx_wing.wav")
death_sound = pygame.mixer.Sound("sound/sfx_hit.wav")
score_sound = pygame.mixer.Sound("sound/sfx_point.wav")


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0  #preventing wrong moves
                bird_movement -= 10
                flap_sound.play()
            if event.key == pygame.K_SPACE and not game_active:
                game_active = True
                pipe_list.clear() #restoring initial conditions of game, otherwise we would met bugs
                bird_rect.center = (int(BG_SIZE[0]/4), int(BG_SIZE[1]/4))
                bird_movement = 0
                score = 0
            if event.key == pygame.K_ESCAPE and not game_active:
                pygame.quit()
                sys.exit()

        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())
        if event.type == BIRDFLAP:
            if bird_index < 2:
                bird_index += 1
            else:
                bird_index = 0

    screen.blit(bg_surface, (0, 0))

    if game_active:
        # Bird
        bird_movement += gravity
        rotated_bird = rotate_bird(bird_frames[bird_index])
        bird_rect.centery += bird_movement
        game_active = check_collision(pipe_list) #checking whether you touched pipe or bottom/top and ending game

        screen.blit(rotated_bird, bird_rect)
        # Pipes
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list, screen)
        score += 0.01
    else:
        screen.blit(game_over_surface, game_over_rect)

    # Floor
    floor_x_pos -= 1
    draw_floor(screen, floor_x_pos)


    if floor_x_pos <= -BG_SIZE[0]:
        floor_x_pos = 0

    score_display(game_active)
    high_score = update_highscore(score, high_score)
    pygame.display.update()
    clock.tick(90)

