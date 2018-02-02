"""Demonstrate the basic method of creating a wxPython Frame."""

import wx

"""Implement the wxPython loop."""
SCREEN_APP = wx.App()
MAIN_FRAME = wx.Frame(parent=None, title="Raw frame")
MAIN_FRAME.Show()
SCREEN_APP.MainLoop()
