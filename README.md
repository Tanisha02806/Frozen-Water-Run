# Frozen Water Run

**Frozen Water Run** is a 2D endless-runner game developed using Python and Pygame. Set in a magical winter world, the game features an ice princess riding a white horse across a frozen ocean, avoiding obstacles and collecting magical crystals.

The objective is simple: survive as long as possible, collect crystals, avoid obstacles, and achieve the highest score!

## Features

- **Endless Runner Gameplay:** Run continuously through a magical winter environment.
- **Pixel-Art Graphics:** Custom pixel-art player and obstacle sprites.
- **Jump Mechanics:** Jump over obstacles using realistic gravity and landing physics.
- **Multiple Obstacles:** Encounter small obstacles, spikes, and double obstacles.
- **Crystal Collection:** Collect magical crystals to earn bonus points.
- **Particle Effects:** Enjoy sparkling visual effects when collecting crystals.
- **Dynamic Difficulty:** Obstacle speed increases as your score grows.
- **Scoring System:** Earn points by passing obstacles and collecting crystals.
- **High Score System:** Automatically save and maintain your highest score.
- **Game States:** Main menu, gameplay, pause, and game-over screens.
- **Audio Effects:** Background music, jumping, crystal collection, and game-over sounds.
- **Pause and Resume:** Pause gameplay and continue whenever you want.

## Technologies Used

| Technology   | Purpose                             |
|--------------|-------------------------------------|
| Python       | Core programming language           |
| Pygame       | Game development and graphics       |
| Random       | Random obstacle generation          |
| Pathlib      | High-score file management          |
| Git & GitHub | Version control and project hosting |

## Project Structure

```text
FrozenWaterRun/
│
├── main.py
│
├── game/
│   ├── __init__.py
│   ├── game.py
│   ├── player.py
│   ├── world.py
│   ├── obstacle.py
│   └── collectible.py
│
├── ui/
│   ├── __init__.py
│   ├── menu.py
│   ├── pause.py
│   └── game_over.py
│
├── assets/
│   ├── images/
│   │   ├── player.png
│   │   ├── small_obstacle.png
│   │   ├── spike_obstacle.png
│   │   └── double_obstacle.png
│   │
│   ├── sounds/
│   │   ├── background_music.mp3
│   │   ├── jump.wav
│   │   ├── collect.wav
│   │   └── game_over.wav
│   │
│   └── fonts/
│
├── data/
│   └── highscore.txt
│
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/FrozenWaterRun.git
```

### 2. Navigate to the project directory

```bash
cd FrozenWaterRun
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

**Mac/Linux:**

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install pygame
```

### 6. Run the game

```bash
python main.py
```

## Game Controls

|    Key   | Action                  |
|----------|-------------------------|
|   ENTER  | Start the game / Resume |
|   SPACE  | Jump                    |
| UP ARROW | Jump                    |
|    P     | Pause / Resume          |
|    ESC   | Quit / Return to menu   |
|    R     | Restart after Game Over |
|    Q     | Quit after Game Over    |

## Scoring System

| Action                        | Points |
|-------------------------------|--------|
| Successfully pass an obstacle |   +1   |
| Collect a magical crystal     |   +5   |

The game becomes progressively harder as your score increases.

- Initial obstacle speed: 6
- Speed increment: 0.5 every 5 points
- Maximum obstacle speed: 12

## Game Screens

The game includes four main screens:

1. **Main Menu:** Introduces the game and displays controls.
2. **Gameplay:** Features the player, obstacles, collectibles, and score.
3. **Pause Screen:** Allows players to pause and resume gameplay.
4. **Game Over Screen:** Displays the end of a run and restart options.

## Learning Outcomes

Through this project, I explored and implemented:

- Object-Oriented Programming (OOP) in Python.
- Game loops and event handling.
- Collision detection using Pygame.
- Gravity and jumping physics.
- Randomized obstacle generation.
- Difficulty progression and score management.
- Particle effects and audio integration.
- File handling for persistent high scores.
- Modular project organization.

## Author

**Tanisha Thakur**

Computer Science Engineering – Artificial Intelligence

[GitHub](https://github.com/Tanisha02806)

---

*Built with Python, Pygame, and a little winter magic!*
