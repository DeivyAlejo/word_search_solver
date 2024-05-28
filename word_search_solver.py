"""
Word Search Solver
The purpose of this code is to find a word in a word search game.
Author: Deivy Munoz
Brief explanation: This code is divided into three steps.
    1. Find all the occurrences of the first letter in the word search board.
    2. Find a match for the second letter next to one of the occurrences of the first letter.
    3. Once the first and second letters are found, compare the rest of the letters of the word with the letters in the word search board
       in the correct direction.

    Note: If there are multiple occurrences of the first letter, the code will compare until there are no more or until it finds the word.
"""

import queue

def find_next_letter(direction, next_letter_location, word_search, word, letter_position, letters_location):
    """
    This function returns the location of the 3rd letter and onwards.
    direction: list of two positions, e.g., [0, 1]
    next_letter_location: the position of the next letter to compare
    word_search: word search board
    word: the word to search in the word search board
    letter_position: letter position in the word to compare with next_letter_location
    letters_location: list of the locations of the found letters that match
    """
    if next_letter_location[0] < 0 or (next_letter_location[0] > len(word_search) or next_letter_location[0] > len(word_search[1])) or next_letter_location[1] < 0 or (next_letter_location[1] > len(word_search) or next_letter_location[1] > len(word_search[1])):
        return False 

    if word_search[next_letter_location[0]][next_letter_location[1]] == word[letter_position-1]:
        letters_location.append(next_letter_location)
        if letter_position >= len(word):
            return letters_location
    else:
        return False

    next_letter_location = [next_letter_location[0]+direction[0],next_letter_location[1]+direction[1]]

    
    
    # print(lettersLocation)
    return find_next_letter(direction, next_letter_location, word_search, word, letter_position+1, letters_location)
        

def get_direction(first_letter_location, second_letter_location2):
    """
    Returns the direction where the word is supposed to be based on the location of the first and second letters.
    first_letter_location: location of the first letter
    second_letter_location: location of the second letter
    """
    direction = [second_letter_location2[0]-first_letter_location[0],second_letter_location2[1]-first_letter_location[1]]
    return direction

def generate_points(coordinate, word_search_size):
    """
    Returns the valid point locations around the first letter matches. 
    If the point is outside the boundaries, it won't be returned.
    coordinate: current coordinate to generate points around
    word_search_size: size of the word search board
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
    Looks for a word in the word search board.
    word_search: the word search board
    word: the word to find in the board
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
    word_search = [ ['J','S','O','L','U','T','I','S'],
                    ['S','U','N','A','R','U','U','A'],
                    ['N','E','P','T','U','N','E','T'],
                    ['S','O','N','I','E','I','S','U'],
                    ['R','C','E','V','T','R','E','R'],
                    ['A','H','T','R','A','E','S','N'],
                    ['M','M','E','R','C','U','R','Y']]

    words = ['SUN', 'SUNBLOCK', 'PLAY', 'WAVES', 'HOT', 'SAND', 'FUN', 'PINEAPPLE', 
    'WATER', 'UMBRELLA', 'SHELL', 'BEACH', 'FUN']

    word = 'EARTH'
    print(lookForWord(word_search, word))



