import pygame  # Game library

pygame.init()  # Initialize all pygame modules
max_axelaration_in_seconds = 0.35
class Soldier(pygame.sprite.Sprite):
    def __init__(self,x_pos,y_pos,scale,speed ):
        super().__init__()

        self.x_pos = x_pos
        self.y_pos = y_pos
        self.scale = scale
        
        
        self.speed = speed
        self.current_speed = 0
        self.acelaration_step = self.speed / (60 * max_axelaration_in_seconds)
        self.moving_right = False
        self.moving_left = False
        self.derection = 1
        self.flip = False



        original_img = pygame.image.load("./assets/img/player/Idle/0.png").convert_alpha()
        self.image = pygame.transform.scale(surface= original_img, size= (original_img.get_width()*self.scale, original_img.get_height()*self.scale))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x_pos, self.y_pos)



    
    def draw(self,screen):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)
        


    def move(self):
        dx = 0
        dy = 0

        target_speed = 0

        if self.moving_right:
            target_speed = self.speed
            self.derection = 1
            self.flip = False
            pass


        if self.moving_left:
            target_speed = -self.speed
            self.derection = -1
            self.flip = True
            pass

        if self.current_speed < target_speed:
            self.current_speed += self.acelaration_step
            if self.current_speed > target_speed:
                self.current_speed = target_speed
        
        elif self.current_speed > target_speed:
            self.current_speed -= self.acelaration_step
            if self.current_speed < target_speed:
                self.current_speed = target_speed

        dx = self.current_speed

        self.rect.x += int(dx)
        self.rect.y += int(dy)