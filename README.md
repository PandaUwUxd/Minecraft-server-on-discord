# Minecraft-server-on-discord

Necesitas Python3 y PiP instalado

PiP install Presence



En colsona/terminal:

- python3 DiscordMC


Para añadir un nuevo servidor necesitas hacer 3 cosas

- Añadir el dialogo que sale al presionar un boton

```
 class NewServer(Gtk.Dialog):
 def __init__(self, parent):
        Gtk.Dialog.__init__(self, title="NewServer", transient_for=parent, flags=0)
        self.add_buttons(
           Gtk.STOCK_CLOSE, Gtk.ResponseType.CLOSE
        )
        self.set_default_size(150, 100)
        label = Gtk.Label(label="Custom text")
        box = self.get_content_area()
        box.add(label)
        self.show_all()
```


- Crear un nuevo boton

```
        button = Gtk.Button.new_with_label("NewServer")
        button.connect("clicked", self.on_NewServer_clicked)
        hbox.pack_start(button, True, True, 0)

```
        
- Añadir el nuevo boton a la interfaz

```
    def on_NewServer_clicked(self, button):
        dialog = NewServer(self)
        start_time=time.time()
        print(RPC.update(state="ServerIP", details="ServerName", start=start_time))
        response = dialog.run()
        if response == Gtk.ResponseType.CLOSE:
            print(RPC.update(state="  ", details="  "))
        dialog.destroy()

```
