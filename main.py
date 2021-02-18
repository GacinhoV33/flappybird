import pygame, sys, random
from typing import List
import time

HERO_PATH = "./heroes/"
IMG_PATH = "./imgs/"
BG_SIZE = (576, 800)
#BIRD_TYPE =
PIPE_SPEED = 5


def draw_floor(screen, floor_x_pos):
    screen.blit(floor_surface, (floor_x_pos, BG_SIZE[1] - int(BG_SIZE[1] / 5)))
    screen.blit(floor_surface, (floor_x_pos + BG_SIZE[0], BG_SIZE[1] - int(BG_SIZE[1] / 5)))


def create_pipe():
    random_pipe_height = random.choice(pipe_heights)
    bottom_pipe = pipe_surface.get_rect(midtop=(int(BG_SIZE[0]*1.1), random_pipe_height))
    top_pipe = pipe_surface.get_rect(midbottom=(int(BG_SIZE[0]*1.1), random_pipe_height - space_btw_pipes))
    return bottom_pipe, top_pipe


def move_pipes(pipes, pipe_spd=5):
    for pipe in pipes:
        pipe.centerx -= pipe_spd
    return pipes


def draw_pipes(pipes, screen):
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
        beat_highscore_sound.play()
    return high_score


def draw_choosing_hereos():
    hero_choosing_surface1 = game_font.render("Zjarany   1   ", True, (255, 255, 255))
    hero_choosing_surface_rect1 = hero_choosing_surface1.get_rect(center=(int(BG_SIZE[0] / 4), 150))
    screen.blit(hero_choosing_surface1, hero_choosing_surface_rect1)
    hero_choosing_surface2 = game_font.render("Prezydent   2", True, (255, 255, 255))
    hero_choosing_surface_rect2 = hero_choosing_surface2.get_rect(center=(int(BG_SIZE[0] / 4), 200))
    screen.blit(hero_choosing_surface2, hero_choosing_surface_rect2)
    hero_choosing_surface3 = game_font.render("Lysy   3      ", True, (255, 255, 255))
    hero_choosing_surface_rect3 = hero_choosing_surface3.get_rect(center=(int(BG_SIZE[0] / 4), 250))
    screen.blit(hero_choosing_surface3, hero_choosing_surface_rect3)
    hero_choosing_surface4 = game_font.render("Icy Tower   4", True, (255, 255, 255))
    hero_choosing_surface_rect4 = hero_choosing_surface4.get_rect(center=(int(BG_SIZE[0] / 4), 300))
    screen.blit(hero_choosing_surface4, hero_choosing_surface_rect4)
    hero_choosing_surface5 = game_font.render("    VicePresident   5", True, (255, 255, 255))
    hero_choosing_surface_rect5 = hero_choosing_surface5.get_rect(center=(int(BG_SIZE[0] / 4), 350))
    screen.blit(hero_choosing_surface5, hero_choosing_surface_rect5)
    hero_choosing_surface6 = game_font.render("Narcos   6    ", True, (255, 255, 255))
    hero_choosing_surface_rect6 = hero_choosing_surface6.get_rect(center=(int(BG_SIZE[0] / 4), 400))
    screen.blit(hero_choosing_surface6, hero_choosing_surface_rect6)
    hero_choosing_surface7 = game_font.render("Alvaro   7    ", True, (255, 255, 255))
    hero_choosing_surface_rect7 = hero_choosing_surface7.get_rect(center=(int(BG_SIZE[0] / 4), 450))
    screen.blit(hero_choosing_surface7, hero_choosing_surface_rect7)
    hero_choosing_surface8 = game_font.render("Rudy   8      ", True, (255, 255, 255))
    hero_choosing_surface_rect8 = hero_choosing_surface8.get_rect(center=(int(BG_SIZE[0] / 4), 500))
    screen.blit(hero_choosing_surface8, hero_choosing_surface_rect8)


def draw_clown_surface():
    clown_surface = pygame.image.load(IMG_PATH + "clown_together.jpg").convert_alpha()
    clown_surface = pygame.transform.scale(clown_surface, (BG_SIZE[0], BG_SIZE[1]))
    clown_rect = game_over_surface.get_rect()
    screen.blit(clown_surface, clown_rect)
    time.sleep(1) #sleep after losing game

#-------------------------------------------------------------------------#
class Hero:

    def __init__(self, look_path, end_game_path, start_sound_path, end_sound_path):
        self.hero_look_surface = pygame.image.load(HERO_PATH + look_path).convert()
        self.hero_look_surface = pygame.transform.scale(self.hero_look_surface, BG_SIZE)
        self.end_picture_surface = pygame.image.load(HERO_PATH + end_game_path).convert()
        self.end_picture_surface = pygame.transform.scale(self.end_picture_surface, BG_SIZE)
        self.rect = self.hero_look_surface.get_rect(center=(int(BG_SIZE[0] / 2), int(BG_SIZE[1] / 2)))
        self.start_sound = pygame.mixer.Sound(start_sound_path)
        self.end_sound = pygame.mixer.Sound(end_sound_path)


    hero_highscore = 0

#-----------------------------------------------------------------------#

# pygame.mixer.pre_init(frequency=44100, size=16, channels=1, buffer=512)
pygame.init()
screen = pygame.display.set_mode(BG_SIZE)
clock = pygame.time.Clock()
game_font = pygame.font.Font("04B_19.ttf", 40)

#Game Variables
gravity = 0.25
bird_movement = 0
space_btw_pipes = int(BG_SIZE[1]/4)
game_active = False
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
beat_highscore_sound = pygame.mixer.Sound("sound/win.mp3")

Mytnik = Hero("Mytnik.png", "Mytnik_end.png", "sound/start_sound/Mytnik_start.wav", "sound/end_sound/Mytnik_end_sound.wav")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0  #preventing wrong moves
                bird_movement -= 7
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
        if not(check_collision(pipe_list)):
            if score <= high_score:
                Mytnik.end_sound.play()
            else:
                high_score = update_highscore(score, high_score)
            game_active = False #checking whether you touched pipe or bottom/top and ending game

        screen.blit(rotated_bird, bird_rect)
        # Pipes
        pipe_list = move_pipes(pipe_list, pipe_spd=PIPE_SPEED)
        draw_pipes(pipe_list, screen)
        score += 0.01
        if score % 3 < 0.01:
           PIPE_SPEED += 0.12

    else:
        # screen.blit(game_over_surface, game_over_rect)
        # screen.blit(Mytnik.hero_look_surface, Mytnik.rect)
        draw_clown_surface()
        draw_choosing_hereos()




    # Floor
    floor_x_pos -= 1
    draw_floor(screen, floor_x_pos)


    if floor_x_pos <= -BG_SIZE[0]:
        floor_x_pos = 0

    score_display(game_active)
    pygame.display.update()
    clock.tick(90)

