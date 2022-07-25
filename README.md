# Checkmate

Checkmate is a chess scorekeeper that records real life games of chess in the Portable Game Notation (PGN) format, and uploads them directly to Lichess for user analysis. It is written in Python, and heavily utilizes the OpenCV, NumPY, PYAutoGUI and Pillow libraries, along with the Lichess API. 

Chess has persisted as a game for hundreds of years, and has evolved accordingly. Modern chess has gained immense popularity and is enjoyed by a wide audience of people, bringing with it innovation to the game. Of these innovations, chess servers such as Chess.com and Lichess have revolutionized the game, as they bring the ability to play chess without a physical board. With this capability, chess servers can also act as scorekeepers for said games, and provide move-by-move analysis. 

While virtual chess has become increasingly prevalent, games on physical boards remain the most popular way to play chess. However, those who play physical games lose the benefit of error-less scorekeeping and move analysis. Checkmate seeks to provide this benefit to physical games of chess. 

# Scorekeeping

# Computer analysis through Lichess

Lichess is one of the most popular internet chess servers in use. It contains many features such as puzzles, variants like Chess960, and tournaments.

Lichess also preforms computer analysis using the Stockfish chess engine, and allows users to import their own games using the PGN format. Checkmate uses these features to allow users to receive computer analysis of their real life chess games. 

Once all moves of a game have been compiled into a .pgn file, it can be uploaded to Lichess for user analysis. Checkmate utilizes the Lichess API to do so. It makes a post request to the server sending the moves to lichess.org/paste. Once compiled into Lichess, Checkmate returns a Lichess link to the user of their recorded game, allowing them to analyze it. Computer analysis through the Stockfish 11 engine can be manually enabled in the provided link as well.	 

# Set up and use


