import arcade

from frontend.SplashScreen import Splashscreen
from frontend.game.GameView import GameView

from frontend.media_utils import resource_path

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Messed Up Farm"

class MessedUpFarmApp():
    def __init__(self):
        splashScreen = Splashscreen()
        
        pass

    def run(self):
        """ Main function """
        # Create a window class. This is what actually shows up on screen
        window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

        # Create and setup the GameView
        game = GameView()

        cow = arcade.Sprite(resource_path("resources/sprites/cow.png"), .0625)
        cow.center_x = 30
        cow.center_y = 30
        game.characters.append(cow)

        first_tile = arcade.Sprite(resource_path("resources/biomes/dirt.png"), .06250)

        first_tile.center_x = 50
        first_tile.center_y = 50
        game.tiles.append(first_tile)

        # Show GameView on screen
        window.show_view(game)

        # Start the arcade game loop
        arcade.run()
