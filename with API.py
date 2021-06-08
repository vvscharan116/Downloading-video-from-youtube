import requests
import json
import tkinter as tk
from tkinter import *
from tkinter import ttk
from pytube import YouTube
from tkinter import messagebox, filedialog

def progress_Check(stream, chunk,bytes_remaining):

    #Gets the percentage of the file that has been downloaded.
    global percent,rot
    percent = (100*(file_size-bytes_remaining))/file_size
    pd()
    print(percent)

def rf():
    pd()
    Download()
def pd():

    fill=Label(root,text="id"+str(id),bg="#E8D579")
    fill.grid(row=4, column=0, pady=5, padx=5)
    pg=ttk.Progressbar(root, orient=HORIZONTAL, mode='determinate', length=300)
    pg.grid(row=5, column=0, pady=5, padx=5)
    pg['value']=percent
    root.update_idletasks()


def Widgets():
    link_label = Label(root,
                       text="API link  :",
                       bg="#E8D579")
    link_label.grid(row=1,
                    column=0,
                    pady=5,
                    padx=5)

    root.linkText = Entry(root,
                          width=55,
                          textvariable=api_Link)
    root.linkText.grid(row=1,
                       column=1,
                       pady=5,
                       padx=5,
                       columnspan=2)

    destination_label = Label(root,
                              text="Destination    :",
                              bg="#E8D579")
    destination_label.grid(row=2,
                           column=0,
                           pady=5,
                           padx=5)

    root.destinationText = Entry(root,
                                 width=40,
                                 textvariable=download_Path)
    root.destinationText.grid(row=2,
                              column=1,
                              pady=5,
                              padx=5)

    browse_B = Button(root,
                      text="Browse",
                      command=Browse,
                      width=10,
                      bg="#05E8E0")
    browse_B.grid(row=2,
                  column=2,
                  pady=1,
                  padx=1)

    Download_B = Button(root,
                        text="Download",
                        command=rf,
                        width=20,
                        bg="#05E8E0")
    Download_B.grid(row=3,
                    column=1,
                    pady=3,
                    padx=3)


# Defining Browse() to select a
# destination folder to save the video

def Browse():
    # Presenting user with a pop-up for
    # directory selection. initialdir
    # argument is optional Retrieving the
    # user-input destination directory and
    # storing it in downloadDirectory
    download_Directory = filedialog.askdirectory(initialdir="/Users/lenovo/Downloads")

    # Displaying the directory in the directory
    # textbox
    download_Path.set(download_Directory)


# Defining Download() to download the video
def Download():
    # getting user-input Youtube Link

    api = api_Link.get()

    r = requests.get(api)

    data = json.loads(r.text)

    download_Folder = download_Path.get()
    # select the optimal location for
    # saving file's

    for item in data:
        id = item['ID']
        videourl = item["VideoUrl"]

        # Creating object of YouTube()
        getVideo = YouTube(videourl,on_progress_callback=progress_Check)
        global file_size
        # Getting all the available streams of the
        # youtube video and selecting the first
        # from the
        videoStream = getVideo.streams.first()
        file_size=videoStream.filesize
        # Downloading the video to destination
        # directory
        videoStream.download(download_Folder,filename=id+".mp4")

        messagebox.showinfo("SUCCESSFULLY",
                            "DOWNLOADED AND SAVED IN\n"
                            + download_Folder)


# Creating object of tk class
root = tk.Tk()

# Setting the title, background color
# and size of the tkinter window and
# disabling the resizing property
root.geometry("600x400")
root.resizable(False, False)
root.title("YouTube_Video_Downloader")
root.config(background="#000000")

# Creating the tkinter Variables
api_Link = StringVar()
download_Path = StringVar()
percent=0
# Calling the Widgets() function
Widgets()

# Defining infinite loop to run
# application
root.mainloop()