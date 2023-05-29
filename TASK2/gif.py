#SCALE IT MORE
#TASK 3
#GIF Creator


from moviepy.editor import *
videoClip = VideoFileClip("Goku.mp4")
clip=videoClip.subclip(4,7)
clip.write_gif("Goku!.gif")