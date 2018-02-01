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
        lbl_name = wx.StaticText(parent=self, label="Name:")
        txt_name = wx.TextCtrl(parent=self, size=(150, -1))
        cmd_cancel = wx.Button(parent=self, id=wx.ID_CANCEL)
        cmd_cancel.Bind(wx.EVT_BUTTON, self.on_cmd_cancel_click)
        horizontal_sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        vertical_sizer = wx.BoxSizer(orient=wx.VERTICAL)
        horizontal_sizer.Add(lbl_name, flag=wx.RIGHT|wx.ALIGN_CENTER, border=10)
        horizontal_sizer.Add(txt_name)
        vertical_sizer.Add((250, 0))
        vertical_sizer.Add(horizontal_sizer, flag=wx.ALL, border=10)
        vertical_sizer.Add(cmd_cancel, flag=wx.RIGHT|wx.BOTTOM, border=10)
        self.SetSizer(vertical_sizer)

    def on_cmd_cancel_click(self, event):
        del event
        quit()

if __name__ == "__main__":
    SCREEN_APP = wx.App()
    MAIN_FRAME = MainFrame(parent=None, title="Frame with widgets")
    SCREEN_APP.MainLoop()
