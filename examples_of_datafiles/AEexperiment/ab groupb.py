'''
Ab training experiment



instrucciones todas sesiones

Performance calculator

test retest, probar y medir
'''

import pygame
from pygame.locals import *
import random

font_size = 70
W, H = 1200, 600
t1_color = [255, 255, 255]
stim_color= [0, 0, 0]
background_gray = 128
bg_col = [128, 128, 128]
distractors=['P','Q','S','I','O','U','T','Y','F','G','H','J','K','L','M','W','C','V','N','B']
t1=['Z','A','E','R']
trials=84
trials_training=120
t1_pos=21*[4]+21*[5]+21*[6]+21*[7]
t1_pos_training=45*[4]+45*[5]+45*[6]+45*[7]
lag=20*[0]+8*[1]+8*[2]+8*[3]+8*[4]+8*[5]+8*[6]+8*[7]+8*[8]
lag_training=40*[0]+10*[1]+10*[2]+10*[3]+10*[4]+10*[5]+10*[6]+10*[7]+10*[8]

random.shuffle(t1_pos)
random.shuffle(t1_pos_training)
random.shuffle(lag)

responses=['Wich was target 1? A Z E or R?','Was X present? left NO right YES','How sure you are? 1a 2z 3e 4r 5t','press space to continue with next trial']
instructionstest=[['We are going to start with the Test','Press spacebar to start'],['We are going to start with the retest','Press spacebar to start']]
instructions=[['Now we are starting with the training. You are going', 'to start with a long distance from T2 to T1', 'and progresiviley descending to shorter times'],['This block will have a short','time interval between','T1 and T2'],['This block will have a medium','time interval between','T1 and T2'],['This block will have a long','time interval between','T1 and T2']]


# draw text to surface, so that its center is at position pos
# using the given color and background_color
# assume that font already exists
def draw_text(surface, color, background_color, text, pos):
    image = font.render(text, True, color, background_color)
    image_w, image_h = image.get_size()
    surface.blit(image, [pos[0] - image_w/2, pos[1] - image_h/2])

def wait(dur):
    ticks0 = pygame.time.get_ticks()
    while True:
        if dur != None and pygame.time.get_ticks() > ticks0 + dur:
            return
        for ev in pygame.event.get():
            if ev.type == QUIT or (ev.type == KEYDOWN and ev.key == K_ESCAPE):
                raise Exception

# waits until space is pressed, then returns
def wait_for_space():
    pygame.event.get()  # clear previous events
    while True:
        window.fill(bg_col)
        draw_text(window, t1_color, bg_col, responses[3], [W/2, H/2])
        pygame.display.flip()
        for ev in pygame.event.get():
            if ev.type == QUIT or (ev.type == KEYDOWN and ev.key == K_ESCAPE):
                raise Exception
            elif ev.type == KEYDOWN and ev.key == K_SPACE:
                return

def test_instructions(test):
    pygame.event.get()  # clear previous events
    while True:
        window.fill(bg_col)
        draw_text(window, t1_color, bg_col, instructionstest[test][0], [W/2, H/5])
        draw_text(window, t1_color, bg_col, instructionstest[test][1], [W/2, H/5*2])
        pygame.display.flip()
        for ev in pygame.event.get():
            if ev.type == QUIT or (ev.type == KEYDOWN and ev.key == K_ESCAPE):
                raise Exception
            elif ev.type == KEYDOWN and ev.key == K_SPACE:
                return

def training_instructions(lag):
    pygame.event.get()  # clear previous events
    while True:
        window.fill(bg_col)
        draw_text(window, t1_color, bg_col, instructions[lag][0], [W/2, H/5])
        draw_text(window, t1_color, bg_col, instructions[lag][1], [W/2, H/5*2])
        draw_text(window, t1_color, bg_col, instructions[lag][2], [W/2, H/5*3])
        pygame.display.flip()
        for ev in pygame.event.get():
            if ev.type == QUIT or (ev.type == KEYDOWN and ev.key == K_ESCAPE):
                raise Exception
            elif ev.type == KEYDOWN and ev.key == K_SPACE:
                return
def feedback():
    pygame.event.get()  # clear previous events
    while True:
        window.fill(bg_col)
        if correct2==1:
            draw_text(window, t1_color, bg_col, 'CORRECT! Press spacebar to continue', [W/2, H/2])
        elif correct2==0:
            draw_text(window, t1_color, bg_col, 'INCORRECT! Press spacebar to continue', [W/2, H/2])
        pygame.display.flip()
        for ev in pygame.event.get():
            if ev.type == QUIT or (ev.type == KEYDOWN and ev.key == K_ESCAPE):
                raise Exception
            elif ev.type == KEYDOWN and ev.key == K_SPACE:
                return
        



def get_response(r):
    while True:
        window.fill([background_gray, background_gray, background_gray])
        draw_text(window, t1_color, bg_col, responses[r], [W/2, H/2])
        pygame.display.flip()
        for ev in pygame.event.get():
            if ev.type == KEYDOWN:
                if ev.key == K_LEFT:
                    return '0'
                elif ev.key == K_RIGHT:
                    return '1'
                elif ev.key == K_a:
                    return '1'
                elif ev.key == K_z:
                    return '2'
                elif ev.key == K_e:
                    return '3'
                elif ev.key == K_r:
                    return '4'
                elif ev.key == K_t:
                    return '5'
                elif ev.key == K_ESCAPE:
                    raise Exception


try:

    subj = raw_input('subject initials (no spaces or accents): ')
    subj = subj.lower()
    #block= raw_input('block: ') #1 lento rapido, dos rapido a lento
    # open data file for writing, write header line
    file_name = subj +'.dat'
    out = open(file_name, 'a')
    print >>out, 'subj','task','isi', 'lagt2', 't2in', 'reponset1', 'reponset2','correct1', 'correct2'

    
    pygame.init()
    window = pygame.display.set_mode((W,H),pygame.FULLSCREEN)

    # create the font
    font = pygame.font.Font(None, font_size)

    '''
    if block=='a':
        start=3
        end=0
        step=-1
    if block=='b':
        start=1
        end=4
        step=1
    '''
    task='test'
    test_instructions(0)
    for j in range(trials):

        window.fill(bg_col)
        draw_text(window, stim_color, bg_col, '+', [W/2, H/2])
        pygame.display.flip()
        wait(random.randint(500,1000))
        stream=random.sample(distractors,19)
        t1_stream=random.choice(t1)
        if t1_stream is 'A':
            t1_nb='1'
        elif t1_stream is 'Z':
            t1_nb='2'
        elif t1_stream is 'E':
            t1_nb='3'
        elif t1_stream is 'R':
            t1_nb='4'
        stream[t1_pos[j]]=t1_stream
        if lag[j]!=0:
            stream[t1_pos[j]+lag[j]]='X'
            t2in='1'
        else:
            t2in='0'
        for i in range(len(stream)):
            window.fill(bg_col)
            if i == t1_pos[j]:
                draw_text(window, t1_color, bg_col, stream[i], [W/2, H/2])
            else:
                draw_text(window, stim_color, bg_col, stream[i], [W/2, H/2])
            pygame.display.flip()
            wait(100)
            
        window.fill(bg_col)
        pygame.display.flip()
        wait(500)
        
        reponset1=get_response(0)
        reponset2=get_response(1)
        correct1=reponset1 is t1_nb
        correct2=reponset2 is t2in
        wait_for_space()
    
        print >>out, subj,task,lag[j],t2in, reponset1, reponset2, correct1, correct2
    

    task='trainingB'
    for j in range(trials_training):

        window.fill(bg_col)
        draw_text(window, stim_color, bg_col, '+', [W/2, H/2])
        pygame.display.flip()
        wait(random.randint(500,1000))
        stream=random.sample(distractors,19)
        t1_stream=random.choice(t1)
        if t1_stream is 'A':
            t1_nb='1'
        elif t1_stream is 'Z':
            t1_nb='2'
        elif t1_stream is 'E':
            t1_nb='3'
        elif t1_stream is 'R':
            t1_nb='4'
        stream[t1_pos_training[j]]=t1_stream
        if lag_training[j]!=0:
            stream[t1_pos_training[j]+lag_training[j]]='X'
            t2in='1'
        else:
            t2in='0'
        for i in range(len(stream)):
            window.fill(bg_col)
            if i == t1_pos_training[j]:
                draw_text(window, t1_color, bg_col, stream[i], [W/2, H/2])
            else:
                draw_text(window, stim_color, bg_col, stream[i], [W/2, H/2])
            pygame.display.flip()
            wait(100)
            
        window.fill(bg_col)
        pygame.display.flip()
        wait(500)
          
        reponset1=get_response(0)
        reponset2=get_response(1)
        correct1=reponset1 is t1_nb
        correct2=reponset2 is t2in
        wait_for_space()
    
        print >>out, subj,task,lag_training[j],t2in, reponset1, reponset2, correct1, correct2

   
    task='retestB'
    test_instructions(1)
    for j in range(trials):

        window.fill(bg_col)
        draw_text(window, stim_color, bg_col, '+', [W/2, H/2])
        pygame.display.flip()
        wait(random.randint(500,1000))
        stream=random.sample(distractors,19)
        t1_stream=random.choice(t1)
        if t1_stream is 'A':
            t1_nb='1'
        elif t1_stream is 'Z':
            t1_nb='2'
        elif t1_stream is 'E':
            t1_nb='3'
        elif t1_stream is 'R':
            t1_nb='4'
        stream[t1_pos[j]]=t1_stream
        if lag[j]!=0:
            stream[t1_pos[j]+lag[j]]='X'
            t2in='1'
        else:
            t2in='0'
        for i in range(len(stream)):
            window.fill(bg_col)
            if i == t1_pos[j]:
                draw_text(window, t1_color, bg_col, stream[i], [W/2, H/2])
            else:
                draw_text(window, stim_color, bg_col, stream[i], [W/2, H/2])
            pygame.display.flip()
            wait(100)
            
        window.fill(bg_col)
        pygame.display.flip()
        wait(500)
        
        reponset1=get_response(0)
        reponset2=get_response(1)
        correct1=reponset1 is t1_nb
        correct2=reponset2 is t2in
        wait_for_space()
    
        print >>out, subj,task,lag[j],t2in, reponset1, reponset2, correct1, correct2

    
        
finally:
    try:
        out.close()
    except:
        pass
    pygame.quit()
