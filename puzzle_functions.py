""" Where's That Word? functions. """
# CSC108 A1 MAIN FILE 
# The constant describing the valid directions. These should be used
# in functions get_factor and check_guess.
UP = 'up'
DOWN = 'down'
FORWARD = 'forward'
BACKWARD = 'backward'

# The constants describing the multiplicative factor for finding a
# word in a particular direction.  This should be used in get_factor.
FORWARD_FACTOR = 1
DOWN_FACTOR = 2
BACKWARD_FACTOR = 3
UP_FACTOR = 4

# The constant describing the threshold for scoring. This should be
# used in get_points.
THRESHOLD = 5
BONUS = 12

# The constants describing two players and the result of the
# game. These should be used as return values in get_current_player
# and get_winner.
P1 = 'player one'
P2 = 'player two'
P1_WINS = 'player one wins'
P2_WINS = 'player two wins'
TIE = 'tie game'

# The constant describing which puzzle to play. Replace the 'puzzle1.txt' with
# any other puzzle file (e.g., 'puzzle2.txt') to play a different game.
PUZZLE_FILE = 'puzzle1.txt'


# Helper functions.  Do not modify these, although you are welcome to
# call them!

def get_column(puzzle: str, col_num: int) -> str:
    """Return column col_num of puzzle.

    Precondition: 0 <= col_num < number of columns in puzzle

    >>> get_column('abcd\nefgh\nijkl\n', 1)
    'bfj'
    """

    puzzle_list = puzzle.strip().split('\n')
    column = ''
    for row in puzzle_list:
        column += row[col_num]

    return column


def get_row_length(puzzle: str) -> int:
    """Return the length of a row in puzzle.

    >>> get_row_length('abcd\nefgh\nijkl\n')
    4
    """

    return len(puzzle.split('\n')[0])


def contains(text1: str, text2: str) -> bool:
    """Return whether text2 appears anywhere in text1.

    >>> contains('abc', 'bc')
    True
    >>> contains('abc', 'cb')
    False
    """

    return text2 in text1


def get_current_player(player_one_turn: bool) -> str:
    """Return 'player one' iff player_one_turn is True; otherwise, return
    'player two'.

    >>> get_current_player(True)
    'player one'
    >>> get_current_player(False)
    'player two'
    """

    if player_one_turn:
        return P1 
    else:
        return P2
   
   
def get_winner(player_one_score: int, player_two_score: int) -> str: 
    """ Return 'player one wins' if player_one_score is greater than 
    player_two_score, and 'player two wins' if less than player_two_score. If 
    player_one_score is equal to player_two_score, then return 'tie game'.
    
    >>> get_winner(55, 39)
    'player one wins' 
    >>> get_winner(40, 45) 
    'player two wins' 
    >>> get_winner(35, 35) 
    'tie game' 
    """
    
    if player_one_score > player_two_score: 
        return P1_WINS 
    elif player_one_score < player_two_score:
        return P2_WINS
    else: 
        return TIE   


def reverse(word: str) -> str: 
    """Return a reversed copy of word. 
    
    >>> reverse('hello') 
    'olleh'
    >>> reverse('chicken')
    'nekcihc' 
    """
    
    return word[::-1] 


def get_row(puzzle: str, row_number: int) -> str:
   
    """Return the row of puzzle that corresponds to the row_number, with the 
    first row having row_number 0.
    
    Precondition: 0 <= row_number < (number of rows in string)
    
    >>> get_row('abcd\nefgh\nijkl\n', 1)
    'efgh' 
    >>> get_row('hello\nhouse\nphone\n', 2) 
    'phone' 
    """
    
    c = get_row_length(puzzle) 
    r = row_number 
    return puzzle[(r * c + r): (r + 1) * c + r]  
    # the puzzle is spliced, and the start and end indexes were determined by 
    # creating a general relationship between the row_number and row length     
 
    
def get_factor(direction: str) -> int: 
    """Return the multiplicative score that corresponds to the direction. 
    
    >>> get_factor('up') 
    4 
    >>> get_factor('down')
    2 
    >>> get_factor('forward')
    1 
    >>> get_factor('backward')
    3 
    """
  
    if direction == UP: 
        return UP_FACTOR 
    elif direction == DOWN: 
        return DOWN_FACTOR 
    elif direction == FORWARD:
        return FORWARD_FACTOR 
    else: 
        return BACKWARD_FACTOR
    

def get_points(direction: str, words_left: int) -> int:
    """Return the number of points earned if a word was found in given direction 
    with words_left. 
    
    >>> get_points('backward', 5) 
    15 
    >>> get_points('forward', 1)
    21 
    """
    
    if words_left >= THRESHOLD: 
        return THRESHOLD * get_factor(direction)
    elif 1 < words_left < THRESHOLD: 
        return (2 * THRESHOLD - words_left) * get_factor(direction)
    else: 
        return (2 * THRESHOLD - words_left) * get_factor(direction) + BONUS 


def check_guess(puzzle: str, direction: str, guess: str, row_or_col_num: int, 
                num_words_left: int) -> int:
    """" Return the number of points earned if guess is in puzzle in the given 
    direction and row_or_col_num, with num_words_left. 
    
    >>> check_guess('abcd\nefgh\nijkl\n', 'forward', 'efg', 1, 5) 
    5
    >>> check_guess('abcd\nefgh\nijkl\n', 'backward', 'cba', 0, 2) 
    24
    >>> check_guess('abcd\nefgh\nijkl\n', 'down', 'dhl', 3, 6)
    10 
    >>> check_guess('abcd\nefgh\nijkl\n', 'up', 'ea', 0, 1)
    48 
    """
    
    points = 0 
    if direction == FORWARD: 
        if contains(get_row(puzzle, row_or_col_num), guess): 
            points = get_points(FORWARD, num_words_left) 
    elif direction == BACKWARD:
        backward_row = reverse(get_row(puzzle, row_or_col_num)) 
        if contains(backward_row, guess):
            points = get_points(BACKWARD, num_words_left) 
    elif direction == DOWN: 
        if contains(get_column(puzzle, row_or_col_num), guess):  
            points = get_points(DOWN, num_words_left)    
    else: 
        up_column = reverse(get_column(puzzle, row_or_col_num))
        if contains(up_column, guess):
            points = get_points(UP, num_words_left)    
    return points 
