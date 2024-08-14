import tkinter as tk
import video_library as lib  # Import the video_library module to manage the video list

# Define the DeleteVideosWindow class to create the video deletion interface
class DeleteVideosWindow:
    def __init__(self, master, listbox, status_lbl, update_display_func):
        # Initialize the interface window and necessary parameters
        self.master = master  # Parent window
        self.listbox = listbox  # Listbox containing the video list
        self.status_lbl = status_lbl  # Label to display status after deletion
        self.update_display_func = update_display_func  # Function to update the display after deletion

        # Create the delete video button and attach the delete event
        self.delete_button = tk.Button(master, text="Delete Selected Video", command=self.delete_video)
        self.delete_button.pack(pady=10)  # Place the button on the interface with vertical padding of 10

    # Function to handle the video deletion event
    def delete_video(self):
        # Get the index of the selected item in the Listbox
        selected_index = self.listbox.curselection()
        if not selected_index:  # Check if no item is selected
            self.status_lbl.config(text="No video selected to delete.", fg="red")  # Display error message
            return  # Stop the function if no item is selected

        # Get the content of the selected item in the Listbox
        selected_item = self.listbox.get(selected_index)
        # Assume that the video ID is the first part of the text string, split the string, and take the first element as the ID
        video_id = selected_item.split()[0]

        # Call the function to delete the video from the library; if successful, display a success message; if not, display an error message
        if lib.delete_video(video_id):
            self.status_lbl.config(text=f"Video ID {video_id} deleted.", fg="green")
        else:
            self.status_lbl.config(text=f"Failed to delete Video ID {video_id}.", fg="red")

        # Update the Listbox after deleting the video
        self.update_display_func()

# Function to open the Delete Videos window from another module (such as video_player.py)
def open_delete_videos_window(master, listbox, status_lbl, update_display_func):
    DeleteVideosWindow(master, listbox, status_lbl, update_display_func)  # Create a new DeleteVideosWindow
