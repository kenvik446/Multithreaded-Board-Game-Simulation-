# Multithreaded-Board-Game-Simulation-

This code simulates a simple turn-based game where a robot, two bombs, and two pieces of gold are placed on a 4x4 grid. The robot moves randomly within valid moves and tries to collect the gold, while the bombs move around the board and can end the game if they collide with the robot.

**Overview of how the game works:**

1.	Board Setup: The game board is a 4x4 grid, and different pieces (robot, bombs, and gold) are placed at random positions at the start of the game. Each cell on the board can either be empty or occupied by one of these pieces.

2.	Pieces:
      o	Robot (R): The robot moves randomly within valid positions and attempts to collect the gold.
      o	Bombs (B): The two bombs also move randomly within valid positions and can destroy the robot if they land on the same position.
      o	Gold (G): The robot wins by collecting both gold pieces.

3.	Valid Moves: Each piece has a set of valid moves defined in the validMoves dictionary. This limits where each piece can move based on its current position on the 4x4 grid.

4.	Game Flow:
      o	The game is controlled using threads, with each piece (robot and two bombs) taking turns to move.
      o	If the robot collects both gold pieces, it wins. If a bomb lands on the robot, the bombs win.

5.	Threading and Synchronization:
      o	 The game uses Python's threading module to create separate threads for each player (robot and bombs). These threads take turns moving their pieces on the board.
      o	A mutex (mutual exclusion) lock ensures that only one piece moves at a time, preventing race conditions between threads.

**Key Considerations:**

•	Thread Safety: The mutex lock ensures that multiple threads do not attempt to modify the board at the same time, maintaining consistency.
•	Randomness: Moves are randomized for both the robot and the bombs, creating unpredictable gameplay.
•	Game Ending: The game ends when either the robot collects both gold pieces or one of the bombs lands on the robot.

**Potential Improvements:**
1.	Add more game mechanics: You could include more obstacles, different types of players, or even score tracking.
2.	Enhance the AI: The robot or bombs could use more sophisticated algorithms to chase gold or avoid bombs.

