## 1. Introduction ##

import csv
f = open("top100.csv","r")
music = list(csv.reader(f))

artists = []
for row in music[1:]:
    artists.append(row[1])

## 2. Extract the Artists Using a List Comprehension ##

artists = []
for row in music[1:]:
    artists.append(row[1])
artists_lc = [row[1] for row in music[1:]]

## 3. Getting the Artist Count Using a Function ##

def counter(artists):
    artist_dict = dict()
    for a in artists:
        if a in artist_dict.keys():
            artist_dict[a] += 1
        else:
            artist_dict[a] = 1
    return artist_dict

counts = counter(artists)

## 4. Getting the Artist Count Using Collections ##

from collections import Counter
artist_counts = Counter(artists)

## 5. Looping Through Counts Using Items() ##

artist_counts = []
for key, value in counts.items():
    artist_counts.append([key,value])

## 6. Using a List Comprehension ##

artist_counts = []
for key, value in counts.items():
    artist_counts.append([key,value])
artist_counts_two = [[key,value] for key,value in counts.items()]

## 7. Sorting A List of Lists ##

sorted_counts = artist_counts.sort()
print(artist_counts)

## 8. Specifying a Key When Sorting a List of Lists ##

def by_count(artists):
    return artists[1]

streams = artist_counts.sort(key=by_count, reverse=True)

## 9. Creating An Anonymous Function ##

def by_count(artists):
    return artists[1]

artist_counts.sort(key=by_count, reverse=True)
lambda_counts = artist_counts.sort(key=lambda x: x[1], reverse=True)

## 10. Creating a Pipeline Using Modularization ##

from collections import Counter 

f = open("top100.csv","r")
music = list(csv.reader(f))
artists = [row[1] for row in music[1:]]
artist_dict = Counter(artists)
artist_counts = [[key,value] for key,value in artist_dict.items()]
artist_counts.sort(key=lambda x: x[1], reverse=True)

# Uncomment when ready!
# artists = extract_artist(music)
# artist_counts = get_count(artists)
# top = sort_by_streams(artist_counts)
def extract_artist(filename):
    return [row[1] for row in music[1:]]

def get_count(artists):
    artist_dict = Counter(artists)
    return [[key,value] for key,value in artist_dict.items()]

def sort_by_streams(artist_counts):
    artist_counts.sort(key=lambda x: x[1], reverse=True)
    return artist_counts
    
artists = extract_artist(music)
artist_counts = get_count(artists)
top = sort_by_streams(artist_counts)

## 11. How to deal with errors ##

cleaned_list = []
for row in music_sample[1:]:
    try:
        cleaned_list.append([row[0],row[1],float(row[-1])])
    except:
        "Pass"

## 12. Passing new data into our pipeline ##

f = open("top100.csv","r")
music_all = list(csv.reader(f))
artists = extract_artist(music_all)
artist_counts = get_count(artists)
top = sort_by_streams(artist_counts)