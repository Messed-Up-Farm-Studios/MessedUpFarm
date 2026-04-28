import arcade

from client.src.GameView import GameView
from client.src.ws_runner import start_ws_thread

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Messed Up Farm"


class MessedUpFarmApp:
    def __init__(self) -> None:
        pass

    def run(self) -> None:
        """Main function"""
        # Create a window class. This is what actually shows up on screen
        window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

        # Create and setup the GameView
        game = GameView()

        start_ws_thread()

        cow = arcade.Sprite("client/src/assets/sprites/cow.png", 0.0625)
        cow.center_x = 30
        cow.center_y = 30
        game.characters.append(cow)

        first_tile = arcade.Sprite("client/src/assets/biomes/dirt.png", 0.06250)

        first_tile.center_x = 50
        first_tile.center_y = 50
        game.tiles.append(first_tile)

        # Show GameView on screen
        window.show_view(game)

        # Start the arcade game loop
        arcade.run()
