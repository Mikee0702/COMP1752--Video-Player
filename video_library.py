import csv

# Define a LibraryItem class to represent an item in the video library
class LibraryItem:
    def __init__(self, video_id, name, director, rating, play_count):
        self.video_id = video_id  # ID of the video
        self.name = name  # Name of the video
        self.director = director  # Director of the video
        self.rating = rating  # Rating of the video (on a scale of 1-5)
        self.play_count = play_count  # Number of times the video has been played

# Create a list of sample videos in the library
video_library = [
    LibraryItem("01", "Tom and Jerry", "Fred Quimby", 4, 10),
    LibraryItem("02", "Breakfast at Tiffany's", "Blake Edwards", 5, 5),
    LibraryItem("03", "Casablanca", "Michael Curtiz", 2, 8),
    LibraryItem("04", "The Sound of Music", "Robert Wise", 1, 3),
    LibraryItem("05", "Gone with the Wind", "Victor Fleming", 3, 7),
]

favorite_videos = []  # List of favorite videos
playlists = {}  # Dictionary containing playlists, with the playlist name as the key
history = []  # List of video playback history

# Function to return a list of all videos in the library
def list_all():
    return video_library

# Function to return the name of a video based on its ID
def get_name(video_id):
    for video in video_library:
        if video.video_id == video_id:
            return video.name
    return None

# Function to return the director of a video based on its ID
def get_director(video_id):
    for video in video_library:
        if video.video_id == video_id:
            return video.director
    return None

# Function to return the rating of a video based on its ID
def get_rating(video_id):
    for video in video_library:
        if video.video_id == video_id:
            return video.rating
    return None

# Function to return the play count of a video based on its ID
def get_play_count(video_id):
    for video in video_library:
        if video.video_id == video_id:
            return video.play_count
    return None

# Function to update the rating of a video based on its ID
def set_rating(video_id, rating):
    for video in video_library:
        if video.video_id == video_id:
            video.rating = rating
            return True
    return False

# Function to increment the play count of a video based on its ID
def increment_play_count(video_id):
    for video in video_library:
        if video.video_id == video_id:
            video.play_count += 1
            return True
    return False

# Function to delete a video from the library based on its ID
def delete_video(video_id):
    global video_library
    original_length = len(video_library)
    video_library = [video for video in video_library if video.video_id != video_id]

    # If the video was deleted, update the CSV file and return True
    if len(video_library) < original_length:
        update_csv()  # Update the CSV file after deletion
        return True
    else:
        return False  # Return False if the video was not found for deletion

# Function to add a new video to the library
def add_video(video_id, name, director, rating, play_count):
    new_video = LibraryItem(video_id, name, director, rating, play_count)
    video_library.append(new_video)

# Function to return a list of favorite videos
def list_favorites():
    return favorite_videos

# Function to return a list of videos to watch later
def list_see_later():
    return see_later_videos

# Function to add a video to the favorites list based on its ID
def add_to_favorites(video_id):
    video = get_video_by_id(video_id)
    if video and video not in favorite_videos:
        favorite_videos.append(video)

# Function to remove a video from the favorites list based on its ID
def remove_from_favorites(video_id):
    global favorite_videos
    favorite_videos = [video for video in favorite_videos if video.video_id != video_id]

# Function to add a video to the watch later list based on its ID
def add_to_see_later(video_id):
    video = get_video_by_id(video_id)
    if video and video not in see_later_videos:
        see_later_videos.append(video)

# Function to remove a video from the watch later list based on its ID
def remove_from_see_later(video_id):
    global see_later_videos
    see_later_videos = [video for video in see_later_videos if video.video_id != video_id]

# Function to return a video object based on its ID
def get_video_by_id(video_id):
    for video in video_library:
        if video.video_id == video_id:
            return video
    return None

# Function to add a video to the playback history
def add_to_history(video_id):
    video = get_video_by_id(video_id)
    if video:
        video.play_count += 1
        history.append(video)

# Function to return the list of video playback history
def get_history():
    return history

# Function to clear the video playback history
def clear_history():
    global history
    history = []

# Function to create a new playlist
def create_playlist(playlist_name):
    if playlist_name not in playlists:
        playlists[playlist_name] = []

# Function to add a video to a playlist based on the playlist name and video ID
def add_to_playlist(playlist_name, video_id):
    video = get_video_by_id(video_id)
    if playlist_name in playlists and video and video not in playlists[playlist_name]:
        playlists[playlist_name].append(video)

# Function to return the list of videos in a playlist based on the playlist name
def get_playlist(playlist_name):
    if playlist_name in playlists:
        return playlists[playlist_name]
    return []

# Function to delete a playlist based on its name
def delete_playlist(playlist_name):
    if playlist_name in playlists:
        del playlists[playlist_name]

# Function to update the CSV file with the latest information from the video library
def update_csv():
    fieldnames = ['Video ID', 'Name', 'Director', 'Rating', 'Play Count']
    with open('video_library.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for video in video_library:
            writer.writerow({
                'Video ID': video.video_id,
                'Name': video.name,
                'Director': video.director,
                'Rating': video.rating,
                'Play Count': video.play_count
            })
