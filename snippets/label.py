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
        lbl_hello = wx.StaticText(self, label="Hello")
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(lbl_hello, flag=wx.ALL, border=10)
        self.SetSizer(sizer)


if __name__ == "__main__":
    SCREEN_APP = wx.App()
    MAIN_FRAME = MainFrame(None, title="Frame with label")
    SCREEN_APP.MainLoop()
