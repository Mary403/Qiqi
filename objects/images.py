import pygame

from objects.base import BaseObject


class Image(BaseObject):
    def __init__(self, x, y, filename, is_transform_scale=False, size=()):
        self.filename = filename
        self.image = pygame.image.load(filename)
        if is_transform_scale:  # подогнать размер изображения в size
            self.image = pygame.transform.scale(self.image, size)

        r = self.image.get_rect()
        super().__init__(x, y, r.width, r.height)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

