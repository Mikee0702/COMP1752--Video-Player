import tkinter as tk
from tkinter import messagebox
import cv2
import PIL.Image, PIL.ImageTk
import threading
import video_library as lib  # Import the video_library module to handle video information

class CreateVideoListWindow:
    def __init__(self, master):
        # Create a new window inside the master (main window)
        self.new_window = tk.Toplevel(master)
        self.new_window.title("Create Playlist")  # Set the title for the new window
        self.new_window.geometry("1200x500")  # Set the size for the window

        # Create the "Enter Video Number" label and entry field
        self.video_number_label = tk.Label(self.new_window, text="Enter Video Number")
        self.video_number_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.video_number_entry = tk.Entry(self.new_window, width=5)  # Entry field for video ID
        self.video_number_entry.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        # Create the "Add Video" button to add a video to the playlist
        self.add_button = tk.Button(self.new_window, text="Add Video", command=self.add_video)
        self.add_button.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        # Create the "Video List" label and Text widget to display the list of videos
        self.video_list_label = tk.Label(self.new_window, text="Video List")
        self.video_list_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        # Use a Text widget with "Courier" font to display video information
        self.video_textbox = tk.Text(self.new_window, width=50, height=10, font=("Courier", 12))
        self.video_textbox.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="w")

        # Create the "Play Videos" button to play the videos in the playlist
        self.play_button = tk.Button(self.new_window, text="Play Videos", command=self.play_videos)
        self.play_button.grid(row=4, column=0, padx=10, pady=5, sticky="w")

        # Create the "Clear List" button to clear the playlist
        self.clear_button = tk.Button(self.new_window, text="Clear List", command=self.clear_list)
        self.clear_button.grid(row=4, column=1, padx=10, pady=5, sticky="w")

        # Create a label to display action messages
        self.action_label = tk.Label(self.new_window, text="")
        self.action_label.grid(row=5, column=0, columnspan=2, padx=10, pady=5, sticky="w")

        # Create a Label to display the video when playing
        self.video_frame = tk.Label(self.new_window)
        self.video_frame.grid(row=0, column=2, rowspan=6, padx=10, pady=5, columnspan=3)

        # Use threading.Event to stop video playback when needed
        self.stop_event = threading.Event()
        self.cap = None  # OpenCV VideoCapture object, used to play video

    def add_video(self):
        # Get the video ID from the entry field and check it in the video library
        video_id = self.video_number_entry.get()
        name = lib.get_name(video_id)
        if name:
            # If the video exists, add the ID and video name to the Text widget
            video_info = f"{video_id} - {name}\n"
            self.video_textbox.insert(tk.END, video_info)
            self.action_label.config(text=f"Video {video_id} added to list.")
        else:
            # If the video is not found, display an error message
            self.action_label.config(text="Invalid video number!")

    def clear_list(self):
        # Clear all content in the Text widget and update the action message
        self.video_textbox.delete(1.0, tk.END)
        self.action_label.config(text="Video list cleared.")

    def play_videos(self):
        # Stop video playback if already playing
        if self.cap:
            self.stop_event.set()
            self.cap.release()
            self.cap = None
            self.video_frame.config(image='')

        # Get the video information from the Text widget and play the first video
        video_info = self.video_textbox.get(1.0, tk.END).strip().split('\n')
        if video_info:
            first_video = video_info[0]
            video_id = first_video.split('-')[0].strip()
            self.video_textbox.delete(1.0, 2.0)  # Delete the first line (ID and video name)
            self.video_number_entry.delete(0, tk.END)
            self.video_number_entry.insert(0, video_id)
            video_path = f"videos/{video_id}.mp4"
            self.cap = cv2.VideoCapture(video_path)

            if not self.cap.isOpened():
                # If the video cannot be opened, display an error message
                self.action_label.config(text=f"Cannot open video {video_id}")
                messagebox.showerror("Error", f"Cannot open video {video_id}")
                return

            # Get the video details and display them in the Text widget
            name = lib.get_name(video_id)
            director = lib.get_director(video_id)
            rating = '*' * lib.get_rating(video_id)
            play_count = lib.get_play_count(video_id)

            video_details = f"Name: {name}\nDirector: {director}\nRating: {rating}\nPlay Count: {play_count}\n\n"
            self.video_textbox.insert(tk.END, video_details)

            # Increment the play count and update the CSV
            lib.increment_play_count(video_id)
            lib.update_csv()

            self.stop_event.clear()
            self.update_frame()
        else:
            # If there are no videos in the list, display a message
            self.action_label.config(text="No videos in the list to play.")

    def update_frame(self):
        # Update the frame of the video being played
        if self.cap and self.cap.isOpened() and not self.stop_event.is_set():
            ret, frame = self.cap.read()
            if ret:
                frame = cv2.resize(frame, (650, 400))  # Resize the video frame to fit
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = PIL.Image.fromarray(frame)
                imgtk = PIL.ImageTk.PhotoImage(image=img)
                self.video_frame.imgtk = imgtk
                self.video_frame.config(image=imgtk)
            self.new_window.after(10, self.update_frame)
        else:
            # End video playback and continue with the next video if available
            if self.cap:
                self.cap.release()
                self.cap = None
            if self.video_textbox.get(1.0, tk.END).strip():
                self.play_videos()
            else:
                self.action_label.config(text="Played all videos in the list.")

if __name__ == '__main__':
    root = tk.Tk()
    app = CreateVideoListWindow(root)
    root.mainloop()
