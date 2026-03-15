import pygame


class Explosion(pygame.sprite.Sprite):
    DURATION = 600   # ms
    MAX_RADIUS = 40

    def __init__(self, screen, position):
        super().__init__()
        self.screen = screen
        self.position = position
        self.spawn_time = pygame.time.get_ticks()
        self._update_image(0.0)

    def _update_image(self, progress):
        radius = max(1, int(self.MAX_RADIUS * progress))
        size = radius * 2 + 2
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        alpha = int(255 * (1.0 - progress))
        pygame.draw.circle(self.image, (255, 140, 0, alpha), (radius + 1, radius + 1), radius)
        self.rect = self.image.get_rect(center=self.position)

    def update(self):
        elapsed = pygame.time.get_ticks() - self.spawn_time
        if elapsed >= self.DURATION:
            self.kill()
            return
        self._update_image(elapsed / self.DURATION)

    def blitme(self):
        self.screen.blit(self.image, self.rect)
