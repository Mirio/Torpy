#                                    LICENSE BSD 2 CLAUSE                                       #
#   Copyright 2011 Mirio. All rights reserved.                                             #
#   Redistribution and use in source and binary forms, with or without modification, are        #
#   permitted provided that the following conditions are met:                                   #
#       1. Redistributions of source code must retain the above copyright notice, this list of  #
#      conditions and the following disclaimer.                                                 #
#       2. Redistributions in binary form must reproduce the above copyright notice, this list  #
#      of conditions and the following disclaimer in the documentation and/or other materials   #
#      provided with the distribution.                                                          #
#                                                                                               #
#   THIS SOFTWARE IS PROVIDED BY Mirio ''AS IS'' AND ANY EXPRESS OR IMPLIED                     #
#   WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND    #
#   FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> OR    #
#   CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR         #
#   CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR    #
#   SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON    #
#   ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING          #
#   NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF        #
#   ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.                                                  #
#                                                                                               #
#   The views and conclusions contained in the software and documentation are those of the      #
#   authors and should not be interpreted as representing official policies, either expressed   #
#   or implied, of Mirio                                                                        #

__version__ = "1.0"

# Import
import gtk
import gtk.glade
import pygtk
from gobject import gobject

# Define
def quit_button(widget, data=None):
    main.hide()
    return False
def hide():
    main.hide()
    gtk.main_quit()
    return False

gladeFile = gtk.glade.XML(fname='pygtk_baloon.glade')
wg = gladeFile.get_widget
main = wg('main')
event = {
    'on_quit_clicked': quit_button ,
}
gladeFile.signal_autoconnect(event)
label_title = wg('title')
label_text = wg('text')


def baloon(title, message, timeout, position):
    label_title.set_text(title)
    label_text.set_text(message)
    width, height = main.get_size()
    gobject.timeout_add(timeout, hide)
    if position == 1:
        main.move(0,0)
    elif position == 2:
        main.move(gtk.gdk.screen_width() - width,0)
    elif position == 3:
        main.move(0, gtk.gdk.screen_height() - height)
    elif position == 4:
        main.move(gtk.gdk.screen_width() - width, gtk.gdk.screen_height() - height)
    elif position == 5:
        main.move(0, gtk.gdk.screen_height() - height-30)
    elif position == 6:
        main.move(gtk.gdk.screen_width() - width, gtk.gdk.screen_height() - height-30)
    else:
        print "The value is not valid."
    main.show()
    gtk.main()
