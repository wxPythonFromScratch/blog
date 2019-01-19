"""Demonstrate the creation of a wxPython FileDialog object."""

import wx
import os


class MainFrame(wx.Frame):
    """Create and show the frame for the application."""
    def __init__(self, *args, **kwargs):
        """Initialise the MainFrame class."""
        super(MainFrame, self).__init__(*args, **kwargs)
        panel = MainPanel(self)
        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        sizer.Add(panel)
        self.SetSizerAndFit(sizer)
        self.Show()


class MainPanel(wx.Panel):
    """Create a panel to hold application widgets."""
    def __init__(self, parent, *args, **kwargs):
        """Initialise the MainPanel class."""
        super(MainPanel, self).__init__(parent, *args, **kwargs)
        self.path = "/home/jeff/"

        path_sizer = self.create_path_sizer()
        button_sizer = self.create_button_sizer()

        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        sizer.Add(path_sizer, flag=wx.ALL, border=10)
        sizer.Add(button_sizer, flag=wx.LEFT|wx.RIGHT|wx.BOTTOM|wx.EXPAND, border=10)
        self.SetSizer(sizer)

    def on_cmd_path_click(self, event):
        """Retrieve a path and assign it to the txt_path control."""
        del event

    def on_cmd_quit_click(self, event):
        """Tear down processes and quit the application."""
        del event
        quit()

    def create_path_sizer(self):
        """Return a sizer containing the txt_path controls."""
        lbl_path = wx.StaticText(parent=self, label="Path:")
        self.txt_path = wx.TextCtrl(parent=self, size=(300, -1))
        cmd_path = wx.Button(parent=self, id=wx.ID_OPEN)
        cmd_path.Bind(wx.EVT_BUTTON, self.on_cmd_path_click)

        sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        sizer.Add(lbl_path, flag=wx.RIGHT, border=10)
        sizer.Add(self.txt_path, flag=wx.RIGHT, border=10)
        sizer.Add(cmd_path)
        return sizer

    def create_button_sizer(self):
        """Return a sizer containing the buttons."""
        cmd_quit = wx.Button(parent=self, id=wx.ID_EXIT)
        cmd_quit.Bind(wx.EVT_BUTTON, self.on_cmd_quit_click)
        sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        sizer.Add((0, 0), proportion=1)
        sizer.Add(cmd_quit)
        return sizer

if __name__ == "__main__":
    """Implement the wxPython loop."""
    SCREEN_APP = wx.App()
    MAIN_FRAME = MainFrame(parent=None, title="Open file dialog")
    SCREEN_APP.MainLoop()
