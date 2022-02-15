import pygame,sys,os,random
pygame.font.init()
pygame.init()



WIDTH,HEIGHT =750,750

# Creating Window
WIN=pygame.display.set_mode((WIDTH,HEIGHT))

# giving caption
pygame.display.set_caption("Space Shooter")


# Load images

RED_SPACE_SHIP = pygame.image.load(os.path.join('assets', 'pixel_ship_red_small.png'))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join('assets', 'pixel_ship_green_small.png'))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join('assets', 'pixel_ship_blue_small.png'))


# Main Image
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join('assets', 'pixel_ship_yellow.png'))

# lasers
RED_LASER = pygame.image.load(os.path.join('assets', 'pixel_laser_red.png'))
BLUE_LASER = pygame.image.load(os.path.join('assets', 'pixel_laser_blue.png'))
GREEN_LASER = pygame.image.load(os.path.join('assets', 'pixel_laser_green.png'))
YELLOW_LASER = pygame.image.load(os.path.join('assets', 'pixel_laser_yellow.png'))

# Background_image:
BG=pygame.image.load(os.path.join('assets',"background-black.png"))
BG=pygame.transform.scale(BG,(WIDTH,HEIGHT))


# Abstract Class

class Ship:
    def __init__(self,x,y,health=100):
        self.x = x
        self.y = y
        self.health = health
        self_ship_img=None
        self.laser_img=None
        self.lasers=[]
        self.cool_down_counter =0

    def draw(self,window):
        window.blit(self.ship_img,(self.x,self.y))

    def get_width(self):
        return self.ship_img.get_width()
    def get_height(self):
        return self.ship_img.get_height()        


# Player Class
     
class Player(Ship):
    def __init__(self,x,y,health=100):
        super().__init__(x,y,health)
        self.ship_img = YELLOW_SPACE_SHIP
        self.laser_img = YELLOW_LASER
        self.mask =pygame.mask.from_surface(self.ship_img)
        self.max_health =health



# Enemy Class

class Enemy(Ship):
    COLOR_MAP = {
                "red": (RED_SPACE_SHIP, RED_LASER),
                "green": (GREEN_SPACE_SHIP, GREEN_LASER),
                "blue": (BLUE_SPACE_SHIP, BLUE_LASER)
                }

    def __init__(self,x,y,color,health=100):
        super().__init__(x,y,health)
        self.ship_img,self.laser_img=self.color[color]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self,vel):
        self.y+=vel    





# CODE;
def main():
    run=True
    FPS=60
    level =0
    enemies = []
    wave_length =5
    lives=5
    player_vel=5
    main_font = pygame.font.SysFont('comicsans',50)

    player = Player(300,650)




    clock = pygame.time.Clock()
    def redraw_window():
        WIN.blit(BG,(0,0))
        # draw Text 
        lives_label = main_font.render(f"Lives:{lives}",1,(255,255,255))
        level_label = main_font.render(f"Level:{level}",1,(255,255,255))
        WIN.blit(lives_label,(10,10))
        WIN.blit(level_label,(WIDTH-level_label.get_width()-10,10))
        player.draw(WIN)
        pygame.display.update()


    while run:
        clock.tick(FPS)
        redraw_window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
                pygame.quit()
                exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x-player_vel >0:
            player.x-=player_vel
        if keys[pygame.K_w] and player.y-player_vel >0:
            player.y-=player_vel
        if keys[pygame.K_d] and player.x+player_vel+player.get_width()<WIDTH:
            player.x+=player_vel
        if keys[pygame.K_s] and player.y+player_vel+player.get_height()<HEIGHT:
            player.y+=player_vel            




# calling the functiom
main()


# 57:23