# 🧟 Pixel Zombies: Apex Survivor

**Pixel Zombies: Apex Survivor** is an intense, retro-arcade "lane defender" game built entirely in HTML5 and JavaScript using the Phaser 3 game engine. 

Hold the line against an endless, speeding horde of the undead. Lock your sights, hold your ground on the left flank, and survive as long as you can to set the ultimate high score.

---

## ✨ Features

* **Classic Arcade Lane-Defense:** Pure, streamlined gameplay. Move vertically to align your shots as zombies swarm from the right at varying speeds.
* **Juicy Game Feel:** Experience heavy camera shake, red damage tints, and 1.5-second Invulnerability Frames (I-Frames) whenever you take a hit.
* **Smooth Physics:** Custom-tuned movement and collision boxes ensure rock-solid, zero-jitter player controls.
* **High Score Tracking:** Your best survival run is automatically saved to your browser's Local Storage.
* **Seamless Audio:** Features an original Darkwave/Chiptune soundtrack that loops seamlessly from the Main Menu through the Game Over screen.
* **Polished UI:** Custom "Press Start 2P" retro font, dedicated health bar, and floating main menu animations.

---

## 🎮 How to Play

**Controls:**
* **[UP] Arrow:** Move Up
* **[DOWN] Arrow:** Move Down
* **[SPACE] Bar:** Fire Weapon
* **[1] (Game Over):** Quick Restart
* **[2] (Game Over):** Return to Main Menu

**Objective:**
Every zombie killed awards **10 Points**. You can sustain up to 20 hits (5% damage each) before you are overrun. Survive as long as possible and beat your High Score!

---

## 📸 Screenshots

* `![Main Menu](Pixel-Zombie-Game/main_menu.png)`
* `![Gameplay](Pixel-Zombie-Game/game_play.png)`
* `![Game Over](Pixel-Zombie-Game/game_over.png)`

---

## 🚀 How to Run Locally

Because the game loads local images and audio assets via `/static/` paths, it needs to be run on a local web server rather than simply double-clicking the HTML file (to avoid CORS policy errors).

If you are running this within your standard Python backend environment (like FastAPI or Flask), simply serve the HTML template and ensure your assets are in the `static` folder. 

Alternatively, you can quickly test it using Python's built-in HTTP server:

1. Open your terminal/command prompt.
2. Navigate to your project's root folder.
3. Start the server:
   ```bash
   python -m http.server 8000
