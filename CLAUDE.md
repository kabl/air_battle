# Air Battle — CLAUDE.md

## Project Overview

2D arcade aerial combat game built with Python and Pygame. A player-controlled aircraft battles AI enemies across an open arena.

## Tech Stack

- **Language:** Python 3.9
- **Framework:** Pygame 1.9.4
- **Environment:** virtualenv (`.venv/`)
- **IDE:** PyCharm

## Setup

```bash
# Activate virtual environment
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the game
python air_battle_main.py
```

## Architecture

### Inheritance Hierarchy

```
pygame.sprite.Sprite
└── BasePlane         (plane/base_plane.py)  — movement, rotation, sprite rendering
    ├── AirPlane      (plane/air_plane.py)   — player aircraft, manages weapon switching
    ├── EnemyPlane    (plane/enemy_plane.py) — AI enemy with random steering
    ├── Bullet2       (plane/bullet2.py)     — standard projectile
    └── Missile       (plane/missile.py)     — homing projectile with target tracking
```

### Weapon Strategy Pattern

`AirPlane` holds a list of gun objects and delegates firing to the active one:
- `SimpleGun` — fires a single `Bullet2`
- `DoubleGun` — fires two `Bullet2` side-by-side
- `MissileGun` — fires a homing `Missile`

### Key Modules

| File | Responsibility |
|------|---------------|
| `air_battle_main.py` | Entry point, game loop, sprite group management |
| `settings.py` | All game configuration constants |
| `game_functions.py` | Input handling, collision detection, screen rendering |
| `game_stats.py` | Score, shots fired, hit ratio tracking |
| `scoreboard.py` | HUD rendering (score, hit ratio) |
| `point.py` | Geometric/trigonometric utilities (position, direction, distance) |

### Sprite Groups

- `air_planes` — player aircraft
- `enemies` — enemy aircraft
- `base_planes` — union of the above, used for unified collision detection
- Each plane also owns its own `bullets` group

## Controls

| Key | Action |
|-----|--------|
| Arrow Left / Right | Rotate aircraft |
| Space | Fire active weapon |
| 1 / 2 / 3 | Switch weapon (Simple / Double / Missile) |
| E | Force enemies to fire (debug) |
| Q | Quit |

## Configuration (`settings.py`)

- Screen: 1400 × 800
- Player speed: 3 px/frame, rotation: 2 °/frame
- Enemy count (config): 5 — currently hardcoded to 2 in `air_battle_main.py`
- Scoring: 50 points per enemy destroyed

## Known Issues / Work In Progress

- `number_of_enemies` is hardcoded to `2` in `air_battle_main.py` (ignores `settings.start_enemies`)
- Background image rendering is commented out in `update_screen()`
- `update_bullets()` is superseded by `update_bullets2()` but left in place
- Several debug `print()` statements remain throughout the codebase
- Game Over on player hit is a `print()` call only — no game state change
- Enemy collision with player plane does not end the game
- Wave progression (incrementing enemy count) is commented out
