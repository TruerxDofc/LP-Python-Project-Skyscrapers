import arcade
import arcade.gui

WIDTH = 1280
HEIGHT = 768


text_of_play_button = ""; text_of_shop_button = ""; text_of_settings_button = ""
text_of_achievements_button = ""; text_of_exit_button = ""; text_of_back_button = ""
text_of_language_settings = ""; text_of_resolution_settings = ""
text_of_tip_button = ""; text_of_tip = ""


class Localization():
    def Russian_lang(self):
        global text_of_play_button, text_of_shop_button, text_of_settings_button, text_of_achievements_button, \
            text_of_exit_button, text_of_back_button, text_of_language_settings, text_of_resolution_settings, \
            text_of_tip_button, text_of_tip

        text_of_play_button = "Играть"
        text_of_shop_button = "Магазин"
        text_of_settings_button = "Настройки"
        text_of_achievements_button = "Достижения"
        text_of_exit_button = "Выход"
        text_of_back_button = "Назад"
        text_of_language_settings = "Язык"
        text_of_resolution_settings = "Разрешение"
        text_of_tip_button = "Подсказка"
        text_of_tip = (
            "\n"
            "Цель игры - разместить небоскрёбы по всем ячейкам сетки в соответствии со следующими правилами: \n\n"
            "1) Высота небоскрёбов варьируется от 1 до величины размера сетки, например для головоломки "
            "размером 4x4 высота небоскрёбов будет иметь значения от 1 до 4 \n\n"
            "2) В каждой строке и каждом столбце запрещено размещать небоскрёбы одинаковой высоты \n\n"
            "3) Числа по краям сетки указывают, какое количество небоскрёбов можно увидеть, "
            "если взглянуть в направлении, указанном стрелкой \n\n"
            "Разместите числа в каждой ячейке сетки для обозначения высоты небоскрёбов"
        )

    def English_lang(self):
        global text_of_play_button, text_of_shop_button, text_of_settings_button, text_of_achievements_button, \
            text_of_exit_button, text_of_back_button, text_of_language_settings, text_of_resolution_settings, \
            text_of_tip_button, text_of_tip

        text_of_play_button = "Play"
        text_of_shop_button = "Shop"
        text_of_settings_button = "Settings"
        text_of_achievements_button = "Achievements"
        text_of_exit_button = "Exit"
        text_of_back_button = "Back"
        text_of_language_settings = "Language"
        text_of_resolution_settings = "Resolution"
        text_of_tip_button = "Tip"
        text_of_tip = (
            "\n"
            "The goal of the game is to place skyscrapers on all cells of the grid in accordance with the following "
            "rules: \n\n"
            "1) The height of skyscrapers varies from 1 to the value of the grid size, for example for a puzzle "
            "4x4 size skyscrapers height will have values from 1 to 4 \n\n"
            "2) It is forbidden to place skyscrapers of the same height in each row and each column \n\n"
            "3) The numbers on the edges of the grid indicate how many skyscrapers you can see, "
            "if you look in the direction indicated by the arrow \n\n"
            "Place numbers in each grid cell to indicate the height of the skyscrapers"
        )


class Main_Menu(arcade.View):
    def __init__(self):
        super().__init__()
        # Create variables here
        self.manager = None
        self.v_box = None

    # Called when switching to this view
    def on_show_view(self):
        # Set background color
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

        def on_click_start(event):
            game_view = Game()
            game_view.setup()
            self.window.show_view(game_view)

        def on_click_shop(event):
            game_view = Shop()
            game_view.setup()
            self.window.show_view(game_view)

        def on_click_settings(event):
            game_view = Settings_Menu()
            game_view.setup()
            self.window.show_view(game_view)

        def on_click_achievements(event):
            game_view = Achievements()
            game_view.setup()
            self.window.show_view(game_view)

        def on_click_exit(event):
            arcade.exit()

        # --- Required for all code that uses UI element,
        # a UIManager to handle the UI.
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Create a vertical BoxGroup to align buttons
        self.v_box = arcade.gui.UIBoxLayout()

        # Create the buttons
        start_button = arcade.gui.UIFlatButton(text=text_of_play_button, width=200)
        self.v_box.add(start_button.with_space_around(bottom=20))

        shop_button = arcade.gui.UIFlatButton(text=text_of_shop_button, width=200)
        self.v_box.add(shop_button.with_space_around(bottom=20))

        settings_button = arcade.gui.UIFlatButton(text=text_of_settings_button, width=200)
        self.v_box.add(settings_button.with_space_around(bottom=20))

        achievements_button = arcade.gui.UIFlatButton(text=text_of_achievements_button, width=200)
        self.v_box.add(achievements_button.with_space_around(bottom=20))

        quit_button = arcade.gui.UIFlatButton(text=text_of_exit_button, width=200)
        self.v_box.add(quit_button.with_space_around(bottom=20))

        # Method for handling click events,
        # assign self.on_click_start as callback
        start_button.on_click = on_click_start
        shop_button.on_click = on_click_shop
        settings_button.on_click = on_click_settings
        achievements_button.on_click = on_click_achievements
        quit_button.on_click = on_click_exit

        # Create a widget to hold the v_box widget, that will center the buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

    # Draw the menu
    def on_draw(self):
        self.clear()
        self.manager.draw()


class Game(arcade.View):
    def __init__(self):
        super().__init__()
        # Create variables here
        self.v_box_of_tip_button = None
        self.manager_of_tip_button = None
        self.manager_of_back_button = None
        self.v_box_of_back_button = None

    def setup(self):
        """ This should set up your game and get it ready to play """
        # Replace 'pass' with the code to set up your game
        pass

    def on_show_view(self):
        """ Called when switching to this view"""
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)


        def on_click_exit_game(event):
            game_view = Main_Menu()
            self.window.show_view(game_view)

        def on_click_tip(event):
            message_box = arcade.gui.UIMessageBox(
                width=400,
                height=400,
                message_text= text_of_tip,
               buttons=["Ok"]
            )
            self.manager_of_tip_button.add(message_box)

        self.manager_of_back_button = arcade.gui.UIManager()
        self.manager_of_back_button.enable()
        self.manager_of_tip_button = arcade.gui.UIManager()
        self.manager_of_tip_button.enable()

        # Create a vertical BoxGroup to align buttons
        self.v_box_of_back_button = arcade.gui.UIBoxLayout()
        self.v_box_of_tip_button = arcade.gui.UIBoxLayout()

        exit_game_button = arcade.gui.UIFlatButton(text=text_of_back_button, width=200)
        self.v_box_of_back_button.add(exit_game_button.with_space_around(bottom=20))
        exit_game_button.on_click = on_click_exit_game

        tip_game_button = arcade.gui.UIFlatButton(text=text_of_tip_button, width=200)
        self.v_box_of_tip_button.add(tip_game_button.with_space_around(bottom=20))
        tip_game_button.on_click = on_click_tip

        self.manager_of_back_button.add(
            arcade.gui.UIAnchorWidget(
                align_x=WIDTH / 2 - 125,
                align_y=HEIGHT / 2 - 50,
                child=self.v_box_of_back_button)
        )
        self.manager_of_tip_button.add(
            arcade.gui.UIAnchorWidget(
                align_x=WIDTH / 2 - 125,
                align_y=HEIGHT / 2 - 115,
                child=self.v_box_of_tip_button)
        )

    def on_draw(self):
        """ Draw everything for the game. """
        self.clear()
        self.manager_of_back_button.draw()
        self.manager_of_tip_button.draw()




class Shop(arcade.View):
    def __init__(self):
        super().__init__()
        # Create variables here
        self.manager = None
        self.v_box = None

    def setup(self):
        """ This should set up your game and get it ready to play """
        # Replace 'pass' with the code to set up your game
        pass

    def on_show_view(self):
        """ Called when switching to this view"""
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

        def on_click_exit_settings(event):
            game_view = Main_Menu()
            self.window.show_view(game_view)

        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Create a vertical BoxGroup to align buttons
        self.v_box = arcade.gui.UIBoxLayout()

        exit_settings_button = arcade.gui.UIFlatButton(text=text_of_back_button, width=200)
        self.v_box.add(exit_settings_button.with_space_around(bottom=20))
        exit_settings_button.on_click = on_click_exit_settings

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                align_x=WIDTH / 2 - 125,
                align_y=HEIGHT / 2 - 50,
                child=self.v_box)
        )

    def on_draw(self):
        """ Draw everything for the game. """
        self.clear()
        self.manager.draw()


class Settings_Menu(arcade.View):
    def __init__(self):
        super().__init__()
        # Create variables here
        self.manager1 = None
        self.manager_of_language = None
        self.v_box = None
        self.v_box_of_language = None

    def setup(self):
        """ This should set up your game and get it ready to play """
        # Replace 'pass' with the code to set up your game
        pass

    def on_show_view(self):
        """ Called when switching to this view"""
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

        def on_click_exit_settings(event):
            game_view = Main_Menu()
            self.window.show_view(game_view)

        def on_click_russian_language(event):
            lang = Localization()
            lang.Russian_lang()
            game_view = Settings_Menu()
            game_view.setup()
            self.window.show_view(game_view)

        def on_click_english_language(event):
            lang = Localization()
            lang.English_lang()
            game_view = Settings_Menu()
            game_view.setup()
            self.window.show_view(game_view)

        self.manager1 = arcade.gui.UIManager()
        self.manager1.enable()
        self.manager_of_language = arcade.gui.UIManager()
        self.manager_of_language.enable()

        # Create a vertical BoxGroup to align buttons
        self.v_box = arcade.gui.UIBoxLayout()
        self.v_box_of_language = arcade.gui.UIBoxLayout()

        exit_settings_button = arcade.gui.UIFlatButton(text=text_of_back_button, width=200)
        self.v_box.add(exit_settings_button.with_space_around(bottom=20))
        exit_settings_button.on_click = on_click_exit_settings
        russian_language = arcade.gui.UIFlatButton(text="Русский", width=300)
        self.v_box_of_language.add(russian_language.with_space_around(bottom=20))
        russian_language.on_click = on_click_russian_language
        english_language = arcade.gui.UIFlatButton(text="English", width=300)
        self.v_box_of_language.add(english_language.with_space_around(bottom=20))
        english_language.on_click = on_click_english_language

        self.manager1.add(
            arcade.gui.UIAnchorWidget(
                align_x=WIDTH / 2 - 125,
                align_y=HEIGHT / 2 - 50,
                child=self.v_box)
        )
        self.manager_of_language.add(
            arcade.gui.UIAnchorWidget(
                align_x=-(WIDTH / 2 - (WIDTH / 8 + 25)),
                align_y=0,
                child=self.v_box_of_language)
        )

    def on_draw(self):
        """ Draw everything for the game. """
        self.clear()
        arcade.draw_rectangle_filled(WIDTH / 8 + 25, (HEIGHT - 250) / 2 + 25, WIDTH / 4, HEIGHT - 250,
                                     arcade.color.GRAY_BLUE)
        arcade.draw_text(text_of_language_settings, WIDTH / 8 + 25, (HEIGHT + 250) / 2 - 15,
                         arcade.color.WHITE, 30, anchor_x="center")
        arcade.draw_rectangle_filled((WIDTH / 3 + 25*5), (HEIGHT - 250) / 2 + 25, WIDTH / 4, HEIGHT - 250,
                                     arcade.color.GRAY_BLUE)
        arcade.draw_text(text_of_resolution_settings, WIDTH / 2.35, (HEIGHT + 250) / 2 - 15,
                         arcade.color.WHITE, 30, anchor_x="center")
        self.manager_of_language.draw()
        self.manager1.draw()


class Achievements(arcade.View):
    def __init__(self):
        super().__init__()
        # Create variables here
        self.manager = None
        self.v_box = None

    def setup(self):
        """ This should set up your game and get it ready to play """
        # Replace 'pass' with the code to set up your game
        pass

    def on_show_view(self):
        """ Called when switching to this view"""
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

        def on_click_exit_settings(event):
            game_view = Main_Menu()
            self.window.show_view(game_view)

        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Create a vertical BoxGroup to align buttons
        self.v_box = arcade.gui.UIBoxLayout()

        exit_settings_button = arcade.gui.UIFlatButton(text=text_of_back_button, width=200)
        self.v_box.add(exit_settings_button.with_space_around(bottom=20))
        exit_settings_button.on_click = on_click_exit_settings

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                align_x=WIDTH / 2 - 125,
                align_y=HEIGHT / 2 - 50,
                child=self.v_box)
        )

    def on_draw(self):
        """ Draw everything for the game. """
        self.clear()
        self.manager.draw()


# Start the program
def main():
    lang = Localization()
    lang.Russian_lang()
    window = arcade.Window(WIDTH, HEIGHT, "Skyscrapers")
    menu_view = Main_Menu()
    window.show_view(menu_view)
    arcade.run()


if __name__ == "__main__":
    main()
