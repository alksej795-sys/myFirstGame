# # # password = 1234567
# # # name = "Lesha"

# # # user = input("введите имя: ")
# # # user_ps = int(input("введите пароль: "))

# # # if name == name and password == password:
# # #     print("вход выполнен")
# # # else:
# # #     print('Ошибка') 




# # print("Добро пожаловать! Вы хотите посетить магазин или ресторан?")

# # choice = input("Введите 'магазин' или 'ресторан': ")

# # if choice.lower() == "магазин":
# #     print("вы пошли в магазин") 
        
# #     print("выберите категорию товаров:")
# #     print("1. Продукты питания")
# #     print("2. Товары для дома")

# #     category_choice = input("введите номер категории: ")

# #     if category_choice == "1":
# #         print("вы выбрали продукты питания. Приятных покупок")
# #     elif category_choice == "2":
# #         print("вы выбрали товары для дома. Удачных покупок")
# #     else:
# #         print("Извините, но такой категории нет.")

# # elif choice.lower() == "ресторан":
# #     print("вы решили посетить ресторан. Приятного аппетита")
    
# #     print("меню ресторана:")
# #     print("1. Завтраки")
# #     print("2. Обеды")
# #     print("3. Ужины")

# #     menu_choice = input("введите номер блюда: ")

# #     if menu_choice == "1":
# #         print("вы заказали завтрак. Приятного аппетита")
# #     elif menu_choice == "2":
# #         print("вы заказали обед. Приятного аппетита")
# #     elif menu_choice == "3":
# #         print("вы заказали ужин. Приятного аппетита")
# #     else:
# #         print("извините, но такого блюда нет")

# # else:
# #     print("извините, но такого варианта нет. Пожалуйста, выберите 'магазин' или 'ресторан'.")


# # import random
# # def game():
# #     print("игра:камень, ножницы, бумага")
# #     print("выбирете: камень, ножницы, бумага")
# #     while True:
# #         user = input("ваш выбор: ")
# #         options = ["камень", "ножницы", "бумага"]
# #         computer = random.choice(options)
# #         print("компьютер выбрал:", computer)
# #         if user == computer:
# #             print("ничья")
# #         elif (user == "камень" and computer == "ножницы") or ("ножницы" and computer == "бумага") or (user == "бумага" and computer == "камень"):
# #             print("вы выйграли")
# #         else:
# #             print("компьтер победил")
# # game()


# print("игра выбери дверь")

# choice = input("выбирете дверь:'1 дверь' '2 дверь' '3 дверь': ")

# while True:

#     if choice.lower() == "1 дверь":
#         print ("вы зашли в первую дверь")

#         print ("здесь монстр что вы будете делать:" 
#         "1.убежать" 
#         "2.сражаться")

    
#         category_choise = input("введите номер действия: ")
   
#         if category_choise == "1":
#             print("вы убежали и выжили но ничего не выйграли")
#         elif category_choise == "2":
#          print("вы начали сражаться и проиграли")
#         else:
#             print("извините, такого действия нету")

#     elif choice.lower() == "2 дверь":
#         print("вы зашли в 2 дверь")

#         print("тут ничего нету")

#         empty_choise = input("выберите что будете делать:"
#         "1.идти дальше"
#         "2.уйти домой")

#         if empty_choise == "1":
#             print("идти дальше")
#         elif empty_choise == "2":
#             print("уйти домой")
#         else:
#             print("такого действия нету")

#     elif choice.lower() == "3 дверь":
#         print("вы зашли в 3 дверь")

#         print("вы нашли сокровища!")

#         treasures_choise = input("выбирите что будете делать:" 
#         "1.пойти дальше чтобы найти еще больше либо же потерять все" 
#         "2.пойти домой с сокровищами")

#         if treasures_choise == "1":
#             print("пойти дальше чтобы найти еще больше либо же потерять все")
#         elif treasures_choise =="2":
#             print("пойти домой с сокровищами")
#         else:
#             print("такого действия нету")
#     break



# import pygame

# pygame.init()
# clock = pygame.time.Clock()

# display = pygame.display.set_mode((800, 440))
# pygame.display.set_caption('Game')

# fon = pygame.image.load('sonti.jpg')
# airplan = pygame.image.load('airplan/airplan-removebg-preview.png')

# player_run = [
#     pygame.image.load('player_run/run1.png'),
#     pygame.image.load('player_run/run2.png'),
#     pygame.image.load('player_run/run3.png'),
#     pygame.image.load('player_run/run4.png'),
#     pygame.image.load('player_run/run5.png'),
#     pygame.image.load('player_run/run6.png'),
#     pygame.image.load('player_run/run7.png'),
#     pygame.image.load('player_run/run8.png'),
#     pygame.image.load('player_run/run9.png'),
# ]

# player_run_left = [
#     pygame.image.load('player_run_left/run1_left.png'),
#     pygame.image.load('player_run_left/run2_left.png'),
#     pygame.image.load('player_run_left/run3_left.png'),
#     pygame.image.load('player_run_left/run4_left.png'),
#     pygame.image.load('player_run_left/run5_left.png'),
#     pygame.image.load('player_run_left/run6_left.png'),
#     pygame.image.load('player_run_left/run7_left.png'),
#     pygame.image.load('player_run_left/run8_left.png'),
#     pygame.image.load('player_run_left/run9_left.png'),
# ]

# player_jump = [
#     pygame.image.load('player_jump/jump1.png'),
#     pygame.image.load('player_jump/jump2.png'),
#     pygame.image.load('player_jump/jump3.png'),
#     pygame.image.load('player_jump/jump4.png'),
#     pygame.image.load('player_jump/jump5.png'),
#     pygame.image.load('player_jump/jump6.png'),
#     pygame.image.load('player_jump/jump7.png'),
# ]

# player_x = 150
# player_y = 250
# player_speed = 10
# player_anim = 0

# fon_x = 0
# airplan_x = 900
# airplan_y = 50

# is_jump = False
# jump_vel = 12
# gravity = 1
# ground_y = 250
# jump_anim = 0 


# run = True
# while run:
#     display.blit(fon, (fon_x, 0))
#     display.blit(fon, (fon_x + 800, 0))
#     keys = pygame.key.get_pressed()

# if not is_jump and keys[pygame.K_SPACE]:
#     is_jump = True
#     jump_vel = 12
#     jump_anim = 0

# if is_jump:
#     player_y -= jump_vel
#     jump_vel -= gravity

#     display.blit(player_jump[jump_anim], (player_x, player_y))
#     jump_anim += 1
#     if jump_anim >= len(player_jump):
#         jump_anim = len(player_jump) - 1

#     if player_y >= ground_y:
#         player_y = ground_y
#         is_jump = False
#         jump_anim = 0
# else:
#     display.blit(player_jump[player_anim], (player_x, player_y))



#     keys = pygame.key.get_pressed()

#     if keys[pygame.K_RIGHT] and player_x < 700:
#         player_x += player_speed
#         display.blit(player_run[player_anim], (player_x, player_y))
#     elif keys[pygame.K_LEFT] and player_x > 50:
#         player_x -= player_speed
#         display.blit(player_run_left[player_anim], (player_x, player_y))
#     else:
#         display.blit(player_run[0], (player_x, player_y))

#     player_anim += 1
#     if player_anim >= len(player_run):
#         player_anim = 0


# keys = pygame.key.get_pressed()


# if not is_jump and keys[pygame.K_SPACE]:
#     is_jump = True
#     jump_vel = 12


# if is_jump:
#     player_y -= jump_vel
#     jump_vel -= gravity

#     if player_y >= ground_y:
#         player_y = ground_y
#         is_jump = False


#     fon_x -= 2
#     if fon_x <= -800:
#         fon_x = 0

#     airplan_x -= 20
#     display.blit(airplan, (airplan_x, airplan_y))

#     pygame.display.update()

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False

#     clock.tick(20)

# pygame.quit()







# import pygame

# pygame.init()
# clock = pygame.time.Clock()

# display = pygame.display.set_mode((800, 440))
# pygame.display.set_caption('Game')


# fon = pygame.image.load('sonti.jpg')
# airplan = pygame.image.load('airplan/airplan-removebg-preview.png')


# player_run = [pygame.image.load(f'player_run/run{i}.png') for i in range(1,10)]

# player_run_left = [pygame.image.load(f'player_run_left/run{i}_left.png') for i in range(1,10)]

# player_jump = [pygame.image.load(f'player_jump/jump{i}.png') for i in range(1,8)]


# player_x = 150
# player_y = 250
# player_speed = 10
# player_anim = 0

# fon_x = 0
# airplan_x = 900
# airplan_y = 50


# is_jump = False
# jump_vel = 12
# gravity = 1
# ground_y = 250
# jump_anim = 0

# run = True
# while run:
#     display.blit(fon, (fon_x, 0))
#     display.blit(fon, (fon_x + 800, 0))

#     keys = pygame.key.get_pressed()

    
#     if not is_jump and keys[pygame.K_SPACE]:
#         is_jump = True
#         jump_vel = 12
#         jump_anim = 0

    
#     current_anim = player_run  

#     if keys[pygame.K_RIGHT] and player_x < 700:
#         player_x += player_speed
#         current_anim = player_run
#     elif keys[pygame.K_LEFT] and player_x > 50:
#         player_x -= player_speed
#         current_anim = player_run_left

    
#     if is_jump:
#         player_y -= jump_vel
#         jump_vel -= gravity

        
#         display.blit(player_jump[jump_anim], (player_x, player_y))
#         jump_anim += 1
#         if jump_anim >= len(player_jump):
#             jump_anim = len(player_jump) - 1

#         if player_y >= ground_y:
#             player_y = ground_y
#             is_jump = False
#             jump_anim = 0
#     else:
#         display.blit(current_anim[player_anim], (player_x, player_y))
#         player_anim += 1
#         if player_anim >= len(current_anim):
#             player_anim = 0

#     fon_x -= 2
#     if fon_x <= -800:
#         fon_x = 0

#     airplan_x -= 20
#     display.blit(airplan, (airplan_x, airplan_y))

#     pygame.display.update()

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False

#     clock.tick(20)
# continue


# pygame.quit()



import pygame
import time

pygame.init()
clock = pygame.time.Clock()

WIDTH, HEIGHT = 800, 440
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

background = pygame.image.load("sonti.jpg").convert()
enemy_img = pygame.image.load("boss flame/enemy ghost.png").convert_alpha()
kunay_img = pygame.image.load("kunay/kunay.png").convert_alpha()

player_run = [pygame.image.load(f"player_run/run{i}.png").convert_alpha() for i in range(1, 10)]
player_run_left = [pygame.image.load(f"player_run_left/run{i}_left.png").convert_alpha() for i in range(1, 10)]
player_jump = [pygame.image.load(f"player_jump/jump{i}.png").convert_alpha() for i in range(1, 8)]

player_x = 150
player_y = 250
ground_y = 250
player_speed = 8

player_anim = 0
anim_delay = 0
jump_anim = 0
direction = "right"

is_jump = False
jump_vel = 0
gravity = 1
jump_count = 0
max_jumps = 3

kunays = []
kunay_speed = 12
kunay_cooldown = 0.5
last_kunay_time = 0

enemy_x = WIDTH + 100  
enemy_y = 250
enemy_speed = 3
enemy_max_hp = 3
enemy_hp = enemy_max_hp
enemy_alive = True

kills = 0
font = pygame.font.SysFont("arial", 30)

bg_x = 0
game_over = False

run = True
while run: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and jump_count < max_jumps and not game_over:
                is_jump = True
                jump_vel = 12
                jump_anim = 0
                jump_count += 1

            if event.key == pygame.K_f and not game_over:
                current_time = time.time()
                if current_time - last_kunay_time >= kunay_cooldown:
                    last_kunay_time = current_time

                    if direction == "right":
                        kunays.append(pygame.Rect(
                            player_x + 50, player_y + 30,
                            kunay_img.get_width(), kunay_img.get_height()
                        ))
                    else:
                        kunays.append(pygame.Rect(
                            player_x, player_y + 30,
                            kunay_img.get_width(), kunay_img.get_height()
                        ))

    screen.blit(background, (bg_x, 0))
    screen.blit(background, (bg_x + WIDTH, 0))

    if not game_over:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] and player_x < WIDTH - 80:
            player_x += player_speed
            direction = "right"
        elif keys[pygame.K_LEFT] and player_x > 20:
            player_x -= player_speed
            direction = "left"

        if is_jump:
            player_y -= jump_vel
            jump_vel -= gravity
            screen.blit(player_jump[jump_anim], (player_x, player_y))
            if jump_anim < len(player_jump) - 1:
                jump_anim += 1
        else:
            anim_delay += 1
            if anim_delay >= 5:
                anim_delay = 0
                player_anim = (player_anim + 1) % len(player_run)

            if direction == "right":
                screen.blit(player_run[player_anim], (player_x, player_y))
            else:
                screen.blit(player_run_left[player_anim], (player_x, player_y))

        if player_y >= ground_y:
            player_y = ground_y
            is_jump = False
            jump_count = 0

        if enemy_alive:
            enemy_x -= enemy_speed
            if enemy_x < -enemy_img.get_width():
                enemy_x = WIDTH + 100

            screen.blit(enemy_img, (enemy_x, enemy_y))
            enemy_rect = enemy_img.get_rect(topleft=(enemy_x, enemy_y))

            hp_text = font.render(f"HP: {enemy_hp}", True, (255, 0, 0))
            screen.blit(hp_text, (enemy_x, enemy_y - 30))

        for kunay in kunays[:]:
            if direction == "right":
                kunay.x += kunay_speed
            else:
                kunay.x -= kunay_speed

            screen.blit(kunay_img, kunay)

            if kunay.x > WIDTH or kunay.x < -50:
                kunays.remove(kunay)
                continue

            if enemy_alive and kunay.colliderect(enemy_rect):
                enemy_hp -= 1
                kunays.remove(kunay)

                if enemy_hp <= 0:
                    enemy_alive = False
                    kills += 1

        if not enemy_alive:
            enemy_x = WIDTH + 200
            enemy_hp = enemy_max_hp
            enemy_alive = True

        player_rect = player_run[0].get_rect(topleft=(player_x, player_y))
        if enemy_alive and player_rect.colliderect(enemy_rect):
            game_over = True

        score_text = font.render(f"Kills: {kills}", True, (255, 255, 255))
        screen.blit(score_text, (20, 20))

        bg_x -= 2
        if bg_x <= -WIDTH:
            bg_x = 0

    else:
        over_font = pygame.font.SysFont("arial", 60)
        text = over_font.render("YOU DIED...", True, (255, 0, 0))
        screen.blit(text, (230, 180))

    pygame.display.update()
    clock.tick(60)

pygame.quit()

