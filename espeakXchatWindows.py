__module_name__ = "Speech "
__module_version__ = "0.1"
__module_description__ = "Speech Synth"
 
import xchat
import os
import thread
import subprocess

channels= ['#haskell', '#brazil']
langs= [ 'italian', 'brazil']
 
audioB=0
audioI=0
audioS=0
 
def espeaking1(chan, lang, nick):
		global audioB
		global audioI
		global audioS 
		if (lang == 'brazil'):
			audioB+=1
			audioS=audioB
		else:
			audioI+=1
			audioS=audioI
		subprocess.Popen('"C:\Program Files\eSpeak\command_line\espeak.exe" -g 10 --pho -p 30 -s 170 -v %s -f C:/Temp/teste-%s-%s ' % (lang, chan[1:], nick), shell=True)
		subprocess.Popen('"C:\Program Files\eSpeak\command_line\espeak.exe" -w C:\Temp\%03d.%s-%s.wav -g 3 --pho -p 10 -s 150 -v %s -f C:/Temp/teste-%s-%s ' % (audioS, lang, nick, lang, chan[1:], nick), shell=True)
 
def falar_(word, word_eol, userdata):
	global audioS
	nickname = word_eol[0]
	palavras = word_eol[1]
	if palavras[-1] == '@':
		palavras = palavras[0:-1]
	current = xchat.get_info('channel')
	nickname = nickname[0:nickname.index(" ")]
	if (nickname[0].isalnum() == False):
		nickname = nickname[3:]
	#print nickname[1].isalpha()
	#print nickname[5].isalpha()
	for lang,canal in enumerate(channels):
			if (current == canal):
				with open("C:/Temp/teste-%s-%s" % (current[1:], nickname), 'w') as f:
					f.write(palavras)
				thre1 = thread.start_new_thread(espeaking1,(current, langs[lang], nickname))
 
xchat.hook_print('Channel Message', falar_)
xchat.hook_print('Channel Msg Hilight', falar_)
xchat.hook_print('Your Message', falar_)
 
print "%s loaded." % __module_name__

