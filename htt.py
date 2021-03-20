import cv2
import time
import speech_recognition as sr
from moviepy.editor import VideoFileClip, concatenate_videoclips, CompositeVideoClip

#coverts voice to text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=10)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        return "none"

    return query

# query = takecommand().lower()
# print(query)
#
# for words in query:
#     print(words)

clip1 = VideoFileClip(r"C:\Users\Akshat\Documents\GitHub\Project-ASS\handsigns\videos\ok.mp4")
clip2 = VideoFileClip(r"C:\Users\Akshat\Documents\GitHub\Project-ASS\handsigns\videos\want.wanted.mp4")

final_clip = concatenate_videoclips([clip1,clip2])
final_clip.write_videofile("new.mp4")


cap= cv2.VideoCapture('new.mp4')
fps= int(cap.get(cv2.CAP_PROP_FPS))

print("This is the fps ", fps)

if cap.isOpened() == False:
    print("Error File Not Found")

while cap.isOpened():
    ret,frame= cap.read()

    if ret == True:
        time.sleep(1/fps)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()


