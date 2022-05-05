import pygame
import sys
from settings import Settings
import ava_functions as af
from ava import Ava

def run_game():
    """游戏主程序"""
    # 界面显示
    ava_settings = Settings()
    screen = pygame.display.set_mode((ava_settings.screen_width,ava_settings.screen_height))
    pygame.display.set_caption('Finding Diana')
    pygame.init()

    screen.fill(ava_settings.screen_color)
    #创建
    ava = Ava(ava_settings,screen)
    ava.blitme()
    # 主循环
    while True:


        pygame.display.flip()
        ava.update()
        af.check_events(ava_settings,screen,ava)


run_game()