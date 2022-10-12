from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

ffmpeg_extract_subclip("media/chaplin.mp4", 0, 5, outputfile="test.mp4")