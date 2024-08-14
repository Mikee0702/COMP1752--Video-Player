import tkinter as tk
import video_library as lib
import tkinter.messagebox as messagebox

# Define the CreateVideoWindow class to create a user interface window for adding a new video
class CreateVideoWindow:
    def __init__(self, master):
        # Initialize the main window of the interface
        self.master = master
        self.master.title("Create Videos")  # Set the title for the window
        self.master.geometry("450x500")  # Set the size of the window

        # Create a title label for the window
        self.title_label = tk.Label(master, text="Enter the details of the new video")
        self.title_label.pack(pady=10)

        # Create an entry field for the video ID
        self.video_number_label = tk.Label(master, text="Video Number:")
        self.video_number_label.pack()
        self.video_number_entry = tk.Entry(master)
        self.video_number_entry.pack(pady=5)

        # Create an entry field for the video name
        self.video_name_label = tk.Label(master, text="Video Name:")
        self.video_name_label.pack()
        self.video_name_entry = tk.Entry(master)
        self.video_name_entry.pack(pady=5)

        # Create an entry field for the video director's name
        self.video_director_label = tk.Label(master, text="Video Director:")
        self.video_director_label.pack()
        self.video_director_entry = tk.Entry(master)
        self.video_director_entry.pack(pady=5)

        # Create an entry field for the video rating
        self.video_rating_label = tk.Label(master, text="Video Rating:")
        self.video_rating_label.pack()
        self.video_rating_entry = tk.Entry(master)
        self.video_rating_entry.pack(pady=5)

        # Create an entry field for the video play count
        self.play_count_label = tk.Label(master, text="Play Count:")
        self.play_count_label.pack()
        self.play_count_entry = tk.Entry(master)
        self.play_count_entry.pack(pady=5)

        # Create a button to add the video to the library
        self.create_button = tk.Button(master, text="Create", command=self.create_video)
        self.create_button.pack(pady=10)

        # Create a button to go back to the previous screen
        self.back_button = tk.Button(master, text="Back", command=master.destroy)
        self.back_button.pack()

    # Function to handle the "Create" button click event
    def create_video(self):
        video_id = self.video_number_entry.get()
        name = self.video_name_entry.get()
        director = self.video_director_entry.get()
        rating = self.video_rating_entry.get()
        play_count = self.play_count_entry.get()

        # Add the video to the video library
        lib.add_video(video_id, name, director, rating, play_count)

        # Update the CSV file after adding the new video
        lib.update_csv()

        # Display a success message when the video is created successfully
        tk.messagebox.showinfo("Success", f"Video {name} has been added successfully!")

# Function to initialize and run the CreateVideoWindow
def open_create_video_window():
    root = tk.Tk()  # Create the main window object of tkinter
    app = CreateVideoWindow(root)  # Initialize an object of the CreateVideoWindow class
    root.mainloop()  # Start the main event loop of the user interface

# Call this function when you want to open the new video creation window
if __name__ == '__main__':
    open_create_video_window()  # Open the window when this file is executed
