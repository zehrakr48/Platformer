import pgzrun

# TODO: Ekran ayarları
WIDTH = 1280
HEIGHT = 720
FPS = 60
TILE_SIZE = 50

game_state = "menu"

buttons = {
    "start": Rect((WIDTH // 2 - 100, HEIGHT // 2 - 60), (200, 60)),
    "toggle_sound": Rect((WIDTH // 2 - 100, HEIGHT // 2 + 20), (200, 60)),
    "exit": Rect((WIDTH // 2 - 100, HEIGHT // 2 + 100), (200, 60)),
}

sound_on = True

gravity = 0.5
player_speed = 5
jump_strength = -12

LEVEL = [
    "........................",
    "........................",
    "........................",
    "........................",
    "........................",
    "........................",
    "........................",
    ".............#####.......",
    "...........#####.........",
    ".........#####...........",
    "#########################",
]


class Player:
    def __init__(self):
        self.image = "player"
        self.x = WIDTH // 4  # Yatay eksen başlangıç konumu
        self.y = HEIGHT - TILE_SIZE * 4  # Dikey eksen başlangıç konumu
        self.vx = 0  # Yatay eksen hız
        self.vy = 0  # Dikey eksen hız
        self.on_ground = False

    def update(self):
        self.vy += gravity  # Yer çekimi mekaniği

        keys_pressed = keyboard
        if keys_pressed.left:
            self.vx = -player_speed
        elif keys_pressed.right:
            self.vx = player_speed
        else:
            self.vx = 0

        if keys_pressed.up and self.on_ground:
            self.vy = jump_strength
            self.on_ground = False

        self.x += self.vx
        self.y += self.vy

        self.check_collisions()

    def check_collisions(self):
        self.on_ground = False
        for row_index, row in enumerate(LEVEL):
            for col_index, tile in enumerate(row):
                if tile == "#":
                    tile_rect = Rect(
                        col_index * TILE_SIZE,
                        row_index * TILE_SIZE,
                        TILE_SIZE,
                        TILE_SIZE,
                    )
                    tile_rect = Rect(
                        col_index * TILE_SIZE,
                        row_index * TILE_SIZE,
                        TILE_SIZE,
                        TILE_SIZE,
                    )
                    player_rect = Rect(self.x, self.y, TILE_SIZE, TILE_SIZE)

                    if player_rect.colliderect(tile_rect):
                        if self.vy > 0:  # Düşerken
                            self.y = tile_rect.top - TILE_SIZE
                            self.vy = 0
                            self.on_ground = True
                        elif self.vy < 0:  # Zıplarken
                            self.y = tile_rect.bottom
                            self.vy = 0

    def draw(self):
        screen.draw.filled_rect(Rect(self.x, self.y, TILE_SIZE, TILE_SIZE), "red")


player = Player()


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
        player.update()


def draw_menu():
    screen.draw.text(
        "Platformer Game - Pause With *P*",
        center=(WIDTH // 2, HEIGHT // 4),
        fontsize=70,
        color="white",
    )

    for key, rect in buttons.items():
        screen.draw.filled_rect(rect, "gray")
        screen.draw.text(
            key.replace("_", " ").title(),
            center=rect.center,
            fontsize=40,
            color="black",
        )


def draw_game():
    screen.draw.text(
        "Game Running...",
        center=(WIDTH // 2, HEIGHT // 2),
        fontsize=40,
        color="white",
    )
    draw_level()
    player.draw()


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
