import pygame

from objects.images import Image
from objects.texts import Text
from scenes.base import BaseScene
from settings import Settings
from objects.figures import Rect


class GameScene(BaseScene):
    PROCESS_ESCAPE = False

    def __init__(self):
        w, h = 400, 400
        self.Qiqi = Image(Settings.WINDOW_WIDTH // 2 - w // 2, Settings.WINDOW_HEIGHT // 2 - h // 2,
                          'images/pic_fun.png', True, (w, h))
        self.rect1 = Rect(100, Settings.WINDOW_HEIGHT // 2 - 300 - 50,
                          280, 100, 10)

        self.rect2 = Rect(100, Settings.WINDOW_HEIGHT // 2 - 200 - 10 - 50,
                          280, 100, 10)

        self.rect3 = Rect(100, Settings.WINDOW_HEIGHT // 2 - 100 - 20 - 50,
                          280, 100, 10)

        self.sc1 = Rect(Settings.WINDOW_WIDTH // 2 + 300, Settings.WINDOW_HEIGHT // 2 - 300,
                        280, 10)
        self.sc2 = Rect(Settings.WINDOW_WIDTH // 2 + 300, Settings.WINDOW_HEIGHT // 2 - 200,
                        280, 10)
        self.sc3 = Rect(Settings.WINDOW_WIDTH // 2 + 300, Settings.WINDOW_HEIGHT // 2 - 100,
                        280, 10)

        self.sc0 = Rect(Settings.WINDOW_WIDTH // 2 - 1000 // 2, Settings.WINDOW_HEIGHT // 2 - 10 // 2 + 300,
                        1000, 10)

        self.b1 = Rect(Settings.WINDOW_WIDTH // 2 + 300, Settings.WINDOW_HEIGHT // 2 - 70 // 2 + 30,
                       70, 70)
        self.b2 = Rect(Settings.WINDOW_WIDTH // 2 + 300 + 105, Settings.WINDOW_HEIGHT // 2 - 70 // 2 + 30,
                       70, 70)
        self.b3 = Rect(Settings.WINDOW_WIDTH // 2 + 300 + 210, Settings.WINDOW_HEIGHT // 2 - 70 // 2 + 30,
                       70, 70)

        self.ev = Rect(100, Settings.WINDOW_HEIGHT // 2 - 70 // 2 + 30,
                       280, 70, 5)
        super().__init__()

    def set_up_objects(self):
        self.objects.append(self.Qiqi)
        self.objects.append(self.rect1)
        self.objects.append(self.rect2)
        self.objects.append(self.rect3)
        self.objects.append(self.sc0)
        self.objects.append(self.sc1)
        self.objects.append(self.sc2)
        self.objects.append(self.sc3)
        self.objects.append(self.b1)
        self.objects.append(self.b2)
        self.objects.append(self.b3)
        # self.objects.append(self.ev)

    def additional_process_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            Settings.set_scene(1)
