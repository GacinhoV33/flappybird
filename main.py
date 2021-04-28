import pygame, sys, random
from typing import List
import time

#TODO ONE FUNCTION TO SHOW SCREEN
# MORE SOUNDS
# MORE HEREOS

HERO_PATH = "./heroes/"
IMG_PATH = "./imgs/"
BG_SIZE = (800, 1000)

#BIRD_SONGS =
PIPE_SPEED = 5


class HeroFace:

    def __init__(self, downflap_path, midflap_path, upflap_path, hero_name, start_sound_list, end_sound_list, highscore=0):
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
        self.hero_name = hero_name
        self.start_sound_list = start_sound_list
        self.end_sound_list = end_sound_list

    def play_start_sound(self):
        self.start_sound_list[random.randint(0, len(self.start_sound_list) - 1)].play()

    def play_end_sound(self):
        self.end_sound_list[random.randint(0, len(self.end_sound_list) - 1)].play()

    # def play_video(self, actual_score): #TODO movie module removed
    #     screen = pygame.display.set_mode(self.video_list[0].get_size())
    #     movie_screen = pygame.Surface(self.video_list[0].get_size().convert())
    #     self.video_list[0].set_display(movie_screen)
    #     if actual_score < 10:
    #         self.video_list[0].play()
    #         screen.blit(movie_screen, (0, 0))


#Floor_functions
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
        if BIRD_TYPE.bird_rect.colliderect(pipe):
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
    if not game_active and not settings_flag:
        highscore_surface = game_font.render(hero.hero_name + " highscore: " + str(int(hero.highscore)), True, (255, 255, 255))
        highscore_surface_rect = highscore_surface.get_rect(center=(int(BG_SIZE[0] / 2), 110))
        screen.blit(highscore_surface, highscore_surface_rect)


#Highscore functions
def update_highscore(score, hero):
    if score > hero.highscore:
        hero.highscore = int(score)
        beat_highscore_sound.play()
        pygame.time.wait(2000)
        save_highscores()
    return hero.highscore


def save_highscores():
    with open("highscore.txt", "w") as file:
        file.write(str(Normal_blue.highscore) + "\n" + str(Mytnik.highscore) + "\n" + str(Strychala.highscore) +
                   "\n" + str(Jacek.highscore) + "\n" + str(Jasiek_highscore))
        file.close()


def show_screen(screen, pos):
    pass

#Draw functions
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
    hero_choosing_surface4 = game_font.render("Jacula   4     ", True, (255, 255, 255))
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
    time.sleep(1.25) #sleep after losing game


def draw_settings():
    resolution_surface = game_font.render("Resolution ", True, (255, 255, 255))
    resolution_surface_rect = resolution_surface.get_rect(center=(int(BG_SIZE[0] / 4), int(BG_SIZE[1]/20 * 15)))
    screen.blit(bg_surface, (0, 0))
    screen.blit(resolution_surface, resolution_surface_rect)

    #TODO


#Functions with sounds_lists
def make_background_music_list():
    background_music_list = list()
    background_music_list.append("music_in_back/Jaramy_Jaramy.mp3")
    background_music_list.append("music_in_back/Czuje_banie.mp3")
    background_music_list.append("music_in_back/Young_Kit$hxOlaf_PDW.mp3")
    return background_music_list


def play_background_music():
    pygame.mixer.music.load(background_music_list[0])
    pygame.mixer.music.play()
    for el in background_music_list[1:]:
        pygame.mixer.music.queue(el)


def switch_music(flag_music):
    if flag_music:
        pygame.mixer.music.pause()
        return not flag_music
    else:
        pygame.mixer.music.unpause()
        return not flag_music


def make_Jacek_elist():
    Jacek_sound_end = list()
    Jacek_sound_end.append(pygame.mixer.Sound("sound/end_sound/Jacek/ani obejrzec wykladu.wav"))
    Jacek_sound_end.append(pygame.mixer.Sound("sound/end_sound/Jacek/co to kurwa za hitboxy.wav"))
    Jacek_sound_end.append(pygame.mixer.Sound("sound/end_sound/Jacek/co za grek jebany.wav"))
    Jacek_sound_end.append(pygame.mixer.Sound("sound/end_sound/Jacek/Co za pojeebana gra.wav"))
    Jacek_sound_end.append(pygame.mixer.Sound("sound/end_sound/Jacek/cos sie popsulo to zagram jeszcze raz.wav"))
    Jacek_sound_end.append(pygame.mixer.Sound("sound/end_sound/Jacek/fatalny to ty jestes.wav"))
    Jacek_sound_end.append(pygame.mixer.Sound("sound/end_sound/Jacek/ja mam to w pizdzie.wav"))
    Jacek_sound_end.append(pygame.mixer.Sound("sound/end_sound/Jacek/Japierdoleee.wav"))
    Jacek_sound_end.append(pygame.mixer.Sound("sound/end_sound/Jacek/kurwaaaa.wav"))
    Jacek_sound_end.append(pygame.mixer.Sound("sound/end_sound/Jacek/Nie, nie da sie grac.wav"))
    Jacek_sound_end.append(pygame.mixer.Sound("sound/end_sound/Jacek/no i w pizdu.wav"))
    Jacek_sound_end.append(pygame.mixer.Sound("sound/end_sound/Jacek/no nie da sie kurwa grac.wav"))
    Jacek_sound_end.append(pygame.mixer.Sound("sound/end_sound/Jacek/pal sie ptaku.wav"))
    Jacek_sound_end.append(pygame.mixer.Sound("sound/end_sound/Jacek/to jest jakies kurwa nieporozumienie.wav"))
    Jacek_sound_end.append(pygame.mixer.Sound("sound/end_sound/Jacek/twoj wynik to jest jakas porazka.wav"))
    Jacek_sound_end.append(pygame.mixer.Sound("sound/end_sound/Jacek/W chuju to mam.wav"))
    Jacek_sound_end.append(pygame.mixer.Sound("sound/end_sound/Jacek/z takim wynikiem to was sie powinno jebac.wav"))
    return Jacek_sound_end


def make_Jacek_slist():
    Jacek_sound_start = list()
    # Jacek_sound_start.append(pygame.mixer.Sound("sound/start_sound/Jacek/halo_karthus.wav"))
    Jacek_sound_start.append(pygame.mixer.Sound("sound/start_sound/Jacek/i believe i can fly.wav"))
    return Jacek_sound_start


def make_Maciek_elist():
    Mytnik_sound_end = list()
    Mytnik_sound_end.append(pygame.mixer.Sound("sound/end_sound/Mytnik/kur.wav"))
    Mytnik_sound_end.append(pygame.mixer.Sound("sound/end_sound/Mytnik/kuuurwa.wav"))
    return Mytnik_sound_end


def make_Maciek_slist():
    Mytnik_sound_start = list()
    Mytnik_sound_start.append(pygame.mixer.Sound("sound/start_sound/Mytnik/halo_karthus.wav"))
    Mytnik_sound_start.append(pygame.mixer.Sound("sound/start_sound/Mytnik/i believe i can fly.wav"))
    return Mytnik_sound_start


def make_classic_elist():
    classic_e = list()
    classic_e.append(pygame.mixer.Sound("sound/end_classics/wpizdu_wyladowal.mp3"))
    classic_e.append(pygame.mixer.Sound("sound/end_classics/no_co_narobiliscie.mp3"))
    return classic_e


def make_classic_slist():
    classic_s = list()
    classic_s.append(pygame.mixer.Sound("sound/start_classics/bede_gral_w_gre.mp3"))
    classic_s.append(pygame.mixer.Sound("sound/start_classics/jedziemy_malina.mp3"))
    return classic_s


# def make_classic_evideo(): #TODO pygame movie module was removed - probably it's impossible to put video into game
#     classic_evideo = list()
#     classic_evideo.append(pygame..Movie("video/classic_end/no_co_narobiliscie.mp4"))
#     return classic_evideo
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

BIRDFLAP = pygame.USEREVENT + 1
pygame.time.set_timer(BIRDFLAP, 200)

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


with open("highscore.txt", 'r') as f:
    Normal_highscore = int(f.readline())
    Mytnik_highscore = int(f.readline())
    Strychala_highscore = int(f.readline())
    Jacek_highscore = int(f.readline())
    Jasiek_highscore = int(f.readline())
    f.close()

#listy z dźwiękami
background_music_list = make_background_music_list()

Jacek_sound_start = make_Jacek_slist()
Jacek_sound_end = make_Jacek_elist()
Mytnik_sound_end = make_Maciek_elist()
Mytnik_sound_start = make_Maciek_slist()

classic_end_sound = make_classic_elist()
classic_start_sound = make_classic_slist()


Mytnik = HeroFace("Mytnik/Mytnik_face_down.png", "Mytnik/Mytnik_face_mid.png", "Mytnik/Mytnik_face_up.png", "Mytniś:", Mytnik_sound_start, Mytnik_sound_end, Mytnik_highscore)

Normal_blue = HeroFace("Normal_blue/bluebird-downflap.png", "Normal_blue/bluebird-midflap.png", "Normal_blue/bluebird-upflap.png",  "Bluebird", Mytnik_sound_start, classic_end_sound, Normal_highscore)

Strychala = HeroFace("Strychala/Strychala_face_down2.png", "Strychala/Strychala_face_mid2.png", "Strychala/Strychala_face_up2.png",  "Strychala", Mytnik_sound_start, Mytnik_sound_end, Strychala_highscore)

Jacek = HeroFace("Jacek/Jacek_down.png", "Jacek/Jacek_mid.png", "Jacek/Jacek_up.png", "Jacula", Jacek_sound_start, Jacek_sound_end, Jacek_highscore)

Jasiek = HeroFace("Jasiek/Jasiek_down.png", "Jasiek/Jasiek_mid.png", "Jasiek/Jasiek_up.png", "Jasiu", Jacek_sound_start, Jacek_sound_end, Jasiek_highscore)
BIRD_TYPE = Normal_blue

#music setting
play_background_music()
pygame.mixer.music.set_volume(0.23)
music_switch = True
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
                BIRD_TYPE.play_start_sound()
                BIRD_TYPE.bird_rect.center = (int(BG_SIZE[0]/4), int(BG_SIZE[1]/4))
                bird_movement = 0
                score = 0
            if event.key == pygame.K_ESCAPE and not game_active:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_7 and not game_active:
                BIRD_TYPE = Mytnik
            if event.key == pygame.K_6 and not game_active:
                BIRD_TYPE = Strychala
            if event.key == pygame.K_4 and not game_active:
                BIRD_TYPE = Jacek
            if event.key == pygame.K_1 and not game_active:
                BIRD_TYPE = Jasiek
            if event.key == pygame.K_0 and not game_active:
                BIRD_TYPE = Normal_blue
            if event.key == pygame.K_s and not game_active:
                settings_flag = True
                draw_settings()
                # settings_flag = not settings_flag
                #reaction -> change_settings()
                #escape -> change flag
            if event.key == pygame.K_m:
                #turn off music
                music_switch = switch_music(music_switch)
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
                # screen.blit(game_over_surface, game_over_rect)
                # screen.blit(Mytnik.hero_look_surface, Mytnik.rect)
                screen.blit(bg_surface, (0, 0))
                BIRD_TYPE.play_end_sound()
                # settings_flag = not settings_flag

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
        if not(check_collision(pipe_list)):
            if score > BIRD_TYPE.highscore:
                BIRD_TYPE.highscore = update_highscore(score, BIRD_TYPE)
            else:
                BIRD_TYPE.play_end_sound()
                pygame.time.wait(2000)
            time.sleep(2)
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

        if not settings_flag:
            draw_clown_surface()
            draw_choosing_hereos()




    # Floor
    floor_x_pos -= 1
    draw_floor(screen, floor_x_pos)

    if floor_x_pos <= -BG_SIZE[0]:
        floor_x_pos = 0

    score_display(game_active, BIRD_TYPE)
    pygame.display.update()
    clock.tick(90)


#TODO LIST
#Remove sounds interupting
#Develope setting menu
#Create normal_bird features
#Apply dark and żubrówka mode
#Develop new heroes
#check collision - bigger tolerance

#PREVIOUS CODE
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
