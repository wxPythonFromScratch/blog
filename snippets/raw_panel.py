import wx

class MainFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        panel = wx.Panel(parent=self)
        self.Show()

if __name__ == "__main__":
    SCREEN_APP = wx.App()
    MAIN_FRAME = MainFrame(parent=None, title="Raw panel")
    SCREEN_APP.MainLoop()
