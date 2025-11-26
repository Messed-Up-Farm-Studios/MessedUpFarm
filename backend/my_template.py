"""
Starting Template

Once you have learned how to use classes, you can begin your program with this
template.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.starting_template
"""
import arcade
from frontend.media_utils import resource_path

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Messed Up Farm"


class GameView(arcade.View):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self):
        super().__init__()

        self.background_color = arcade.color.AIR_FORCE_BLUE
        arcade.set_background_color(self.background_color)

        # If you have sprite lists, you should create them here,
        # and set them to None

        self.tiles = arcade.SpriteList()
        self.characters = arcade.SpriteList()

    def reset(self):
        """Reset the game to the initial state."""
        # Do changes needed to restart the game here if you want to support that
        pass

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        self.clear()

        # Call draw() on all your sprite lists below
        self.tiles.draw()
        self.characters.draw()


    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        pass

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        https://api.arcade.academy/en/latest/arcade.key.html
        """
        pass

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass



class MessedUpFarmApp():
    def __init__(self):
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
