import pygame


class Settings:
    WINDOW_WIDTH = 1366
    WINDOW_HEIGHT = 768
    # 1280 × 1024
    # 1024 × 768
    # 1920×1080
    # 1366 × 768
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
        Settings.set_scene(0)
