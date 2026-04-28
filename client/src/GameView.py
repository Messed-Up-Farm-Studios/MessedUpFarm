"""
Starting Template

Once you have learned how to use classes, you can begin your program with this
template.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.starting_template
"""

import arcade

from client.src.WSManager import wsManager


class GameView(arcade.View):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self) -> None:
        super().__init__()

        arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

        self.tiles: arcade.SpriteList[arcade.Sprite] = arcade.SpriteList()

        self.characters: arcade.SpriteList[arcade.Sprite] = arcade.SpriteList()

    def reset(self) -> None:
        """Reset the game to the initial state."""
        # Do changes needed to restart the game here if you want to support that
        pass

    def on_draw(self) -> None:
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        self.clear()

        # Call draw() on all your sprite lists below
        self.tiles.draw()
        self.characters.draw()

    def on_update(self, delta_time) -> None:
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        while not wsManager.queue.empty():
            msg = wsManager.queue.get()
            print(f"Game got: {msg}")

    def on_key_press(self, key, key_modifiers) -> None:
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        https://api.arcade.academy/en/latest/arcade.key.html
        """
        if key == arcade.key.UP:
            player = self.characters[0]

            player.center_y += 10

            wsManager.send_ws(
                {"type": "move", "x": player.center_x, "y": player.center_y}
            )

        elif key == arcade.key.DOWN:
            self.characters[0].center_y -= 10

    def on_key_release(self, key, key_modifiers) -> None:
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y) -> None:
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers) -> None:
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers) -> None:
        """
        Called when a user releases a mouse button.
        """
        pass
