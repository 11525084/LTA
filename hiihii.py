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

#grahic
mika =pygame.image.load('mika nmahope (1).png').convert_alpha()
kogi = pygame.image.load('kogitsunemaru nmahope.png').convert_alpha()
ishi = pygame.image.load('ishikiri nmahope.png')
bg = pygame.image.load('jp pastel bg.jpg')
wood = pygame.image.load('wood_bg.webp')
wood = pygame.transform.scale(wood, screen.get_size())
star=pygame.image.load('starr.png')
starnote = pygame.transform.scale(star, (70, 80))

#rectangle
mikarect = mika.get_rect(topleft = (30,250))
#mikarect = mika.get_rect(topleft = (10,-340))
kogirect = kogi.get_rect(topleft= (360,250))
#kogirect = kogi.get_rect(topleft= (360,-340))
ishirect= ishi.get_rect(topleft = (700,250))
#ishirect= ishi.get_rect(topleft = (700,-340))
woodrect = wood.get_rect(topleft = (0,600))

#audio
startbgm = pygame.mixer.music.load('Danzen, kimi ni koishiteru! (Original Karaoke) - YouTube.wav')
openingbgm = pygame.mixer.music.load('OST. LOVE NIKKI BGM3 - YouTube.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)
tapsound = pygame.mixer.Sound('existentialtaco-confirm-tap-394001.mp3')
musicstarted = False

def bgm(state):
    if state =="opening": 
        pygame.mixer.music.load('OST. LOVE NIKKI BGM3 - YouTube.mp3')
        pygame.mixer.music.play(-1)
    if state =="start": 
        pygame.mixer.music.load('Danzen, kimi ni koishiteru! (Original Karaoke) - YouTube.wav')
        pygame.mixer.music.play(-1)

    

#text
font1 = pygame.font.Font(None, size = 30)
font2 = pygame.font.Font(None, size = 70)
nmahopeparade  = font1.render('RUNNING NOTES (SPACE to star)',True,'Brown')
nmahoperect = nmahopeparade.get_rect(center =(540,80))
nmahopeparade1  = font1.render('RUNNING NOTES',True,'Brown')
nmahoperect1 = nmahopeparade1.get_rect(center =(540,80))



        #if mikarect.bottom <720+340: mikarect.bottom +=6
        #if mikarect.bottom >=720+340:mikarect.bottom = -340 ; mikarect.bottom +=6

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


    """def pressbutton(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == self.target_key:
                self.sound.play()
                # Visual feedback: flash the button color
                self.image.fill((255, 255, 255))"""



    """ self.pressbutton(event)
            if event.type == pygame.KEYDOWN:
            target_key = pygame.key.key_code(self.name)
            if keycode.key == target_key:
                tapsound.play()"""


        

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
    def __init__(self,barnumber):
        super().__init__()
        self.image = starnote
        
        if barnumber <=3:
            self.rect = self.image.get_rect(topleft =(100+80*(0+barnumber),0))
        if barnumber >3:
            self.rect = self.image.get_rect(topleft = (100+100*(0+barnumber),0))
        
        
    def update(self,starspeed):
        self.rect.top +=starspeed
        if self.rect.top >600 : self.kill()  

stars = pygame.sprite.Group()
star1 = Note(0)
star2 = Note(1)
star3 =Note(2) ;star4 =Note(3);star7=Note(5) ;star8=Note(6);star9=Note(7);star0=Note(8)

stars.add(star1,star2,star3,star4,star7,star8,star9,star0)
#stars.movenote()
#stars.draw(screen)


clock =pygame.time.Clock()

while running: 
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_SPACE:
                game_opening = False

            if event.key == pygame.K_ESCAPE:
                game_opening = True    


        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit()
        
        
    if game_opening == True: 
        state1='opening'
        bgm(state1)

        screen.blit(bg,(0,0))
        screen.blit(mika, (30,250))
        screen.blit(kogi,(370,250))
        screen.blit(ishi, (650,250))

        pygame.draw.rect(screen,'Yellow',nmahoperect,0,5)
        screen.blit(nmahopeparade, nmahoperect)
        screen.blit(wood,woodrect)
        #pygame.draw.rect(screen,(170,0,170),button1rect,0,10)
        #screen.blit(button1,button1rect)


    if game_opening==False:
        state2 ='start'
        bgm(state2)
    
        
        screen.blit(bg, (0,0))
        pygame.draw.rect(screen,'Yellow',nmahoperect,0,5)
        screen.blit(nmahopeparade1, nmahoperect1)
        
        #pygame.draw.rect(screen,(170,0,170),button1rect,0,10)
        #screen.blit(button1,button1rect)
    

        screen.blit(mika, mikarect)
        if mikarect.left <1080 : mikarect.left +=6
        if mikarect.left >=1080: mikarect.left = -340 ;mikarect.left +=6
        #if mikarect.bottom <720+340: mikarect.bottom +=6
        #if mikarect.bottom >=720+340:mikarect.bottom = -340 ; mikarect.bottom +=6
        screen.blit(ishi, ishirect)
        if ishirect.left <1080 : ishirect.left +=6
        if ishirect.left >=1080: ishirect.left = -340 ;ishirect.left +=6
        #if ishirect.top <720: ishirect.top +=6
        screen.blit(kogi,kogirect)
        if kogirect.left <1080 : kogirect.left +=6
        if kogirect.left >=1080: kogirect.left = -340 ;kogirect.left +=6
        #if kogirect.top <720: kogirect.top +=6

        stars.update(5)
        star1.update(10) ; star2.update(7);star3.update(8) ;star4.update(10);star7.update(8);star8.update(7);star9.update(8);star0.update(6)
        stars.draw(screen)

        screen.blit(wood,woodrect)


       
        button.draw(screen)    

        
      
        

    #if all note past, end game"""


    pygame.display.flip()

    delta_time =clock.tick(30)



