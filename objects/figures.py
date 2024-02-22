import pygame

from objects.base import BaseObject


class Rect(BaseObject):
    def __init__(self, x, y, width, height, outline=False):
        super().__init__(x, y, width, height)
        self.outline = outline

    def draw(self, screen):
        if self.outline:
            pygame.draw.rect(screen, (255, 255, 255), self.rect, self.outline)
        else:
            pygame.draw.rect(screen, (255, 255, 255), self.rect)
        # screen.blit(self.image, self.rect)