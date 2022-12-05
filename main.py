from pydub import AudioSegment
from pydub.silence import split_on_silence
import os
directory=os.fsencode("C:/Users/hilla goren barnea/Desktop/openu/thesis/records/")
directoryname=os.fsdecode(directory)
for file in os.listdir(directory):
   filename=os.fsdecode(file)
   print(filename)
   if filename.endswith(".wav"):
      sound = AudioSegment.from_wav(directoryname+filename)
      count = 0
      sum = 0
      audio_chunks = split_on_silence(sound, min_silence_len=300, silence_thresh=-40)
      for i, chunk in enumerate(audio_chunks):
         # output_file = "C:/Users/hilla goren barnea/Desktop/openu/thesis/records/distelAnger{0}.wav".format(i)
         output_file = directoryname + filename[0:-4] + (str)(i) + ".wav"
         print("Exporting file", output_file)
         chunk.export(output_file, format="wav")
         sum += (len(chunk))
         count += 1
      average_seconds = sum / (count*1000)
      print("average ", average_seconds)
   else:
      continue
