# ENDG 233 Fall 2023
# Portfolio Project 2 - awards.py
# Mujtaba Zia
# Terminal program for analyzing movie award data.
# This script must include the provided code; feel free to add extra functions or variables.
# No additional module imports are allowed.
# Use only built-in functions for managing strings, lists, dictionaries, sets, and tuples.
# Make sure to add docstrings for your functions and inline comments throughout.

# --------------------------------------------------------------------------------
# The following data is imported from awards_data.py, which should reside in the same directory.
# Do not alter any code in this section.
# Hardcoding any extra data is not permitted.

from awards_data import SAG, oscars, NBR, ISA, GLAAD, NAACP
award_list_names = ['sag', 'oscars', 'nbr', 'isa', 'glaad', 'naacp']
award_list_options = [SAG, oscars, NBR, ISA, GLAAD, NAACP]
# --------------------------------------------------------------------------------

# --------------------------------------------------------------------------------
# FUNCTION DEFINITIONS

def to_lowercase(items):
    """
    Convert all strings in the provided list to lowercase.
    
    Args:
        items (list): A list containing strings.
    
    Returns:
        list: The list with each string converted to lowercase.
    """
    for index in range(len(items)):
        items[index] = items[index].lower()
    return items


def get_award_count(movie):
    """
    Tally the total number of awards won by the specified movie.
    
    Args:
        movie (str): The movie title in lowercase.
        
    Returns:
        int: The count of awards the movie has won.
    """
    count = 0
    for idx in range(len(award_list_options)):
        current_award_list = award_list_options[idx]
        # Standardize the award list entries to lowercase for accurate matching
        current_award_list = to_lowercase(current_award_list)
        if movie in current_award_list:
            for title in current_award_list:
                if movie == title:
                    count += 1
    return count


def display_award_winners(award_name):
    """
    Print the list of movies that have won the specified award.
    
    Args:
        award_name (str): The name of the award list in lowercase.
    """
    if award_name not in award_list_names:
        print("Awards list not found.")
        return
    for i in range(len(award_list_options)):
        if award_name == award_list_names[i]:
            # Join each movie title with a newline to display them individually.
            print("\n".join(award_list_options[i]))
# --------------------------------------------------------------------------------

print("ENDG 233 Awards Data Program")

# Main execution starts here

user_choice = int(input("\nSelect 1 to search for a movie, 2 to display an awards list, or 0 to exit: "))

# Continue running until the user opts to terminate the program.
while user_choice != 0:
    if user_choice == 1:
        # Option to search for a movie's award count.
        movie_title = input("Enter the movie title you wish to search for: ")
        movie_title = movie_title.lower().strip()  # Normalize the input
        print("--Number of Awards Won--")
        print(get_award_count(movie_title))
    elif user_choice == 2:
        # Option to display winners for a selected awards list.
        award_input = input("\nSelect one of the following awards lists:\nOscars\nSAG\nNBR\nISA\nGLAAD\nNAACP\n\n")
        award_input = award_input.lower().strip()  # Format the input correctly
        print("--Award Winners List--")
        display_award_winners(award_input)
    else:
        print("Invalid selection. Please choose 1, 2, or 0.")
    
    user_choice = int(input("\nSelect 1 to search for a movie, 2 to display an awards list, or 0 to exit: "))

print("Thank you for using the awards data program.")
