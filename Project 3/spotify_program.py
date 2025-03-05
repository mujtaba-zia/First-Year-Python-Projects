# spotify_program.py
# Mujtaba Zia, ENDG 233 F23
# A terminal-based application to process and plot data based on given user input and provided data values.
# You may only import numpy, matplotlib, and math. 
# No other modules may be imported. Only built-in functions that support compound data structures, user entry, or casting may be used.
# Remember to include docstrings for any functions/classes, and comments throughout your code.
#

import numpy as np
import matplotlib.pyplot as plt

# ******************************************************************************************************
# Data is imported from the included csv file. You may not modify the content, order, or location of the csv file.
# Do not modify the code in this section.
# You may not hardcode (manually enter in the code) any other data.
column_names = ['title', 'artist(s)', 'release', 'num_of_streams', 'bpm', 'key', 'mode', 'danceability', 'valence', 'energy', 'acousticness', 'instrumentalness', 'liveness', 'speechiness']
data = np.genfromtxt('spotify_data.csv', delimiter = ',', skip_header = True, dtype = str)
# ******************************************************************************************************


# ******************************************************************************************************
# DEFINE BONUS CLASS HERE (optional)

class Song:
    """
    Represents a song with various attributes and features for analysis.

    Attributes:
        title (str): The title of the song.
        artist (str): The artist of the song.
        release (float): The release year of the song as a float.
        num_of_streams (float): The number of streams for the song as a float.
        bpm (float): Beats per minute of the song as a float.
        key (str): The musical key of the song.
        mode (str): The musical mode of the song.
        danceability (float): The danceability score of the song as a float.
        valence (float): The valence score of the song as a float.
        energy (float): The energy score of the song as a float.
        acousticness (float): The acousticness score of the song as a float.
        instrumentalness (float): The instrumentalness score of the song as a float.
        liveness (float): The liveness score of the song as a float.
        speechiness (float): The speechiness score of the song as a float.
        percentages (list): A list containing selected audio features for easy access.
    """
    def __init__(self, bonus_value):
        # Initialize a Song object with attributes based on the bonus_value list.
        self.title = bonus_value[0]
        self.artist = bonus_value[1]
        self.release = float(bonus_value[2])
        self.num_of_streams = float(bonus_value[3])
        self.bpm = float(bonus_value[4])
        self.key = bonus_value[5]
        self.mode = bonus_value[6]
        self.danceability = float(bonus_value[7])
        self.valence = float(bonus_value[8])
        self.energy = float(bonus_value[9])
        self.acousticness = float(bonus_value[10])
        self.instrumentalness = float(bonus_value[11])
        self.liveness = float(bonus_value[12])
        self.speechiness = float(bonus_value[13])
        self.percentages = [self.danceability, self.valence, self.energy, self.acousticness, self.instrumentalness, self.liveness, self.speechiness]




# ******************************************************************************************************
# DEFINE FUNCTIONS HERE

def feature_stats(user_input):
    """
    Analyzes a specific song feature in the dataset.

    Parameters:
        user_input (int): The index representing the chosen feature for analysis.

    Returns:
        tuple: A tuple containing the index of the song with the maximum feature value,
               the index of the song with the minimum feature value, and the sum of
               the feature values for all songs.

    """
    song_data = [int(data[i][user_input]) for i in range(len(data))]
    max_feature = song_data.index(max(song_data))
    min_feature = song_data.index(min(song_data))
    sum_needed = sum(song_data)
    return max_feature, min_feature, sum_needed



def age_stats(user_input):
    """
    Analyzes the age-related statistics of songs based on a specified feature.

    Parameters:
        user_input (int): The index representing the chosen feature for age analysis.

    Returns:
        None (prints analysis results to the console)

    """
    song_data = [int(data[i, user_input]) for i in range(len(data))]
    oldest_song = song_data.index(min(song_data))
    age = 2023 - int(data[oldest_song, 2])

    # Print the results
    print(f'Span of years: {age}')  # Print the span of years for the oldest song
    print(f'Artist of oldest song: {data[oldest_song, 1]}')  # Print the artist of the oldest song
    print(f'Key and mode of oldest song: {data[oldest_song, 5]} {data[oldest_song, 6]}')  # Print the key and mode of the oldest song
    pass




# ******************************************************************************************************
# DEFINE MAIN CODE
# Add your code within the main function. A docstring is not required for this function.

# You may find the following hints helpful:
# A list comprehension can be used to convert data values in a column and create a new array
# e.g. converted_data = np.array([row[column_value] for row in data], dtype='float')
# NumPy has many built-in functions/methods, including those for finding the index location of a value (e.g. argmax(), argmin(), etc.)
# Refer to the NumPy and Matplotlib documentation for more


def main():
    print("ENDG 233 Spotify Statistics\n")
    print("Song analysis options: ")
    for menu, option in enumerate(column_names):
         print(menu, option)
    print("Choose -1 to end the program.")

# Main code below

    while True:
        # Prompt the user to enter a song feature for analysis and convert the input to an integer
        user_input = int(input("Please enter a song feature to analyze: "))

        # Check if the user input corresponds to features that do not require analysis
        if user_input in (0, 1, 5, 6):
            pass

        # Check if the user input is -1, indicating the desire to end the program
        elif user_input == -1:
            break

        # Check if the user input corresponds to features that require statistical analysis
        elif user_input in (3, 4, 7, 8, 9, 10, 11, 12, 13):
            # Display statistics for the selected feature
            print(f'Highest value: {data[feature_stats(user_input)[0]][user_input]}')
            print(f'Lowest value: {data[feature_stats(user_input)[1]][user_input]}')
            print(f'Mean value: {(feature_stats(user_input)[2]) // len(data)}')
            print(f'Top song in selected feature: {data[feature_stats(user_input)[0]][0]}')

        # Check if the user input corresponds to the release year feature
        elif user_input == 2:
            # Display statistics for the release year feature
            age_stats(user_input)

        # Check if the user input is outside the valid range
        elif user_input not in range(-1, 14):
            print('You must enter a valid menu option.')


        # Create and print bonus plot (optional)

    # Prompt the user to enter a row number for bonus analysis
    row_num = int(input("Bonus - Enter any row number: "))

    # Create a Song object using the data from the specified row
    selected_song = Song(data[row_num])

    # Plot a bar chart for the selected song's audio feature percentages
    plt.figure(figsize=(8, 6))
    plt.bar(column_names[7:], selected_song.percentages)

    # Set y-axis limit to ensure percentages are within the range [0, 100]
    plt.ylim(0, 100)

    # Set title, x-axis label, and y-axis label for the plot
    plt.title(f'Song Stats for {selected_song.title}')
    plt.xlabel('Feature')
    plt.ylabel('Percentage')

    # Adjust layout for better appearance
    plt.tight_layout()

    # Save the plot as an image file with the name 'Selected song Percentages.png'
    plt.savefig('Selected song Percentages.png')




        # Create and print danceability vs. bpm plot

    # Create a NumPy array for danceability, extracting data from the 7th column of the dataset
    dance = np.array([int(data[i][7]) for i in range(len(data))])

    # Create a NumPy array for BPM (Beats Per Minute), extracting data from the 4th column of the dataset
    bpm = np.array([int(data[i][4]) for i in range(len(data))])

    # Create a scatter plot comparing danceability and BPM
    plt.figure(figsize=(8, 6))
    plt.scatter(bpm, dance, label='Song stats', marker='.')

    # Set labels for the x and y axes
    plt.xlabel('BPM')
    plt.ylabel('Danceability')

    # Add a legend to the plot
    plt.legend()

    # Set the title of the plot
    plt.title('Danceability vs. Beats per minute')

    # Save the plot as an image file with the name 'Dance and Bpm.png'
    plt.savefig('Dance and Bpm.png')

    # Display the plot
    plt.show()



if __name__ == '__main__':
    main()

