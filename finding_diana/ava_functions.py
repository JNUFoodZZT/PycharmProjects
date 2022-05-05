import sys
import pygame

def check_events(ava_settings,screen,ava):
    #记录事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ava_settings,screen,ava,)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ava)

def check_keydown_events(event,ava_settings,screen,ava):
    """按键按下"""
    if event.key == pygame.K_RIGHT:
        ava.moving_right = True
    elif event.key == pygame.K_LEFT:
        ava.moving_left = True
    elif event.key == pygame.K_UP:
        ava.moving_up = True
    elif event.key == pygame.K_DOWN:
        ava.moving_down = True
    # elif event.key == pygame.K_SPACE:
    #     #创建子弹
    #     fire_bullets(ai_settings, screen, diana, bullets)

    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event,ava):
    """松开"""
    if event.key == pygame.K_RIGHT:
        ava.moving_right = False
    elif event.key == pygame.K_LEFT:
        ava.moving_left = False
    elif event.key == pygame.K_UP:
        ava.moving_up = False
    elif event.key == pygame.K_DOWN:
        ava.moving_down = False