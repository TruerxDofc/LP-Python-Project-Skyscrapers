import arcade
import arcade.gui

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 768

# Размер игрового поля
ROW_COUNT = 3
COLUMN_COUNT = 3

# Высота и ширина ячейки игрового поля и граница между ними
WIDTH = 100
HEIGHT = 100
MARGIN = 4


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

class MySprite(arcade.Sprite):
    def __init__(self, image_file, scale):
        super().__init__(image_file, scale)

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
            managerclear(self)

        def on_click_shop(event):
            game_view = Shop()
            game_view.setup()
            self.window.show_view(game_view)
            managerclear(self)

        def on_click_settings(event):
            game_view = Settings_Menu()
            game_view.setup()
            self.window.show_view(game_view)
            managerclear(self)

        def on_click_achievements(event):
            game_view = Achievements()
            game_view.setup()
            self.window.show_view(game_view)
            managerclear(self)

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
        self.v_box_of_tip_button = None
        self.manager_of_tip_button = None
        self.manager_of_back_button = None
        self.v_box_of_back_button = None

        self.grid_sprite_list = arcade.SpriteList()
        # тоже самое что выше, только на двумерный манер
        self.grid_sprites = []
        # указатель на значения в игровом поле
        self.grid_numbers = []

        # Создание игрового поля
        for row in range(ROW_COUNT):
            self.grid_sprites.append([])
            self.grid_numbers.append([])
            for column in range(COLUMN_COUNT):
                x = column * (WIDTH + MARGIN) + SCREEN_WIDTH/2 - (WIDTH + MARGIN)
                y = row * (HEIGHT + MARGIN) + SCREEN_HEIGHT/2 - (HEIGHT + MARGIN)
                sprite = MySprite("Product/0.png", 1)
                sprite.center_x = x
                sprite.center_y = y
                self.grid_sprite_list.append(sprite)
                self.grid_sprites[row].append(sprite)
                self.grid_numbers[row].append(0)
                print(self.grid_numbers) 

    def setup(self):
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
                align_x=SCREEN_WIDTH / 2 - 125,
                align_y=SCREEN_HEIGHT / 2 - 50,
                child=self.v_box_of_back_button)
        )
        self.manager_of_tip_button.add(
            arcade.gui.UIAnchorWidget(
                align_x=SCREEN_WIDTH / 2 - 125,
                align_y=SCREEN_HEIGHT / 2 - 115,
                child=self.v_box_of_tip_button)
        )

    def on_draw(self):
        # Отображение элементов
        self.clear()
        self.manager_of_back_button.draw()
        self.manager_of_tip_button.draw()

        self.grid_sprite_list.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        # Вызываетя при нажатии на мышь

        # Перевод координат нажатия мышью в элемент на сетке
        if x>= ((WIDTH + MARGIN) + SCREEN_WIDTH/2 - (WIDTH + MARGIN)*2.5 + 4) and y >= ((HEIGHT + MARGIN) + SCREEN_HEIGHT/2 - (HEIGHT + MARGIN)*2.5 + 4):
            column = int((x-((WIDTH + MARGIN) + SCREEN_WIDTH/2 - (WIDTH + MARGIN)*2.5 + 4)) // (WIDTH + MARGIN))
            row = int((y-((HEIGHT + MARGIN) + SCREEN_HEIGHT/2 - (HEIGHT + MARGIN)*2.5 + 4)) // (HEIGHT + MARGIN))

            print(f"Click coordinates: ({x}, {y}). Grid coordinates: ({row}, {column})")

        # Make sure we are on-grid. It is possible to click in the upper right
        # corner in the margin and go to a grid location that doesn't exist
            if row >= ROW_COUNT or column >= COLUMN_COUNT:
                # Simply return from this method since nothing needs updating
                return
            
            for i in range(0, 5):
                if self.grid_numbers[row][column] == i:
                    self.grid_sprites[row][column].texture = arcade.load_texture(f"Product/{i+1}.png")
                    self.grid_numbers[row][column] = i+1
                    break
                elif self.grid_numbers[row][column] == 5:
                    self.grid_sprites[row][column].texture = arcade.load_texture("Product/0.png")
                    self.grid_numbers[row][column] = 0
                    break
            print(self.grid_numbers)




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
                align_x=SCREEN_WIDTH / 2 - 125,
                align_y=SCREEN_HEIGHT / 2 - 50,
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
                align_x=SCREEN_WIDTH / 2 - 125,
                align_y=SCREEN_HEIGHT / 2 - 50,
                child=self.v_box)
        )
        self.manager_of_language.add(
            arcade.gui.UIAnchorWidget(
                align_x=-(SCREEN_WIDTH / 2 - (SCREEN_WIDTH / 8 + 25)),
                align_y=0,
                child=self.v_box_of_language)
        )

    def on_draw(self):
        """ Draw everything for the game. """
        self.clear()
        arcade.draw_rectangle_filled(SCREEN_WIDTH / 8 + 25, (SCREEN_HEIGHT - 250) / 2 + 25, SCREEN_WIDTH / 4, SCREEN_HEIGHT - 250,
                                     arcade.color.GRAY_BLUE)
        arcade.draw_text(text_of_language_settings, SCREEN_WIDTH / 8 + 25, (SCREEN_HEIGHT + 250) / 2 - 15,
                         arcade.color.WHITE, 30, anchor_x="center")
        arcade.draw_rectangle_filled((SCREEN_WIDTH / 3 + 25*5), (SCREEN_HEIGHT - 250) / 2 + 25, SCREEN_WIDTH / 4, SCREEN_HEIGHT - 250,
                                     arcade.color.GRAY_BLUE)
        arcade.draw_text(text_of_resolution_settings, SCREEN_WIDTH / 2.35, (SCREEN_HEIGHT + 250) / 2 - 15,
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
                align_x=SCREEN_WIDTH / 2 - 125,
                align_y=SCREEN_HEIGHT / 2 - 50,
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
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "Skyscrapers")
    menu_view = Main_Menu()
    window.show_view(menu_view)
    arcade.run()

def managerclear(self):
    self.manager.clear()

if __name__ == "__main__":
    main()


