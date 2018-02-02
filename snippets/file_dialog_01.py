"""Demonstrate the creation of a wxPython FileDialog object."""

import wx


class MainFrame(wx.Frame):
    """Create and show the frame for the application."""
    def __init__(self, *args, **kwargs):
        """Initialise the MainFrame class."""
        wx.Frame.__init__(self, *args, **kwargs)
        panel = MainPanel(self)
        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        sizer.Add(panel)
        self.SetSizerAndFit(sizer)
        self.Show()


class MainPanel(wx.Panel):
    """Create a panel to hold application widgets."""
    def __init__(self, parent, *args, **kwargs):
        """Initialise the MainPanel class."""
        wx.Panel.__init__(self, parent, *args, **kwargs)

        path_panel = PathPanel(self)
        cmd_quit = wx.Button(parent=self, id=wx.ID_EXIT)
        button_sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        button_sizer.Add((0, 0), proportion=1)
        button_sizer.Add(cmd_quit)

        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        sizer.Add(path_panel, flag=wx.ALL, border=10)
        sizer.Add(button_sizer, flag=wx.LEFT|wx.RIGHT|wx.BOTTOM|wx.EXPAND, border=10)
        self.SetSizer(sizer)

class PathPanel(wx.Panel):
    def __init__(self, parent, *args, **kwargs):
        wx.Panel.__init__(self, parent, *args, **kwargs)
        lbl_path = wx.StaticText(parent=self, label="Path:")
        self.txt_path = wx.TextCtrl(parent=self, size=(300, -1))
        cmd_path = wx.Button(parent=self, id=wx.ID_OPEN)

        sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        sizer.Add(lbl_path, flag=wx.RIGHT, border=10)
        sizer.Add(self.txt_path, flag=wx.RIGHT, border=10)
        sizer.Add(cmd_path)
        self.SetSizer(sizer)


if __name__ == "__main__":
    """Implement the wxPython loop."""
    SCREEN_APP = wx.App()
    MAIN_FRAME = MainFrame(parent=None, title="Open file dialog")
    SCREEN_APP.MainLoop()
