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
        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        self.colours = ["red", "green", "blue"]
        self.colour_box = wx.RadioBox(parent=self, label="Colours",
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

if __name__ == "__main__":
    SCREEN_APP = wx.App()
    MAIN_FRAME = MainFrame(parent=None, title="Frame with radiobox")
    SCREEN_APP.MainLoop()
