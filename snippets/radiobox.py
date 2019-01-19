"""Demonstrate the creation of a wxPython RadioBox."""

import wx


class MainFrame(wx.Frame):
    """Create and show the frame for the application."""
    def __init__(self, *args, **kwargs):
        """Initialise the MainFrame class."""
        super(MainFrame, self).__init__(*args, **kwargs)
        panel = MainPanel(self)
        sizer = wx.BoxSizer()
        sizer.Add(panel)
        self.SetSizerAndFit(sizer)
        self.Show()


class MainPanel(wx.Panel):
    """Create a panel to hold application widgets."""
    def __init__(self, parent, *args, **kwargs):
        """Initialise the MainPanel class."""
        super(MainPanel, self).__init__(parent, *args, **kwargs)
        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        self.colours = ["red", "green", "blue"]
        self.colour_box = wx.RadioBox(parent=self, label="Colours",
                                      choices=self.colours,
                                      style=wx.RA_SPECIFY_ROWS)
        self.colour_box.Bind(wx.EVT_RADIOBOX, self.on_rb_colour_click)
        sizer.Add(self.colour_box, flag=wx.ALL, border=10)
        self.SetSizer(sizer)

    def on_rb_colour_click(self, event):
        """Handle the rb_colour click event."""
        del event
        print(self.colours[self.colour_box.GetSelection()])

    def on_cmd_quit_click(self, event):
        """Tear down processes and quit the application."""
        del event
        quit()

if __name__ == "__main__":
    """Implement the wxPython loop."""
    SCREEN_APP = wx.App()
    MAIN_FRAME = MainFrame(parent=None, title="Frame with radiobox")
    SCREEN_APP.MainLoop()
