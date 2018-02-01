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
        self.txt_name = wx.TextCtrl(parent=self, size=(150, -1))
        cmd_print = wx.Button(parent=self, id=wx.ID_PRINT)
        cmd_quit = wx.Button(parent=self, id=wx.ID_EXIT)

        name_sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        name_sizer.Add(lbl_name, flag=wx.RIGHT, border=10)
        name_sizer.Add(self.txt_name)

        button_sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        button_sizer.Add(cmd_print)
        button_sizer.Add((0, 0), proportion=1)
        button_sizer.Add(cmd_quit)

        main_sizer = wx.BoxSizer(orient=wx.VERTICAL)
        main_sizer.Add(name_sizer, flag=wx.ALL, border=10)
        main_sizer.Add(button_sizer, flag=wx.LEFT|wx.RIGHT|wx.BOTTOM|wx.EXPAND, border=10)
        self.SetSizer(main_sizer)


if __name__ == "__main__":
    SCREEN_APP = wx.App()
    MAIN_FRAME = MainFrame(parent=None, title="Align button")
    SCREEN_APP.MainLoop()
