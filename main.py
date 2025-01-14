from tkinter import filedialog
from tkinter import ttk
import spotube
import tkinter

selected_directory = "./Songs"
my_downloaded = None

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

def click_button():
    global my_downloaded
    spotify_link1 = spotify_link.get()
    my_downloaded = spotube.DownloadManager(spotify_id, spotify_secret, genius_token, normalize_sound=False, directory=selected_directory)
    my_downloaded.start_downloader(spotify_link1)

def stop_button():
    global my_downloaded
    if my_downloaded:
        my_downloaded.cancel_downloader()
    else:
        print("No download in progress to stop.")

def exit():
    window.destroy()

def start_move(event):
    window.x = event.x
    window.y = event.y

def do_move(event):
    x = window.winfo_pointerx() - window.x
    y = window.winfo_pointery() - window.y
    window.geometry(f"+{x}+{y}")

def set_directory():
    global selected_directory
    directory = filedialog.askdirectory(title="Select Download Directory")
    my_downloaded = spotube.DownloadManager(spotify_id, spotify_secret, genius_token, normalize_sound=False)
    my_downloaded.set_directory(directory)
    if directory:
        selected_directory = directory


# Şarkılar Default olarak Uygulamanın yer aldığı Mevcut Dizinde Songs adlı bir klasör oluşturacak ve altına eklenecektir.

spotify_id = "6f471769f2f84113a76262e4eafeb1ee"
spotify_secret = "b157d03107d54099a564c4055d79fec6"
genius_token = "uwMlwY4wMotBeenVwI6SI5jfex_eqJchF8oLv85dXzdus9D-Zqstar-aU3znzmoo"

window_hex= "#303030"
button_hex = "#207243"
exit_hex= "#FF0000"

window = tkinter.Tk()
window.title("Spotify Playlist Downloader")
window.config(bg=window_hex)
window.minsize(height=300,width=500)
center_window(window)

#title_bar = tkinter.Frame(window, bg=button_hex, relief="raised", bd=10)
#title_bar.pack(side="top", fill="x")

#title_bar.bind("<Button-1>", start_move)
#title_bar.bind("<B1-Motion>", do_move)

#exit_button = tkinter.Button( text="x", bg=exit_hex, fg="white", font=("Inter", 10), command=exit, borderwidth=0, activebackground=exit_hex)
#exit_button.place(x=480,y=1)

#appname_label = tkinter.Label(text="Spotify Playlist Downloader", font=('Inter', 20, "normal"), background=window_hex, fg="white")
#appname_label.place(x=75,y=20)

label= tkinter.Label(text="Download Link", font=("Inter", 10, "normal"), background=window_hex, fg="white")
label.place(x=200,y=60)

spotify_link = tkinter.Entry(width=60, borderwidth=0, background=button_hex)
spotify_link.place(x=75,y=90)

download_button = tkinter.Button(text="Download", font=('Inter', 8, 'normal'), command=click_button, background=button_hex, borderwidth=0, fg="white")
download_button.config(padx=75,pady=4)
download_button.place(x=50,y=200)

stop_button = tkinter.Button(text="Stop", font=('Inter', 8, 'normal'), command=stop_button, background=exit_hex, borderwidth=0, fg="white")
stop_button.config(padx=75,pady=4)
stop_button.place(x=275,y=200)

change_directory_button = tkinter.Button(text="Change Directory", font=('Inter', 8, 'normal'),command=set_directory, background="black", borderwidth=0, fg="white")
change_directory_button.config(padx=75,pady=4)
change_directory_button.place(x=132,y=250)

window.mainloop()

