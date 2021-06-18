#-----------------------------AUTHOR: Follow on Instagram @_.b_a_a_g_h_i._ -------------------------------#

import pygame


pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 1280, 660
BLACK = (0, 0, 0)
WHITE = (255, 255 ,255)
YELLOW = (204, 170, 0)
RED = (255, 0, 0)



WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('IRON GAUNTLET!')


BULLET_HIT_SOUND =pygame.mixer.Sound(r'Grenade+1.mp3')
BULLET_FIRE_SOUND =pygame.mixer.Sound(r'Gun+Silencer.mp3')
BACKGROUND_SOUND = pygame.mixer.Sound(r'Avengers Suite (Theme) 128 kbps.mp3')


ICON = pygame.image.load(r'icon.ico')
BACKGRND = pygame.transform.scale(pygame.image.load(r'GY8Rg8f.png'),(WIDTH, HEIGHT))
IRON_MAN = pygame.transform.scale(pygame.image.load(r'ironmannew.png'),(100,140))
THANOS = pygame.transform.scale(pygame.image.load(r'thanos1.png'),(100,140))


BORDER = pygame.Rect(WIDTH//2-5, 0, 10, HEIGHT)

IRONMAN_HIT = pygame.USEREVENT + 1
THANOS_HIT = pygame.USEREVENT + 2

HEALTH_FONT = pygame.font.SysFont('comicsans', 40, bold=True )
WINNER_FONT = pygame.font.SysFont('georgia',100, bold=True, italic=True)

FPS = 60
VEL = 5
BULLET_VEL = 15
MAX_BULLETS = 2


def draw_window(ironman, thanos, laser_beam, stone_beam, thanos_health, ironman_health):
    pygame.display.set_icon(ICON)
    WIN.blit(BACKGRND,(0, 0))
    thanos_health_text = HEALTH_FONT.render('HEALTH:' + str(thanos_health)+'%', 1, BLACK)
    ironman_health_text = HEALTH_FONT.render('HEALTH:' + str(ironman_health)+'%', 1, BLACK)
    WIN.blit(thanos_health_text, (WIDTH - thanos_health_text.get_width() - 10, 10))
    WIN.blit(ironman_health_text, (10, 10))
    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(IRON_MAN,(ironman.x, ironman.y))
    WIN.blit(THANOS,(thanos.x, thanos.y))

    for bullet in laser_beam:
        pygame.draw.rect(WIN, YELLOW, bullet)
    for bullet in stone_beam:
        pygame.draw.rect(WIN,RED,bullet)


    pygame.display.update()

def ironman_handle_movement(keys_pressed, ironman):
    if keys_pressed[pygame.K_a] and ironman.x- VEL > 0:  # left
        ironman.x -= VEL
    if keys_pressed[pygame.K_d] and ironman.x + VEL + ironman.width < BORDER.x:  # right
        ironman.x += VEL
    if keys_pressed[pygame.K_w] and ironman.y + VEL > 5:  # up
        ironman.y -= VEL
    if keys_pressed[pygame.K_s] and ironman.y + VEL + ironman.height < HEIGHT+15:  # down
        ironman.y += VEL



def thanos_handle_movement(keys_pressed, thanos):
    if keys_pressed[pygame.K_LEFT] and thanos.x +VEL> BORDER.width+ BORDER.x+5:  # left
        thanos.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and thanos.x + VEL + thanos.width< WIDTH:  # right
        thanos.x += VEL
    if keys_pressed[pygame.K_UP] and thanos.y - VEL +5> 0:  # up
        thanos.y -= VEL
    if keys_pressed[pygame.K_DOWN] and thanos.y + VEL + thanos.height< HEIGHT+15:  # down
        thanos.y += VEL

def handle_bullets(laser_beam, stone_beam, ironman, thanos):
    for bullet in laser_beam:
        bullet.x += BULLET_VEL
        if thanos.colliderect(bullet):
            pygame.event.post(pygame.event.Event(THANOS_HIT))
            laser_beam.remove(bullet)
        elif bullet.x > WIDTH:
           laser_beam.remove(bullet)

    for bullet in stone_beam:
        bullet.x -= BULLET_VEL
        if ironman.colliderect(bullet):
            pygame.event.post(pygame.event.Event(IRONMAN_HIT))
            stone_beam.remove(bullet)
        elif bullet.x > WIDTH:
            stone_beam.remove(bullet)





def draw_winner(text, ):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width()/2, HEIGHT/2- draw_text.get_width()/2+250))


    pygame.display.update()
    pygame.time.delay(5000)

def main():
    BACKGROUND_SOUND.play()
    ironman = pygame.Rect(212, 330, 100, 150)
    thanos = pygame.Rect(937, 330, 100, 150)

    laser_beam = []
    stone_beam = []
    ironman_health = 100
    thanos_health = 100

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(laser_beam)< MAX_BULLETS:
                    bullet = pygame.Rect(ironman.x + ironman.width-10, ironman.y +20, 25, 3)
                    laser_beam.append(bullet)
                    BULLET_FIRE_SOUND.play()
                if event.key == pygame.K_RCTRL and len(stone_beam)< MAX_BULLETS:
                    bullet = pygame.Rect(thanos.x-20, thanos.y + +20, 50, 6)
                    stone_beam.append(bullet)
                    BULLET_FIRE_SOUND.play()

            if event.type == THANOS_HIT:
                thanos_health -= 7
                BULLET_HIT_SOUND.play()

            if event.type == IRONMAN_HIT:
                ironman_health -= 9
                BULLET_HIT_SOUND.play()


        winner_text = ""
        if thanos_health <= 0:
            winner_text = "Iron Man Wins!"


        if ironman_health <= 0:
            winner_text = "Thanos Wins!"


        if winner_text != "":
            draw_winner(winner_text)

            break

        keys_pressed = pygame.key.get_pressed()
        ironman_handle_movement(keys_pressed, ironman)
        thanos_handle_movement(keys_pressed, thanos)
        handle_bullets(laser_beam, stone_beam, ironman, thanos)
        draw_window(ironman, thanos, laser_beam, stone_beam, thanos_health, ironman_health)
    main()
if __name__ == "__main__":
    main()

    
#-----------------------------AUTHOR: Follow on Instagram @_.b_a_a_g_h_i._ -------------------------------#

