from pyo import *

s = Server().boot()

path =r"F:\Songs\Hans Zimmer  Oogway Ascends Kung Fu Panda Soundtrack.mp3"

# stereo playback with a slight shift between the two channels.
sf = SfPlayer(path, speed=[1, 0.995], loop=True, mul=0.4).out()

s.gui(locals())