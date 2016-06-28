#To create a single wav file from the audio log, go to /tmp and execute the following command:
# sox 0**audioGroup*  outputSingleFileName.wav
__module_name__ = "Speech "
__module_version__ = "0.1"
__module_description__ = "Speech Synth"
 
import xchat
import os
import thread
 
channels= ['#haskell', '#inordinatio']
langs= [ 'italian-', 'brazil-']
 
audioB=0
audioI=0
audioS=0
record=True
def espeaking1(chan, lang, nick):
		global audioB
		global audioI
		global audioS 
		if (lang == 'brazil-'):
			audioB+=1
			audioS=audioB
		else:
			audioI+=1
			audioS=audioI
		eu = xchat.get_info("nick")
		if (nick == eu):
#			print "voce"
			identidade = "mbrola-4"
		else:
#			print "eles"
			identidade = "mbrola-3"
		os.system('espeak -g 10 --pho -p 30 -s 170 -v %s%s -f /tmp/teste-%s-%s ' % (lang, identidade, chan, nick))
		if (record == True):
			os.system('espeak -w /tmp/%03d.%s%s.wav -g 3 --pho -p 10 -s 150 -v %s%s -f /tmp/teste-%s-%s ' % (audioS, lang, nick, lang, identidade, chan, nick))

def subcom_(cmds):
	global record
	if cmds[0] != '!':
		return None
		
	if(cmds[1:-2]  == 'no rec'):
		record = False
		print "recording= %s" % record
	if(cmds[1:-2]  == 'rec'):
		record = True
		print "recording= %s" % record
		
def falar_(word, word_eol, userdata):
	global audioS
	nickname = word_eol[0]
	palavras = word_eol[1]
#		print palavras[0]

	subcom_(palavras)
	
	if palavras[-1] == '@':
		palavras = palavras[0:-1]
	current = xchat.get_info('channel')
	nickname = nickname[0:nickname.index(" ")]
	for index,canal in enumerate(channels):
			if (current == canal):
				with open('/tmp/teste-%s-%s' % (current, nickname), 'w') as f:
					f.write(palavras)
				thre1 = thread.start_new_thread(espeaking1,(current, langs[index], nickname))
 
xchat.hook_print('Channel Message', falar_)
xchat.hook_print('Channel Msg Hilight', falar_)
xchat.hook_print('Your Message', falar_)
 
print "%s loaded." % __module_name__
