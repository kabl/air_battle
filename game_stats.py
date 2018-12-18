class GameStats():


    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.high_score = 0
        self.score = 0
        self.shot_bullets = 0
        self.shot_enemies = 0

    def increment_shot_bullets(self):
        self.shot_bullets += 1
        print("inc shot bullets:", self.shot_bullets)

    def increment_shot_enemies(self):
        self.shot_enemies += 1

    def calc_scores(self):
        result = self.shot_enemies * self.ai_settings.scoring_points
        print("calc_points:", result)
        return result

    def calc_hit_ratio(self):
        if self.shot_bullets == 0:
            return 0
        else:
            return round(self.shot_enemies / self.shot_bullets, 3)
