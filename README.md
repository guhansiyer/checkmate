# Checkmate

Checkmate is a chess scorekeeper that records physical games of chess and uploads them directly to Lichess for user analysis. It is written in Python, and heavily utilizes the OpenCV, NumPY, PYAutoGUI and Pillow (Python Imaging Library) libraries, along with the Lichess API. 

Chess has persisted as a game for hundreds of years, and has evolved accordingly. Modern chess has gained immense popularity and is enjoyed by a wide audience of people, bringing with it innovation to the game. Of these innovations, chess servers such as [Chess.com](https://chess.com) and [Lichess](https://lichess.org) have revolutionized the game, as they bring the ability to play chess without a physical board. With this capability, chess servers can also act as scorekeepers for said games, and provide move-by-move analysis. 

While virtual chess has become increasingly prevalent, games on physical boards remain the most popular way to play chess. However, those who play physical games lose the benefit of error-less scorekeeping and move analysis. Checkmate seeks to provide this benefit to physical games of chess. 

# Scorekeeping

Chess games are usually recorded in [Standard Algebraic Notation (SAN)](https://www.chess.com/article/view/chess-notation), the FIDE standard for recording moves in a game of chess. SAN identifies each square through a coordinate system, and each piece (except pawns) by a capital letter. An example of a move in SAN is Be5, which is read as "Bishop moves to square E5". There are also symbols for moves such as captures, denoted by an "x", check, denoted by a "+", checkmate, denoted by a "#", and other special cases such as en passant, castling and promotion.

Lichess and most chess software are able to process game data through a  slight variation of standard algebraic notation called [Portable Game Notation (PGN)](https://www.chess.com/terms/chess-pgn), which is just SAN, combined with markup text. It is also based in it's own filetype; .pgn.

# Computer analysis through Lichess

Lichess is one of the most popular internet chess servers in use. It contains many features such as puzzles, variants like Chess960, and tournaments.

Lichess also preforms computer analysis using the Stockfish chess engine, and allows users to import their own games using the PGN format. Checkmate uses these features to allow users to receive computer analysis of their real life chess games. 

Once all moves of a game have been compiled into a .pgn file, it can be uploaded to Lichess for user analysis. Checkmate utilizes the Lichess API to do so. It makes a post request to the Lichess server, sending the move data to https://lichess.org/paste. Once compiled by Lichess, Checkmate returns a Lichess link to the user of their recorded game, allowing them to analyze it. Computer analysis through the Stockfish engine can be manually enabled in the provided link as well.	 

# Set up and use

Checkmate has very minimal requirements for use. All it requires from the user is a version of Python as recent as, or more recent than Python 2.7. Python 2.7 is MacOS's default version, which Checkmate can run on.

The setup for Checkmate is also quite simple, and we have done our best to provide easy to follow instructions for this process.

Firstly, Checkmate requires Python on a user's system. To check if you have Python installed already, open the default terminal (for example, Command Prompt on Windows and Terminal on MacOS) on your system and type "python --version". If it returns some version of Python, then it is installed on your system. Otherwise, go to https://python.org/downloads and follow the download instructions for the most recent version of Python, and for your specific operating system.

Once you have Python installed, open your default terminal, and double check the version using the previously mentioned command. Once you have double checked, enter "pip install pip" to download the package manager for Python.

Now that we have Python fully set up, we can clone the repository for Checkmate. There are two ways to do this: through Git and the terminal, or by downloading the repository in a ZIP file. 

For the first method, open your default terminal and type "cd Desktop" so that the repository can be downloaded to that location. Double check that this is the Desktop folder by typing "ls" on MacOS/Linux or "dir" on Windows, which will show you all the files in the folder. If they match up with your Desktop folder, then you are in the right environment. Copy the link to the repository by clicking the "Code" button, and copy the link for HTTPS. Then return to the terminal, making sure you are still in the Desktop folder, and type the command "git clone https://github.com/guuuuie/checkmate.git". Follow all instructions that may be required. Check if the repository has been successfully cloned afterwards by typing "cd checkmate", then either "ls" or "dir" to check if the files line up with the GitHub repository. 

For the second method, click "Code" on the GitHub repository, then click "Download as ZIP" and pick an easy to reach location to reach location for the ZIP file. Once downloaded, drag the "checkmate" folder out of it and into the same location as the ZIP file.

Now with the repository cloned, we are nearly finished with the setup. Open your default terminal run the command "pip install -r import.txt" to install the necessary libraries for Checkmate.  
