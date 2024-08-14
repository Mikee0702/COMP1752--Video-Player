import tkinter as tk  # Import the tkinter library to create a GUI
import video_library as lib  # Import the video_library module to access video data
from font_manager import FontManager  # Import FontManager from the font_manager module to manage fonts

# Define the CheckVideos class to create the video checking interface
class CheckVideos:
    def __init__(self, window):
        # Initialize the FontManager object to manage fonts for the interface
        self.fm = FontManager(window)
        # Call the function to configure the interface
        self.configure(window)

    def configure(self, window):
        # Define the size and title of the main window
        window.geometry("750x350")
        window.title("Check Videos")

        # Create the "List All Videos" button to list all videos
        list_videos_btn = tk.Button(window, text="List All Videos", command=self.list_videos_clicked)
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10)  # Place the button in the grid
        self.fm.apply_font(list_videos_btn, "default")  # Apply font to the button

        # Create the "Enter Video Number" label to guide the user to enter a video number
        enter_lbl = tk.Label(window, text="Enter Video Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)  # Place the label in the grid
        self.fm.apply_font(enter_lbl, "default")  # Apply font to the label

        # Create an entry box for the video number
        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)  # Place the entry box in the grid
        self.fm.apply_font(self.input_txt, "text")  # Apply font to the entry box

        # Create the "Check Video" button to check the video information based on the entered video number
        check_video_btn = tk.Button(window, text="Check Video", command=self.check_video_clicked)
        check_video_btn.grid(row=0, column=3, padx=10, pady=10)  # Place the button in the grid
        self.fm.apply_font(check_video_btn, "default")  # Apply font to the button

        # Create a Listbox to display the list of videos with Courier font
        self.listbox = tk.Listbox(window, width=48, height=12, font=('Courier', 12))
        self.listbox.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)  # Place the Listbox in the grid

        # Create a text area to display detailed video information with Courier font
        self.video_txt = tk.Text(window, width=24, height=4, wrap="none", font=('Courier', 12))
        self.video_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)  # Place the text area in the grid

        # Create a label to display the application's status
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)  # Place the label in the grid
        self.fm.apply_font(self.status_lbl, "default")  # Apply font to the label

        # Call the function to list all videos when initializing the interface
        self.list_videos_clicked()

    # Event handler for when the user clicks the "Check Video" button
    def check_video_clicked(self):
        # Get the video ID from the Listbox if an item is selected
        selected_idx = self.listbox.curselection()
        if selected_idx:
            selected_video = self.listbox.get(selected_idx)
            key = selected_video.split(":")[0].strip()  # Get the ID from the string in the Listbox
        else:
            key = self.input_txt.get()  # If no item is selected, get the ID from the entry box

        name = lib.get_name(key)  # Get the video name from the video library
        if name is not None:
            # If the video is found, retrieve the detailed information
            director = lib.get_director(key)  # Get the director's name
            rating = '*' * lib.get_rating(key)  # Convert the rating from a number to a string of *
            play_count = lib.get_play_count(key)  # Get the play count
            video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"  # String of video information
            self.set_text(self.video_txt, video_details)  # Display the video information in the text area
        else:
            # If the video is not found, display an error message
            self.set_text(self.video_txt, f"Video {key} not found")
        self.status_lbl.configure(text="Check Video button was clicked!")  # Update the status

    # Event handler for when the user clicks the "List All Videos" button
    def list_videos_clicked(self):
        # Get the list of all videos and display them in the Listbox
        video_list = lib.list_all()  # Get the video list from the library
        self.listbox.delete(0, tk.END)  # Clear all items in the Listbox
        for video in video_list:
            self.listbox.insert(tk.END, f"{video.video_id}: {video.name}")  # Add each video to the Listbox
        self.status_lbl.configure(text="List Videos button was clicked!")  # Update the status

    # Function to set the text in the text area
    def set_text(self, text_area, content):
        text_area.delete("1.0", tk.END)  # Clear all text in the text area
        text_area.insert(1.0, content)  # Insert new text into the text area

# Run this code if this is the main file
if __name__ == "__main__":
    window = tk.Tk()  # Create a TK object
    CheckVideos(window)  # Initialize the CheckVideos interface
    window.mainloop()  # Run the main loop of the window, handling button clicks, etc.
