import tkinter as tk  # Import the tkinter library to create the GUI
import video_library as lib  # Import the video_library module and alias it as lib

# Define the UpdateVideosWindow class
class UpdateVideosWindow:
    def __init__(self, master):
        # Create a new child window (Toplevel) from the main window (master)
        self.new_window = tk.Toplevel(master)
        self.new_window.title("Update Videos")  # Set the title for the window

        # Arrange the interface
        self.new_window.geometry("800x420")  # Set the window size

        # "Enter Video Number" label to guide the user to enter the video number
        self.video_number_label = tk.Label(self.new_window, text="Enter Video Number")
        self.video_number_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        # Entry field for the video number
        self.video_number_entry = tk.Entry(self.new_window, width=5)
        self.video_number_entry.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        # "Enter New Rating" label to guide the user to enter a new rating
        self.rating_label = tk.Label(self.new_window, text="Enter New Rating")
        self.rating_label.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        # Entry field for the new rating
        self.rating_entry = tk.Entry(self.new_window, width=5)
        self.rating_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        # "Update Video" button to update the video with the new rating
        self.update_button = tk.Button(self.new_window, text="Update Video", command=self.update_video)
        self.update_button.grid(row=1, column=2, padx=10, pady=5, sticky="w")

        # "Updated Video List" label to display the list of updated videos
        self.updated_list_label = tk.Label(self.new_window, text="Updated Video List")
        self.updated_list_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        # Listbox to display the list of updated videos
        self.updated_listbox = tk.Listbox(self.new_window, width=50, height=10)
        self.updated_listbox.grid(row=3, column=0, columnspan=3, padx=10, pady=5, sticky="w")

        # Label to notify the user about the update status
        self.action_label = tk.Label(self.new_window, text="")
        self.action_label.grid(row=4, column=0, columnspan=3, padx=10, pady=5, sticky="w")

        # Responsive
        self.new_window.grid_rowconfigure(1, weight=1)
        self.new_window.grid_columnconfigure(0, weight=1)

    # Function to handle the event when the user clicks the "Update Video" button
    def update_video(self):
        video_id = self.video_number_entry.get()  # Get the video number from the entry field
        new_rating = self.rating_entry.get()  # Get the new rating from the entry field

        # Validate the video number and new rating
        if video_id.isdigit() and new_rating.isdigit():
            new_rating = int(new_rating)  # Convert the new rating to an integer
            # Check if the rating is out of the range of 1 to 5
            if new_rating < 1 or new_rating > 5:
                self.action_label.config(
                    text="Rating must be between 1 and 5!")  # Display an error if the rating is invalid
                return

            # Get the video name by video number
            name = lib.get_name(video_id)
            if name:
                lib.set_rating(video_id, new_rating)  # Update the video with the new rating
                play_count = lib.get_play_count(video_id)  # Get the play count of the video
                # Display the updated video information
                self.updated_listbox.insert(tk.END,
                                            f"{video_id} {name} - New Rating: {new_rating} - Plays: {play_count}")
                self.action_label.config(
                    text=f"Video {video_id} updated: {name}, Rating: {new_rating}, Plays: {play_count}")
            else:
                self.action_label.config(
                    text="Invalid video number!")  # Display an error message if the video number is invalid
        else:
            self.action_label.config(
                text="Please enter valid video number and rating!")  # Display an error message if the input is invalid

# Run this code if this is the main file
if __name__ == '__main__':
    root = tk.Tk()  # Create the main window
    app = UpdateVideosWindow(root)  # Create an instance of the UpdateVideosWindow class
    root.mainloop()  # Run the main loop of tkinter to display the user interface
