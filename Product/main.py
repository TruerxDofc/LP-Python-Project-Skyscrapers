import arcade
import arcade.gui
import random
import re

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 768

# Размер игрового поля
ROW_COUNT = 5
COLUMN_COUNT = 5

# Высота и ширина ячейки игрового поля и граница между ними
WIDTH = 60
HEIGHT = 60
MARGIN = 2


text_of_play_button = ""; text_of_shop_button = ""; text_of_settings_button = ""
text_of_achievements_button = ""; text_of_exit_button = ""; text_of_back_button = ""; text_of_back_to_mm = ""
text_of_language_settings = ""; text_of_resolution_settings = ""
text_of_tip_button = ""; text_of_tip = ""; text_of_game3x3 = ""; text_of_game4x4 = ""; text_of_game5x5 = ""; text_of_win_window = ""; text_of_win_window_coins = ""
text_of_win_window_coin = ""; text_of_shop_coins = ""; text_of_shop_background = ""; text_of_shop_grid = "";
text_of_shop_background_default = ""; text_of_shop_background_car = ""; text_of_shop_background_mountain = ""; text_of_shop_background_window = ""
text_of_shop_grid_default = ""; text_of_shop_grid_orange = ""; text_of_shop_grid_pastel = ""; text_of_shop_grid_pixel = "";

class Localization():
    def Russian_lang(self):
        global text_of_play_button, text_of_shop_button, text_of_settings_button, text_of_achievements_button, \
            text_of_exit_button, text_of_back_button, text_of_back_to_mm, text_of_language_settings, text_of_resolution_settings, \
            text_of_tip_button, text_of_tip, text_of_game3x3, text_of_game4x4, text_of_game5x5, text_of_win_window, text_of_win_window_coins, \
            text_of_win_window_coin, text_of_shop_coins, text_of_shop_background, text_of_shop_grid, \
            text_of_shop_background_default, text_of_shop_background_car, text_of_shop_background_mountain, text_of_shop_background_window, \
            text_of_shop_grid_default, text_of_shop_grid_orange, text_of_shop_grid_pastel, text_of_shop_grid_pixel

        text_of_play_button = "Играть"
        text_of_shop_button = "Магазин"
        text_of_settings_button = "Настройки"
        text_of_achievements_button = "Достижения"
        text_of_exit_button = "Выход"
        text_of_back_button = "Назад"
        text_of_back_to_mm = "В Главное меню"
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
        text_of_game3x3 = "Размер 3х3"
        text_of_game4x4 = "Размер 4х4"
        text_of_game5x5 = "Размер 5х5"
        text_of_win_window = "Поздравляем! Вы решили задачку!"
        text_of_win_window_coins = "Вы получили: "
        text_of_win_window_coin = "монет"
        text_of_shop_coins = "Ваши монеты: "
        text_of_shop_background = "Фон" 
        text_of_shop_grid = "Сетка"
        text_of_shop_background_default = "Простой" 
        text_of_shop_background_car = "Спорткар"
        text_of_shop_background_mountain = "Горы"
        text_of_shop_background_window = "Окно"
        text_of_shop_grid_default = "Простая"; 
        text_of_shop_grid_orange = "Фиолетово-оранжевая"
        text_of_shop_grid_pastel = "Пастельная"
        text_of_shop_grid_pixel = "Пиксельная";

    def English_lang(self):
        global text_of_play_button, text_of_shop_button, text_of_settings_button, text_of_achievements_button, \
            text_of_exit_button, text_of_back_button, text_of_back_to_mm, text_of_language_settings, text_of_resolution_settings, \
            text_of_tip_button, text_of_tip, text_of_game3x3, text_of_game4x4, text_of_game5x5, text_of_win_window, text_of_win_window_coins, \
            text_of_win_window_coin, text_of_shop_coins, text_of_shop_background, text_of_shop_grid, \
            text_of_shop_background_default, text_of_shop_background_car, text_of_shop_background_mountain, text_of_shop_background_window, \
            text_of_shop_grid_default, text_of_shop_grid_orange, text_of_shop_grid_pastel, text_of_shop_grid_pixel

        text_of_play_button = "Play"
        text_of_shop_button = "Shop"
        text_of_settings_button = "Settings"
        text_of_achievements_button = "Achievements"
        text_of_exit_button = "Exit"
        text_of_back_button = "Back"
        text_of_back_to_mm = "To the Main Menu"
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
        text_of_game3x3 = "Size 3x3"
        text_of_game4x4 = "Size 4x4"
        text_of_game5x5 = "Size 5x5"
        text_of_win_window = "Congratulations! You solved the problem!"
        text_of_win_window_coins = "You got: "
        text_of_win_window_coin = "coins"
        text_of_shop_coins = "Your coins: "
        text_of_shop_background = "Background" 
        text_of_shop_grid = "Grid"
        text_of_shop_background_default = "Простой" 
        text_of_shop_background_car = "Спорткар"
        text_of_shop_background_mountain = "Горы"
        text_of_shop_background_window = "Окно"
        text_of_shop_grid_default = "Простая"; 
        text_of_shop_grid_orange = "Фиолетово-оранжевая"
        text_of_shop_grid_pastel = "Пастельная"
        text_of_shop_grid_pixel = "Пиксельная";

    def German_lang(self):
        global text_of_play_button, text_of_shop_button, text_of_settings_button, text_of_achievements_button, \
            text_of_exit_button, text_of_back_button, text_of_back_to_mm, text_of_language_settings, text_of_resolution_settings, \
            text_of_tip_button, text_of_tip, text_of_game3x3, text_of_game4x4, text_of_game5x5, text_of_win_window, text_of_win_window_coins, \
            text_of_win_window_coin, text_of_shop_coins, text_of_shop_background, text_of_shop_grid, \
            text_of_shop_background_default, text_of_shop_background_car, text_of_shop_background_mountain, text_of_shop_background_window, \
            text_of_shop_grid_default, text_of_shop_grid_orange, text_of_shop_grid_pastel, text_of_shop_grid_pixel

        text_of_play_button = "Spielen"
        text_of_shop_button = "Geschäft"
        text_of_settings_button = "Einstellungen"
        text_of_achievements_button = "Errungenschaften"
        text_of_exit_button = "Ausfahrt"
        text_of_back_button = "Zurück"
        text_of_back_to_mm = "Zum Hauptmenü"
        text_of_language_settings = "Sprache"
        text_of_resolution_settings = "Auflösung"
        text_of_tip_button = "Tipp"
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
        text_of_game3x3 = "Format 3x3"
        text_of_game4x4 = "Format 4x4"
        text_of_game5x5 = "Format 5x5"
        text_of_win_window = "Herzlichen Glückwunsch! Sie haben das Problem gelöst!"
        text_of_win_window_coins = "Sie haben: "
        text_of_win_window_coin = "Münzen"
        text_of_shop_coins = "Ihre Münzen: "
        text_of_shop_background = "Hintergrund" 
        text_of_shop_grid = "Raster"
        text_of_shop_background_default = "Простой" 
        text_of_shop_background_car = "Спорткар"
        text_of_shop_background_mountain = "Горы"
        text_of_shop_background_window = "Окно"
        text_of_shop_grid_default = "Простая"; 
        text_of_shop_grid_orange = "Фиолетово-оранжевая"
        text_of_shop_grid_pastel = "Пастельная"
        text_of_shop_grid_pixel = "Пиксельная";

    def Franch_lang(self):
        global text_of_play_button, text_of_shop_button, text_of_settings_button, text_of_achievements_button, \
            text_of_exit_button, text_of_back_button, text_of_back_to_mm, text_of_language_settings, text_of_resolution_settings, \
            text_of_tip_button, text_of_tip, text_of_game3x3, text_of_game4x4, text_of_game5x5, text_of_win_window, text_of_win_window_coins, \
            text_of_win_window_coin, text_of_shop_coins, text_of_shop_background, text_of_shop_grid, \
            text_of_shop_background_default, text_of_shop_background_car, text_of_shop_background_mountain, text_of_shop_background_window, \
            text_of_shop_grid_default, text_of_shop_grid_orange, text_of_shop_grid_pastel, text_of_shop_grid_pixel

        text_of_play_button = "Jouer"
        text_of_shop_button = "Boutique"
        text_of_settings_button = "Paramètres"
        text_of_achievements_button = "Réalisations"
        text_of_exit_button = "Sortie"
        text_of_back_button = "Retour"
        text_of_back_to_mm = "Vers le menu principal"
        text_of_language_settings = "Langue"
        text_of_resolution_settings = "Résolution"
        text_of_tip_button = "Conseil"
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
        text_of_game3x3 = "Taille 3x3"
        text_of_game4x4 = "Taille 4x4"
        text_of_game5x5 = "Taille 5x5"
        text_of_win_window = "Félicitations ! Vous avez résolu le problème !"
        text_of_win_window_coins = "Vous avez: "
        text_of_win_window_coin = "pièces de monnaie"
        text_of_shop_coins = "Vos pièces: "
        text_of_shop_background = "Contexte" 
        text_of_shop_grid = "Grille"
        text_of_shop_background_default = "Простой" 
        text_of_shop_background_car = "Спорткар"
        text_of_shop_background_mountain = "Горы"
        text_of_shop_background_window = "Окно"
        text_of_shop_grid_default = "Простая"; 
        text_of_shop_grid_orange = "Фиолетово-оранжевая"
        text_of_shop_grid_pastel = "Пастельная"
        text_of_shop_grid_pixel = "Пиксельная";

# Перестановка столбцов массива
def transpose_columns(matrix, col1, col2):
    for row in matrix:
        row[col1], row[col2] = row[col2], row[col1]

# Перестановка строк массива
def transpose_rows(matrix, row1, row2):
    matrix[row1], matrix[row2] = matrix[row2], matrix[row1]

# Уменьшение массива
def resize_array(array, rangeArr):
    resized_array = [[0] * rangeArr for _ in range(rangeArr)]  # Создаем новый массив размером 3x3, заполненный нулями
    
    for i in range(1, len(array[0])-1):
        for j in range(1, len(array[0])-1):
            resized_array[i-1][j-1] = array[i][j]  # Копируем элементы из исходного массива
            
    return resized_array

# Генерация подсказок на границах
def generate_array(input_array):
    n = len(input_array)
    output_array = [[0] * (n + 2) for _ in range(n + 2)]

    max_visible = 0
    count_visible = 0
    # Заполнение левой стороны
    for i in range(n):
        for j in range(n):
            if max_visible < input_array[i][j]:
                max_visible = input_array[i][j]
                count_visible += 1

        output_array[i+1][0] = count_visible
        max_visible = 0
        count_visible = 0

    # Заполнение правой стороны
    for i in range(n):
        for j in range(n, -1, -1):
            if max_visible < input_array[i][j-1]:
                max_visible = input_array[i][j-1]
                count_visible += 1

        output_array[i+1][n+1] = count_visible
        max_visible = 0
        count_visible = 0

    # Заполнение нижней стороны
    for j in range(n):
        for i in range(n, -1, -1):
            if max_visible < input_array[i-1][j]:
                max_visible = input_array[i-1][j]
                count_visible += 1

        output_array[n+1][j+1] = count_visible
        max_visible = 0
        count_visible = 0

    # Заполнение верхней стороны
    for j in range(n):
        for i in range(n):
            if max_visible < input_array[i][j]:
                max_visible = input_array[i][j]
                count_visible += 1

        output_array[0][j+1] = count_visible
        max_visible = 0
        count_visible = 0

    return output_array

# Добавить значение в meta файл
def write_data(file_name, word, data):
    with open(file_name, 'r+') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            if word in line:
                lines[i] = '{} {}\n'.format(word, data)
                break
        file.seek(0)
        file.writelines(lines)

# Извлечь значение из meta файла
def read_data(file_name, word):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if word in line:
                data = re.search(r'{}(.*)'.format(word), line).group(1)
                return data.strip()
            

class MySprite(arcade.Sprite):
    def __init__(self, image_file, scale):
        super().__init__(image_file, scale)


class Main_Menu(arcade.View):
    def __init__(self):
        super().__init__()
        # Create variables here
        self.manager = None
        self.v_box = None

        self.background = arcade.load_texture(f"Product/background_{background_mode}.jpg")
        

    # Called when switching to this view
    def on_show_view(self):
        # Set background color
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

        def on_click_start(event):
            game_view = Game_Choose()
            game_view.setup()
            self.window.show_view(game_view)
            managerclear(self)
            uimanagerclear(self)

        def on_click_shop(event):
            game_view = Shop()
            game_view.setup()
            self.window.show_view(game_view)
            managerclear(self)
            uimanagerclear(self)

        def on_click_settings(event):
            game_view = Settings_Menu()
            game_view.setup()
            self.window.show_view(game_view)
            managerclear(self)
            uimanagerclear(self)

        def on_click_achievements(event):
            game_view = Achievements()
            game_view.setup()
            self.window.show_view(game_view)
            managerclear(self)
            uimanagerclear(self)

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
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.manager.draw()


class Game_Choose(arcade.View):
    def __init__(self):
        super().__init__()
        # Create variables here
        self.manager = None
        self.v_box = None

        self.background = arcade.load_texture(f"Product/background_{background_mode}.jpg")

        self.manager_of_back_button = None
        self.v_box_of_back_button = None

    def setup(self):
        """ This should set up your game and get it ready to play """
        # Replace 'pass' with the code to set up your game
        pass

    def on_show_view(self):
        """ Called when switching to this view"""
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

        def on_click_game3x3(event):
            game_view = Game_3x3()
            self.window.show_view(game_view)
            managerclear(self)
            uimanagerclear(self)

        def on_click_game4x4(event):
            game_view = Game_4x4()
            self.window.show_view(game_view)
            managerclear(self)
            uimanagerclear(self)

        def on_click_game5x5(event):
            game_view = Game_5x5()
            self.window.show_view(game_view)
            managerclear(self)
            uimanagerclear(self)

        def on_click_exit_settings(event):
            game_view = Main_Menu()
            self.window.show_view(game_view)
            managerclear(self)
            uimanagerclear(self)

        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        self.manager_of_back_button = arcade.gui.UIManager()
        self.manager_of_back_button.enable()

        # Create a vertical BoxGroup to align buttons
        self.v_box = arcade.gui.UIBoxLayout()
        self.v_box_of_back_button = arcade.gui.UIBoxLayout()

        game3x3 = arcade.gui.UIFlatButton(text=text_of_game3x3, width=200)
        self.v_box.add(game3x3.with_space_around(bottom=20))
        game3x3.on_click = on_click_game3x3

        game4x4 = arcade.gui.UIFlatButton(text=text_of_game4x4, width=200)
        self.v_box.add(game4x4.with_space_around(bottom=20))
        game4x4.on_click = on_click_game4x4

        game5x5 = arcade.gui.UIFlatButton(text=text_of_game5x5, width=200)
        self.v_box.add(game5x5.with_space_around(bottom=20))
        game5x5.on_click = on_click_game5x5

        exit_settings_button = arcade.gui.UIFlatButton(text=text_of_back_button, width=200)
        self.v_box_of_back_button.add(exit_settings_button.with_space_around(bottom=20))
        exit_settings_button.on_click = on_click_exit_settings

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                align_x=0,
                align_y=0,
                child=self.v_box)
        )
        self.manager_of_back_button.add(
            arcade.gui.UIAnchorWidget(
                align_x=SCREEN_WIDTH / 2 - 125,
                align_y=SCREEN_HEIGHT / 2 - 50,
                child=self.v_box_of_back_button)
        )

    def on_draw(self):
        """ Draw everything for the game. """
        self.clear()
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.manager.draw()
        self.manager_of_back_button.draw()


class Game_3x3(arcade.View):
    def __init__(self):
        super().__init__()
        self.v_box_of_tip_button = None
        self.manager_of_tip_button = None
        self.manager_of_back_button = None
        self.v_box_of_back_button = None

        self.background = arcade.load_texture(f"Product/background_{background_mode}.jpg")

        self.grid_sprite_list = arcade.SpriteList()
        # тоже что {grid_sprite_list}, только на двумерный манер
        self.grid_sprites = []
        # указатель на значения в игровом поле
        self.grid_numbers = []

        # основа сгенерированной сетки
        self.grid_generated = [
            [1,2,3],
            [3,1,2],
            [2,3,1]
        ]

        self.grid_numbers_less = []

        global ROW_COUNT
        ROW_COUNT = 5
        global COLUMN_COUNT
        COLUMN_COUNT = 5

        # Случайная перестановка столбцов
        randomLoopCount = random.randint(1,4)
        for i in range(1, randomLoopCount):
            randomLine1 = random.randint(0,2)
            randomLine2 = random.randint(0,2)
            while randomLine1 == randomLine2:
                randomLine2 = random.randint(0,2)
            transpose_columns(self.grid_generated, randomLine1, randomLine2)
        
        # Случайная перестановка строк
        randomLoopCount = random.randint(1,4)
        for i in range(1, randomLoopCount):
            randomLine1 = random.randint(0,2)
            randomLine2 = random.randint(0,2)
            while randomLine1 == randomLine2:
                randomLine2 = random.randint(0,2)
            transpose_rows(self.grid_generated, randomLine1, randomLine2)

        for line in self.grid_generated:
            print(line)

        # Создаем подсказки на границах
        self.grid_numbers = generate_array(self.grid_generated)

        global grid_mode
        # Создание игрового поля
        for row in range(ROW_COUNT):
            self.grid_sprites.append([])
            self.grid_numbers.append([])
            for column in range(COLUMN_COUNT):
                x = column * (WIDTH + MARGIN) + SCREEN_WIDTH/2 - (WIDTH + MARGIN)*2
                y = row * (HEIGHT + MARGIN) + SCREEN_HEIGHT/2 - (HEIGHT + MARGIN)*3
                sprite = MySprite(f"Product/0_{grid_mode}.png", 0.6)
                like_empty_sprite = MySprite("Product/empty.png", 0.6)
                if row == 0 and self.grid_numbers[row][column] != 0:
                    like_empty_sprite = MySprite(f"Product/down{self.grid_numbers[row][column]}_{grid_mode}.png", 0.6)
                if row == ROW_COUNT-1 and self.grid_numbers[row][column] != 0:
                    like_empty_sprite = MySprite(f"Product/up{self.grid_numbers[row][column]}_{grid_mode}.png", 0.6)
                if column == 0 and self.grid_numbers[row][column] != 0:
                    like_empty_sprite = MySprite(f"Product/left{self.grid_numbers[row][column]}_{grid_mode}.png", 0.6)    
                if column == COLUMN_COUNT-1 and self.grid_numbers[row][column] != 0:
                    like_empty_sprite = MySprite(f"Product/right{self.grid_numbers[row][column]}_{grid_mode}.png", 0.6)    
                empty_sprite = MySprite("Product/empty.png", 0.6)
                sprite.center_x = x
                sprite.center_y = y
                like_empty_sprite.center_x = x
                like_empty_sprite.center_y = y
                empty_sprite.center_x = x
                empty_sprite.center_y = y
                if (row == 0 and column == 0) or (row == ROW_COUNT-1 and column == COLUMN_COUNT-1) or (row == 0 and column == COLUMN_COUNT-1) or (row == ROW_COUNT-1 and column == 0):
                    self.grid_sprite_list.append(empty_sprite)
                    self.grid_sprites[row].append(empty_sprite)
                elif row == 0 or row == ROW_COUNT - 1 or column == 0 or column == COLUMN_COUNT - 1:
                    self.grid_sprite_list.append(like_empty_sprite)
                    self.grid_sprites[row].append(like_empty_sprite)
                else:
                    self.grid_sprite_list.append(sprite)
                    self.grid_sprites[row].append(sprite)
                self.grid_numbers[row].append(0)

    def setup(self):
        pass

    def on_show_view(self):
        """ Called when switching to this view"""
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)


        def on_click_exit_to_mm(event):
            game_view = Main_Menu()
            self.window.show_view(game_view)
            managerclear(self)
            uimanagerclear(self)

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

        exit_game_button = arcade.gui.UIFlatButton(text=text_of_back_to_mm, width=200)
        self.v_box_of_back_button.add(exit_game_button.with_space_around(bottom=20))
        exit_game_button.on_click = on_click_exit_to_mm

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

        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        self.grid_sprite_list.draw()
        
        self.manager_of_back_button.draw()
        self.manager_of_tip_button.draw()

        

    def on_mouse_press(self, x, y, button, modifiers):
        # Вызываетя при нажатии на мышь

        # Перевод координат нажатия мышью в элемент на сетке
        # В условии необходимо ставить коэффициент равный генерации сетки+0,5, а в вычислении ячейки ставить коэффициент равный генерации сетки+1,5
        if x>= ((WIDTH + MARGIN) + SCREEN_WIDTH/2 - (WIDTH + MARGIN)*2.4 + 2) and y >= ((HEIGHT + MARGIN) + SCREEN_HEIGHT/2 - (HEIGHT + MARGIN)*3.4 + 2) and x<= ((WIDTH + MARGIN) + SCREEN_WIDTH/2 + (WIDTH + MARGIN)*0.5 + 2) and y <= ((HEIGHT + MARGIN) + SCREEN_HEIGHT/2 - (HEIGHT + MARGIN)*0.5 + 2):
            column = int((x-((WIDTH + MARGIN) + SCREEN_WIDTH/2 - (WIDTH + MARGIN)*3.5 + 4)) // (WIDTH + MARGIN))
            row = int((y-((HEIGHT + MARGIN) + SCREEN_HEIGHT/2 - (HEIGHT + MARGIN)*4.5 + 4)) // (HEIGHT + MARGIN))

            print(f"Click coordinates: ({x}, {y}). Grid coordinates: ({row}, {column})")

        # Make sure we are on-grid. It is possible to click in the upper right
        # corner in the margin and go to a grid location that doesn't exist
            if row >= ROW_COUNT or column >= COLUMN_COUNT:
                # Simply return from this method since nothing needs updating
                return
            
            for i in range(0, 3):
                if self.grid_numbers[row][column] == i:
                    self.grid_sprites[row][column].texture = arcade.load_texture(f"Product/{i+1}_{grid_mode}.png")
                    self.grid_numbers[row][column] = i+1
                    break
                elif self.grid_numbers[row][column] == 3:
                    self.grid_sprites[row][column].texture = arcade.load_texture(f"Product/0_{grid_mode}.png")
                    self.grid_numbers[row][column] = 0
                    break
            print(self.grid_numbers)

            # Проверка на правильность
            self.grid_numbers_less = [row[1:4] for row in self.grid_numbers[1:4]]

            if self.grid_numbers_less == self.grid_generated:
                global amount_of_coins
                amount_of_coins = 5
                coin = int(read_data('Product/meta.txt', 'coins =')) + 5
                write_data('Product/meta.txt', 'coins =', coin)
                game_view = Win_window()
                self.window.show_view(game_view)
                managerclear(self)
                uimanagerclear(self)

            
            

class Game_4x4(arcade.View):
    def __init__(self):
        super().__init__()
        self.v_box_of_tip_button = None
        self.manager_of_tip_button = None
        self.manager_of_back_button = None
        self.v_box_of_back_button = None

        self.background = arcade.load_texture(f"Product/background_{background_mode}.jpg")

        self.grid_sprite_list = arcade.SpriteList()
        # тоже что {grid_sprite_list}, только на двумерный манер
        self.grid_sprites = []
        # указатель на значения в игровом поле
        self.grid_numbers = []

        # основа сгенерированной сетки
        self.grid_generated = [
            [1,2,3,4],
            [4,1,2,3],
            [3,4,1,2],
            [2,3,4,1]
        ]

        self.grid_numbers_less = []

        global ROW_COUNT
        ROW_COUNT = 6
        global COLUMN_COUNT
        COLUMN_COUNT = 6

        # Случайная перестановка столбцов
        randomLoopCount = random.randint(1,4)
        for i in range(1, randomLoopCount):
            randomLine1 = random.randint(0,3)
            randomLine2 = random.randint(0,3)
            while randomLine1 == randomLine2:
                randomLine2 = random.randint(0,3)
            transpose_columns(self.grid_generated, randomLine1, randomLine2)
        
        # Случайная перестановка строк
        randomLoopCount = random.randint(1,4)
        for i in range(1, randomLoopCount):
            randomLine1 = random.randint(0,3)
            randomLine2 = random.randint(0,3)
            while randomLine1 == randomLine2:
                randomLine2 = random.randint(0,3)
            transpose_rows(self.grid_generated, randomLine1, randomLine2)

        for line in self.grid_generated:
            print(line)

        # Создаем подсказки на границах
        self.grid_numbers = generate_array(self.grid_generated)

        # Создание игрового поля
        for row in range(ROW_COUNT):
            self.grid_sprites.append([])
            self.grid_numbers.append([])
            for column in range(COLUMN_COUNT):
                x = column * (WIDTH + MARGIN) + SCREEN_WIDTH/2 - (WIDTH + MARGIN)*2.5
                y = row * (HEIGHT + MARGIN) + SCREEN_HEIGHT/2 - (HEIGHT + MARGIN)*3.5
                sprite = MySprite(f"Product/0_{grid_mode}.png", 0.6)
                like_empty_sprite = MySprite("Product/empty.png", 0.6)
                if row == 0 and self.grid_numbers[row][column] != 0:
                    like_empty_sprite = MySprite(f"Product/down{self.grid_numbers[row][column]}_{grid_mode}.png", 0.6)
                if row == ROW_COUNT-1 and self.grid_numbers[row][column] != 0:
                    like_empty_sprite = MySprite(f"Product/up{self.grid_numbers[row][column]}_{grid_mode}.png", 0.6)
                if column == 0 and self.grid_numbers[row][column] != 0:
                    like_empty_sprite = MySprite(f"Product/left{self.grid_numbers[row][column]}_{grid_mode}.png", 0.6)    
                if column == COLUMN_COUNT-1 and self.grid_numbers[row][column] != 0:
                    like_empty_sprite = MySprite(f"Product/right{self.grid_numbers[row][column]}_{grid_mode}.png", 0.6)    
                empty_sprite = MySprite("Product/empty.png", 0.6)
                sprite.center_x = x
                sprite.center_y = y
                like_empty_sprite.center_x = x
                like_empty_sprite.center_y = y
                empty_sprite.center_x = x
                empty_sprite.center_y = y
                if (row == 0 and column == 0) or (row == ROW_COUNT-1 and column == COLUMN_COUNT-1) or (row == 0 and column == COLUMN_COUNT-1) or (row == ROW_COUNT-1 and column == 0):
                    self.grid_sprite_list.append(empty_sprite)
                    self.grid_sprites[row].append(empty_sprite)
                elif row == 0 or row == ROW_COUNT - 1 or column == 0 or column == COLUMN_COUNT - 1:
                    self.grid_sprite_list.append(like_empty_sprite)
                    self.grid_sprites[row].append(like_empty_sprite)
                else:
                    self.grid_sprite_list.append(sprite)
                    self.grid_sprites[row].append(sprite)
                self.grid_numbers[row].append(0)

    def setup(self):
        pass

    def on_show_view(self):
        """ Called when switching to this view"""
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)


        def on_click_exit_to_mm(event):
            game_view = Main_Menu()
            self.window.show_view(game_view)
            managerclear(self)
            uimanagerclear(self)

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

        exit_game_button = arcade.gui.UIFlatButton(text=text_of_back_to_mm, width=200)
        self.v_box_of_back_button.add(exit_game_button.with_space_around(bottom=20))
        exit_game_button.on_click = on_click_exit_to_mm

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
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.grid_sprite_list.draw()
        
        self.manager_of_back_button.draw()
        self.manager_of_tip_button.draw()

        

    def on_mouse_press(self, x, y, button, modifiers):
        # Вызываетя при нажатии на мышь

        # Перевод координат нажатия мышью в элемент на сетке
        # В условии необходимо ставить коэффициент равный генерации сетки+0,5, а в вычислении ячейки ставить коэффициент равный генерации сетки+1,5
        if x>= ((WIDTH + MARGIN) + SCREEN_WIDTH/2 - (WIDTH + MARGIN)*3 + 4) and y >= ((HEIGHT + MARGIN) + SCREEN_HEIGHT/2 - (HEIGHT + MARGIN)*4 + 4) and x<= ((WIDTH + MARGIN) + SCREEN_WIDTH/2 + (WIDTH + MARGIN)*1 + 2) and y <= ((HEIGHT + MARGIN) + SCREEN_HEIGHT/2 + (HEIGHT + MARGIN)*0 + 2):
            column = int((x-((WIDTH + MARGIN) + SCREEN_WIDTH/2 - (WIDTH + MARGIN)*4 + 4)) // (WIDTH + MARGIN))
            row = int((y-((HEIGHT + MARGIN) + SCREEN_HEIGHT/2 - (HEIGHT + MARGIN)*5 + 4)) // (HEIGHT + MARGIN))

            print(f"Click coordinates: ({x}, {y}). Grid coordinates: ({row}, {column})")

        # Make sure we are on-grid. It is possible to click in the upper right
        # corner in the margin and go to a grid location that doesn't exist
            if row >= ROW_COUNT or column >= COLUMN_COUNT:
                # Simply return from this method since nothing needs updating
                return
            
            for i in range(0, 4):
                if self.grid_numbers[row][column] == i:
                    self.grid_sprites[row][column].texture = arcade.load_texture(f"Product/{i+1}_{grid_mode}.png")
                    self.grid_numbers[row][column] = i+1
                    break
                elif self.grid_numbers[row][column] == 4:
                    self.grid_sprites[row][column].texture = arcade.load_texture(f"Product/0_{grid_mode}.png")
                    self.grid_numbers[row][column] = 0
                    break
            print(self.grid_numbers)

            # Проверка на правильность
            self.grid_numbers_less = self.grid_numbers

            self.grid_numbers_less = [row[1:5] for row in self.grid_numbers[1:5]]

            if self.grid_numbers_less == self.grid_generated:
                global amount_of_coins
                amount_of_coins = 30
                coin = int(read_data('Product/meta.txt', 'coins =')) + 30
                write_data('Product/meta.txt', 'coins =', coin)
                game_view = Win_window()
                self.window.show_view(game_view)
                managerclear(self)
                uimanagerclear(self)


class Game_5x5(arcade.View):
    def __init__(self):
        super().__init__()
        self.v_box_of_tip_button = None
        self.manager_of_tip_button = None
        self.manager_of_back_button = None
        self.v_box_of_back_button = None

        self.background = arcade.load_texture(f"Product/background_{background_mode}.jpg")

        self.grid_sprite_list = arcade.SpriteList()
        # тоже что {grid_sprite_list}, только на двумерный манер
        self.grid_sprites = []
        # указатель на значения в игровом поле
        self.grid_numbers = []

        # основа сгенерированной сетки
        self.grid_generated = [
            [1,2,3,4,5],
            [5,1,2,3,4],
            [4,5,1,2,3],
            [3,4,5,1,2],
            [2,3,4,5,1]
        ]

        self.grid_numbers_less = []

        global ROW_COUNT
        ROW_COUNT = 7
        global COLUMN_COUNT
        COLUMN_COUNT = 7

        # Случайная перестановка столбцов
        randomLoopCount = random.randint(1,4)
        for i in range(1, randomLoopCount):
            randomLine1 = random.randint(0,4)
            randomLine2 = random.randint(0,4)
            while randomLine1 == randomLine2:
                randomLine2 = random.randint(0,4)
            transpose_columns(self.grid_generated, randomLine1, randomLine2)
        
        # Случайная перестановка строк
        randomLoopCount = random.randint(1,4)
        for i in range(1, randomLoopCount):
            randomLine1 = random.randint(0,4)
            randomLine2 = random.randint(0,4)
            while randomLine1 == randomLine2:
                randomLine2 = random.randint(0,4)
            transpose_rows(self.grid_generated, randomLine1, randomLine2)

        for line in self.grid_generated:
            print(line)

        # Создаем подсказки на границах
        self.grid_numbers = generate_array(self.grid_generated)

        # Создание игрового поля
        for row in range(ROW_COUNT):
            self.grid_sprites.append([])
            self.grid_numbers.append([])
            for column in range(COLUMN_COUNT):
                x = column * (WIDTH + MARGIN) + SCREEN_WIDTH/2 - (WIDTH + MARGIN)*3
                y = row * (HEIGHT + MARGIN) + SCREEN_HEIGHT/2 - (HEIGHT + MARGIN)*4
                sprite = MySprite(f"Product/0_{grid_mode}.png", 0.6)
                like_empty_sprite = MySprite("Product/empty.png", 0.6)
                if row == 0 and self.grid_numbers[row][column] != 0:
                    like_empty_sprite = MySprite(f"Product/down{self.grid_numbers[row][column]}_{grid_mode}.png", 0.6)
                if row == ROW_COUNT-1 and self.grid_numbers[row][column] != 0:
                    like_empty_sprite = MySprite(f"Product/up{self.grid_numbers[row][column]}_{grid_mode}.png", 0.6)
                if column == 0 and self.grid_numbers[row][column] != 0:
                    like_empty_sprite = MySprite(f"Product/left{self.grid_numbers[row][column]}_{grid_mode}.png", 0.6)    
                if column == COLUMN_COUNT-1 and self.grid_numbers[row][column] != 0:
                    like_empty_sprite = MySprite(f"Product/right{self.grid_numbers[row][column]}_{grid_mode}.png", 0.6)    
                empty_sprite = MySprite("Product/empty.png", 0.6)
                sprite.center_x = x
                sprite.center_y = y
                like_empty_sprite.center_x = x
                like_empty_sprite.center_y = y
                empty_sprite.center_x = x
                empty_sprite.center_y = y
                if (row == 0 and column == 0) or (row == ROW_COUNT-1 and column == COLUMN_COUNT-1) or (row == 0 and column == COLUMN_COUNT-1) or (row == ROW_COUNT-1 and column == 0):
                    self.grid_sprite_list.append(empty_sprite)
                    self.grid_sprites[row].append(empty_sprite)
                elif row == 0 or row == ROW_COUNT - 1 or column == 0 or column == COLUMN_COUNT - 1:
                    self.grid_sprite_list.append(like_empty_sprite)
                    self.grid_sprites[row].append(like_empty_sprite)
                else:
                    self.grid_sprite_list.append(sprite)
                    self.grid_sprites[row].append(sprite)
                self.grid_numbers[row].append(0)

    def setup(self):
        pass

    def on_show_view(self):
        """ Called when switching to this view"""
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)


        def on_click_exit_to_mm(event):
            game_view = Main_Menu()
            self.window.show_view(game_view)
            managerclear(self)
            uimanagerclear(self)

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

        exit_game_button = arcade.gui.UIFlatButton(text=text_of_back_to_mm, width=200)
        self.v_box_of_back_button.add(exit_game_button.with_space_around(bottom=20))
        exit_game_button.on_click = on_click_exit_to_mm

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
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.grid_sprite_list.draw()
        
        self.manager_of_back_button.draw()
        self.manager_of_tip_button.draw()


        

    def on_mouse_press(self, x, y, button, modifiers):
        # Вызываетя при нажатии на мышь

        # Перевод координат нажатия мышью в элемент на сетке
        # В условии необходимо ставить коэффициент равный генерации сетки+0,5, а в вычислении ячейки ставить коэффициент равный генерации сетки+1,5
        if x>= ((WIDTH + MARGIN) + SCREEN_WIDTH/2 - (WIDTH + MARGIN)*3.5 + 4) and y >= ((HEIGHT + MARGIN) + SCREEN_HEIGHT/2 - (HEIGHT + MARGIN)*4.5 + 4) and x<= ((WIDTH + MARGIN) + SCREEN_WIDTH/2 + (WIDTH + MARGIN)*1.5 + 2) and y <= ((HEIGHT + MARGIN) + SCREEN_HEIGHT/2 + (HEIGHT + MARGIN)*0.5 + 2):
            column = int((x-((WIDTH + MARGIN) + SCREEN_WIDTH/2 - (WIDTH + MARGIN)*4.5 + 4)) // (WIDTH + MARGIN))
            row = int((y-((HEIGHT + MARGIN) + SCREEN_HEIGHT/2 - (HEIGHT + MARGIN)*5.5 + 4)) // (HEIGHT + MARGIN))

            print(f"Click coordinates: ({x}, {y}). Grid coordinates: ({row}, {column})")

        # Make sure we are on-grid. It is possible to click in the upper right
        # corner in the margin and go to a grid location that doesn't exist
            if row >= ROW_COUNT or column >= COLUMN_COUNT:
                # Simply return from this method since nothing needs updating
                return
            
            for i in range(0, 5):
                if self.grid_numbers[row][column] == i:
                    self.grid_sprites[row][column].texture = arcade.load_texture(f"Product/{i+1}_{grid_mode}.png")
                    self.grid_numbers[row][column] = i+1
                    break
                elif self.grid_numbers[row][column] == 5:
                    self.grid_sprites[row][column].texture = arcade.load_texture(f"Product/0_{grid_mode}.png")
                    self.grid_numbers[row][column] = 0
                    break
            print(self.grid_numbers)

            # Проверка на правильность
            self.grid_numbers_less = self.grid_numbers

            self.grid_numbers_less = [row[1:6] for row in self.grid_numbers[1:6]]

            if self.grid_numbers_less == self.grid_generated:
                global amount_of_coins
                amount_of_coins = 100
                coin = int(read_data('Product/meta.txt', 'coins =')) + 100
                write_data('Product/meta.txt', 'coins =', coin)
                game_view = Win_window()
                self.window.show_view(game_view)
                managerclear(self)
                uimanagerclear(self)



class Shop(arcade.View):
    def __init__(self):
        super().__init__()
        # Create variables here
        self.manager = None
        self.v_box = None

        self.manager_background = None
        self.v_box_background = None

        self.manager_grid = None
        self.v_box_grid = None

        self.background = arcade.load_texture(f"Product/background_{background_mode}.jpg")

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
            managerclear(self)
            uimanagerclear(self)

        def on_click_background_default(event):
            global background_mode
            background_mode = "default"
            write_data('Product/meta.txt', 'background_mode =', "default")
            game_view = Shop()
            game_view.setup()
            self.window.show_view(game_view)
            managerclear(self)
            uimanagerclear(self)

        def on_click_background_car(event):
            global background_mode
            background_mode = "car"
            write_data('Product/meta.txt', 'background_mode =', "car")
            game_view = Shop()
            game_view.setup()
            self.window.show_view(game_view)
            managerclear(self)
            uimanagerclear(self)
        
        def on_click_background_mountain(event):
            global background_mode
            background_mode = "mountain"
            write_data('Product/meta.txt', 'background_mode =', "mountain")
            game_view = Shop()
            game_view.setup()
            self.window.show_view(game_view)
            managerclear(self)
            uimanagerclear(self)
        
        def on_click_background_window(event):
            global background_mode
            background_mode = "window"
            write_data('Product/meta.txt', 'background_mode =', "window")
            game_view = Shop()
            game_view.setup()
            self.window.show_view(game_view)
            managerclear(self)
            uimanagerclear(self)

        def on_click_grid_default(event):
            global grid_mode
            grid_mode = "default"
            write_data('Product/meta.txt', 'grid_mode =', "default")
        
        def on_click_grid_orange(event):
            global grid_mode
            grid_mode = "orange"
            write_data('Product/meta.txt', 'grid_mode =', "orange")
        
        def on_click_grid_pastel(event):
            global grid_mode
            grid_mode = "pastel"
            write_data('Product/meta.txt', 'grid_mode =', "pastel")

        def on_click_grid_pixel(event):
            global grid_mode
            grid_mode = "pixel"
            write_data('Product/meta.txt', 'grid_mode =', "pixel")

        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        self.manager_background = arcade.gui.UIManager()
        self.manager_background.enable()

        self.manager_grid = arcade.gui.UIManager()
        self.manager_grid.enable()

        # Create a vertical BoxGroup to align buttons
        self.v_box = arcade.gui.UIBoxLayout()
        self.v_box_background = arcade.gui.UIBoxLayout()
        self.v_box_grid = arcade.gui.UIBoxLayout()

        exit_settings_button = arcade.gui.UIFlatButton(text=text_of_back_button, width=200)
        self.v_box.add(exit_settings_button.with_space_around(bottom=20))
        exit_settings_button.on_click = on_click_exit_settings

        background_default_button = arcade.gui.UIFlatButton(text=text_of_shop_background_default, width=250)
        self.v_box_background.add(background_default_button.with_space_around(bottom=20))
        background_default_button.on_click = on_click_background_default

        background_car_button = arcade.gui.UIFlatButton(text=text_of_shop_background_car, width=250)
        self.v_box_background.add(background_car_button.with_space_around(bottom=20))
        background_car_button.on_click = on_click_background_car

        background_mountain_button = arcade.gui.UIFlatButton(text=text_of_shop_background_mountain, width=250)
        self.v_box_background.add(background_mountain_button.with_space_around(bottom=20))
        background_mountain_button.on_click = on_click_background_mountain

        background_window_button = arcade.gui.UIFlatButton(text=text_of_shop_background_window, width=250)
        self.v_box_background.add(background_window_button.with_space_around(bottom=20))
        background_window_button.on_click = on_click_background_window

        grid_default_button = arcade.gui.UIFlatButton(text=text_of_shop_grid_default, width=250)
        self.v_box_grid.add(grid_default_button.with_space_around(bottom=20))
        grid_default_button.on_click = on_click_grid_default

        grid_orange_button = arcade.gui.UIFlatButton(text=text_of_shop_grid_orange, width=250)
        self.v_box_grid.add(grid_orange_button.with_space_around(bottom=20))
        grid_orange_button.on_click = on_click_grid_orange

        grid_pastel_button = arcade.gui.UIFlatButton(text=text_of_shop_grid_pastel, width=250)
        self.v_box_grid.add(grid_pastel_button.with_space_around(bottom=20))
        grid_pastel_button.on_click = on_click_grid_pastel

        grid_pixel_button = arcade.gui.UIFlatButton(text=text_of_shop_grid_pixel, width=250)
        self.v_box_grid.add(grid_pixel_button.with_space_around(bottom=20))
        grid_pixel_button.on_click = on_click_grid_pixel

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                align_x=SCREEN_WIDTH / 2 - 125,
                align_y=SCREEN_HEIGHT / 2 - 50,
                child=self.v_box)
        )

        self.manager_background.add(
            arcade.gui.UIAnchorWidget(
                align_x= -SCREEN_WIDTH/2 + 185,
                align_y= - 50,
                child=self.v_box_background)
        )

        self.manager_grid.add(
            arcade.gui.UIAnchorWidget(
                align_x=SCREEN_WIDTH/2 - 185,
                align_y= - 50,
                child=self.v_box_grid)
        )

    def on_draw(self):
        """ Draw everything for the game. """
        self.clear()
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        arcade.draw_text(f"{text_of_shop_coins}{read_data('Product/meta.txt', 'coins =')}", SCREEN_WIDTH / 2, SCREEN_HEIGHT/2 + 200,
                         arcade.color.PIGGY_PINK, 30, anchor_x="center")
        arcade.draw_rectangle_filled(SCREEN_WIDTH / 8 + 25, (SCREEN_HEIGHT - 120) / 2 + 25, SCREEN_WIDTH / 4, SCREEN_HEIGHT/2,
                                     arcade.color.GRAY_BLUE)
        arcade.draw_text(text_of_shop_background, SCREEN_WIDTH / 8 + 25, (SCREEN_HEIGHT + 250) / 2 - 15,
                         arcade.color.WHITE, 30, anchor_x="center")
        arcade.draw_rectangle_filled((SCREEN_WIDTH - 180), (SCREEN_HEIGHT - 120) / 2 + 25, SCREEN_WIDTH / 4, SCREEN_HEIGHT/2,
                                     arcade.color.GRAY_BLUE)
        arcade.draw_text(text_of_shop_grid, SCREEN_WIDTH - 175, (SCREEN_HEIGHT + 250) / 2 - 15,
                         arcade.color.WHITE, 30, anchor_x="center")
        self.manager.draw()
        self.manager_background.draw()
        self.manager_grid.draw()


class Settings_Menu(arcade.View):
    def __init__(self):
        super().__init__()
        # Create variables here
        self.manager1 = None
        self.manager_of_language = None
        self.v_box = None
        self.v_box_of_language = None

        self.background = arcade.load_texture(f"Product/background_{background_mode}.jpg")

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
            managerclear(self)
            uimanagerclear(self)

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

        def on_click_german_language(event):
            lang = Localization()
            lang.German_lang()
            game_view = Settings_Menu()
            game_view.setup()
            self.window.show_view(game_view)

        def on_click_franch_language(event):
            lang = Localization()
            lang.Franch_lang()
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
        german_language = arcade.gui.UIFlatButton(text="Deutsch", width=300)
        self.v_box_of_language.add(german_language.with_space_around(bottom=20))
        german_language.on_click = on_click_german_language
        franch_language = arcade.gui.UIFlatButton(text="Français", width=300)
        self.v_box_of_language.add(franch_language.with_space_around(bottom=20))
        franch_language.on_click = on_click_franch_language

        self.manager1.add(
            arcade.gui.UIAnchorWidget(
                align_x=SCREEN_WIDTH / 2 - 125,
                align_y=SCREEN_HEIGHT / 2 - 50,
                child=self.v_box)
        )
        self.manager_of_language.add(
            arcade.gui.UIAnchorWidget(
                align_x=-(SCREEN_WIDTH / 2 - (SCREEN_WIDTH / 8 + 25)),
                align_y= -75,
                child=self.v_box_of_language)
        )

    def on_draw(self):
        """ Draw everything for the game. """
        self.clear()
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
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

        self.background = arcade.load_texture(f"Product/background_{background_mode}.jpg")

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
            managerclear(self)
            uimanagerclear(self)

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
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.manager.draw()


class Win_window(arcade.View):
    def __init__(self):
        super().__init__()
        # Create variables here
        self.manager = None
        self.v_box = None

        self.background = arcade.load_texture("Product/win_window.jpg")

        global amount_of_coins

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
            managerclear(self)
            uimanagerclear(self)

        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Create a vertical BoxGroup to align buttons
        self.v_box = arcade.gui.UIBoxLayout()

        exit_settings_button = arcade.gui.UIFlatButton(text=text_of_back_to_mm, width=400)
        self.v_box.add(exit_settings_button.with_space_around(bottom=40))
        exit_settings_button.on_click = on_click_exit_settings

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                align_x= 0,
                align_y= 100,
                child=self.v_box)
        )

    def on_draw(self):
        """ Draw everything for the game. """
        self.clear()
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.manager.draw()
        arcade.draw_text(text_of_win_window, SCREEN_WIDTH / 2, 100,
                         arcade.color.BLACK, 30, anchor_x="center")
        arcade.draw_text(f"{text_of_win_window_coins}{amount_of_coins} {text_of_win_window_coin}", SCREEN_WIDTH / 2, 50,
                         arcade.color.BLACK, 30, anchor_x="center")


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

def uimanagerclear(self):
    self.uimanager.clear()

grid_mode = read_data("Product/meta.txt", "grid_mode = ")
background_mode = read_data("Product/meta.txt", "background_mode = ")
amount_of_coins = 0

if __name__ == "__main__":
    main()
