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
        lbl_name = wx.StaticText(self, label="Name:")
        txt_name = wx.TextCtrl(self, size=(150, -1))
        cmd_cancel = wx.Button(self, wx.ID_CANCEL)
        cmd_cancel.Bind(wx.EVT_BUTTON, self.on_cmd_cancel_click)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(lbl_name, flag=wx.ALL, border=10)
        sizer.Add(txt_name, flag=wx.TOP|wx.RIGHT|wx.BOTTOM, border=10)
        sizer.Add(cmd_cancel, flag=wx.TOP|wx.RIGHT|wx.BOTTOM, border=10)
        self.SetSizer(sizer)

    def on_cmd_cancel_click(self, event):
        del event
        quit()

if __name__ == "__main__":
    SCREEN_APP = wx.App()
    MAIN_FRAME = MainFrame(None, title="Frame with widgets")
    SCREEN_APP.MainLoop()
