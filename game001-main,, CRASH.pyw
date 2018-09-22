import pygame

import random
pygame.init()



#800x600
dpw=800
dph=600
his=0                       
black=(0,0,0)
white=(255,255,255)
red=(55,0,0)
bred=(255,0,0)
green=(0,55,0)
bgreen=(0,255,0)
blue=(0,0,255)
bblue=(27,196,255)
grey=(48,48,48)
pygame.mixer.music.load('carsound.mp3')
gamed=pygame.display.set_mode((dpw,dph))     #800x600
crashs=pygame.mixer.Sound("crashc.wav")
pygame.display.set_caption("CLASH")
clock=pygame.time.Clock()

carimg=pygame.image.load('car02.png')
bkj=pygame.image.load("bkj.png")
icimg=pygame.image.load('icon.png')
pygame.display.set_icon(icimg)
cw=85
gamed.blit(bkj,(0,0))
ch=100
paus=False
f=open("waste.txt","w")
f.close()
def mrk(cnt):
     g=open("his.txt","r")
     q=g.read()
     q=int(q)
     font=pygame.font.SysFont('comicsansms',12)
     text=font.render("HI_SCORE: "+str(q), True,bblue)
     gamed.blit(text,(690,46))
     g.close()
     if cnt>q:
          fl=open("his.txt","w")
          fl.write(str(cnt))
          fl.close()
          font=pygame.font.SysFont('comicsansms',12)
          text=font.render("HI_SCORE: "+str(cnt), True,bblue)
          gamed.blit(text,(690,46))
                   
     font=pygame.font.SysFont('comicsansms',20)
     text=font.render("score : "+str(cnt), True,bblue)
     gamed.blit(text,(0,0))
     
def level(lvl):
     font=pygame.font.SysFont('comicsansms',20)
     text=font.render("lvl : "+str(lvl), True,bblue)
     gamed.blit(text,(0,25))

def thg(thgx,thgy,thgw,thgh,color):
     pygame.draw.rect(gamed,color,[thgx,thgy,thgw,thgh])
     
def qtg():
     pygame.quit()
     quit()
     
def cnt():
     global paus
     pygame.mixer.music.unpause()
     
     paus=False
def button(bx,by,bw,bh,txt,ic,ac,action):
#button(150,450,100,45,'play',white,bgreen,gm)
    mus=pygame.mouse.get_pos()
    #print(mus)
    clk=pygame.mouse.get_pressed()
   # print(clk)

    if bx+bw>mus[0]>bx and by+bh>mus[1]>by :
      pygame.draw.rect(gamed,ac,[bx,by,bw,bh])
      if clk[0]==1:
           action()
    else:
         pygame.draw.rect(gamed,ic,[bx,by,bw,bh])
      
    stxt=pygame.font.SysFont('comicsansms',23)
    TextSurf,TextRect=text_objects(txt,stxt,bblue)
    TextRect.center=(bx+(bw/2),by+(bh/2))
    gamed.blit(TextSurf,TextRect)


def car(x,y):
     gamed.blit(carimg,(x,y))

def text_objects(text,font,color):
     textSurface=font.render(text,True,color)
     return textSurface,textSurface.get_rect()
  



def cra():

     pygame.mixer.Sound.play(crashs)
     pygame.mixer.music.stop()
     largeText=pygame.font.SysFont('comicsansms',80)
     TextSurf,TextRect=text_objects('__YOU CRASHED__',largeText,bgreen)
     TextRect.center=((dpw/2),(dph/2))
     gamed.blit(TextSurf,TextRect)
     while True:
          for event in pygame.event.get():
               if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
          button(150,450,100,45,'play',white,bgreen,gm)
          button(550,450,100,45,'quit',white,bred,qtg)
                    
     
                 
          pygame.display.update()
          clock.tick(65)
def pas():
     pygame.mixer.music.pause()
     largeText=pygame.font.SysFont('comicsansms',80)
     TextSurf,TextRect=text_objects('paused',largeText,bgreen)
     TextRect.center=((dpw/2),(dph/2))
     gamed.blit(TextSurf,TextRect)

     while paus:
          mus=pygame.mouse.get_pos()
          print(mus)
          clk=pygame.mouse.get_pressed()
          print(clk)

          for event in pygame.event.get():
               if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
          button(150,450,100,45,'continue',white,bgreen,cnt)
          button(550,450,100,45,'quit',white,bred,qtg)

          
          pygame.display.update()
          clock.tick(65)

          



def intro():
     
     intr=True
     while intr:
          for event in pygame.event.get():
               if event.type==pygame.QUIT:
                    
                    pygame.quit()
                    quit()
          gamed.fill(white)
          largeText=pygame.font.SysFont('couriernew',78)
          TextSurf,TextRect=text_objects("PLAY  CRASH",largeText,black)
          TextRect.center=((dpw/2),(dph/2))
          gamed.blit(TextSurf,TextRect)
          mus=pygame.mouse.get_pos()
          print(mus)
          clk=pygame.mouse.get_pressed()
          print(clk)

##          
##button(150,450,100,45,'play',white,bgreen,gm)
          button(150,450,100,45,'play',green,bgreen,gm)
          button(550,450,100,45,'quit',red,bred,qtg)

          
          pygame.display.update()
          clock.tick(60)
                                         
                                   


def gm():
     global paus
     pygame.mixer.music.play(-1)
     x=(dpw*0.45)
     y=(dph*0.79)

     xch=0
     ych=0
     thgwi=127
     thghi=100
     thgsx=random.randrange(0,dpw-thgwi)
     thgsy=-351
     thgv=3
     
     lvl=0
     cmr=0
##     t2x=random.randrange(0,dpw-129)
##     t2y=-200
##
##     t2v=5

     
    
     xit=0
     
     while xit==0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 #print(event)
                 
                 pygame.quit()
                 quit()
                 
                 
            if event.type==pygame.KEYDOWN:
                 if event.key==pygame.K_LEFT:
                      xch=-4
                 elif event.key==pygame.K_RIGHT:
                      xch=4
                 elif event.key==pygame.K_UP:
                      ych=-4
                 elif event.key==pygame.K_DOWN:
                      ych=4
                 elif event.key==pygame.K_SPACE:
                      
                      paus=True
                      pas()
            if event.type==pygame.KEYUP:
                 if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                      xch=0
                 elif event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                      ych=0
 
  
        x=x+xch
        y=y+ych
        
        gamed.fill(grey)
##        thg(ttfx,0,ttfw,ttfh,bgreen)
##        thg(ttfx2,0,ttfw,ttfh,bgreen)
        
        mus=pygame.mouse.get_pos()
        clk=pygame.mouse.get_pressed()
        if 700+100>mus[0]>700 and 0+45>mus[1]>0:
               pygame.draw.rect(gamed,bred,[700,0,100,45])
               if clk[0]==1:
                    pygame.quit()
                    quit()

        stxt=pygame.font.SysFont('comicsansms',23)
        TextSurf,TextRect=text_objects("quit!",stxt,bblue)
        TextRect.center=((700+50),0+(45/2))
        gamed.blit(TextSurf,TextRect)
        
        thg(thgsx,thgsy,thgwi,thghi,bred)
        thgsy=thgsy+thgv
        
        
        

        car(x,y)
        
        mrk(cmr)
       
        level(lvl)
        
        #h_s(cmr)
        
        ###wall crash
        if x > dpw-cw or x < 0:
             print("side wall crash") 
             cra()
        if y>dph-ch or y<0:
             print("frn/bk crash")
             cra()
        ###new objct ,, point 
        if thgsy>dph:
             thgsy=-200
             thgsx=random.randrange(0,dpw-thgwi)
             f=open("waste.txt","a")
             f.write(str(thgsx)+'\n')
             f.close()
             cmr=cmr+1
             if cmr%3==0:
                  lvl=lvl+1
                  
                  thgv=thgv+1
                  thgwi=thgwi
##             if lvl>=2:
##                 tflvl(t2x,t2y,t2v,thgsx,thgsy,thgwi,thghi)
                 
                  
                  
             
             
            
                       
        ### crash_                    
        if y<thgsy+thghi and y+ch>thgsy:
             if x>thgsx and x<thgsx+thgwi or x+cw>thgsx and x+cw<thgsx+thgwi:
                  print("object crash")
                  cra()
             
                  
            
             
                  
                  
        
      
        
        pygame.display.update()
        clock.tick(60)

intro()
gm()
pygame.quit()
quit()    

