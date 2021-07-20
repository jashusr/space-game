import pygame ,sys ,random

pygame.init()

select = int(input("select 1 player or 2 players: "))

player_loc = [400, 650]
player_loc_s = [400, 650]
player_size = 40
player_movement = 40
hight = 800
width = 700
green = ((0, 255, 0))
bg_color = (0, 0, 0)
speed = 4
player_two_loc = [400, 10]
red = ((0, 0, 0))
blue = ((0, 0, 255))
line = [(0, 349), (800, 349)]
white = ((255, 255, 255))
enemy_size = 40
line_size = 10
enemy_loc = [random.randint(0, hight - enemy_size), 355]
enemy_loc_s = [random.randint(0, hight - enemy_size), 0]
enemy_two_loc = [random.randint(0, hight - enemy_size), 305]
enemy_list = [enemy_loc]
enemy_list_s = [enemy_loc_s]
enemy_list_two = [enemy_two_loc]
player_list = [player_loc]

score = 0
score_one = 0
score_two = 0

screen = pygame.display.set_mode((hight, width))

game_over = False

clock = pygame.time.Clock()

shooter_img = pygame.image.load('shooter.png')
shooter_img = pygame.transform.scale(shooter_img,(40,40))

shooterr_img = pygame.image.load('shooterr.png')
shooterr_img = pygame.transform.scale(shooterr_img,(40,40))

rock_img = pygame.image.load('rock.jpg')
rock_img = pygame.transform.scale(rock_img,(40,40))

bg_img = pygame.image.load('spacebg.png')

myFont = pygame.font.SysFont("monospace", 35)

# ememies for player 1
def falling_enemies(enemy_list):
    gap = random.random()
    if len(enemy_list) < 10 and gap < 0.1:
        x_loc = random.randint(0, hight - enemy_size)
        y_loc = 355
        enemy_list.append([x_loc, y_loc])


def more_enemies(enemy_list):
    for enemy_loc in enemy_list:
        pygame.draw.rect(screen, red, (enemy_loc[0], enemy_loc[1], enemy_size, enemy_size))

def more_enemies_img_one(enemy_list):
    for enemy_loc_one in enemy_list:
        screen.blit(rock_img,(enemy_loc_one[0],enemy_loc_one[1]))

# enemies for player 2
def falling_enemies_two(enemy_list_two):
    gap_two = random.random()
    if len(enemy_list_two) < 10 and gap_two < 0.1:
        x_pos = random.randint(0, hight - enemy_size)
        y_pos = 305
        enemy_list_two.append([x_pos, y_pos])


def more_enemies_two(enemy_list_two):
    for enemy_two_loc in enemy_list_two:
        pygame.draw.rect(screen, red, (enemy_two_loc[0], enemy_two_loc[1], enemy_size, enemy_size))

def more_enemies_img_two(enemy_list_two):
    for enemy_loc_two in enemy_list_two:
        screen.blit(rock_img,(enemy_loc_two[0],enemy_loc_two[1]))

# update for player 1
def update_falling_enemy(enemy_list,score_one):
    for idx, enemy_loc in enumerate(enemy_list):
        if enemy_loc[1] >= 0 and enemy_loc[1] < hight:
            enemy_loc[1] += speed
        else:
            enemy_list.pop(idx)
            score_one += 1
    return score_one

def player_one_collision_check_(enemy_list, player_loc):
    for enemy_loc in enemy_list:
        if game_over_player_one(enemy_loc, player_loc):
            return True
    return False


# update for player 2
def update_falling_enemy_two(enemy_list_two,score_two):
    for idx, enemy_two_loc in enumerate(enemy_list_two):
        if enemy_two_loc[1] >= 0 and enemy_two_loc[1] < hight:
            enemy_two_loc[1] -= speed
        else:
            enemy_list_two.pop(idx)
            score_two += 1
    return score_two

def player_two_collision_check_(enemy_list_two, player_two_loc):
    for enemy_two_loc in enemy_list_two:
        if game_over_player_two(enemy_two_loc, player_two_loc):
            return True
    return False


# game over for player one
def game_over_player_one(player_loc, enemy_loc):
    p_x = player_loc[0]
    p_y = player_loc[1]

    e_x = enemy_loc[0]
    e_y = enemy_loc[1]

    if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x + enemy_size)):
        if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y + enemy_size)):
            return True
        return False


# game over for player two
def game_over_player_two(player_two_loc, enemy_two_loc):
    pt_x = player_two_loc[0]
    pt_y = player_two_loc[1]

    et_x = enemy_two_loc[0]
    et_y = enemy_two_loc[1]

    if (et_x >= pt_x and et_x < (pt_x + player_size)) or (pt_x >= et_x and pt_x < (et_x + enemy_size)):
        if (et_y >= pt_y and et_y < (pt_y + player_size)) or (pt_y >= et_y and pt_y < (et_y + enemy_size)):
            return True
        return False


# border
def border(player_list):
    for idx, player_loc in enumerate(player_list):
        if player_loc[0] >= 800:
            player_loc[0] = 760
        else:
            player_list.pop(idx)

#def's for singel player
def falling_enemies_s(enemy_list_s):
    gap = random.random()
    if len(enemy_list) < 10 and gap < 0.1:
        x_loc = random.randint(0, hight - enemy_size)
        y_loc = 0
        enemy_list_s.append([x_loc, y_loc])


def more_enemies_s(enemy_list_s):
    for enemy_loc_s in enemy_list_s:
        pygame.draw.rect(screen, red, (enemy_loc_s[0], enemy_loc_s[1], enemy_size, enemy_size))
        
def more_enemies_img_s(enemy_list_s):
    for enemy_loc_s in enemy_list_s:
        screen.blit(rock_img,(enemy_loc_s[0],enemy_loc_s[1]))

def update_falling_enemy_s(enemy_list_s,score):
    for idx, enemy_loc_s in enumerate(enemy_list_s):
        if enemy_loc_s[1] >= 0 and enemy_loc_s[1] < hight:
            enemy_loc_s[1] += speed
        else:
            enemy_list_s.pop(idx)
            score += 1
    return score

def player_one_collision_check_s(enemy_list_s, player_loc_s):
    for enemy_loc_s in enemy_list_s:
        if game_over_player_one_s(enemy_loc_s, player_loc_s):
            return True
    return False

def game_over_player_one_s(player_loc_s, enemy_loc_s):
    p_x = player_loc_s[0]
    p_y = player_loc_s[1]

    e_x = enemy_loc_s[0]
    e_y = enemy_loc_s[1]

    if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x + enemy_size)):
        if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y + enemy_size)):
            return True
        return False
    
# looping
while not game_over:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:

            x = player_loc[0]
            y = player_loc[1]

            if event.key == pygame.K_LEFT:
                x -= player_movement
            elif event.key == pygame.K_RIGHT:
                x += player_movement
            player_loc = [x, y]
            
        if event.type == pygame.KEYDOWN:

            a = player_two_loc[0]
            b = player_two_loc[1]

            if event.key == pygame.K_a:
                a -= player_movement
            elif event.key == pygame.K_d:
                a += player_movement
            player_two_loc = [a, b]
            
        if player_loc[0] <= -40:
            player_loc[0] += 800
        if player_loc[0] >= 800:
            player_loc[0] -= 800
        
        if player_two_loc[0] <= -40:
            player_two_loc[0] += 800
        if player_two_loc[0] >= 800:
            player_two_loc[0] -= 800

        if event.type == pygame.KEYDOWN:

            x = player_loc_s[0]
            y = player_loc_s[1]

            if event.key == pygame.K_LEFT:
                x -= player_movement
            elif event.key == pygame.K_RIGHT:
                x += player_movement
            player_loc_s = [x, y]

        if player_loc_s[0] <= -40:
            player_loc_s[0] += 800
        if player_loc_s[0] >= 800:
            player_loc_s[0] -= 800
            
    screen.fill(bg_color)

    if game_over_player_one(player_loc, enemy_loc):
        game_over = True
        break
    if game_over_player_two(player_two_loc, enemy_two_loc):
        game_over = True
        break
    if select == 2:
        more_enemies(enemy_list)
        more_enemies_two(enemy_list_two)
        score_two = update_falling_enemy_two(enemy_list_two,score_two)
        score_one = update_falling_enemy(enemy_list,score_one)
        pygame.draw.rect(screen, blue, (player_two_loc[0], player_two_loc[1], player_size, player_size))
        pygame.draw.rect(screen, green, (player_loc[0], player_loc[1], player_size, player_size))
        
        screen.blit(bg_img,(0,0))
        
        more_enemies_img_two(enemy_list_two)
        more_enemies_img_one(enemy_list)
        
        screen.blit(shooter_img,(player_loc[0]-2,player_loc[1]))
        screen.blit(shooterr_img,(player_two_loc[0]-2,player_two_loc[1]))
        
        pygame.draw.line(screen, white, line[0], line[1], line_size)
        
        falling_enemies(enemy_list)
        border(player_list)
        if player_one_collision_check_(enemy_list, player_loc):
            print("player down out","==> up player score: ",score_one ,"; ==> down player score: ", score_two)
            input()
            game_over = True
            break
        
        falling_enemies_two(enemy_list_two)
        if player_two_collision_check_(enemy_list_two, player_two_loc):
            print("player up out","==> up player score: ",score_one ,"; ==> down player score: ", score_two)
            input()
            game_over = True
            break
        
        text = "Score:" + str(score_one)
        label = myFont.render(text,1,(200,255,0))
        screen.blit(label, (600,0))
        
        text = "Score:" + str(score_two)
        label = myFont.render(text,1,(255,255,0))
        screen.blit(label, (600,650))
        
        clock.tick(15)
        
    elif select == 1:
        pygame.draw.rect(screen, (0,0,0), (player_loc_s[0], player_loc_s[1], player_size, player_size))
        more_enemies_s(enemy_list_s)
        score = update_falling_enemy_s(enemy_list_s,score)
        
        screen.blit(bg_img,(0,0))
        
        more_enemies_img_s(enemy_list_s)
        
        falling_enemies_s(enemy_list_s)
        border(player_list)

        screen.blit(shooter_img,(player_loc_s[0]-2,player_loc_s[1]))
        
        if player_one_collision_check_s(enemy_list_s, player_loc_s):
            print("you are out","==>your score: ", score)
            input()
            game_over = True
            break
        clock.tick(30)
        
        text = "Score:" + str(score)
        label = myFont.render(text,1,(255,255,0))
        screen.blit(label, (600,650))

    else:
        print("Choose only 1 or 2")
        input()
        break
    
    pygame.display.update()
