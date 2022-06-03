import vlc

player = vlc.MediaPlayer("raspi-files/audio/1khz.wav")

player.play()
    