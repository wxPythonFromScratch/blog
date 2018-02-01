import wx


class MainFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        self.Bind(wx.EVT_CLOSE, self.on_close_click)
        self.Show()

    def on_close_click(self, event):
        warning_dialog = wx.MessageDialog(parent=self,
                                          message="Close frame?",
                                          style=wx.ICON_QUESTION|wx.YES_NO)
        result = warning_dialog.ShowModal()
        if result == wx.ID_YES:
            print("Now closing")
            quit()

if __name__ == "__main__":
    SCREEN_APP = wx.App()
    MAIN_FRAME = MainFrame(parent=None, title="Warning dialog")
    SCREEN_APP.MainLoop()
