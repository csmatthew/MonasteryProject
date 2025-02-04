# Monastery Growth Game - MVP Plan
◀️ [Back to README.md](../README.md)

## Game Concept:
- **Player Role**: You play as an abbot, managing a small monastery and trying to grow it over time.
- **Goal**: Grow the monastery by interacting with resources and completing tasks. The player will be able to move the abbot around the monastery, perform basic actions, and monitor progress.

## MVP Features:

- [x] **Abbot Movement**  
   The abbot (represented by a simple dot or circle) can move in four directions (up, down, left, right) using keyboard input.  
   - Time Estimate: 1-2 days

- [ ] **Basic Game Loop**  
   The game should run in a loop where the screen refreshes continuously and the game checks for player input (movement) and updates the display.  
   - Time Estimate: 1 day

- [ ] **Monastery Background**  
   Create a simple static background to represent the monastery area (e.g., a grid or basic visual layout).  
   - Time Estimate: 1 day

- [ ] **Basic UI/Score Display**  
   Display basic information like the player's "score," such as a resource count (e.g., food, money, monks).  
   - Time Estimate: 1-2 days

- [ ] **Simple Game State Management**  
   Implement basic game state logic, such as a win condition (e.g., grow the monastery to a certain size or complete a task).  
   - Time Estimate: 1-2 days

- [ ] **Basic Interactions**  
   Allow the player (abbot) to interact with basic objects in the monastery (e.g., collecting food, building a new structure).  
   - Time Estimate: 1-2 days

- [ ] **Saving Game Progress**  
   Allow the player to save and load their progress (e.g., store the state of resources, abbot position).  
   - Time Estimate: 1 day

---

## MVP Scope Breakdown:

- **Visuals**:  
  - [ ] Use simple graphics (e.g., circles or squares for the abbot, and simple shapes for structures). _(In Development)_
  - [ ] Keep the visuals minimal — focus on gameplay and mechanics first. _(In Development)_
  
- **Movement Mechanics**:  
  - [x] Implement basic movement with keyboard controls (e.g., arrow keys or WASD).
  - [ ] Smooth movement will be key, but it doesn’t need to be perfect for the MVP. _(In Development)_
  
- **Game State**:  
  - [ ] Introduce a simple resource management mechanic. For example, you can track resources like food or stone, which increase when the abbot interacts with certain objects (e.g., collecting resources from a farm or quarry). _(Pending)_

- **UI Elements**:  
  - [ ] Display a simple score or resource count on the screen. You could also have a basic “game over” screen once the game ends (e.g., when the monastery reaches a certain size or resource threshold). _(Pending)_
  
- **Game Saving**:  
  - [ ] Create a way to save the player's progress and reload it after quitting the game. You could use simple text files or Python’s `pickle` library for this. _(Pending)_

---

## Steps for a Basic MVP:

1. **Day 1**: Set up the basic game window, initialize Pygame, and create the abbot object.
   - Handle basic keyboard input to move the abbot.

2. **Day 2-3**: Design the background, creating a simple layout for the monastery (e.g., a grid, or just a blank space with objects).
   - Display the abbot on the screen.

3. **Day 4**: Add basic UI elements to show resources (food, monks, etc.).
   - Track the resources and display them in the corner of the screen.

4. **Day 5**: Add a basic interaction mechanic (e.g., collecting food or building structures).
   - Implement basic logic to update the game state when interacting with objects (e.g., the monastery's size grows when certain conditions are met).

5. **Day 6**: Implement game saving and loading.
   - Allow players to save and resume their game progress.

6. **Day 7**: Polish the game loop and test all features.
   - Make sure the movement is smooth, the UI updates correctly, and resources are tracked properly.

---

## Outcome:
By the end of the week, you will have a simple game where:
- [ ] The player can move around the screen.
- [ ] Basic resources (e.g., food, monks) are collected.
- [ ] The player can track their progress and potentially save/load their game.

---

## Next Steps (Post MVP):
Once the MVP is finished, you can work on improving the game by adding more content (e.g., new structures, challenges, NPCs) or improving the visuals and interactivity. You could also start working on adding sound effects, animations, and other advanced game mechanics.

This MVP gives you a solid foundation to build upon as you improve your game development skills!
