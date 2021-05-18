import pygame, sys, random
from typing import List
import time

#TODO ONE FUNCTION TO SHOW SCREEN
# MORE SOUNDS
# MORE HEREOS
# if you beat highscore, show winning frame!

HERO_PATH = "./heroes/"
IMG_PATH = "./imgs/"
BG_SIZE = (800, 1000)

#BIRD_SONGS =
PIPE_SPEED = 5

pygame.init()
screen = pygame.display.set_mode(BG_SIZE)
clock = pygame.time.Clock()
game_font = pygame.font.Font("04B_19.ttf", 40)

#Game Variables
gravity = 0.25
bird_movement = 0
space_btw_pipes = int(BG_SIZE[1]/4)
score = 0
high_score = 0
click_pos = [0, 0]


#flags
game_active = False
settings_flag = False
Max_flag = False
Jacek_flag = False
Olaf_flag = False
Mytnik_flag = False
Fido_flag = False
Jasiek_flag = False
Maksiu_flag = False
Gacek_flag = False
start_game_flag = True

#load everything
game_font2 = pygame.font.Font("04B_19.ttf", 70)

#you lost display
surface1 = game_font2.render("YOU LOST!", True, (255, 255, 255))
surface1_rect = surface1.get_rect(center=(int(BG_SIZE[0] / 2), int(BG_SIZE[1] / 4)))


#choose hero 2
game_font3 = pygame.font.Font("04B_19.ttf", 50)
choose_hero_surface = game_font3.render("Choose your hero: ", True, (255, 255, 255))
choose_hero_surface_rect = choose_hero_surface.get_rect(center=(int(BG_SIZE[0] / 2), int(BG_SIZE[1] / 20)))

Olaf_choose_im_color = pygame.image.load("intro/Olaf_color.png").convert_alpha()
Olaf_choose_im_color = pygame.transform.scale(Olaf_choose_im_color, (int(BG_SIZE[0]/5)+10, int(BG_SIZE[0]/5)+10))
Olaf_choose_color_rect = Olaf_choose_im_color.get_rect()

Olaf_choose_im = pygame.image.load("intro/Olaf.png").convert_alpha()
Olaf_choose_im = pygame.transform.scale(Olaf_choose_im, (int(BG_SIZE[0]/5), int(BG_SIZE[0]/5)))
Olaf_choose_rect = Olaf_choose_im.get_rect()


Mytnik_choose_im_color = pygame.image.load("intro/Mytnik_color.png").convert_alpha()
Mytnik_choose_im_color = pygame.transform.scale(Mytnik_choose_im_color, (int(BG_SIZE[0] / 5) + 10, int(BG_SIZE[0] / 5) + 10))
Mytnik_choose_rect = Mytnik_choose_im_color.get_rect()

Mytnik_choose_im = pygame.image.load("intro/Mytnik.png").convert_alpha()
Mytnik_choose_im = pygame.transform.scale(Mytnik_choose_im, (int(BG_SIZE[0]/5), int(BG_SIZE[0]/5)))
# Mytnik_choose_rect = Mytnik_choose_im.get_rect()

Fido_choose_im_color = pygame.image.load("intro/Fido_color.png").convert_alpha()
Fido_choose_im_color = pygame.transform.scale(Fido_choose_im_color, (int(BG_SIZE[0] / 5) + 10, int(BG_SIZE[0] / 5) + 10))
Fido_choose_color_rect = Fido_choose_im_color.get_rect()

Fido_choose_im = pygame.image.load("intro/Fido.png").convert_alpha()
Fido_choose_im = pygame.transform.scale(Fido_choose_im, (int(BG_SIZE[0] / 5), int(BG_SIZE[0] / 5)))
Fido_choose_rect = Fido_choose_im.get_rect()

Jasiek_choose_im_color = pygame.image.load("intro/Jasiek_color.png").convert_alpha()
Jasiek_choose_im_color = pygame.transform.scale(Jasiek_choose_im_color, (int(BG_SIZE[0] / 5) + 10, int(BG_SIZE[0] / 5)+10))
Jasiek_choose_color_rect = Jasiek_choose_im_color.get_rect()

Jasiek_choose_im = pygame.image.load("intro/Jasiek.png").convert_alpha()
Jasiek_choose_im = pygame.transform.scale(Jasiek_choose_im, (int(BG_SIZE[0] / 5), int(BG_SIZE[0] / 5)))
Jasiek_choose_rect = Jasiek_choose_im.get_rect()

Maksiu_choose_im_color = pygame.image.load("intro/Maksymowicz_color.png").convert_alpha()
Maksiu_choose_im_color = pygame.transform.scale(Maksiu_choose_im_color, (int(BG_SIZE[0] / 5) + 10, int(BG_SIZE[0] / 5)+10))
Maksiu_choose_rect_color = Maksiu_choose_im_color.get_rect()

Maksiu_choose_im = pygame.image.load("intro/Maksymowicz.png").convert_alpha()
Maksiu_choose_im = pygame.transform.scale(Maksiu_choose_im, (int(BG_SIZE[0] / 5), int(BG_SIZE[0] / 5)))
Maksiu_choose_rect = Maksiu_choose_im.get_rect()

Gacek_choose_im_color = pygame.image.load("intro/Gacek_color.png").convert_alpha()
Gacek_choose_im_color = pygame.transform.scale(Gacek_choose_im_color, (int(BG_SIZE[0] / 5), int(BG_SIZE[0] / 5)))
Gacek_choose_rect_color = Gacek_choose_im_color.get_rect()

Gacek_choose_im = pygame.image.load("intro/Gacek.png").convert_alpha()
Gacek_choose_im = pygame.transform.scale(Gacek_choose_im, (int(BG_SIZE[0] / 5), int(BG_SIZE[0] / 5)))
Gacek_choose_rect = Gacek_choose_im.get_rect()

Max_choose_im_color = pygame.image.load("intro/Max_color.png").convert_alpha()
Max_choose_im_color = pygame.transform.scale(Max_choose_im_color, (int(BG_SIZE[0] / 5), int(BG_SIZE[0] / 5)))
Max_choose_color_rect = Max_choose_im_color.get_rect()

Max_choose_im = pygame.image.load("intro/Max.png").convert_alpha()
Max_choose_im = pygame.transform.scale(Max_choose_im, (int(BG_SIZE[0] / 5), int(BG_SIZE[0] / 5)))
Max_choose_rect = Max_choose_im.get_rect()

Jacek_choose_im_color = pygame.image.load("intro/Jacek_color.png").convert_alpha()
Jacek_choose_im_color = pygame.transform.scale(Jacek_choose_im_color, (int(BG_SIZE[0] / 5), int(BG_SIZE[0] / 5)))
Jacek_choose_color_rect = Jacek_choose_im_color.get_rect()

Jacek_choose_im = pygame.image.load("intro/Jacek.png").convert_alpha()
Jacek_choose_im = pygame.transform.scale(Jacek_choose_im, (int(BG_SIZE[0] / 5), int(BG_SIZE[0] / 5)))
Jacek_choose_rect = Jacek_choose_im.get_rect()


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
    score_rect = score_surface.get_rect(center=(int(BG_SIZE[0] / 2), 60))
    screen.blit(score_surface, score_rect)
    # if not game_active and not settings_flag:


def highscore_display(hero: HeroFace):
    highscore_surface = game_font.render(hero.hero_name + " highscore: " + str(int(hero.highscore)), True, (255, 255, 255))
    highscore_surface_rect = highscore_surface.get_rect(center=(int(BG_SIZE[0] / 2), 110))
    screen.blit(highscore_surface, highscore_surface_rect)


def show_intro():
    intro_surface = pygame.image.load("imgs/clown_together_aka_zubrowka.jpg").convert_alpha()
    intro_surface = pygame.transform.scale(intro_surface, (int(BG_SIZE[0]), int(BG_SIZE[0])))
    intro_rect = intro_surface.get_rect(center=(int(BG_SIZE[0])/2, int(BG_SIZE[1])/2))
    wodka_right_surface = pygame.image.load("imgs/wodka_right.jpg").convert_alpha()
    wodka_right_surface = pygame.transform.scale(wodka_right_surface, (int(BG_SIZE[0]), int((BG_SIZE[1] - BG_SIZE[0])/2)))
    wodka_rect = wodka_right_surface.get_rect(center=(int(BG_SIZE[0]) / 2, int(BG_SIZE[1]-BG_SIZE[0])))
    background_intro_surface = pygame.image.load("imgs/background_intro.jpg").convert_alpha()
    background_intro_surface = pygame.transform.scale(background_intro_surface, (int(BG_SIZE[0]), int((BG_SIZE[1] - BG_SIZE[0])/2)))
    background_intro_surface_rect_up = background_intro_surface.get_rect(center=(int(BG_SIZE[0]/2), int((BG_SIZE[1] - BG_SIZE[0])/4)))
    background_intro_surface_rect_down = background_intro_surface.get_rect(center=(int(BG_SIZE[0]/2), int(BG_SIZE[1] - (BG_SIZE[1] - BG_SIZE[0])/4)))
    #TODO
    game_name = game_font3.render("CLOWNBIRD", True, (255, 255, 255))
    game_name_rect = game_name.get_rect(center=(int(BG_SIZE[0]/2), int(BG_SIZE[1]/20)))
    screen.blit(wodka_right_surface, wodka_rect)
    screen.blit(intro_surface, intro_rect)
    screen.blit(background_intro_surface, background_intro_surface_rect_up)
    screen.blit(background_intro_surface, background_intro_surface_rect_down)
    screen.blit(game_name, game_name_rect)
    pygame.display.update()
    pygame.time.wait(4500)
    return False


#Highscore functions
def show_highscore_display(hero):
    highscore_beat_surf = game_font.render("You've beaten " + hero.hero_name + " highscore!", True,
                                         (255, 255, 255))
    highscore_beat_rect = highscore_beat_surf.get_rect(center=(int(BG_SIZE[0] / 2), int(BG_SIZE[1]/5)))
    screen.blit(highscore_beat_surf, highscore_beat_rect)
    pygame.display.update()
    #TODO funny image with hero


def update_highscore(score, hero):
    if score > hero.highscore:
        hero.highscore = int(score)
        beat_highscore_sound.play()
        show_highscore_display(hero)
        #you_won()
        pygame.time.wait(4000)
        save_highscores()
    return hero.highscore


def save_highscores():
    with open("highscore.txt", "w") as file:
        file.write(str(Normal_blue.highscore) + "\n" + str(Mytnik.highscore) + "\n" + str(Strychala.highscore) +
                   "\n" + str(Jacek.highscore) + "\n" + str(Jasiek.highscore) + "\n" + str(Gacek.highscore) + "\n" +
                   str(Fido.highscore) + "\n" + str(Maksymowicz.highscore) + "\n" + str(Olaf.highscore))
        file.close()


def you_lost_display(hero: HeroFace):
    # rand_number = random.randint(0, len(list_of_end_words)-1)
    # surface1 = game_font2.render(list_of_end_words[rand_number], True, (255, 255, 255))
    screen.blit(surface1, surface1_rect)

    # funny_image =

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


def draw_choosing_hereos2(Max_flag, Jacek_flag, Olaf_flag, Mytnik_flag, Fido_flag, Jasiek_flag, Maksiu_flag, Gacek_flag):
    screen.blit(choose_hero_surface, choose_hero_surface_rect)

    if Olaf_flag:
        screen.blit(Olaf_choose_im_color, dest=[int(BG_SIZE[0] / 10), int(BG_SIZE[1] / 2.5)])
    else:
        screen.blit(Olaf_choose_im, dest=[int(BG_SIZE[0]/10), int(BG_SIZE[1]/2.5)])

    if Mytnik_flag:
        screen.blit(Mytnik_choose_im_color, dest=[int(BG_SIZE[0] / 10) * 4, int(BG_SIZE[1] / 2.5)])
    else:
        screen.blit(Mytnik_choose_im, dest=[int(BG_SIZE[0]/10) * 4, int(BG_SIZE[1]/2.5)])

    if Fido_flag:
        screen.blit(Fido_choose_im_color, dest=[int(BG_SIZE[0] / 10) * 7, int(BG_SIZE[1] / 2.5)])
    else:
        screen.blit(Fido_choose_im, dest=[int(BG_SIZE[0] / 10) * 7, int(BG_SIZE[1] / 2.5)])

    if Jasiek_flag:

        screen.blit(Jasiek_choose_im_color, dest=[int(BG_SIZE[0] / 10), int(BG_SIZE[1] / 1.7)])
    else:

        screen.blit(Jasiek_choose_im, dest=[int(BG_SIZE[0] / 10), int(BG_SIZE[1] / 1.7)])

    if Maksiu_flag:
        screen.blit(Maksiu_choose_im_color, dest=[int(BG_SIZE[0] / 10) * 4, int(BG_SIZE[1] / 1.7)])
    else:
        screen.blit(Maksiu_choose_im, dest=[int(BG_SIZE[0] / 10) * 4, int(BG_SIZE[1] / 1.7)])

    if Gacek_flag:
        screen.blit(Gacek_choose_im_color, dest=[int(BG_SIZE[0] / 10) * 7, int(BG_SIZE[1] / 1.7)])
    else:
        screen.blit(Gacek_choose_im, dest=[int(BG_SIZE[0] / 10) * 7, int(BG_SIZE[1] / 1.7)])

    if Max_flag:
        screen.blit(Max_choose_im_color, dest=[int(BG_SIZE[0] / 10) * 2.5, int(BG_SIZE[1] / 4.8)])
    else:
        screen.blit(Max_choose_im, dest=[int(BG_SIZE[0] / 10) * 2.5, int(BG_SIZE[1] / 4.8)])

    if Jacek_flag:

        screen.blit(Jacek_choose_im_color, dest=[int(BG_SIZE[0] / 10) * 5.5, int(BG_SIZE[1] / 4.8)])
    else:
        screen.blit(Jacek_choose_im, dest=[int(BG_SIZE[0] / 10) * 5.5, int(BG_SIZE[1] / 4.8)])


def show_hero_name(birdtype: HeroFace):
    hero_choosing_surface1 = game_font.render(birdtype.hero_name, True, (255, 255, 255))
    hero_choosing_surface_rect1 = hero_choosing_surface1.get_rect(center=(int(BG_SIZE[0] / 2), int(BG_SIZE[1] / 20 * 2.5)))
    screen.blit(hero_choosing_surface1, hero_choosing_surface_rect1)

# def draw_clown_surface():
#     clown_surface = pygame.image.load(IMG_PATH + "clown_together.jpg").convert_alpha()
#     clown_surface = pygame.transform.scale(clown_surface, (BG_SIZE[0], BG_SIZE[1]))
#     clown_rect = game_over_surface.get_rect()
#     screen.blit(clown_surface, clown_rect)
#     time.sleep(1.25) #sleep after losing game

#
# def draw_settings():
#     resolution_surface = game_font.render("Resolution ", True, (255, 255, 255))
#     resolution_surface_rect = resolution_surface.get_rect(center=(int(BG_SIZE[0] / 4), int(BG_SIZE[1]/20 * 15)))
#     screen.blit(bg_surface, (0, 0))
#     screen.blit(resolution_surface, resolution_surface_rect)

    #TODO


#Functions with sounds_lists
def make_background_music_list():
    background_music_list = list()
    background_music_list.append("music_in_back/Jaramy_Jaramy.wav")
    background_music_list.append("music_in_back/Czuje_banie.wav")
    background_music_list.append("music_in_back/Young_Kit$hxOlaf_PDW.wav")
    return background_music_list


def play_background_music():
    pygame.mixer.music.load(background_music_list[0])
    pygame.mixer.music.play()
    for el in background_music_list[1:]:
        pygame.mixer.music.queue(el)


def show_music_settings(flag: bool):
    if flag:
        music_surface = pygame.image.load("imgs/sound_emote_on.png").convert_alpha()
        music_surface = pygame.transform.scale(music_surface, (int(BG_SIZE[0]/20), int(BG_SIZE[0]/20)))
        music_surface_rect = game_over_surface.get_rect()
        screen.blit(music_surface, (int(BG_SIZE[0]/20) * 17, int(BG_SIZE[1]/35)))
    else:
        music_off_surface = pygame.image.load("imgs/sound_off.png")
        music_off_surface = pygame.transform.scale(music_off_surface, (int(BG_SIZE[0]/20), int(BG_SIZE[0]/20)))
        screen.blit(music_off_surface, (int(BG_SIZE[0]/20) * 17, int(BG_SIZE[1]/35)))


def switch_music(flag_music):
    if flag_music:
        pygame.mixer.music.unpause()

    else:
        pygame.mixer.music.pause()


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


def make_Fido_slist():
    pass


def make_Fido_elist():
    pass


def make_Gacek_slist():
    pass


def make_Gacek_elist():
    pass


def make_Jasiek_slist():
    Jan_start_list = list()
    Jan_start_list.append(pygame.mixer.Sound("sound/start_sound/Jasiek/amor1.wav"))
    Jan_start_list.append(pygame.mixer.Sound("sound/start_sound/Jasiek/amor2.wav"))
    return Jan_start_list

def make_Jasiek_elist():
    pass


def make_Olaf_slist():
    pass


def make_Olaf_elist():
    pass


def make_Maksymowicz_slist():
    Maksymowicz_slist = list()
    Maksymowicz_slist.append(pygame.mixer.Sound("sound/start_sound/Maksymowicz/pijemy.wav"))
    return Maksymowicz_slist


def make_Maksymowicz_elist():
    Maksymowicz_elist = list()
    Maksymowicz_elist.append(pygame.mixer.Sound("sound/end_sound/Maksymowicz/bede_rzygol.wav"))
    return Maksymowicz_elist


def make_classic_elist():
    classic_e = list()
    classic_e.append(pygame.mixer.Sound("sound/end_classics/wpizdu_wyladowal.wav"))
    classic_e.append(pygame.mixer.Sound("sound/end_classics/no_co_narobiliscie.wav"))
    return classic_e


def make_classic_slist():
    classic_s = list()
    classic_s.append(pygame.mixer.Sound("sound/start_classics/bede_gral_w_gre.wav"))
    classic_s.append(pygame.mixer.Sound("sound/start_classics/jedziemy_malina.wav"))
    return classic_s


def restore_initial_sett():
    pipe_list.clear()  # restoring initial conditions of game, otherwise we would met bugs
    BIRD_TYPE.play_start_sound()
    BIRD_TYPE.bird_rect.center = (int(BG_SIZE[0] / 4), int(BG_SIZE[1] / 4))


# def make_classic_evideo(): #TODO pygame movie module was removed - probably it's impossible to put video into game

# pygame.mixer.pre_init(frequency=44100, size=16, channels=1, buffer=512)





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
beat_highscore_sound = pygame.mixer.Sound("sound/win.wav")


with open("highscore.txt", 'r') as f:
    Normal_highscore = int(f.readline())
    Mytnik_highscore = int(f.readline())
    Strychala_highscore = int(f.readline())
    Jacek_highscore = int(f.readline())
    Jasiek_highscore = int(f.readline())
    Gacek_highscore = int(f.readline())
    Fido_highscore = int(f.readline())
    Maksymowicz_highscore = int(f.readline())
    Olaf_highscore = int(f.readline())
    f.close()

#listy z dźwiękami
background_music_list = make_background_music_list()

Jacek_sound_start = make_Jacek_slist()
Jacek_sound_end = make_Jacek_elist()
Mytnik_sound_end = make_Maciek_elist()
Mytnik_sound_start = make_Maciek_slist()
Jasiek_sound_start = make_Jasiek_slist()
# Fido_sound_start = make_Fido_slist()
# Fido_end_start = make_Fido_elist()
Maksymowicz_sound_start = make_Maksymowicz_slist()
Maksymowicz_sound_end = make_Maksymowicz_elist()

classic_end_sound = make_classic_elist()
classic_start_sound = make_classic_slist()

# list_of_end_words = ["Fatalnie :(", "Fido by lepiej zagral", "rzal.pl"]

Mytnik = HeroFace("Mytnik/Mytnik_down.png", "Mytnik/Mytnik_mid.png", "Mytnik/Mytnik_up.png", "Mytnik", Mytnik_sound_start, Mytnik_sound_end, Mytnik_highscore)

Normal_blue = HeroFace("Normal_blue/bluebird-downflap.png", "Normal_blue/bluebird-midflap.png", "Normal_blue/bluebird-upflap.png",  "Bluebird", Mytnik_sound_start, classic_end_sound, Normal_highscore)

Strychala = HeroFace("Strychala/Strychala_face_down2.png", "Strychala/Strychala_face_mid2.png", "Strychala/Strychala_face_up2.png",  "Strychala", Mytnik_sound_start, Mytnik_sound_end, Strychala_highscore)

Jacek = HeroFace("Jacek/Jacek_down.png", "Jacek/Jacek_mid.png", "Jacek/Jacek_up.png", "Jacula", Jacek_sound_start, Jacek_sound_end, Jacek_highscore)

Jasiek = HeroFace("Jasiek/Jasiek_down.png", "Jasiek/Jasiek_mid.png", "Jasiek/Jasiek_up.png", "Jasiu", Jasiek_sound_start, Jacek_sound_end, Jasiek_highscore)

Fido = HeroFace("Fido/Fido_down.png", "Fido/Fido_mid.png", "Fido/Fido_up.png", "Fido", classic_start_sound, classic_end_sound, Fido_highscore)

Maksymowicz = HeroFace("Maksymowicz/Maksymowicz_down.png", "Maksymowicz/Maksymowicz_mid.png", "Maksymowicz/Maksymowicz_up.png", "Maksymowicz", Maksymowicz_sound_start, Maksymowicz_sound_end, Maksymowicz_highscore)

Olaf = HeroFace("Olaf/Olaf_down.png", "Olaf/Olaf_mid.png", "Olaf/Olaf_up.png", "Pan Prezydent", Jacek_sound_start, Jacek_sound_end, Olaf_highscore)

Gacek = HeroFace("Gacek/Gacek_down.png", "Gacek/Gacek_mid.png", "Gacek/Gacek_up.png", "Gacinho", classic_start_sound, classic_end_sound, Gacek_highscore)


BIRD_TYPE = Normal_blue



#music setting
play_background_music()
pygame.mixer.music.set_volume(0.33)
music_switch = True


while True:
    if start_game_flag:
        start_game_flag = show_intro()

    for event in pygame.event.get():
        click_pos = [0, 0]  #mouse for choosing heroes

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
            # if event.key == pygame.K_s and not game_active:
            #     settings_flag = True
            #     draw_settings()
                # settings_flag = not settings_flag
                #reaction -> change_settings()
                #escape -> change flag
            if event.key == pygame.K_m:
                #turn off music
                switch_music(music_switch)
        #settings
        # if event.type == pygame.MOUSEBUTTONUP and not game_active:
        #     mouse_postion = pygame.mouse.get_pos()
        #     if hero_choosing_surface_rect10.collidepoint(mouse_postion) and pygame.mouse.get_pressed(num_buttons=5)[0]:
        #         settings_flag = True
        #         #TODO
        #         #Show_settings_screen
        #         #if choose something do something
        #         #do resolution change
        #         #do speed change
        #         #do color of backgroumd change
        #         #do żubrówka change
        #         # screen.blit(game_over_surface, game_over_rect)
        #         # screen.blit(Mytnik.hero_look_surface, Mytnik.rect)
        #         screen.blit(bg_surface, (0, 0))
        #         BIRD_TYPE.play_end_sound()
        #         # settings_flag = not settings_flag
        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())
        if event.type == BIRDFLAP:
            if BIRD_TYPE.bird_index < 2:
                BIRD_TYPE.bird_index += 1
            else:
                BIRD_TYPE.bird_index = 0

        if event.type == pygame.MOUSEBUTTONDOWN:
            click_pos = pygame.mouse.get_pos()
            print(click_pos)
    screen.blit(bg_surface, (0, 0))

    if game_active:
        # Bird
        score_display(game_active, BIRD_TYPE)
        bird_movement += gravity
        rotated_bird = rotate_bird(BIRD_TYPE.bird_frames[BIRD_TYPE.bird_index])
        BIRD_TYPE.bird_rect.centery += bird_movement
        if not (check_collision(pipe_list)):
            if score > BIRD_TYPE.highscore:
                BIRD_TYPE.highscore = update_highscore(score, BIRD_TYPE)
            else:
                BIRD_TYPE.play_end_sound()
                pygame.time.wait(750)
                # BIRD_TYPE.end_graphic() TODO
                highscore_display(BIRD_TYPE)
                you_lost_display(BIRD_TYPE)
                pygame.display.update()
                pygame.time.wait(4000)

            game_active = False  # checking whether you touched pipe or bottom/top and ending game

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

        # draw_clown_surface()
        show_music_settings(music_switch)
        if BG_SIZE[0]/80 * 21 < pygame.mouse.get_pos()[0] < BG_SIZE[0]/80 * 34 and BG_SIZE[1]/100 * 21 < pygame.mouse.get_pos()[1] < BG_SIZE[1]/100 * 34:
            Max_flag = True
            BIRD_TYPE = Strychala
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)
            show_hero_name(BIRD_TYPE)
            if BG_SIZE[0]/80 * 21 < click_pos[0] < BG_SIZE[0]/80 * 34 and  BG_SIZE[1]/100 * 21 < click_pos[1] < BG_SIZE[1]/100 * 34:
                restore_initial_sett()
                PIPE_SPEED = 5
                bird_movement = 0
                score = 0
                game_active = True
                pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)

        else:
            Max_flag = False

        if BG_SIZE[0]/80 * 44.5 < pygame.mouse.get_pos()[0] < BG_SIZE[0]/80 * 60 and BG_SIZE[1]/100 * 22.5 < pygame.mouse.get_pos()[1] < BG_SIZE[1]/100 * 35.5:
            Jacek_flag = True
            BIRD_TYPE = Jacek
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)
            show_hero_name(BIRD_TYPE)
            if BG_SIZE[0]/80 * 44.5 < click_pos[0] < BG_SIZE[0]/80 * 60 and BG_SIZE[1]/100 * 22.5 < click_pos[1] < BG_SIZE[1]/100 * 35.5:
                restore_initial_sett()
                PIPE_SPEED = 5
                bird_movement = 0
                score = 0
                game_active = True
                pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)
        else:
            Jacek_flag = False

        if BG_SIZE[0]/80 * 8.5 < pygame.mouse.get_pos()[0] < BG_SIZE[0]/80 * 24 and BG_SIZE[1]/100 * 40 < pygame.mouse.get_pos()[1] < BG_SIZE[1]/100 * 54.5:
            Olaf_flag = True
            BIRD_TYPE = Olaf
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)
            show_hero_name(BIRD_TYPE)
            if BG_SIZE[0]/80 * 8.5 < click_pos[0] < BG_SIZE[0]/80 * 24 and BG_SIZE[1]/100 * 40 < click_pos[1] < BG_SIZE[1]/100 * 54.5:
                restore_initial_sett()
                PIPE_SPEED = 5
                bird_movement = 0
                score = 0
                game_active = True
                pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)
        else:
            Olaf_flag = False

        if BG_SIZE[0]/80 * 32 < pygame.mouse.get_pos()[0] < BG_SIZE[0]/80 * 47.5 and BG_SIZE[1]/100 * 40.5 < pygame.mouse.get_pos()[1] < BG_SIZE[1]/100 * 54.5:
            Mytnik_flag = True
            BIRD_TYPE = Mytnik
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)
            show_hero_name(BIRD_TYPE)
            if BG_SIZE[0]/80 * 32 < click_pos[0] < BG_SIZE[0]/80 * 47.5 and BG_SIZE[1]/100 * 40.5 < click_pos[1] < BG_SIZE[1]/100 * 54.5:
                restore_initial_sett()
                PIPE_SPEED = 5
                bird_movement = 0
                score = 0
                game_active = True
                pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)
        else:
            Mytnik_flag = False

        if BG_SIZE[0]/80 * 57 < pygame.mouse.get_pos()[0] < BG_SIZE[0]/80 * 70.5 and BG_SIZE[1]/100 * 40.5 < pygame.mouse.get_pos()[1] < BG_SIZE[1]/100 * 54.5:
            Fido_flag = True
            BIRD_TYPE = Fido
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)
            show_hero_name(BIRD_TYPE)
            if BG_SIZE[0]/80 * 57 < click_pos[0] < BG_SIZE[0]/80 * 70.5 and 405 < click_pos[1] < BG_SIZE[1]/100 * 54.5:
                restore_initial_sett()
                PIPE_SPEED = 5
                bird_movement = 0
                score = 0
                game_active = True
                pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)
        else:
            Fido_flag = False

        if BG_SIZE[0]/80 * 10 < pygame.mouse.get_pos()[0] < BG_SIZE[0]/80 * 22 and BG_SIZE[1]/100 * 59.5 < pygame.mouse.get_pos()[1] < BG_SIZE[1]/100 * 74:
            Jasiek_flag = True
            BIRD_TYPE = Jasiek
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)
            show_hero_name(BIRD_TYPE)
            if BG_SIZE[0]/80 * 10 < click_pos[0] < BG_SIZE[0]/80 * 22 and BG_SIZE[1]/100 * 59.5 < click_pos[1] < BG_SIZE[1]/100 * 74:
                restore_initial_sett()
                PIPE_SPEED = 5
                bird_movement = 0
                score = 0
                game_active = True
                pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)
        else:
            Jasiek_flag = False

        if BG_SIZE[0]/80 * 32.5 < pygame.mouse.get_pos()[0] < BG_SIZE[0]/80 * 46.5 and BG_SIZE[1]/100 * 59.5 < pygame.mouse.get_pos()[1] < BG_SIZE[1]/100 * 73:
            Maksiu_flag = True
            BIRD_TYPE = Maksymowicz
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)
            show_hero_name(BIRD_TYPE)
            if BG_SIZE[0]/80 * 32.5 < click_pos[0] < BG_SIZE[0]/80 * 46.5 and BG_SIZE[1]/100 * 59.5 < click_pos[1] < BG_SIZE[1]/100 * 73:
                restore_initial_sett()
                PIPE_SPEED = 5
                bird_movement = 0
                score = 0
                game_active = True
                pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)
        else:
            Maksiu_flag = False

        if BG_SIZE[0]/80 * 56.5 < pygame.mouse.get_pos()[0] < BG_SIZE[0]/80 * 70.5 and BG_SIZE[1]/100 * 60 < pygame.mouse.get_pos()[1] < BG_SIZE[1]/100 * 74:
            Gacek_flag = True
            BIRD_TYPE = Gacek
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)
            show_hero_name(BIRD_TYPE)
            if BG_SIZE[0]/80 * 56.5 < click_pos[0] < BG_SIZE[0]/80 * 70.5 and BG_SIZE[1]/100 * 60 < click_pos[1] < BG_SIZE[1]/100 * 74:
                restore_initial_sett()
                PIPE_SPEED = 5
                bird_movement = 0
                score = 0
                game_active = True
                pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)
        else:
            Gacek_flag = False

        if BG_SIZE[0]/80 * 67 < click_pos[0] < BG_SIZE[0]/80 * 72.5 and BG_SIZE[1]/100 * 3 < click_pos[1] < BG_SIZE[1]/100 *7:
            music_switch = not music_switch
            switch_music(music_switch)
            pygame.time.wait(90)

        draw_choosing_hereos2(Max_flag, Jacek_flag, Olaf_flag, Mytnik_flag, Fido_flag, Jasiek_flag, Maksiu_flag,
                              Gacek_flag)

    # Floor
    floor_x_pos -= 1
    draw_floor(screen, floor_x_pos)

    if floor_x_pos <= -BG_SIZE[0]:
        floor_x_pos = 0

    # score_display(game_active, BIRD_TYPE)
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
