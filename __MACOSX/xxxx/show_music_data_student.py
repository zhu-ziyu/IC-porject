from tkinter import *
from tkinter.font import Font


def generate_spotify_list(filename):
    global position_list, track_list, artist_list, stream_list
    position_list = []
    track_list = []
    artist_list = []
    stream_list = []

    file_in = open(filename, encoding='utf-8', errors='replace')
    file_in.readline()

    for line in file_in:
        line = line.strip().split(",")

        position_list.append(int(line[0]))
        track_list.append(line[1].strip().replace('"', ''))
        artist_list.append(line[2].strip().replace('"', ''))
        stream_list.append(int(line[3]))


def format_music():
    global position_list, track_list, artist_list, stream_list

    data_list = []
    # create "Track by Artist" entries
    for i in range(len(position_list)):
        data_list.append(f"{track_list[i]} by {artist_list[i]}")
    return data_list


def see_song_details():
    global position_list, track_list, artist_list, stream_list

    sel = music_listbox.curselection()
    if sel:
        idx = sel[0]
        # build the three‐line detail string
        info = (
            f"chart # {position_list[idx]}\n"
            f"{track_list[idx]} by {artist_list[idx]}\n"
            f"#streams: {stream_list[idx]}"
        )
        info_var.set(info)


# MAIN
# Holding frames
#########
global position_list, track_list, artist_list, stream_list
generate_spotify_list("spotifyNov102023.csv")

root = Tk()
mainframe = Frame(root)

monofur_font = Font(family="monofur", size=20)
monofur_medium = Font(family="monofur", size=30)
monofur_large = Font(family="monofur", size=40)

# Widgets
#########
title = Label(mainframe, text="music", font=monofur_large)

music_list = format_music()
music_var = StringVar(value=music_list)
music_listbox = Listbox(mainframe, listvariable=music_var, \
                        selectmode=SINGLE, \
                        width=80, font=monofur_font)

info_var = StringVar()
info_var.set("")
info_label = Label(mainframe, textvariable=info_var, justify=LEFT, \
                   fg="#dd0054", font=monofur_medium)

seemore_button = Button(mainframe, text="see more", font=monofur_large, \
                        command=see_song_details)

# GRID THE WIDGETS
###########

mainframe.grid(padx=50, pady=50)
title.grid(row=1, column=1, sticky=W, padx=20, pady=5)
music_listbox.grid(row=2, column=1, columnspan=2, padx=10)
info_label.grid(row=3, column=1, sticky=W, padx=10, pady=10)
seemore_button.grid(row=3, column=2, ipady=20, ipadx=40, padx=10, pady=10, sticky=E)

root.mainloop()
