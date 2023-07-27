import tkinter
from tkinter import ttk, filedialog
import customtkinter
from pytube import YouTube
import os

def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink)
        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text="")

        # Check the selected download option (video or audio)
        download_option = download_options_var.get()
        if download_option == "Video":
            video = ytObject.streams.get_highest_resolution()
            download_folder = "Videos"  # Folder name for video downloads
        elif download_option == "Audio":
            audio = ytObject.streams.filter(only_audio=True).first()
            download_folder = "Audio"  # Folder name for audio downloads

        # Create the download folder if it doesn't exist
        if not os.path.exists(download_folder):
            os.makedirs(download_folder)

        # Change the current working directory to the download folder
        os.chdir(download_folder)

        # Download the video or audio to the selected folder
        if download_option == "Video":
            video.download()
        elif download_option == "Audio":
            audio.download()

        # Change back to the original working directory
        os.chdir("..")

        finishLabel.configure(text="Download Complete!", text_color="white")
    except Exception as e:
        finishLabel.configure(text=f"Download Failed: {str(e)}", text_color="red")
        

# def open_file():
#     # Choose download folder path using a file dialog
#     download_folder = filedialog.askdirectory()
#     # User input for the new file name
#     new_file = input("Name file: ")
#     # Open the file for writing in the selected folder
#     with open(f"{download_folder}/{new_file}.py", 'w') as open_file:
#         open_file.write("print('Hello, World!')")


# System settings
customtkinter.set_appearance_mode("System")  # dark mode
customtkinter.set_default_color_theme("blue")

# App frame description - window size, title, etc.
app = customtkinter.CTk()  # window init
app.geometry("720x480")  # window size
app.title("YouTube Downloader")

# UI elements

# Asking for link Input
title = customtkinter.CTkLabel(app, text="Insert a YouTube link", font=("Arial", 15))
title.pack(padx=10, pady=10)

# The link input box
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var, font=("Arial", 15))
link.pack(padx=10, pady=10)

finishLabel = customtkinter.CTkLabel(app, text="", font=("Arial", 15))
finishLabel.pack()


# Download options - Video or Audio
download_options_var = tkinter.StringVar()
download_options_var.set("Video")  # Default selection
download_options = tkinter.OptionMenu(app, download_options_var, "Video", "Audio")
download_options.config(font=("Arial", 15))
download_options.pack(padx=10, pady=10)

# Add a Label widget
label = customtkinter.CTkLabel(app, text="Click the Button to browse the Files")
label.pack(pady=10)

# Create a Button
# ttk.Button(app, text="Browse", command=open_file).pack(pady=20)

# Download button
download = customtkinter.CTkButton(app, text="Download", font=("Arial", 15), command=startDownload)
download.pack(padx=10, pady=10)

# Run app
app.mainloop()
