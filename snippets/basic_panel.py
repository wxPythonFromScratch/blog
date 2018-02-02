"""Demonstrate the creation of a wxPanel object."""


import wx


class MainFrame(wx.Frame):
    """Create and show the frame for the application."""
    def __init__(self, *args, **kwargs):
        """Initialise the MainFrame class."""
        wx.Frame.__init__(self, *args, **kwargs)
        panel = MainPanel(parent=self)
        self.Show()


class MainPanel(wx.Panel):
    """Create a panel to hold application widgets."""
    def __init__(self, parent, *args, **kwargs):
        """Initialise the MainPanel class."""
        wx.Panel.__init__(self, parent, *args, **kwargs)


if __name__ == "__main__":
    """Implement the wxPython loop."""
    SCREEN_APP = wx.App()
    MAIN_FRAME = MainFrame(parent=None, title="Basic panel")
    SCREEN_APP.MainLoop()
