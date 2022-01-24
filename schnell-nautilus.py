# Schnell Nautilus Extension
#
# Place me in ~/.local/share/nautilus-python/extensions/,
# ensure you have python-nautilus package, restrart Nautilus, and enjoy :)

from gi import require_version
require_version('Gtk', '3.0')
require_version('Nautilus', '3.0')
from gi.repository import Nautilus, GObject
from subprocess import call
import os

# path to schnell
schnell = 'schnell'

# what name do you want to see in the context menu?
schnellname = 'Schnell'

# always create new window?
NEWWINDOW = False


class SchnellExtension(GObject.GObject, Nautilus.MenuProvider):

    def schnellname(self, menu, files):
        safepaths = ''

        for file in files:
            filepath = file.get_location().get_path()
            safepaths += '"' + filepath + '" '

            # If one of the files we are trying to open is a folder
            # create a new instance of schnell


        call(schnell + ' ' + safepaths + '&', shell=True)

    def get_file_items(self, window, files):
        item = Nautilus.MenuItem(
            name='SchnellOpen',
            label='Open In ' + schnellname,
            tip='Opens the selected files with Schnell'
        )
        item.connect('activate', self.schnellname, files)

        return [item]

    def get_background_items(self, window, file_):
        item = Nautilus.MenuItem(
            name='SchnellOpenBackground',
            label='Open in ' + schnellname,
            tip='Opens Schnell in the current directory'
        )
        item.connect('activate', self.schnellname, [file_])

        return [item]
