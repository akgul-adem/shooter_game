import pygame  # Game library

pygame.init()  # Initialize all pygame modules

class Soldier(pygame.sprite.Sprite):
    def __init__(self,x_pos,y_pos,scale,speed ):
        super().__init__()

        self.x_pos = x_pos
        self.y_pos = y_pos
        self.scale = scale
        
        
        self.speed = speed
        self.moving_right = False
        self.moving_left = False




        original_img = pygame.image.load("./assets/img/player/Idle/0.png").convert_alpha()
        self.image = pygame.transform.scale(surface= original_img, size= (original_img.get_width()*self.scale, original_img.get_height()*self.scale))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x_pos, self.y_pos)



    
    def draw(self,screen):
        screen.blit(self.image, self.rect)


    def move(self):
        dx = 0
        dy = 0


        if self.moving_right:
            dx = self.speed
            pass


        if self.moving_left:
            dx = -self.speed
            pass


        self.rect.x += dx
        self.rect.y += dy