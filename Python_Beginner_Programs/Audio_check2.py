import audiodiff
import sounddevice as sd
from scipy.io.wavfile import write
i=0
while True:
	fs = 44100  # Sample rate
	seconds = 2  

	myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
	sd.wait()  # Wait until recording is finished
	path=r'C:\Users\admin\Downloads\Audio\output{}.mp3'.format(i)
	write(path,fs,myrecording)
	if(i>2):
		j=i-2
		path1 = r'C:\Users\admin\Downloads\Audio\output{}.mp3'.format(j)
		remove(path)
	++i

	#audiodiff.audio_equal('airplane.flac', 'airplane.m4a')


