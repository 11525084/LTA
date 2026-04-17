import pygame, time
from sys import exit

pygame.init()
pygame.mixer.init()

screen=pygame.display.set_mode((1080, 720))
pygame.display.set_caption('cute')

#variable
game_opening = True
running = True
delta_time = 0.1
current_track = None

#grahic
mika =pygame.image.load('mika nmahope (1).png').convert_alpha()
kogi = pygame.image.load('music notes.png').convert_alpha()
ishi = pygame.image.load('ishikiri nmahope.png')
bg = pygame.image.load('7c6f5669-5bc2-47da-a3e6-ad05d613997d (1).jpg')
wood = pygame.image.load('wood_bg.webp')
wood = pygame.transform.scale(wood, screen.get_size())
star=pygame.image.load('starr.png')
starnote = pygame.transform.scale(star, (70, 80))


#rectangle


kogirect = kogi.get_rect(topleft= (-10,100))
woodrect = wood.get_rect(topleft = (0,600))

#audio
tapsound = pygame.mixer.Sound('existentialtaco-confirm-tap-394001.mp3')

#text
font1 = pygame.font.Font(None, size = 30)
font2 = pygame.font.Font(None, size = 70)
nmahopeparade  = font1.render('RUNNING NOTES (SPACE to star)',True,'Brown')
nmahoperect = nmahopeparade.get_rect(center =(540,80))
nmahopeparade1  = font1.render('RUNNING NOTES',True,'Brown')
nmahoperect1 = nmahopeparade1.get_rect(center =(540,80))


class Button(pygame.sprite.Sprite):
    def __init__(self,name:str,buttonnumber):
        super().__init__()
        self.image = pygame.Surface((70,70))
        self.image.fill((170,80,170))
        self.key_name = name
        self.button = font2.render(self.key_name,True, 'White')
        text_rect = self.button.get_rect(center=(35, 35))
        self.image.blit(self.button, text_rect)
        if buttonnumber <=3:
            self.rect = self.button.get_rect(topleft = (100+100*(0+buttonnumber),650))
        if buttonnumber >3:
            self.rect = self.button.get_rect(topleft = (100+100*(0+buttonnumber),650))
        
        self.target_key = pygame.key.key_code(self.key_name)
        self.sound = pygame.mixer.Sound('existentialtaco-confirm-tap-394001.mp3')



    

button = pygame.sprite.Group()
button1 = Button('1',0)
button2 = Button('2',1)
button3 = Button('3',2)
button4 = Button('4',3)
button7 = Button('7',5)
button8 = Button('8',6)
button9 = Button('9',7)
button0 = Button('0',8)
button.add(button1,button2,button3,button4,button7,button8,button9,button0)





class Note(pygame.sprite.Sprite):
    def __init__(self,barnumber,rownumber):
        super().__init__()
        self.image = starnote
        self.rownumber = rownumber
        if barnumber ==0:
            self.rect = self.image.get_rect(topleft =(100+80*(0+barnumber),(-240*rownumber)))
        if barnumber >0:
            self.rect = self.image.get_rect(topleft = (100+100*(0+barnumber),(-120*rownumber)))
        
        
    def update(self,starspeed = 10):
        self.rect.top +=starspeed
        if self.rect.top >720 : self.rect.bottom = -8*80 ; self.rect.top +=starspeed


starcol0 = pygame.sprite.Group()
starcol1= pygame.sprite.Group()
star00 = Note(0,0)
star02 = Note(0,2)
star03 =Note(0,3) ;star10 =Note(1,0);star7=Note(1,1) ;star8=Note(1,2);star9=Note(1,3);star0=Note(1,4); star15=Note(1,5)
star01 =Note(0,1)
star04 =Note(0,4) ; star05 = Note(0,5) 

starcol0.add(star00,star01,star02,star03,star04)
starcol1.add(star10,star7,star8,star9,star0,star15)



clock =pygame.time.Clock()

while running: 
    for event in pygame.event.get():

        if game_opening ==True:
            if current_track != "openingbgm":
                openingbgm = pygame.mixer.music.load('OST. LOVE NIKKI BGM3 - YouTube.mp3')
                pygame.mixer.music.play()
                current_track = openingbgm

        if game_opening == False:
            if current_track != "startbgm":
                startbgm = pygame.mixer.music.load('Danzen, kimi ni koishiteru! (Original Karaoke) - YouTube.mp3')
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_volume(0.5)
                current_track = startbgm

        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_SPACE:
                game_opening = False

            if event.key == pygame.K_ESCAPE:
                game_opening = True    

        if event.type == pygame.KEYDOWN:
            press_time = pygame.time.get_ticks()


        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit()
        
        
    if game_opening == True: 

        current_track = None
        
        screen.blit(bg,(0,0))
        screen.blit(kogi,(-10,250))
        

        pygame.draw.rect(screen,'Yellow',nmahoperect,0,5)
        screen.blit(nmahopeparade, nmahoperect)
        screen.blit(wood,woodrect)
        


    if game_opening==False:
        
        current_track=None

        screen.blit(bg, (0,0))
        pygame.draw.rect(screen,'Yellow',nmahoperect,0,5)
        screen.blit(nmahopeparade1, nmahoperect1)

        
        screen.blit(kogi,kogirect)
        if kogirect.left <1080 : kogirect.left +=6
        if kogirect.left >=1080: kogirect.left = -340 ;kogirect.left +=6
        

        starcol0.update() ; 
        starcol1.update() ; 
        starcol0.draw(screen) ; starcol1.draw(screen)

        screen.blit(wood,woodrect)
        button.draw(screen)    

        for star in starcol0.sprites() + starcol1.sprites():
            if star.rect.colliderect(woodrect) and not hasattr(star, 'hit'):
                tapsound.play()
                star.hit = True
        if star.rect.top < 0:
            if hasattr(star, 'hit'): del star.hit
        
        """if star.rect.colliderect(woodrect):
            if not hasattr(star, 'collision_time'):
                star.collision_time = pygame.time.get_ticks()
        
        for star in starcol0.sprites() + starcol1.sprites():
            if hasattr(star, 'collision_time'):
                # Calculate the difference in time
                # abs() ensures we catch hits 10ms before OR 10ms after
                time_diff = abs(press_time - star.collision_time)
                if time_diff <= 50:
                    tapsound.play()

        for star in starcol0:
            if not star.rect.colliderect(woodrect):
                if hasattr(star, 'collision_time'):
                    del star.collision_time"""
        


    #if all note past, end game


    pygame.display.flip()

    delta_time =clock.tick(30)



