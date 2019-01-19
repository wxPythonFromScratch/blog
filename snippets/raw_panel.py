"""Demonstrate the abstraction of a wxPython Frame to its own class."""

import wx

class MainFrame(wx.Frame):
    """Create and show the frame for the application."""
    def __init__(self, *args, **kwargs):
        """Initialise the MainFrame class."""
        super(MainFrame, self).__init__(*args, **kwargs)
        panel = wx.Panel(parent=self)
        self.Show()

if __name__ == "__main__":
    """Implement the wxPython loop."""
    SCREEN_APP = wx.App()
    MAIN_FRAME = MainFrame(parent=None, title="Raw panel")
    SCREEN_APP.MainLoop()
