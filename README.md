# Word Search Solver

This is a Python program designed to solve word search puzzles. The purpose of this code is to find a given word within a word search grid.

## Author
Deivy Munoz

## Video
https://youtu.be/PPkMyLJM1gI

In this video, I show how I deployed the code to AWS. I used Lambda, Amplify, and API Gateway.

## Brief Explanation
The program is divided into three main steps:

1. Find all occurrences of the first letter: Locate all instances of the first letter of the target word in the word search board.
2. Find the second letter: Identify a match for the second letter adjacent to one of the occurrences of the first letter.
3. Compare the remaining letters: Once the first and second letters are found, compare the rest of the letters of the target word with the letters in the word search board in the correct direction.

## Note
If there are multiple occurrences of the first letter, the code will continue to compare until there are no more occurrences left or until it finds the word.

## Functions

`find_next_letter`
```python
def find_next_letter(direction, next_letter_location, word_search, word, letter_position, letters_location):
```

* **Description:** This function returns the location of the 3rd letter and onwards.
*  **Parameters:**
     - `direction`: List of two positions, e.g., `[0, 1]`.
     - `next_letter_location`: The position of the next letter to compare.
     - `word_search`: Word search board.
     - `word`: The word to search in the word search board.
     - `letter_position`: Letter position in the word to compare with `next_letter_location`.
     - `letters_location`: List of the locations of the found letters that match.

`get_direction`
```python
def get_direction(first_letter_location, second_letter_location):
```
* **Description:** Returns the direction where the word is supposed to be based on the location of the first and second letters.
*  **Parameters:**
     - `first_letter_location`: Location of the first letter.
     - `second_letter_location`: Location of the second letter.

`generate_points`
```python
def generate_points(coordinate, word_search_size):
```
* **Description:** Returns the valid point locations around the first letter matches. If the point is outside the boundaries, it won't be returned.
*  **Parameters:**
     - `coordinate`: Current coordinate to generate points around.
     - `word_search_size`: Size of the word search board.
 
`lookForWord`
```python
def lookForWord(word_search, word):
```
* **Description:** Looks for a word in the word search board.
*  **Parameters:**
     - `word_search`: The word search board.
     - `word`: The word to find in the board.
 
# Example of usage

```python
if __name__ == "__main__":
    word_search = [
        ['J', 'S', 'O', 'L', 'U', 'T', 'I', 'S'],
        ['S', 'U', 'N', 'A', 'R', 'U', 'U', 'A'],
        ['N', 'E', 'P', 'T', 'U', 'N', 'E', 'T'],
        ['S', 'O', 'N', 'I', 'E', 'I', 'S', 'U'],
        ['R', 'C', 'E', 'V', 'T', 'R', 'E', 'R'],
        ['A', 'H', 'T', 'R', 'A', 'E', 'S', 'N'],
        ['M', 'M', 'E', 'R', 'C', 'U', 'R', 'Y']
    ]

    words = ['SUN', 'SUNBLOCK', 'PLAY', 'WAVES', 'HOT', 'SAND', 'FUN', 'PINEAPPLE', 
             'WATER', 'UMBRELLA', 'SHELL', 'BEACH', 'FUN']

    word = 'EARTH'
    print(lookForWord(word_search, word))
```
