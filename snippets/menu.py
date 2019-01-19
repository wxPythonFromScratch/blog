"""Demonstrate the creation of a wxPython MenuBar."""

import wx


class MainFrame(wx.Frame):
    """Create and show the frame for the application."""
    def __init__(self, *args, **kwargs):
        """Initialise the MainFrame class."""
        super(MainFrame, self).__init__(*args, **kwargs)
        self.SetMenuBar(MenuBar())
        self.Show()

class MenuBar(wx.MenuBar):
    """A MenuBar class to hold menus for the application."""
    def __init__(self):
        """Initialise the MenuBar class."""
        wx.MenuBar.__init__(self)
        file_menu = self.create_file_menu()
        self.Append(file_menu, '&File')

    def create_file_menu(self):
        """Return the 'file' menu."""
        menu = wx.Menu()
        new_menu_item = wx.MenuItem(parentMenu=menu, id=wx.ID_NEW)
        self.Bind(wx.EVT_MENU, self.on_new_menu_click, id=wx.ID_NEW)
        menu.Append(new_menu_item)
        return menu

    def on_new_menu_click(self, event):
        """Process the 'new' menu click event."""
        del event
        print('New clicked')

if __name__ == "__main__":
    """Implement the wxPython loop."""
    SCREEN_APP = wx.App()
    MAIN_FRAME = MainFrame(parent=None, title="Frame with menu and status panel")
    SCREEN_APP.MainLoop()
