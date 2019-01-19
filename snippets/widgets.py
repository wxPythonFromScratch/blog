"""Demonstrate the creation of a simple wxPython application."""

import wx


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
        lbl_name = wx.StaticText(parent=self, label="Name:")
        txt_name = wx.TextCtrl(parent=self, size=(150, -1))
        cmd_quit = wx.Button(parent=self, id=wx.ID_CANCEL)
        cmd_quit.Bind(wx.EVT_BUTTON, self.on_cmd_quit_click)
        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        sizer.Add(lbl_name, flag=wx.ALL, border=10)
        sizer.Add(txt_name, flag=wx.LEFT|wx.RIGHT|wx.BOTTOM, border=10)
        sizer.Add(cmd_quit, flag=wx.LEFT|wx.RIGHT|wx.BOTTOM, border=10)
        self.SetSizer(sizer)

    def on_cmd_quit_click(self, event):
        """Tear down processes and quit the application."""
        del event
        quit()

if __name__ == "__main__":
    """Implement the wxPython loop."""
    SCREEN_APP = wx.App()
    MAIN_FRAME = MainFrame(parent=None, title="Frame with widgets")
    SCREEN_APP.MainLoop()
