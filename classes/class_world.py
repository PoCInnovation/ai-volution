from enum import Enum
import random

import pygame as py

class scene(Enum):
    GAME = 1
    ENDGAME = 2


class class_world():
    def __init__(self, width=1000, height=1000, size_font=36, min_radius = 30, max_radius = 250, impact_timer_min = 1,
                    impact_timer_max = 3, end_time=15, min_impact = 5, max_impact = 10):

        # Window_size
        self.width = width
        self.height = height

        # Radius
        self.min_radius = min_radius
        self.max_radius = max_radius

        # Colors
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0, 255)
        self.grey =(175, 175, 175, 175)

        # Window
        self.window = py.display.set_mode((self.width, self.height))
        self.window.fill(self.white)

        # Time
        self.running = True
        self.size_font = size_font
        self.font = py.font.Font(None, self.size_font)

        # Scene
        self.scene = scene(1)

        # Timer
        self.actual_time = 0
        self.delta_time = 0
        self.impact_timer_min = impact_timer_min
        self.impact_timer_max = impact_timer_max
        self.start_time = py.time.get_ticks()
        self.end_time = end_time
        self.time_elapsed = 0

        # Impact
        self.min_impact = min_impact
        self.max_impact = max_impact

        self.list_impact_co = []
        self.list_impact_radius = []
        self.list_impact_radius_timer = []
        self.list_impact_timer_start = []
        self.list_impact_timer_time = []
        self.list_impact_red_zone = []

        for i in range(random.randint(self.min_impact, self.max_impact)):
            self.list_impact_co.append((random.randint(0, self.width), random.randint(0, self.height)))
            self.list_impact_radius.append(random.randint(self.min_radius, self.max_radius))
            self.list_impact_timer_start.append(random.randint(1, self.end_time))
            self.list_impact_timer_time.append(random.randint(self.impact_timer_min, self.impact_timer_max))
            self.list_impact_red_zone.append([0, self.list_impact_radius[i] / self.list_impact_timer_time[i]])


    def update_red_zone(self, i: int):
        self.list_impact_red_zone[i][0] += self.list_impact_red_zone[i][1] * self.delta_time
        return self.list_impact_red_zone[i][0]

    def draw_impact(self):
        for i in range(len(self.list_impact_co)):
            if self.list_impact_timer_start[i] < self.actual_time // 1000 and self.list_impact_red_zone[i][0] < \
                    self.list_impact_radius[i]:
                py.draw.circle(self.window, self.grey, self.list_impact_co[i], self.list_impact_radius[i])
        for i in range(len(self.list_impact_co)):
            if self.list_impact_timer_start[i] < self.actual_time // 1000:
                if self.list_impact_red_zone[i][0] < self.list_impact_radius[i]:
                    py.draw.circle(self.window, self.red, self.list_impact_co[i], self.update_red_zone(i))
                else:
                    py.draw.circle(self.window, self.red, self.list_impact_co[i], self.list_impact_radius[i])

    def draw_time(self):
        timer_text = self.font.render("Time: {} seconds".format(self.actual_time // 1000), True, self.black)
        self.window.blit(timer_text, (self.width // 2 - timer_text.get_width() // 2,
                                                self.size_font + 5 - timer_text.get_height() // 2))
    def draw_game(self):
        self.window.fill(self.white)
        self.draw_impact()
        self.draw_time()
    
    def draw_endgame(self):
        self.window.fill(self.white)
        self.window.fill(self.white)
        timer_text = self.font.render("The end", True, self.black)
        self.window.blit(timer_text, (
        self.width // 2 - timer_text.get_width() // 2, self.size_font + 5 - timer_text.get_height() // 2))

    def actualised_time(self):
        if self.actual_time > self.end_time * 1000 + self.impact_timer_max * 1000 * 3:
            self.scene = scene(2)
        self.time_elapsed = (py.time.get_ticks() - self.start_time)
        self.delta_time = (self.time_elapsed - self.actual_time) / 1000
        self.actual_time = self.time_elapsed