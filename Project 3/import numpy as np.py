import numpy as np
import matplotlib.pyplot as plt

class Song:
    def __init__(self, bonus_value):
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

    # Create and print bonus plot (optional)
    
    row_num = int(input("Bonus - Enter any row number: "))
    selected_song = Song(data[row_num])

    plt.figure(figsize=(12,6))
    plt.bar(column_name[7:], selected_song.percentages)
    plt.ylim(0, 100)
    plt.title(f'Song Stats for {selected_song}')
    plt.xlabel('Feature')
    plt.ylabel('Percentage')
    plt.tight_layout()
    plt.savefig('Selected song Percentages.png')