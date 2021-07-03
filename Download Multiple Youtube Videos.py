import pafy

# ----------------------------------------
# Here you need to input your videos, 
# where it sais "[Put video link here]"
# Make sure to deleted the square brackets
urls = ["[Put video link here]", "[Put video link here]"]
# and everything inside of the square brackets
# and then put your YouTube video link there
# You can do this infinately
# ----------------------------------------

for url in urls:
    video = pafy.new(url)

    streams = video.streams
    for i in streams:
	    print(i)
	
# get best resolution regardless of format
    best = video.getbest()

    print(best.resolution, best.extension)

    #Download the video
    best.download()