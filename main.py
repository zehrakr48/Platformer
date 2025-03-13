import pgzrun

# TODO: Ekran ayarları
WIDTH = 1280
HEIGHT = 720
FPS = 60

game_state = "menu"


def draw():
    screen.clear()
    if game_state == "menu":
        draw_menu()
    elif game_state == "playing":
        draw_game()


def update():
    if game_state == "playing":
        update_game()


def draw_menu():
    screen.draw.text(
        "Platformer Game", center=(WIDTH // 2, HEIGHT // 4), fontsize=50, color="white"
    )
    screen.draw.text(
        "Başlamak için ENTER basın...",
        center=(WIDTH // 2, HEIGHT // 2),
        fontsize=30,
        color="yellow",
    )


def draw_game():
    screen.draw.text(
        "Oyun Çalışıyor...",
        center=(WIDTH // 2, HEIGHT // 2),
        fontsize=30,
        color="white",
    )


def update_game():
    pass  # TODO: Oyunun ana mekanikleri


def on_key_down(key):
    global game_state
    if game_state == "menu" and key == keys.RETURN:
        game_state = "playing"


pgzrun.go()
