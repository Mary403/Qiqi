import pygame


class Settings:
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600
    MAX_COLLISION_COUNT = 5
    MAX_WAIT_SECONDS = 3
    BACKGROUND_COLOR = pygame.Color('black')
    scene_changed = True
    scene_index = 0

    @staticmethod
    def set_scene(index):
        Settings.scene_changed = True
        Settings.scene_index = index

    @staticmethod
    def set_game_scene():
        Settings.set_scene(1)