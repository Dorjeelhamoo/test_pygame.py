import unittest
import pygame
from car import check_collision, update_game_state

class Testcar(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.width, self.height = (400, 800)
        self.road_w = int(self.width / 1.6)
        self.roadmark_w = int(self.width / 80)
        self.right_lane = self.width / 2 + self.road_w / 4
        self.left_lane = self.width / 2 - self.road_w / 4
        self.speed = 1
        self.size = self.width, self.height
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption('car game')
        self.screen.fill((60, 220, 0))
        self.car = pygame.image.load('green-car.png')
        self.car_loc = self.car.get_rect()
        self.car_loc.center = self.right_lane, self.height * 0.9
        self.car2 = pygame.image.load('red-car.png')
        self.car2_loc = self.car2.get_rect()
        self.car2_loc.center = self.left_lane, self.height * 0.3
        self.counter = 0

    def test_level_up(self):
        self.counter = 5000
        update_game_state(self.speed, self.counter)
        self.assertEqual(self.speed, 1)
        update_game_state(self.speed, self.counter)
        self.assertEqual(self.speed, 1.15)

    def test_collision_detection(self):
        self.car_loc.center = self.right_lane, self.height * 0.9
        self.car2_loc.center = self.right_lane, self.height * 0.75
        self.assertTrue(check_collision(self.car_loc, self.car2_loc))

    def tearDown(self):
        pygame.quit()

if __name__ == '_main_':
    unittest.main()

    