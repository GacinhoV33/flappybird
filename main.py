import pygame, sys, random

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


pygame.init()
screen = pygame.display.set_mode(BG_SIZE)
clock = pygame.time.Clock()

#Game Variables
gravity = 0.25
bird_movement = 0
space_btw_pipes = BG_SIZE[1]/4

bg_surface = pygame.image.load(IMG_PATH + "background-day.png").convert()
bg_surface = pygame.transform.scale(bg_surface, BG_SIZE)

floor_surface = pygame.image.load(IMG_PATH + "base.png").convert()
floor_surface = pygame.transform.scale(floor_surface, (int(BG_SIZE[0]*1.5), int(BG_SIZE[1]/5)))
floor_x_pos = 0

bird_surface = pygame.image.load(IMG_PATH + "bluebird-midflap.png")
bird_surface = pygame.transform.scale(bird_surface, (int(BG_SIZE[0]/15), int(BG_SIZE[1]/20)))
bird_rect = bird_surface.get_rect(center=(int(BG_SIZE[0]/4), int(BG_SIZE[1]/2)))

pipe_surface = pygame.image.load(IMG_PATH + "pipe-green.png")
pipe_surface = pygame.transform.scale(pipe_surface, (int(BG_SIZE[0]/10), int(BG_SIZE[1]/1.5)))
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)
pipe_heights = [int(BG_SIZE[1]*0.4), int(BG_SIZE[1]*0.5), int(BG_SIZE[1]*0.6)] #int(BG_SIZE[1]*0.8) [int(BG_SIZE[1]*0.2),

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0 #preventing wrong moves
                bird_movement -= 10
        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())

    screen.blit(bg_surface, (0, 0))
    # Bird
    bird_movement += gravity
    bird_rect.centery += bird_movement

    screen.blit(bird_surface, bird_rect)
    # Pipes
    pipe_list = move_pipes(pipe_list)
    draw_pipes(pipe_list, screen)
    # Floor
    floor_x_pos -= 1
    draw_floor(screen, floor_x_pos)

    if floor_x_pos <= -BG_SIZE[0]:
        floor_x_pos = 0

    pygame.display.update()
    clock.tick(120)

