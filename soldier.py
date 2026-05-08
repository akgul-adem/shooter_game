import pygame  # Game library

pygame.init()  # Initialize all pygame modules
max_axelaration_in_seconds = 0.25
class Soldier(pygame.sprite.Sprite):
    def __init__(self,x_pos,y_pos,scale,speed,charactar_type):
        super().__init__()

        self.charactar_type = charactar_type

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



        
        
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()

        # idle animation

        temp_anim_list = []

        for i in range (5):
            original_img = pygame.image.load(f"./assets/img/{self.charactar_type}/Idle/{i}.png").convert_alpha()
            img = pygame.transform.scale(surface= original_img, size= (original_img.get_width()*self.scale, original_img.get_height()*self.scale))
        
            temp_anim_list.append(img)

        self.image = self.animation_list.append(temp_anim_list)

        # run animation

        temp_anim_list = []

        for i in range (6):
            original_img = pygame.image.load(f"./assets/img/{self.charactar_type}/Run/{i}.png").convert_alpha()
            img = pygame.transform.scale(surface= original_img, size= (original_img.get_width()*self.scale, original_img.get_height()*self.scale))
        
            temp_anim_list.append(img)

        self.image = self.animation_list.append(temp_anim_list)

        # self image

        self.image = self.animation_list [self.action] [self.frame_index]

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
    def update_action(self,new_action):
        # Check if the new action is differnet then the preveious one
        if new_action != self.action:
            self.action = new_action
            #update animation settings
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def update_animation(self):
        ANIMATION_COOLDOWN = 100


        self.image = self.animation_list [self.action] [self.frame_index]

        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
            if self.frame_index >= len(self.animation_list [self.action]):
                self.frame_index = 0