import wx


class MainFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        panel = MainPanel(self)
        sizer = wx.BoxSizer()
        sizer.Add(panel)
        self.SetSizerAndFit(sizer)
        self.Show()


class MainPanel(wx.Panel):
    def __init__(self, parent, *args, **kwargs):
        wx.Panel.__init__(self, parent, *args, **kwargs)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.colours = ["red", "green", "blue"]
        self.colour_box = wx.RadioBox(self, label="Colours",
                                      choices=self.colours,
                                      style=wx.RA_SPECIFY_ROWS)
        self.colour_box.Bind(wx.EVT_RADIOBOX, self.on_rb_colour_click)
        sizer.Add(self.colour_box, flag=wx.ALL, border=10)
        self.SetSizer(sizer)

    def on_rb_colour_click(self, event):
        del event
        print(self.colours[self.colour_box.GetSelection()])

    def on_cmd_cancel_click(self, event):
        del event
        quit()

class RadioButtonPanel(wx.Panel):
    def __init__(self, parent, *args, **kwargs):
        wx.Panel.__init__(self, parent, *args, **kwargs)
        colour_box = wx.StaticBox(self, label="Colours")
        sizer = wx.StaticBoxSizer(colour_box, wx.VERTICAL)
        self.rb_colours = []
        colours = ["red", "green", "blue"]
        for colour in colours:
            rb_colour = wx.RadioButton(colour_box, label=colour, name=colour)
            rb_colour.Bind(wx.EVT_CHECKBOX, parent.on_rb_colour_click)
            sizer.Add(rb_colour, flag=wx.LEFT|wx.RIGHT, border=10)
            self.rb_colours.append(rb_colour)
        self.SetSizer(sizer)

if __name__ == "__main__":
    SCREEN_APP = wx.App()
    MAIN_FRAME = MainFrame(None, title="Frame with radiobox")
    SCREEN_APP.MainLoop()
