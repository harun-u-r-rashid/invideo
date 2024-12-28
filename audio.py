# text = input("Enter your text: ")

# sound = gtts.gTTS(text=text, lang="en")
# sound.save("audio/text.mp3")

# playsound.playsound("audio/text.mp3")



import gtts
import playsound


# It will return the keyword of this txt file.
def readKeyword(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
        keyword = lines[0].split(":")[1].strip()
    return keyword

keyword = readKeyword("input.txt")
print(keyword)


# # It will return the story of txt file.
# def readStory(file_path):
#     with open(file_path, "r") as file:
#         lines = file.readlines()
#         story = lines[1].split(":")[1].strip()
#     return story

# story = readStory("input.txt")
# print(story)


# Read all text
def inputTextRead(path):
        with open(path, 'r') as file:
                text = file.read().strip()
        return text



def textToSpeech(text, output_path):
        sound = gtts.gTTS(text=text, lang="en")
        sound.save(output_path)
   

if __name__ == "__main__":
        inputFilePath = "input.txt"
        outputFilePath = f"audio/{keyword}.mp3"
        text = inputTextRead(inputFilePath)
        textToSpeech(text, outputFilePath)


