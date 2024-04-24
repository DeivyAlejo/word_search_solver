"""
Word Search Solver
The purpose of this code is to find a word in a word search game.
Author: Deivy Munoz
Brief explanaition: This code is divided into three steps.
    1. Find all the coincidents of the first letter in the word search board.
    2. Find a coincidence of the sencond letter next to one of the coincidents for the first letter.
    3. Once the first and the second letter were found, compare the rest of the letters of the words with the letters of the word search board
        in the correct direction.

    Note: If there are mulriple coincidences of the first letter the code will compare until there are no more or until if finds the word. 

"""

import queue

def find_next_letter(direction, next_letter_location, word_search, word, letter_position, letters_location):
    """
    This function returns the location of the 3th letter and foward.
    direction: list of two positions ex [o,1]
    next_letter_location: the position of the next letter to compare
    word_search: word search board
    word: the word to search in the word search board
    letter_position: letter position in the word to compare with next_letter_location
    letters_location: list of the locations of the found letters that match
    """
    if word_search[next_letter_location[0]][next_letter_location[1]] == word[letter_position-1]:
        letters_location.append(next_letter_location)
        if letter_position >= len(word):
            return letters_location
    else:
        return False

    next_letter_location = [next_letter_location[0]+direction[0],next_letter_location[1]+direction[1]]

    if next_letter_location[0] < 0 or (next_letter_location[0] > len(word_search) or next_letter_location[0] > len(word_search[1])) or next_letter_location[1] < 0 or (next_letter_location[1] > len(word_search) or next_letter_location[1] > len(word_search[1])):
        return False 
    
    # print(lettersLocation)
    return find_next_letter(direction, next_letter_location, word_search, word, letter_position+1, letters_location)
        

def get_direction(first_letter_location, second_letter_location2):
    """
    get_direction returns the direction where the word supose to be based on the location of first and second letter.
    
    """
    direction = [second_letter_location2[0]-first_letter_location[0],second_letter_location2[1]-first_letter_location[1]]
    return direction

def generate_points(coordinate, word_search_size):
    """
    generate_poinst returns the valid point locations around the firts letter matches. If the point is outside the boundaries, it wont be returned.
    """
    point_list = []
    point_list.append([coordinate[0]-1,coordinate[1]-1])
    point_list.append([coordinate[0]-1,coordinate[1]])
    point_list.append([coordinate[0]-1,coordinate[1]+1])
    point_list.append([coordinate[0],coordinate[1]+1])
    point_list.append([coordinate[0]+1,coordinate[1]+1])
    point_list.append([coordinate[0]+1,coordinate[1]])
    point_list.append([coordinate[0]+1,coordinate[1]-1])
    point_list.append([coordinate[0],coordinate[1]-1])
    correct_points = queue.Queue()
    for point in point_list:
        if point[0] < 0 or point[0] > word_search_size[0]-1 or point[1] < 0 or point[1] > word_search_size[1]-1:
            pass
        else:
            correct_points.put(point)
    return correct_points

def lookForWord(word_search, word):
    """

    """
    word_search_size = [len(word_search),len(word_search[1])]
    first_letter_q = queue.Queue()
    second_letter_q = queue.Queue()
    first_letter = word[0]
    second_letter = word[1]
    word_location = []

    # Looking for all the matches of first letter in the wordSearch
    for i, row in enumerate(word_search):
        for j, letter in enumerate(row):
            if letter == first_letter:
                first_letter_q.put([i,j])
    
    # Looking for the first match for the second letter
    while not first_letter_q.empty():
        first_letter_location = first_letter_q.get()
        second_letter_q = generate_points(first_letter_location, word_search_size)
        while not second_letter_q.empty():
            second_letter_location = second_letter_q.get()
            letter = word_search[second_letter_location[0]][second_letter_location[1]]
            # looking for the 3th letter and foward
            if letter == second_letter:
                direction = get_direction(first_letter_location,second_letter_location)
                next_letter_location = [second_letter_location[0]+direction[0],second_letter_location[1]+direction[1]]
                letters_location = []
                lette_position = 3
                remain_letters_location = find_next_letter(direction, next_letter_location, word_search, word, lette_position, letters_location)
                if remain_letters_location:
                    word_location.append(first_letter_location)
                    word_location.append(second_letter_location)
                    for location in remain_letters_location:
                        word_location.append(location)
                    return word_location
    return False
    
if __name__ == "__main__":
    word_search = [ ['S','U','N','W','A','N','P','U','A'],
                    ['U','S','B','A','E','I','P','L','H'],
                    ['N','H','T','T','W','C','L','S','O'],
                    ['B','E','N','E','U','E','A','A','T'],
                    ['L','L','W','R','R','D','Y','N','N'],
                    ['O','L','N','B','O','T','S','D','F'],
                    ['C','A','M','B','E','A','C','H','U'],
                    ['K','U','W','A','V','E','S','C','N'],
                    ['P','I','N','E','A','P','P','L','E']]

    words = ['SUN', 'SUNBLOCK', 'PLAY', 'WAVES', 'HOT', 'SAND', 'FUN', 'PINEAPPLE', 
    'WATER', 'UMBRELLA', 'SHELL', 'BEACH', 'FUN']

    word = 'SHELL'
    print(lookForWord(word_search, word))



