import pygame.font


class Scoreboard():


    def __init__(self, ai_settings, screen, stats):
        self.ai_settings = ai_settings
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()
        self.prep_hit_ratio()
        self.prep_high_score()


    def prep_score(self):
        score_str = str(self.stats.calc_scores())
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.ai_settings.bg_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20


    def prep_hit_ratio(self):
        hit_ratio_str = str(self.stats.calc_hit_ratio())
        self.hit_ratio_image = self.font.render(hit_ratio_str, True, self.text_color,
                                            self.ai_settings.bg_color)

        self.hit_ratio_rect = self.hit_ratio_image.get_rect()
        self.hit_ratio_rect.right = self.screen_rect.right - 20
        self.hit_ratio_rect.top = 60

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)

    def show_hit_ratio(self):
        self.screen.blit(self.hit_ratio_image, self.hit_ratio_rect)

    def prep_high_score(self):
        high_score = int(round(self.stats.high_score, -1))
