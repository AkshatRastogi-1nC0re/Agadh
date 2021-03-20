import cv2
import time
import speech_recognition as sr
from moviepy.editor import VideoFileClip, concatenate_videoclips, CompositeVideoClip
from os import listdir
from os.path import isfile, join

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
query = takecommand().lower()
# query = "animal bird"
print(query)
mypath = "C:\\Users\\Akshat\\Documents\\GitHub\\Project-ASS\\handsigns\\videos\\"
mypath2 = "C:\\Users\\Akshat\\Documents\\GitHub\\Project-ASS\\handsigns\\letter_videos\\"
onlyfiles = [f.strip(".mp4") for f in listdir(mypath) if isfile(join(mypath, f))]
onlyfiles_neo = [f for f in listdir(mypath) if isfile(join(mypath, f))]
onlyfiles2 = [f for f in listdir(mypath2) if isfile(join(mypath2, f))]
print(onlyfiles)
print(onlyfiles2)
query_list = query.split()
list_file_names = []

for word in query_list:
    if word in onlyfiles:
        for fn in onlyfiles_neo:
            if word in fn:
                clip1 = VideoFileClip(join(mypath,fn))
                list_file_names.append(clip1)
                break
    else:
        for i in word:
            for fn1 in onlyfiles2:
                x = "".join(list(fn1)[:-4])
                if i in x:
                    list_file_names.append(VideoFileClip(join(mypath2, fn1)))
                    break

print(list_file_names)

final_clip = concatenate_videoclips(list_file_names, method='compose')
final_clip.write_videofile("new.mp4",fps=60)


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


