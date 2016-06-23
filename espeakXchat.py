__module_name__ = "Speech "
__module_version__ = "0.1"
__module_description__ = "Speech Synth"
 
import xchat
import os
import thread
 
channels= ['#haskell', '#brazil']
langs= [ 'italian-', 'brazil-']
 
audioB=0
audioI=0
audioS=0
 
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
			identidade = "mbrola-1"
		os.system('espeak -g 10 --pho -p 30 -s 170 -v %s%s -f /tmp/teste-%s-%s ' % (lang, identidade, chan, nick))
		os.system('espeak -w /tmp/%03d.%s-%s.wav -g 3 --pho -p 10 -s 150 -v %s%s -f /tmp/teste-%s-%s ' % (audioS, lang, identidade, nick, lang, chan, nick))
 
def falar_(word, word_eol, userdata):
	global audioS
	nickname = word_eol[0]
	palavras = word_eol[1]
	if palavras[-1] == '@':
		palavras = palavras[0:-1]
	current = xchat.get_info('channel')
	nickname = nickname[0:nickname.index(" ")]
	for lang,canal in enumerate(channels):
			if (current == canal):
				with open('/tmp/teste-%s-%s' % (current, nickname), 'w') as f:
					f.write(palavras)
				thre1 = thread.start_new_thread(espeaking1,(current, langs[lang], nickname))
 
xchat.hook_print('Channel Message', falar_)
xchat.hook_print('Channel Msg Hilight', falar_)
xchat.hook_print('Your Message', falar_)
 
print "%s loaded." % __module_name__
