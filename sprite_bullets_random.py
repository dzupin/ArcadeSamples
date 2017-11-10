"""
Show how to have enemies shoot bullets at random intervals.
"""
import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyApplication(arcade.Window):
    """ Main application class """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)

        self.frame_count = 0
        self.all_sprites_list = None
        self.enemy_list = None
        self.bullet_list = None

        self.player = None

    def setup(self):
        self.all_sprites_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()

        self.player = arcade.Sprite("images/playerShip1_orange.png", 0.5)
        self.all_sprites_list.append(self.player)

        enemy = arcade.Sprite("images/playerShip1_green.png", 0.5)
        enemy.center_x = 120
        enemy.center_y = SCREEN_HEIGHT - enemy.height
        enemy.angle = 180
        self.all_sprites_list.append(enemy)
        self.enemy_list.append(enemy)

        enemy = arcade.Sprite("images/playerShip1_green.png", 0.5)
        enemy.center_x = SCREEN_WIDTH - 120
        enemy.center_y = SCREEN_HEIGHT - enemy.height
        enemy.angle = 180
        self.all_sprites_list.append(enemy)
        self.enemy_list.append(enemy)

    def on_draw(self):
        """Render the screen. """

        arcade.start_render()

        self.enemy_list.draw()
        self.bullet_list.draw()
        self.player.draw()

        # Draw the text
        arcade.draw_text("This is a simple template to start your game.",
                         10, SCREEN_HEIGHT // 2, arcade.color.BLACK, 20)

    def update(self, delta_time):
        """All the logic to move, and the game logic goes here. """

        self.frame_count += 1

        for enemy in self.enemy_list:

            # Have a random 1 in 200 change of shooting each frame
            if random.randrange(200) == 0:
                bullet = arcade.Sprite("images/laserBlue01.png")
                bullet.center_x = enemy.center_x
                bullet.angle = -180
                bullet.top = enemy.bottom
                bullet.change_y = -2
                self.bullet_list.append(bullet)
                self.all_sprites_list.append(bullet)

        # Get rid of the bullet when it flies off-screen
        for bullet in self.bullet_list:
            if bullet.top < 0:
                bullet.kill()

        self.bullet_list.update()

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """ Called whenever the mouse moves. """
        self.player.center_x = x
        self.player.center_y = 20


def main():
    """ Main method """
    window = MyApplication(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()