# MIT License
#
# Copyright (c) 2021 pyobtimus
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import tkinter as tk
import vlc
import time

root = tk.Tk()

class TkIptvPlayer(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        
        """Init fonction for create the tkinter frame containing the direct live source

        Args:
            frame ([type]) : [frame content]
            parent ([type]): [tkinter frame]
            instance ([type]): [vlc instance]
            player ([type]): [vlc player]
        """
        
        self.frame = tk.Frame.__init__(self, parent, borderwidth = 0, highlightthickness = 0)
        self.parent = parent
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()
    
    def get_media(self):
        return self.frame

    def get_media(self):
        return self.media

    def get_instance(self):
        return self.instance

    def audio_output_device_enum(self):
        
        """Return current audio track in enum

        Returns:
            [type]: current audio track in enum
        """
        
        return self.player.audio_output_device_enum()

    def audio_set_volume(self, volume: int):
        
        """Set the sound for the vlc player

        Args:
            volume (int): volume for the vlc player
        """
        
        self.player.audio_set_volume(volume)

    def play(self, url: str):
        
        """Played the source live

        Args:
            url (str): [the url of the direct video source]
        """

        self.url = self
        self.media = self.instance.media_new(url)
        self.media.get_mrl()
        self.player.set_media(self.media)
        self.player.set_hwnd(self.winfo_id())
        self.player.play()         

    def stop(self):
        
        """stop direct video source

        """
        
        self.player.stop()

WINSIZE = (960, 540)
root.minsize(WINSIZE[0], WINSIZE[1])

player = TkIptvPlayer(root)
player.place(x=0, y=0, width=WINSIZE[0], height=WINSIZE[1])
URL = "https://turnerlive.warnermediacdn.com/hls/live/586495/cnngo/cnn_slate/VIDEO_0_3564000.m3u8"
player.play(URL)

root.mainloop()