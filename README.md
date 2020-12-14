# Reversi Game Project
## Team Member
- Team Leader
    - Name: Shuo-Chen Ho
    - Student ID: B09902053
    - github: [EdgedSquirrels](https://github.com/EdgedSquirrels/)
- Member
    - Name: Chun-Ning-Adrian Sham
    - Student ID: B09902099
    - github: [shamadrian](https://github.com/shamadrian/)
    
## Report 
### Initial Test 
   - Since we did not have much experience in playing reversi, we started off by writing a simple programme that flips the most pieces each move. However, reversi is not a game that depends on how many flips at the start of the game but at the end of the game. As expected, our first test went horribly, with a win rate about 50% and really inconsistent performance. 

### Our Programme 
   We then moved forward, literally, and wrote a programme that computes the next 3 steps and chooses the "best" move. We defined few different criterias in which each of these criterias have a corresponding +- points. Ultimately, the best move is determined by choosing the move with the highest allocated points.
- "Best" move criterias: 
    1. "Danger" moves are moves that occupies the spots next to corners. Since these spots will allow the opponent to claim the corner, these spots are considered      "dangerous" and we would avoid them.
    2. "corner" moves are moves that occupies the corner of the board. These spots are the most valuable as they cannot be flipped once occupied. As a result, they  reward the most points.
    3. "Side" moves are moves that occupies a spot on the side, restricted by the middle four spots only (excluding the corner and the danger spots). Since sides are considered good and bad, differentiated by how you occupy them, they are considered moderately good and reward some points.
    4. "Better" moves are moves that occupies three specific spots around the "danger" spots. These three spots are spots that are two spaces away from the corner horizontally, vertically, and diagonally. Since these spots directly involves pinning down the enemy to occupy danger spots and ultimately allowing us to claim the corner, these moves are "better" than "side" moves and reward more points.
    
   In terms of the points, we used the negamax algorithm to help us determine which moves award the most points. 





