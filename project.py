from moviepy.config import change_settings

# Explicitly set the ImageMagick binary path
change_settings(
    {"IMAGEMAGICK_BINARY": "C:\\Program Files\\ImageMagick-7.1.1-Q16-HDRI\\magick.exe"}
)



def readKeyword(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
        keyword = lines[0].split(":")[1].strip()
    return keyword

keyword = readKeyword("input.txt")


# def read_story(file_path):
#     with open(file_path, "r") as file:
#         lines = file.readlines()
#         story = lines[1].split(":")[1].strip()
#     return story


# print(read_keyword("input.txt"))




def readInputFile(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
        keyword = lines[0].split(":")[1].strip()
        story = lines[1].split(":")[1].strip()
    return keyword, story


import os
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.editor import (
    VideoFileClip,
    ImageClip,
    TextClip,
    CompositeVideoClip,
    AudioFileClip,
    concatenate_videoclips,
)


def loadMediaFiles(folderPath, keyword):
    mediaFiles = []
    for fileName in os.listdir(folderPath):
        if keyword.lower() in fileName.lower():
            filePath = os.path.join(folderPath, fileName)
            if fileName.endswith(".mp4"):
                mediaFiles.append(VideoFileClip(filePath))
            elif fileName.endswith((".jpg", ".png")):
                mediaFiles.append(
                    ImageClip(filePath).set_duration(2)
                )  
    return mediaFiles


def generateVideo(mediaFiles, story, outputPath, audio):
    finalClip = concatenate_videoclips(mediaFiles, method="compose")

    textClip = (
        TextClip(story, fontsize=24, color="white")
        .set_position("bottom")
        .set_duration(finalClip.duration)
    )
    finalVideo = CompositeVideoClip([finalClip, textClip])
    audioClip = AudioFileClip(audio).set_duration(finalVideo.duration)
    finalVideo = finalVideo.set_audio(audioClip)
    finalVideo.write_videofile(outputPath, codec="libx264", fps=24)


if __name__ == "__main__":
    inputFile = "input.txt"
    mediaFolder = "media"
    audioFolder = "audio"
    audioFileName =  f"{keyword}.mp3"
    outputFile = "generated_video/generated.mp4"
    audioFile = os.path.join(audioFolder, audioFileName)
    keyword, story = readInputFile(inputFile)
    mediaFiles = loadMediaFiles(mediaFolder, keyword)
    generateVideo(mediaFiles, story, outputFile, audioFile)


