import sys
import pygame


class MainMenu:
    BG_COLOR = (20, 20, 40)
    TEXT_COLOR = (200, 200, 200)
    SELECTED_COLOR = (255, 200, 0)
    GAMEOVER_COLOR = (220, 50, 50)

    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.title_font = pygame.font.SysFont(None, 100)
        self.menu_font = pygame.font.SysFont(None, 60)
        self.msg_font = pygame.font.SysFont(None, 72)
        self.options = ['New Game', 'Quit']
        self.selected = 0

    def run(self, message=None):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_UP, pygame.K_LEFT):
                        self.selected = (self.selected - 1) % len(self.options)
                    elif event.key in (pygame.K_DOWN, pygame.K_RIGHT):
                        self.selected = (self.selected + 1) % len(self.options)
                    elif event.key == pygame.K_RETURN:
                        self._activate(self.selected)
                    elif event.key == pygame.K_q:
                        sys.exit()
                elif event.type == pygame.MOUSEMOTION:
                    for i, rect in enumerate(self._option_rects()):
                        if rect.collidepoint(event.pos):
                            self.selected = i
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for i, rect in enumerate(self._option_rects()):
                        if rect.collidepoint(event.pos):
                            self._activate(i)

            self._draw(message)
            pygame.display.flip()

    def _activate(self, index):
        if self.options[index] == 'Quit':
            sys.exit()
        # 'New Game' — return control to caller
        raise _StartGame()

    def _option_rects(self):
        rects = []
        start_y = self.screen_rect.centery + 40
        for i in range(len(self.options)):
            surf = self.menu_font.render(self.options[i], True, self.TEXT_COLOR)
            rect = surf.get_rect(center=(self.screen_rect.centerx, start_y + i * 90))
            rects.append(rect)
        return rects

    def _draw(self, message):
        self.screen.fill(self.BG_COLOR)

        title = self.title_font.render('AIR BATTLE', True, self.SELECTED_COLOR)
        self.screen.blit(title, title.get_rect(center=(self.screen_rect.centerx,
                                                       self.screen_rect.centery - 180)))

        if message:
            msg_surf = self.msg_font.render(message, True, self.GAMEOVER_COLOR)
            self.screen.blit(msg_surf, msg_surf.get_rect(center=(self.screen_rect.centerx,
                                                                  self.screen_rect.centery - 60)))

        start_y = self.screen_rect.centery + 40
        for i, option in enumerate(self.options):
            color = self.SELECTED_COLOR if i == self.selected else self.TEXT_COLOR
            surf = self.menu_font.render(option, True, color)
            self.screen.blit(surf, surf.get_rect(center=(self.screen_rect.centerx,
                                                         start_y + i * 90)))


class _StartGame(Exception):
    pass
