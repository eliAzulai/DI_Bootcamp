import pygame, sys, random 

def draw_floor():
    screen.blit(floor_surface,(floor_x_pos,900))
    screen.blit(floor_surface,(floor_x_pos + 576,900))

def create_pipe():
    
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop = (700,random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midbottom = (700,random_pipe_pos - 300))

    return top_pipe, bottom_pipe

# influences all the different rect by moving them to the left a little bit
 
def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes


def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 1024: 
            screen.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flip_pipe, pipe)

def check_collision(pipes): 
    for pipe in pipes: 
        if bird_rect.colliderect(pipe):
            
            return False
    
    if bird_rect.top <= -100 or bird_rect.bottom >= 900:
        death_sound.play()
        return False
    
    return True

def rotate_bird(bird):
    new_bird = pygame.transform.rotozoom(bird, -bird_movement *3, 1)
    return new_bird
        
def bird_animation(): 
    new_bird = bird_frames[bird_index]
    new_bird_rect = new_bird.get_rect(center = (100,bird_rect.centery))
    return new_bird, new_bird_rect

def score_display(game_state):
    if game_state == 'main_game':
        score_surface = game_font.render(str(int(score)), True,(255,255,255))
        score_rect = score_surface.get_rect(center = (288,100))
        screen.blit(score_surface, score_rect)
        
    if game_state == 'game_over':
        score_surface = game_font.render(f'Score: {int(score)}', True,(255,255,255))
        score_rect = score_surface.get_rect(center = (288,100))
        screen.blit(score_surface, score_rect)
        
        high_score_surface = game_font.render(f'High score: {int(score)}', True,(255,255,255))
        high_score_rect = high_score_surface.get_rect(center = (288,850))
        screen.blit(high_score_surface, high_score_rect)
        
def update_score(score, high_score):
    if score > high_score:
        high_score = score
    return high_score
        
pygame.mixer.pre_init(frequency= 44100, size = 16, channels = 1, buffer = 512)   
pygame.init()
screen = pygame.display.set_mode((576,1024))
clock = pygame.time.Clock()
game_font = pygame.font.Font('/Users/Azulai/Dropbox/Developers_Institute/Week6/Hackathon2/04B_19.TTF', 40)


# Game Variables
gravity = 0.25
bird_movement = 0
game_active = True
score = 0 
high_score = 0 



# sets the display surface image
bg_surface = pygame.image.load('/Users/Azulai/Dropbox/Developers_Institute/Week6/Hackathon2/assets/background-day.png').convert()
bg_surface = pygame.transform.scale2x(bg_surface)


floor_surface = pygame.image.load('/Users/Azulai/Dropbox/Developers_Institute/Week6/Hackathon2/assets/base.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_pos = 0

bird_downflap = pygame.transform.scale2x(pygame.image.load('/Users/Azulai/Dropbox/Developers_Institute/Week6/Hackathon2/assets/bluebird-downflap.png').convert_alpha())
bird_midflap = pygame.transform.scale2x(pygame.image.load('/Users/Azulai/Dropbox/Developers_Institute/Week6/Hackathon2/assets/bluebird-midflap.png').convert_alpha())
bird_upflap = pygame.transform.scale2x(pygame.image.load('/Users/Azulai/Dropbox/Developers_Institute/Week6/Hackathon2/assets/bluebird-upflap.png').convert_alpha())
bird_frames = [bird_downflap, bird_midflap, bird_upflap]
bird_index = 0
bird_surface = bird_frames[bird_index]
bird_rect = bird_surface.get_rect(center = (100,512))

BIRDFLAP = pygame.USEREVENT + 1
pygame.time.set_timer(BIRDFLAP, 200)

pipe_surface = pygame.image.load('/Users/Azulai/Dropbox/Developers_Institute/Week6/Hackathon2/assets/pipe-green.png').convert()
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)
pipe_height = [400,600,800]

game_over_surface = pygame.transform.scale2x(pygame.image.load('/Users/Azulai/Dropbox/Developers_Institute/Week6/Hackathon2/assets/message.png').convert_alpha())
game_over_rect = game_over_surface.get_rect(center = (288,512))

flap_sound = pygame.mixer.Sound('/Users/Azulai/Dropbox/Developers_Institute/Week6/Hackathon2/sound/sfx_wing.wav')
death_sound = pygame.mixer.Sound('/Users/Azulai/Dropbox/Developers_Institute/Week6/Hackathon2/sound/sfx_hit.wav')
death_point = pygame.mixer.Sound('/Users/Azulai/Dropbox/Developers_Institute/Week6/Hackathon2/sound/sfx_point.wav')
score_sound_countdown = 100

while True:
# looks for all the events in pygame happening right now for example moving mouse or opening a window 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 
# checks whether any keys have been pressed down
        if event.type == pygame.KEYDOWN:
# checks whether specific key has been pressed
# set bird movemet to zero since if not then every run of the while loop the birdmovement is getting += gravity and therefore wont move at all if it less than bird movement with key space 
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0 
                bird_movement -= 12
                flap_sound.play()
            if event.key == pygame.K_SPACE and game_active == False:
                game_active = True
                pipe_list.clear()
                bird_rect.center = (100,512)
                bird_movement = 0
                score = 0
               
        if event.type == SPAWNPIPE: 
            pipe_list.extend(create_pipe())
            
        
        if event.type == BIRDFLAP:
            if bird_index < 2:
                bird_index += 1
            else:
                bird_index = 0
                
            bird_surface,bird_rect = bird_animation()
                    
# sets the display window to surface image            
    screen.blit(bg_surface,(0,0))
    
    if game_active:     
# Bird movement 
        bird_movement += gravity
        rotated_bird = rotate_bird(bird_surface)
        bird_rect.centery += bird_movement
        screen.blit(rotated_bird, bird_rect)
        game_active = check_collision(pipe_list)
        
    # Pipes
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)
        
        score  += 0.01
        score_display('main_game')
        score_sound_countdown -= 1
        if score_sound_countdown <= 0: 
            score_sound.play()
            score_sound_countdown = 100
        
    else:
        screen.blit(game_over_surface, game_over_rect)
        high_score = update_score(score, high_score)
        score_display('game_over')
        
# Floor
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -576:
        floor_x_pos = 0


# takes anthing that you did in the while loop before it and draws on the screen 
    pygame.display.update()
# sets the framerate at 120, since we need to limit the framerate so gaming experience will be stable and consistant.   
    clock.tick(120)

