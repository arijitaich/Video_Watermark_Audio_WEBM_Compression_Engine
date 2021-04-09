import moviepy.editor as mp
import sys, getopt
import requests
from datetime import datetime
from random import randint
import os, os.path, random



value = randint(0, 10)
rand_aud = str(randint(0, len(os.listdir('aud/'))))
now = datetime.now()
dt_stamp = now.strftime("%d%m%Y%H%M%S") + str(value)
inputfile = ''
keypass = ''

def main(argv):
   inputfile = ''
   keypass = ''
   try:
      opts, args = getopt.getopt(argv,"hi:k:",["ifile=","key="])
   except getopt.GetoptError:
      print ('in.py -i <inputfile> -k <user_key>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('in.py -i <inputfile> -k <user_key>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-k", "--key"):
         keypass = arg
        
#    print(inputfile)
#    print(keypass)

   inp = inputfile
   if inp == '':
       inp = 'in/f.mp4'
   out = 'out/' + keypass + '_' + dt_stamp + '.webm'
   # aud = 'aud/' + rand_aud +'.WAV'
   aud = 'aud/' + random.choice(os.listdir("aud/"))

   logu = 'logo.png'


   video = mp.VideoFileClip(inp)
   # if video.rotation == 90:
   video = video.resize(video.size[::-1])
   video.rotation = 0


   logo = (mp.ImageClip(logu)
           .set_duration(video.duration)
           .resize(height=50) # if you need to resize...
           .margin(right=8, top=8, opacity=0) # (optional) logo-border padding
           .set_pos(("right","top")))

   if aud != '':
       audioclip = mp.AudioFileClip(aud).set_duration(video.duration)
       new_audioclip = mp.CompositeAudioClip([audioclip])
       video.audio = new_audioclip



   final = mp.CompositeVideoClip([video, logo])
   final.write_videofile(out)
   
   url = 'https://xxxxxx.com.au?auth=' + keypass + '&handle=stream'
   print ('Posting Data To ' + url)

   userdata = {"loc": out, "stamp": dt_stamp, "Auth": keypass, "handle": "stream"}
   resp = requests.post(url)


#    files = {'file': open(out, 'rb')}
#    userdata = {"loc": out, "stamp": dt_stamp, "Auth": keypass, "handle": "stream"}
#    resp = requests.post(url, files=files, params=userdata)
#    r = requests.get(url, headers={"Auth":keypass, "handle":"stream"})

   print ('Call Response:')
   print (resp)

if __name__ == "__main__":
   main(sys.argv[1:])
