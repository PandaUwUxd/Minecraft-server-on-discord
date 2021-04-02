from pypresence import Presence
import time
import gi
client_id = '807429611641110528' # Id de aplicacion discord https://discord.com/developers/applications
RPC = Presence(client_id)
RPC.connect()
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

#class NewServer(Gtk.Dialog):
#   def __init__(self, parent):
#       Gtk.Dialog.__init__(self, title="NewServer", transient_for=parent, flags=0)
#       self.add_buttons(
#           Gtk.STOCK_CLOSE, Gtk.ResponseType.CLOSE
#       )
#       self.set_default_size(150, 100)
#       label = Gtk.Label(label="Custom text")
#       box = self.get_content_area()
#       box.add(label)
#       self.show_all()

class HyPixel(Gtk.Dialog):
    def __init__(self, parent):
        Gtk.Dialog.__init__(self, title="HyPixel", transient_for=parent, flags=0)
        self.add_buttons(
            Gtk.STOCK_CLOSE, Gtk.ResponseType.CLOSE
        )
        self.set_default_size(150, 100)
        label = Gtk.Label(label="Jugando HyPixel")
        box = self.get_content_area()
        box.add(label)
        self.show_all()

class McMexico(Gtk.Dialog):
    def __init__(self, parent):
        Gtk.Dialog.__init__(self, title="McMexico", transient_for=parent, flags=0)
        self.add_buttons(
            Gtk.STOCK_CLOSE, Gtk.ResponseType.CLOSE
        )
        self.set_default_size(150, 100)
        label = Gtk.Label(label="Jugando McMexico")
        box = self.get_content_area()
        box.add(label)
        self.show_all()
        
class localhost(Gtk.Dialog):
    def __init__(self, parent):
        Gtk.Dialog.__init__(self, title="localhost", transient_for=parent, flags=0)
        self.add_buttons(
            Gtk.STOCK_CLOSE, Gtk.ResponseType.CLOSE
        )
        self.set_default_size(150, 100)
        label = Gtk.Label(label="Jugando localhost")
        box = self.get_content_area()
        box.add(label)
        self.show_all()
        
class ButtonWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Minecraft server")
        self.set_border_width(20)
        hbox = Gtk.Box(spacing=6)
        self.add(hbox)
        
#       button = Gtk.Button.new_with_label("NewServer")
#       button.connect("clicked", self.on_NewServer_clicked)
#       hbox.pack_start(button, True, True, 0)
        
        button = Gtk.Button.new_with_label("HyPixel")
        button.connect("clicked", self.on_hypixel_clicked)
        hbox.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_label("McMexico")
        button.connect("clicked", self.on_mcmexico_clicked)
        hbox.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_label("localhost")
        button.connect("clicked", self.on_localhost_clicked)
        hbox.pack_start(button, True, True, 0)
        
        button = Gtk.Button.new_with_label("Salir")
        button.connect("clicked", self.on_exit_clicked)
        hbox.pack_start(button, True, True, 0)
        
#   def on_NewServer_clicked(self, button):
#       dialog = NewServer(self)
#       start_time=time.time()
#       print(RPC.update(state="ServerIP", details="ServerName", start=start_time))
#       response = dialog.run()
#       if response == Gtk.ResponseType.CLOSE:
#           print(RPC.update(state="  ", details="  "))
#       dialog.destroy()

    def on_hypixel_clicked(self, button):
        dialog = HyPixel(self)
        start_time=time.time()
        print(RPC.update(large_image="hypixel", state="play.hypixel.net", details="HyPixel", start=start_time))
        response = dialog.run()
        if response == Gtk.ResponseType.CLOSE:
            print(RPC.update(state="  ", details="  "))
        dialog.destroy()

    def on_mcmexico_clicked(self, button):
        dialog = McMexico(self)
        start_time=time.time()
        print(RPC.update(state="play.mcmexico.net", details="McMexico", start=start_time))
        response = dialog.run()
        if response == Gtk.ResponseType.CLOSE:
            print(RPC.update(state="  ", details="  "))
        dialog.destroy()

    def on_localhost_clicked(self, button):
        dialog = localhost(self)
        start_time=time.time()
        print(RPC.update(state="localhost", details="PruebasUwU", start=start_time))
        response = dialog.run()
        if response == Gtk.ResponseType.CLOSE:
            print(RPC.update(state="  ", details="  "))
            dialog.destroy()
        
    def on_exit_clicked(self, button):
        print("Closing application")
        Gtk.main_quit()

win = ButtonWindow()
win.connect("destroy", Gtk.main_quit, print(RPC.update(state="  ", details="  ")))
win.show_all()
Gtk.main()
