import tkinter as tk
import tkinter.font as tkfont
from tkinter import messagebox
import csv
import os
import check_videos
import create_videos
import update_videos
import favorite_videos
import create_playlist
import video_library as lib


# Define the FontManager class to manage and apply fonts to GUI elements
class FontManager:
    def __init__(self, root):
        family = "Helvetica"  # Set the default font for the interface elements to "Helvetica"

        # Configure different font styles for the interface elements
        default_font = tkfont.nametofont("TkDefaultFont", root=root)
        default_font.configure(size=15, family=family)

        text_font = tkfont.nametofont("TkTextFont", root=root)
        text_font.configure(size=12, family=family)

        fixed_font = tkfont.nametofont("TkFixedFont", root=root)
        fixed_font.configure(size=12, family=family)

        # Store the font styles in a dictionary for easy application later
        self.font_styles = {
            "default": default_font,
            "text": text_font,
            "fixed": fixed_font,
        }

    def apply_font(self, widget, style="default"):
        # This function applies the font style to a specific widget
        if style in self.font_styles:
            widget.config(font=self.font_styles[style])
        else:
            raise ValueError(f"Font style '{style}' is not recognized.")


# Event handling functions for when the user clicks buttons on the interface

def check_videos_clicked():
    # When the "Check Videos" button is clicked
    status_lbl.configure(text="Check Videos button was clicked")
    check_videos.CheckVideos(tk.Toplevel(window))  # Open a new video checking window
    update_csv_display()  # Update the video list on the interface


def create_video_button():
    # When the "Create Videos" button is clicked
    create_videos.CreateVideoWindow(tk.Toplevel(window))  # Open a new video creation window
    update_csv_display()  # Update the video list on the interface


def update_videos_button():
    # When the "Update Videos" button is clicked
    update_videos.UpdateVideosWindow(window)  # Open the video update window
    update_csv_display()  # Update the video list on the interface


def favorite_videos_button():
    # When the "Favorite Videos" button is clicked
    favorite_videos.FavoriteVideosWindow(window)  # Open the favorite videos management window
    update_csv_display()  # Update the video list on the interface


def create_playlist_button():
    # When the "Create Playlist" button is clicked
    create_playlist.CreateVideoListWindow(window)  # Open the playlist creation window
    update_csv_display()  # Update the video list on the interface


def update_csv():
    # This function updates the CSV file that stores the current video list
    fieldnames = ['Video ID', 'Name', 'Director', 'Rating', 'Play Count']
    with open('video_library.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for video in lib.list_all():
            writer.writerow({
                'Video ID': video.video_id,
                'Name': video.name,
                'Director': video.director,
                'Rating': video.rating,
                'Play Count': video.play_count
            })


def update_csv_display():
    # This function updates the contents of the Listbox displaying the video list on the interface
    listbox.delete(0, tk.END)  # Clear all existing items in the Listbox
    if os.path.exists('video_library.csv'):
        with open('video_library.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row in the CSV file
            listbox.insert(tk.END, "{:<10} {:<25} {:<25} {:<10} {:<10}".format("Video ID", "Name", "Director", "Rating",
                                                                               "Play Count"))
            listbox.insert(tk.END, "-" * 85)
            for row in reader:
                try:
                    # Convert the rating from a number to a string of "*" for display
                    rating_stars = '*' * int(row[3])
                except ValueError:
                    rating_stars = row[3]
                # Update the Listbox with the data row
                listbox.insert(tk.END, "{:<10} {:<25} {:<25} {:<10} {:<10}".format(row[0], row[1], row[2], rating_stars,
                                                                                   row[4]))
            status_lbl.config(text="Listed all videos!", fg="red")


def list_all_videos_button():
    # When the "List All Videos" button is clicked
    update_csv()  # Update the CSV file content
    update_csv_display()  # Update the video list on the interface


def delete_videos_button():
    # When the "Delete Video" button is clicked
    selected_index = listbox.curselection()
    if not selected_index:
        status_lbl.config(text="No video selected to delete.", fg="red")
        return

    selected_item = listbox.get(selected_index)
    video_id = selected_item.split()[0]

    # Display a confirmation dialog to delete the video
    confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete Video ID {video_id}?")
    if confirm:
        lib.delete_video(video_id)  # Delete the video from the library
        update_csv_display()  # Update the Listbox after deletion
        status_lbl.config(text=f"Video ID {video_id} deleted.", fg="green")
    else:
        status_lbl.config(text="Delete action cancelled.", fg="blue")


# Initialize the main application window
window = tk.Tk()
fm = FontManager(window)

label = tk.Label(window, text="Select an option by clicking one of the buttons below")
fm.apply_font(label, "default")
label.pack(pady=20)

frame = tk.Frame(window)
frame.pack(pady=10)

button_width = 20

# Create the buttons on the main interface and attach event handlers to each button
btn_check_videos = tk.Button(frame, text="Check Videos", command=check_videos_clicked, width=button_width)
fm.apply_font(btn_check_videos, "default")
btn_check_videos.grid(row=0, column=0, padx=10, pady=(0, 10))

btn_create_video_list = tk.Button(frame, text="Create Videos", command=create_video_button, width=button_width)
fm.apply_font(btn_create_video_list, "default")
btn_create_video_list.grid(row=0, column=1, padx=10, pady=(0, 10))

btn_update_videos = tk.Button(frame, text="Update Videos", command=update_videos_button, width=button_width)
fm.apply_font(btn_update_videos, "default")
btn_update_videos.grid(row=0, column=2, padx=10, pady=(0, 10))

btn_favorite_videos = tk.Button(frame, text="Favorite Videos", command=favorite_videos_button, width=button_width)
fm.apply_font(btn_favorite_videos, "default")
btn_favorite_videos.grid(row=1, column=0, padx=10)

btn_delete_videos = tk.Button(frame, text="Delete Video", command=delete_videos_button, width=button_width)
fm.apply_font(btn_delete_videos, "default")
btn_delete_videos.grid(row=1, column=1, padx=10)

btn_create_playlist = tk.Button(frame, text="Create Playlist", command=create_playlist_button, width=button_width)
fm.apply_font(btn_create_playlist, "default")
btn_create_playlist.grid(row=1, column=2, padx=10)

# Use a Listbox with a fixed-width (monospace) font to display the video list
global listbox
listbox = tk.Listbox(window, width=85, height=15, selectmode=tk.SINGLE,
                     font=('Courier', 12))  # The Courier font is only applied to the Listbox
listbox.pack(padx=10, pady=10)

# Create other buttons on the main interface
btn_list_all_videos = tk.Button(window, text="List All Videos", command=list_all_videos_button, width=button_width)
fm.apply_font(btn_list_all_videos, "default")
btn_list_all_videos.pack(pady=(0, 10))

# Label to display the application's status
status_lbl = tk.Label(window, text="")
fm.apply_font(status_lbl, "default")
status_lbl.pack(pady=10)

# Update the content from the CSV file when the application starts
update_csv()

# Start the main loop of the interface, handling events
window.mainloop()
