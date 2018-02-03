# VirtualROB
 python based GUI to simulate the actions of R.O.B.

This program requires python as well as the PyGame library.

The intent of this script is to allow you to play Stack-Up without a real life R.O.B. (The blocks in particular are expensive). Note that the real world R.O.B. is given commands by detecting flashes on the screen, this program does not simulate that. In order to follow along you'll need to manually copy the game commands by using keyboard inputs to this program (or devise some other method to do so yourself).

The GUI presents a visual simulation of the blocks for NES Stack-Up along with R.O.B.'s hands. The controls allow you to move the hands (and ultimately the blocks) similar to how the real R.O.B. would. I would note that move are effectively instant and do not simulate the time take for real life R.O.B. to move. Moves that would likely result in blocks dropped, blocks knocked over, or R.O.B. gettings are shown by a red screen. Note the real life blocks are conical at the bottom to fit together, and as a result moving a block sideways just above another block would knock the lower block over.

The controls are as follows, and are mapped for convenience based on the layout of the in-game 'Direct' mode. I would note that the controls can easily be remapped by editing the event handler at the bottom of the script.

* Q - Move Left
* E - Move Right
* W - Move Up
* S - Move Down
* A - Open Hands
* D - Close Hands
* U - Undo error (clear illegal move red screen)
* R - Reset (Reset blocks and hands to default starting position)

