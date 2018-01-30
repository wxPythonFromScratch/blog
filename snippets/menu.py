import wx


class MainFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        self.SetMenuBar(MenuBar())
        self.Show()

class MenuBar(wx.MenuBar):
    def __init__(self):
        wx.MenuBar.__init__(self)
        file_menu = FileMenu()
        self.Append(file_menu, '&File')

class FileMenu(wx.Menu):
    def __init__(self):
        wx.Menu.__init__(self)
        new_menu_item = wx.MenuItem(self, wx.ID_NEW)
        self.Bind(wx.EVT_MENU, self.on_new_menu_click, id=wx.ID_NEW)
        self.Append(new_menu_item)

    def on_new_menu_click(self, event):
        del event
        print('New clicked')

if __name__ == "__main__":
    SCREEN_APP = wx.App()
    MAIN_FRAME = MainFrame(None, title="Frame with menu and status panel")
    SCREEN_APP.MainLoop()
