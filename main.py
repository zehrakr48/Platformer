import pgzrun

# TODO: Ekran ayarları
WIDTH = 1280
HEIGHT = 720
FPS = 60
TILE_SIZE = 50

game_state = "menu"

buttons = {
    "start": Rect((WIDTH // 2 - 75, HEIGHT // 2 - 40), (150, 50)),
    "toggle_sound": Rect((WIDTH // 2 - 75, HEIGHT // 2 + 20), (150, 50)),
    "exit": Rect((WIDTH // 2 - 75, HEIGHT // 2 + 80), (150, 50)),
}

sound_on = True

LEVEL = [
    "........................",
    "........................",
    "........................",
    ".............#####.......",
    "...........#####.........",
    ".........#####...........",
    "#########################",
]


def draw():
    screen.clear()
    if game_state == "menu":
        draw_menu()
    elif game_state == "playing":
        draw_game()
    elif game_state == "paused":
        draw_game()
        screen.draw.text(
            "PAUSED", center=(WIDTH // 2, HEIGHT // 2), fontsize=70, color="red"
        )


def update():
    if game_state == "playing":
        update_game()


def draw_menu():
    screen.draw.text(
        "Platformer Game", center=(WIDTH // 2, HEIGHT // 4), fontsize=50, color="white"
    )

    for key, rect in buttons.items():
        screen.draw.filled_rect(rect, "gray")
        screen.draw.text(
            key.replace("_", " ").title(),
            center=rect.center,
            fontsize=30,
            color="black",
        )


def draw_game():
    screen.draw.text(
        "Game Running...",
        center=(WIDTH // 2, HEIGHT // 2),
        fontsize=30,
        color="white",
    )
    draw_level()


def draw_level():
    for row_index, row in enumerate(LEVEL):
        for col_index, tile in enumerate(row):
            if tile == "#":
                screen.draw.filled_rect(
                    Rect(
                        col_index * TILE_SIZE,
                        row_index * TILE_SIZE,
                        TILE_SIZE,
                        TILE_SIZE,
                    ),
                    "blue",
                )


def update_game():
    pass  # TODO: Oyunun ana mekanikleri


def on_mouse_down(pos):
    global game_state, sound_on
    if game_state == "menu":
        if buttons["start"].collidepoint(pos):
            game_state = "playing"
        elif buttons["toggle_sound"].collidepoint(pos):
            sound_on = not sound_on
        elif buttons["exit"].collidepoint(pos):
            exit()


def on_key_down(key):
    global game_state
    if game_state == "playing" and key == keys.P:
        game_state = "paused"
    elif game_state == "paused" and key == keys.P:
        game_state = "playing"


pgzrun.go()
