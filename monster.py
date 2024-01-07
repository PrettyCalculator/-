from settings import *


class MonsterVertical(pygame.sprite.Sprite):
    def __init__(self, pos, image):
        super().__init__()
        self.image = image
        self.direction = pygame.math.Vector2(0, 0)
        self.direction.y = -1
        self.rect = self.image.get_rect(topleft=pos)
        self.speed = 1

    def update(self, x_shift):
        self.rect.y += self.speed * self.direction.y
        self.rect.x += x_shift


class MonsterHorizontal(MonsterVertical):
    def __init__(self, pos, image):
        super().__init__(pos, image)
        self.direction.x = -1

    def update(self, x_shift):
        self.rect.x += self.speed * self.direction.x
        self.rect.x += x_shift
