import wx


class MainFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        panel = MainPanel(self)
        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        sizer.Add(panel)
        self.SetSizerAndFit(sizer)
        self.Show()


class MainPanel(wx.Panel):
    def __init__(self, parent, *args, **kwargs):
        wx.Panel.__init__(self, parent, *args, **kwargs)
        lbl_heading = wx.StaticText(parent=self, label="Heading")
        lbl_column_one = wx.StaticText(parent=self, label="Column one")
        lbl_column_two = wx.StaticText(parent=self, label="Column two")

        sizer = wx.GridBagSizer(5, 5)
        sizer.Add(lbl_heading, pos=(0, 0), span=(1, 2), flag=wx.TOP|wx.ALIGN_CENTER, border=10)
        sizer.Add(lbl_column_one, pos=(1, 0), flag=wx.LEFT|wx.BOTTOM|wx.RIGHT, border=10)
        sizer.Add(lbl_column_two, pos=(1, 1), flag=wx.BOTTOM|wx.RIGHT, border=10)
        self.SetSizer(sizer)


if __name__ == "__main__":
    SCREEN_APP = wx.App()
    MAIN_FRAME = MainFrame(parent=None, title="Frame with GridBagSizer")
    SCREEN_APP.MainLoop()
