from views.game.game import GameView
from views.menus.mainmenu import MainMenu
from views.menus.options import Options
from views.menus.sound import SoundOptionsView
from views.menus.language import LanguageOptionsView
from views.menus.keybinds import KeybindsOptionsView
from views.menus.difficulty import DifficultyOptionsView
from views.menus.leaderboard import LeaderboardView


game_view = GameView()
main_menu = MainMenu()
options_view = Options()
sound_view = SoundOptionsView()
language_view = LanguageOptionsView()
keybinds_view = KeybindsOptionsView()
difficulty_view = DifficultyOptionsView()
leaderboard_view = LeaderboardView()

