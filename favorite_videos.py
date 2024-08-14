import tkinter as tk
import video_library as lib

class FavoriteVideosWindow:
    def __init__(self, master):
        # Create a new window
        self.new_window = tk.Toplevel(master)
        self.new_window.title("Favorite Videos")

        # Set the window size
        self.new_window.geometry("1000x650")

        # Create a guide label
        self.label = tk.Label(self.new_window, text="Favorite Videos List")
        self.label.grid(row=0, column=0, padx=10, pady=5)

        # Create a listbox for favorite videos
        self.favorite_listbox = tk.Listbox(self.new_window, width=50, height=15)
        self.favorite_listbox.grid(row=1, column=0, padx=10, pady=5)

        # Create an entry field for the video ID to add to favorites
        self.add_label = tk.Label(self.new_window, text="Enter Video ID to add to favorites:")
        self.add_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        self.add_entry = tk.Entry(self.new_window, width=10)
        self.add_entry.grid(row=3, column=0, padx=10, pady=5, sticky="w")

        # Create a button to add the video to the favorites list
        self.add_button = tk.Button(self.new_window, text="Add to Favorites", command=self.add_to_favorites)
        self.add_button.grid(row=3, column=1, padx=10, pady=5)

        # Create an entry field for the video ID to remove from favorites
        self.remove_label = tk.Label(self.new_window, text="Enter Video ID to remove from favorites:")
        self.remove_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")

        self.remove_entry = tk.Entry(self.new_window, width=10)
        self.remove_entry.grid(row=5, column=0, padx=10, pady=5, sticky="w")

        # Create a button to remove the video from the favorites list
        self.remove_button = tk.Button(self.new_window, text="Remove from Favorites", command=self.remove_from_favorites)
        self.remove_button.grid(row=5, column=1, padx=10, pady=5)

        # Create a button to refresh the list
        self.refresh_button = tk.Button(self.new_window, text="Refresh List", command=self.refresh_favorites_list)
        self.refresh_button.grid(row=6, column=0, padx=10, pady=5)

        # Display the initial favorites list
        self.refresh_favorites_list()

    # Function to add a video to the favorites list
    def add_to_favorites(self):
        video_id = self.add_entry.get()
        lib.add_to_favorites(video_id)
        self.refresh_favorites_list()

    # Function to remove a video from the favorites list
    def remove_from_favorites(self):
        video_id = self.remove_entry.get()
        lib.remove_from_favorites(video_id)
        self.refresh_favorites_list()

    # Function to refresh the favorites list
    def refresh_favorites_list(self):
        self.favorite_listbox.delete(0, tk.END)
        favorites = lib.list_favorites()
        for video in favorites:
            self.favorite_listbox.insert(tk.END, f"{video.video_id}: {video.name}")
