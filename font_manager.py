import tkinter as tk
import tkinter.font as tkfont

# Define the FontManager class to manage and apply font styles to widgets in the GUI
class FontManager:
    def __init__(self, root):
        # Define the font family you want to use for the interface components
        family = "Helvetica"  # Set the font family to "Helvetica"

        # Configure the default font for interface components
        # TkDefaultFont: This is the default font for common widgets like Label, Button, etc.
        default_font = tkfont.nametofont("TkDefaultFont", root=root)
        default_font.configure(size=15, family=family)  # Set the font size to 15 and font family to Helvetica

        # TkTextFont: This is the default font for text-containing widgets like Text, Entry, etc.
        text_font = tkfont.nametofont("TkTextFont", root=root)
        text_font.configure(size=12, family=family)  # Set the font size to 12 and font family to Helvetica

        # TkFixedFont: This is a fixed-width (monospace) font, often used for widgets like Text or Label displaying aligned data
        fixed_font = tkfont.nametofont("TkFixedFont", root=root)
        fixed_font.configure(size=12, family=family)  # Set the font size to 12 and font family to Helvetica

        # Store the font styles in a dictionary for easy application later
        self.font_styles = {
            "default": default_font,  # Default font
            "text": text_font,        # Font for text
            "fixed": fixed_font,      # Fixed-width font
        }

    # Function to apply the font style to the specified widget
    def apply_font(self, widget, style="default"):
        # Apply the specified font style to the widget
        if style in self.font_styles:  # Check if the style exists in the font_styles dictionary
            widget.config(font=self.font_styles[style])  # Apply the selected font to the widget
        else:
            # If the style does not exist, raise a ValueError to indicate an error
            raise ValueError(f"Font style '{style}' is not recognized.")

# Test the application with the new FontManager
if __name__ == '__main__':
    window = tk.Tk()  # Create the main window of the application
    fm = FontManager(window)  # Pass the root window when initializing the FontManager

    # Create a Label widget and apply the "default" font
    label = tk.Label(window, text="Sample Label")
    fm.apply_font(label, "default")  # Apply the default font from FontManager
    label.pack()  # Display the Label on the interface

    # Create an Entry widget and apply the "text" font
    entry = tk.Entry(window)
    fm.apply_font(entry, "text")  # Apply the text font from FontManager
    entry.pack()  # Display the Entry on the interface

    # Create a Button widget and apply the "default" font
    button = tk.Button(window, text="Sample Button")
    fm.apply_font(button, "default")  # Apply the default font from FontManager
    button.pack()  # Display the Button on the interface

    window.mainloop()  # Start the event loop of the interface, listening for events and updating the interface
