import pygame, sys, random
from typing import List
import time

HERO_PATH = "./heroes/"
IMG_PATH = "./imgs/"
BG_SIZE = (800, 1000)

#BIRD_SONGS =
PIPE_SPEED = 5


class HeroFace:

    def __init__(self, downflap_path, midflap_path, upflap_path, name, highscore=0):
        # self.hero_look_surface = pygame.image.load(HERO_PATH + look_path).convert()
        # self.hero_look_surface = pygame.transform.scale(self.hero_look_surface, BG_SIZE)
        # self.end_picture_surface = pygame.image.load(HERO_PATH + end_game_path).convert()
        # self.end_picture_surface = pygame.transform.scale(self.end_picture_surface, BG_SIZE)
        # self.rect = self.hero_look_surface.get_rect(center=(int(BG_SIZE[0] / 2), int(BG_SIZE[1] / 2)))

        self.bird_downflap = pygame.image.load(HERO_PATH + downflap_path).convert_alpha()
        self.bird_downflap = pygame.transform.scale(self.bird_downflap, (int(BG_SIZE[0] / 12.5), int(BG_SIZE[1] / 15)))
        self.bird_midflap = pygame.image.load(HERO_PATH + midflap_path).convert_alpha()
        self.bird_midflap = pygame.transform.scale(self.bird_midflap, (int(BG_SIZE[0] / 12.5), int(BG_SIZE[1] / 15)))
        self.bird_upflap = pygame.image.load(HERO_PATH + upflap_path).convert_alpha()
        self.bird_upflap = pygame.transform.scale(self.bird_upflap, (int(BG_SIZE[0] / 12.5), int(BG_SIZE[1] / 15)))
        self.bird_frames = [self.bird_downflap, self.bird_midflap, self.bird_upflap]
        self.bird_index = 0
        self.bird_surface = self.bird_frames[self.bird_index]
        self.bird_rect = self.bird_surface.get_rect(center=(int(BG_SIZE[0] / 4), int(BG_SIZE[1] / 4)))
        self.highscore = highscore
        self.name = name


class HeroSound:

    def __init__(self, start_sound_path, death_sound_path, death_image_path):
        self.start_sound = pygame.mixer.Sound(start_sound_path)
        self.death_sound = pygame.mixer.Sound(death_sound_path)
        self.death_image = pygame.image.load(death_image_path).convert_alpha()
        self.death_image = pygame.transform.scale(self.death_image, (BG_SIZE[0], BG_SIZE[1]))
        self.death_rect = game_over_surface.get_rect()

    def show_death(self):
        screen.blit(self.death_image, self.death_rect)
        self.death_sound.play()


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


def check_collision(pipes, birdtype_sound):
    for pipe in pipes:
        if BIRD_TYPE.bird_rect.colliderect(pipe):
            if score <= high_score:
                birdtype_sound.show_death()
            return False

    if BIRD_TYPE.bird_rect.top <= -int(BG_SIZE[1]*0.2) or BIRD_TYPE.bird_rect.bottom >= int(BG_SIZE[1]-BG_SIZE[1]/5):
        death_sound.play()
        return False

    return True


def rotate_bird(bird):
    return pygame.transform.rotozoom(bird, -3*bird_movement, 1)


def score_display(game_active, hero: HeroFace):
    score_surface = game_font.render("Score: " + str(int(score)), True, (255, 255, 255))
    score_rect = score_surface.get_rect(center=(int(BG_SIZE[0]/2), 60))
    screen.blit(score_surface, score_rect)
    if not game_active:
        highscore_surface = game_font.render(hero.name + " highscore: " + str(int(hero.highscore)), True, (255, 255, 255))
        highscore_surface_rect = highscore_surface.get_rect(center=(int(BG_SIZE[0] / 2), 110))
        screen.blit(highscore_surface, highscore_surface_rect)


def update_highscore(score, hero):
    if score > hero.highscore:
        hero.highscore = int(score)
        beat_highscore_sound.play()
        save_highscores()
    return hero.highscore


def draw_choosing_hereos():
    hero_choosing_surface1 = game_font.render("Zjarany   1   ", True, (255, 255, 255))
    hero_choosing_surface_rect1 = hero_choosing_surface1.get_rect(center=(int(BG_SIZE[0] / 4), int(BG_SIZE[1]/20 * 4)))
    screen.blit(hero_choosing_surface1, hero_choosing_surface_rect1)
    hero_choosing_surface2 = game_font.render("Prezydent   2", True, (255, 255, 255))
    hero_choosing_surface_rect2 = hero_choosing_surface2.get_rect(center=(int(BG_SIZE[0] / 4), int(BG_SIZE[1]/20 * 5)))
    screen.blit(hero_choosing_surface2, hero_choosing_surface_rect2)
    hero_choosing_surface3 = game_font.render("Lysy   3       ", True, (255, 255, 255))
    hero_choosing_surface_rect3 = hero_choosing_surface3.get_rect(center=(int(BG_SIZE[0] / 4), int(BG_SIZE[1]/20 * 6)))
    screen.blit(hero_choosing_surface3, hero_choosing_surface_rect3)
    hero_choosing_surface4 = game_font.render("Icy Tower   4", True, (255, 255, 255))
    hero_choosing_surface_rect4 = hero_choosing_surface4.get_rect(center=(int(BG_SIZE[0] / 4), int(BG_SIZE[1]/20 * 7)))
    screen.blit(hero_choosing_surface4, hero_choosing_surface_rect4)
    hero_choosing_surface5 = game_font.render("    VicePresident   5", True, (255, 255, 255))
    hero_choosing_surface_rect5 = hero_choosing_surface5.get_rect(center=(int(BG_SIZE[0] / 4), int(BG_SIZE[1]/20 * 8)))
    screen.blit(hero_choosing_surface5, hero_choosing_surface_rect5)
    hero_choosing_surface6 = game_font.render("Narcos   6    ", True, (255, 255, 255))
    hero_choosing_surface_rect6 = hero_choosing_surface6.get_rect(center=(int(BG_SIZE[0] / 4), int(BG_SIZE[1]/20 * 9)))
    screen.blit(hero_choosing_surface6, hero_choosing_surface_rect6)
    hero_choosing_surface7 = game_font.render("Alvaro   7    ", True, (255, 255, 255))
    hero_choosing_surface_rect7 = hero_choosing_surface7.get_rect(center=(int(BG_SIZE[0] / 4), int(BG_SIZE[1]/20 * 10)))
    screen.blit(hero_choosing_surface7, hero_choosing_surface_rect7)
    hero_choosing_surface8 = game_font.render("Rudy   8      ", True, (255, 255, 255))
    hero_choosing_surface_rect8 = hero_choosing_surface8.get_rect(center=(int(BG_SIZE[0] / 4), int(BG_SIZE[1]/20 * 11)))
    screen.blit(hero_choosing_surface8, hero_choosing_surface_rect8)
    hero_choosing_surface9 = game_font.render("Rom  9        ", True, (255, 255, 255))
    hero_choosing_surface_rect9 = hero_choosing_surface9.get_rect(center=(int(BG_SIZE[0] / 4), int(BG_SIZE[1]/20 * 12)))
    screen.blit(hero_choosing_surface9, hero_choosing_surface_rect9)
    screen.blit(hero_choosing_surface10, hero_choosing_surface_rect10)


def draw_clown_surface():
    clown_surface = pygame.image.load(IMG_PATH + "clown_together.jpg").convert_alpha()
    clown_surface = pygame.transform.scale(clown_surface, (BG_SIZE[0], BG_SIZE[1]))
    clown_rect = game_over_surface.get_rect()
    screen.blit(clown_surface, clown_rect)
    time.sleep(1.5) #sleep after losing game


def save_highscores():
    with open("highscore.txt", "w") as file:
        file.write(str(Normal_blue.highscore) + "\n" + str(Mytnik.highscore) + "\n" + str(Strychala.highscore))
        file.close()

#-------------------------------------------------------------------------#
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

#only for mouse purpose
hero_choosing_surface10 = game_font.render("Settings", True, (255, 255, 255))
hero_choosing_surface_rect10 = hero_choosing_surface10.get_rect(center=(int(BG_SIZE[0] / 2), int(BG_SIZE[1] / 20 * 15)))
#Bird_face
# bird_downflap = pygame.image.load(IMG_PATH + "bluebird-downflap.png").convert_alpha()
# bird_downflap = pygame.transform.scale(bird_downflap, (int(BG_SIZE[0]/15), int(BG_SIZE[1]/20)))
# bird_midflap = pygame.image.load(IMG_PATH + "bluebird-midflap.png").convert_alpha()
# bird_midflap = pygame.transform.scale(bird_midflap, (int(BG_SIZE[0]/15), int(BG_SIZE[1]/20)))
# bird_upflap = pygame.image.load(IMG_PATH + "bluebird-upflap.png").convert_alpha()
# bird_upflap = pygame.transform.scale(bird_upflap, (int(BG_SIZE[0]/15), int(BG_SIZE[1]/20)))
# bird_frames = [bird_downflap, bird_midflap, bird_upflap]
# bird_index = 0
# bird_surface = bird_frames[bird_index]
# bird_rect = bird_surface.get_rect(center=(int(BG_SIZE[0]/4), int(BG_SIZE[1]/4)))

BIRDFLAP = pygame.USEREVENT + 1
pygame.time.set_timer(BIRDFLAP, 200)
# bird_surface = pygame.image.load(IMG_PATH + "bluebird-midflap.png").convert_alpha()
# bird_surface = pygame.transform.scale(bird_surface, (int(BG_SIZE[0]/15), int(BG_SIZE[1]/20)))
# bird_rect = bird_surface.get_rect(center=(int(BG_SIZE[0]/4), int(BG_SIZE[1]/4)))

pipe_surface = pygame.image.load(IMG_PATH + "pipe-green.png")
#pipe_surface = pygame.image.load(IMG_PATH + "wodka.jpg")
pipe_surface = pygame.transform.scale(pipe_surface, (int(BG_SIZE[0]/10), int(BG_SIZE[1]/1.5)))
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)
pipe_heights = [int(BG_SIZE[1]*0.335), int(BG_SIZE[1]*0.35), int(BG_SIZE[1]*0.4), int(BG_SIZE[1]*0.45), int(BG_SIZE[1]*0.5),
                int(BG_SIZE[1]*0.65), int(BG_SIZE[1]*0.6), int(BG_SIZE[1]*0.7)] #int(BG_SIZE[1]*0.8) [int(BG_SIZE[1]*0.2),

game_over_surface = pygame.image.load(IMG_PATH + "message.png").convert_alpha()
game_over_surface = pygame.transform.scale(game_over_surface, tuple(int(x/2) for x in BG_SIZE))
game_over_rect = game_over_surface.get_rect(center=(int(BG_SIZE[0]/2), int(BG_SIZE[1]/2)))

flap_sound = pygame.mixer.Sound("sound/sfx_wing.wav")
death_sound = pygame.mixer.Sound("sound/sfx_hit.wav")
score_sound = pygame.mixer.Sound("sound/sfx_point.wav")
beat_highscore_sound = pygame.mixer.Sound("sound/win.mp3")
settings_flag = False

#NormalBird = HeroFace()
with open("highscore.txt", 'r') as f:
    Normal_highscore = int(f.readline())
    Mytnik_highscore = int(f.readline())
    Strychala_highscore = int(f.readline())
    f.close()



Mytnik = HeroFace("Mytnik/Mytnik_face_down.png", "Mytnik/Mytnik_face_mid.png", "Mytnik/Mytnik_face_up.png", "Mytniś", Mytnik_highscore)
Mytnik_sound = HeroSound("sound/start_sound/Mytnik_start.wav", "sound/end_sound/Mytnik_end_sound.wav", "heroes/Mytnik/Mytnik_end.png")
Normal_blue = HeroFace("Normal_blue/bluebird-downflap.png", "Normal_blue/bluebird-midflap.png", "Normal_blue/bluebird-upflap.png", "Bluebird", Normal_highscore)
Normal_blue_sound = HeroSound("sound/sfx_die.wav", "sound/sfx_die.wav", "imgs/gameover.png")
Strychala = HeroFace("Strychala/Strychala_face_down2.png", "Strychala/Strychala_face_mid2.png", "Strychala/Strychala_face_up2.png", "Strychala", Strychala_highscore)
Strychala_sound = HeroSound(HERO_PATH + "Strychala/pierd.wav", HERO_PATH + "Strychala/pierd2.wav", HERO_PATH + "Strychala/Strychala_dupa.jpg")
BIRD_TYPE = Normal_blue
BIRD_TYPE_SOUND = Normal_blue_sound


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0  #preventing wrong moves
                bird_movement -= 8
                flap_sound.play()
            if event.key == pygame.K_SPACE and not game_active:
                game_active = True
                pipe_list.clear() #restoring initial conditions of game, otherwise we would met bugs
                PIPE_SPEED = 5
                BIRD_TYPE.bird_rect.center = (int(BG_SIZE[0]/4), int(BG_SIZE[1]/4))
                bird_movement = 0
                score = 0
            if event.key == pygame.K_ESCAPE and not game_active:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_7 and not game_active:
                BIRD_TYPE = Mytnik
                BIRD_TYPE_SOUND = Mytnik_sound
            if event.key == pygame.K_6 and not game_active:
                BIRD_TYPE = Strychala
                BIRD_TYPE_SOUND = Strychala_sound
            if event.key == pygame.K_0 and not game_active:
                BIRD_TYPE = Normal_blue
                BIRD_TYPE_SOUND = Normal_blue_sound
        #settings
        if event.type == pygame.MOUSEBUTTONUP and not game_active:
            mouse_postion = pygame.mouse.get_pos()
            if hero_choosing_surface_rect10.collidepoint(mouse_postion) and pygame.mouse.get_pressed(num_buttons=5)[0]:
                settings_flag = True
                #TODO
                #Show_settings_screen
                #if choose something do something
                #do resolution change
                #do speed change
                #do color of backgroumd change
                #do żubrówka change
                screen.blit(bg_surface, (0, 0))
                BIRD_TYPE_SOUND.show_death()
                settings_flag = not settings_flag

        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())
        if event.type == BIRDFLAP:
            if BIRD_TYPE.bird_index < 2:
                BIRD_TYPE.bird_index += 1
            else:
                BIRD_TYPE.bird_index = 0

    screen.blit(bg_surface, (0, 0))

    if game_active:
        # Bird
        bird_movement += gravity
        rotated_bird = rotate_bird(BIRD_TYPE.bird_frames[BIRD_TYPE.bird_index])
        BIRD_TYPE.bird_rect.centery += bird_movement
        if not(check_collision(pipe_list, BIRD_TYPE_SOUND)):
            if score > BIRD_TYPE.highscore:
                BIRD_TYPE.highscore = update_highscore(score, BIRD_TYPE)
            game_active = False #checking whether you touched pipe or bottom/top and ending game

        screen.blit(rotated_bird, BIRD_TYPE.bird_rect)
        # Pipes
        pipe_list = move_pipes(pipe_list, pipe_spd=PIPE_SPEED)
        draw_pipes(pipe_list, screen)
        score += 0.01
        if score % 3 < 0.01:
           PIPE_SPEED += 0.25

    else:
        # screen.blit(game_over_surface, game_over_rect)
        # screen.blit(Mytnik.hero_look_surface, Mytnik.rect)
        draw_clown_surface()
        if not settings_flag:
            draw_choosing_hereos()




    # Floor
    floor_x_pos -= 1
    draw_floor(screen, floor_x_pos)

    if floor_x_pos <= -BG_SIZE[0]:
        floor_x_pos = 0

    score_display(game_active, BIRD_TYPE)
    pygame.display.update()
    clock.tick(90)

