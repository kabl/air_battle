# Air Battle — Project Requirements & Stories

## Game Concept

Air Battle is a single-player, top-down 2D aerial combat game. The player pilots a fighter aircraft in an open arena, engaging waves of AI enemy ships. The goal is to destroy as many enemies as possible while surviving, maximizing score and hit accuracy.

---

## Core Game Rules

- The player aircraft moves continuously forward and can rotate left/right.
- Enemies spawn in waves. When all enemies in a wave are destroyed, the next wave begins.
- Any projectile from one faction that collides with a plane from the opposing faction destroys both.
- The game tracks score (enemies destroyed × 50 points) and hit ratio (hits / shots fired).
- The game ends when the player's aircraft is destroyed.

---

## Player Aircraft

- Spawns at the bottom-center of the screen with a random position and heading.
- Always moves forward (cannot stop or reverse).
- Can rotate left or right using the arrow keys.
- Has three selectable weapons, switched via keys 1, 2, 3.
- Bullets that leave the screen boundary are removed.

---

## Enemy Aircraft

- Each enemy spawns at a random position with a random heading and speed (1–3 px/frame).
- AI steers randomly: every 10 frames, a random turn angle is applied.
- Enemies are armed with a missile gun.
- When all enemies are destroyed, a new wave of the same count respawns.
- Future: wave size should increase progressively.

---

## Weapons

| Weapon | Key | Projectile | Behavior |
|--------|-----|------------|----------|
| Simple Gun | 1 | Single bullet | Travels straight at fixed speed |
| Double Gun | 2 | Two bullets | Fired side-by-side |
| Missile | 3 | Homing missile | Tracks nearest target within 300 px radius |

### Missile Homing Logic

1. Each frame, the missile scans a 300 px radius ahead of itself.
2. All targets within that radius are collected and sorted by distance.
3. The missile steers toward the closest target by comparing which small turn (±5°) brings it closer.
4. Turn magnitude is proportional to the distance difference between the two candidate paths.

---

## Scoring & Stats

- **Score:** `enemies_destroyed × 50 points`
- **Hit Ratio:** `enemies_hit / bullets_fired` (rounded to 3 decimal places)
- **High Score:** tracked in `GameStats` (not yet persisted across sessions)
- Both score and hit ratio are displayed on-screen via the `Scoreboard` HUD.

---

## User Stories

### MVP (Core Gameplay)

**US-01 — Player movement**
As a player, I can rotate my aircraft left and right with the arrow keys so that I can aim and navigate the arena.

**US-02 — Fire weapons**
As a player, I can press Space to fire my active weapon so that I can attack enemies.

**US-03 — Switch weapons**
As a player, I can press 1, 2, or 3 to switch between Simple Gun, Double Gun, and Missile so that I can choose the right tool for each situation.

**US-04 — Homing missiles**
As a player, I can fire a homing missile that automatically steers toward the nearest enemy within range, rewarding strategic positioning over pure aim.

**US-05 — Enemy AI**
As a player, I face enemies that move and steer randomly, making them unpredictable and harder to hit.

**US-06 — Enemy destruction**
As a player, when my bullet or missile hits an enemy, both the projectile and the enemy are destroyed, and my score increases.

**US-07 — Score & hit ratio display**
As a player, I can see my current score and hit ratio on screen at all times so I can track my performance.

**US-08 — Wave respawn**
As a player, when I destroy all enemies a new wave spawns automatically so the game continues without interruption.

---

### Game Feel & Completeness

**US-09 — Game Over state**
As a player, when an enemy bullet or missile hits my aircraft, the game ends and a Game Over screen is displayed, so there is a meaningful consequence to being hit.
> Currently: collision is detected but only prints to console; no game state change occurs.

**US-10 — Background rendering**
As a player, I see a background image instead of a plain gray fill, improving visual immersion.
> Currently: background blit is commented out in `update_screen()`.

**US-11 — Quit via key**
As a player, I can press Q at any time to quit the game immediately.

---

### Progression

**US-12 — Escalating waves**
As a player, each new wave spawns more enemies than the last (e.g., +2 per wave), so difficulty increases over time and I am continually challenged.
> Currently: wave size is fixed; the increment logic is commented out in `air_battle_main.py`.

**US-13 — High score persistence**
As a player, my high score is saved between sessions so I can compete against my previous best.
> Currently: high score is tracked in memory only and resets on restart.

**US-14 — Enemy firing behavior**
As a player, enemies autonomously fire their missiles at me during gameplay, increasing the challenge.
> Currently: enemy firing is only triggered by pressing E (debug key).

---

### Polish

**US-15 — Remove debug output**
As a developer, all debug `print()` statements are removed or replaced with proper logging so the console is not cluttered during normal play.

**US-16 — Consistent settings usage**
As a developer, `air_battle_main.py` reads `start_enemies` from `Settings` instead of hardcoding `2`, so configuration is managed in one place.

**US-17 — Window title**
As a player, the window title reads "Air Battle" instead of the placeholder "GAME".

---

## Open Design Questions

1. **Lives system:** Should the player have multiple lives before Game Over, or is one hit fatal?
2. **Enemy difficulty scaling:** Should enemies get faster, smarter, or more numerous each wave?
3. **Power-ups:** Should destroying enemies occasionally drop pickups (e.g., weapon upgrades, shields)?
4. **Sound:** Should weapon fire, explosions, and background music be added?
5. **Enemy firing rate:** How frequently should enemies fire, and should it scale with wave number?
