import socket
import time
import re
import bayes
import threading
import pyttsx
import featurize
import speech_recognition as sr
from collections import defaultdict
from sklearn.naive_bayes import MultinomialNB as MNB


HOST = "irc.twitch.tv"              # the Twitch IRC server
PORT = 6667                         # always use port 6667!
NICK = "greenautobot"            # your Twitch username, lowercase
PASS = "oauth:XXXXXXXXXX" # your Twitch OAuth token
CHAN = "#CHANNEL"                   # the channel you want to join

def chat(sock, msg):
    sock.send("PRIVMSG #{} :{}".format(cfg.CHAN, msg))
    
def ban(sock, user):
    chat(sock, ".ban {}".format(user))

def timeout(sock, user, secs=600):
    chat(sock, ".timeout {}".format(user, secs))
    
# network functions go here
s = socket.socket()
s.connect((HOST, PORT))
s.send("PASS {}\r\n".format(PASS).encode("utf-8"))
s.send("NICK {}\r\n".format(NICK).encode("utf-8"))
s.send("JOIN {}\r\n".format(CHAN).encode("utf-8"))

CHAT_MSG=re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")
train = True # are we in training mode?
read = False # or are we in reading mode?
yesNo = None # variable used to tell the model if the current chat message should be used as a positive or negative training example
lastProcessed = True
freq = 2 # frequency of messages read

def pong_and_read():
    bayes = MNB()
    engine = pyttsx.init()
    i = 0
    global train
    global lastProcessed
    global yesNo
    while True:
        response = s.recv(1024).decode("utf-8")
        if response == "PING :tmi.twitch.tv\r\n":
            s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
        else:
            username = re.search(r"\w+", response).group(0).encode("utf-8") # return the entire match
            message = CHAT_MSG.sub("", response).encode("utf-8")
            if not re.match("^:\w+!\w+@\w", message) and not re.match("\w+\.tmi\.twitch\.tv", message):
                print(username + ": " + message)

                if message == "!train": 
                    train = True
                    
                if message == "!read": 
                    read = True
                    
                if train == True:
                    if  yesNo == None and lastProcessed == True and (i+1)%freq == 0:
                        engine.say(username + message)
                        engine.runAndWait()
                        read_message = message
                        print read_message, "MESSAGE WHICH WAS READ"
                        lastProcessed = False
                        
                    if yesNo != None and lastProcessed == False:
                        word_count = defaultdict(int)
                        if yesNo == True:
                            bayes.partial_fit(featurize.generate_feature_vector(read_message, word_count), [1], classes=[0,1]) #generate feature vectors to convert chat messages to usable form for naive bayes model
                        if yesNo == False:
                            bayes.partial_fit(featurize.generate_feature_vector(read_message, word_count), [0], classes=[0,1])
                        lastProcessed = True
                        yesNo = None
                        print "Trained"
                        engine.say("Trained")
                        engine.runAndWait()
                        
                if read == True:
                    prob = MNB.predict_proba(featurize.generate_feature_vector(message, word_count))[1]
                    if prob > .5:
                        engine.say(username + message)
                        engine.runAndWait()
                        
        time.sleep(.01)
        i+=1
    
def listen():
    i=0
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.adjust_for_ambient_noise(source) # listen for 1 second to calibrate the energy threshold for ambient noise levels
        while True:
            print "Listening ", i
            audio = r.listen(source)                   # now when we listen, the energy threshold is already set to a good value, and we can reliably catch speech right away
            print "Done Listening"
            threading.Thread(target=decipher, args=(audio,i)).start()
            i+=1
    
def decipher(audio, i):
    global train
    global read
    global yesNo
    try:
        said = sr.Recognizer().recognize(audio)
        print("You said " + said, i)    # recognize speech using Google Speech Recognition
        if "train" in said:
            train = True
            read = False
        if "read" in said:
            read = True
            train  = False
        if "yes" in said:
            yesNo = True
        if "no" in said:
            yesNo = False
            
    except LookupError:                            # speech is unintelligible
        print("Could not understand audio", i)
    
    
try:
   threading.Thread(target=pong_and_read).start()
   threading.Thread(target=listen).start()
except:
   print "Error: unable to start thread"
