"""Demonstrate the use of a wxPython MessageDialog."""

import wx


class MainFrame(wx.Frame):
    """Create and show the frame for the application."""
    def __init__(self, *args, **kwargs):
        """Initialise the MainFrame class."""
        super(MainFrame, self).__init__(*args, **kwargs)
        self.Bind(wx.EVT_CLOSE, self.on_quit_click)
        self.Show()

    def on_quit_click(self, event):
        """Display close warning dialog and quit if confirmed."""
        warning_dialog = wx.MessageDialog(parent=self,
                                          message="Quit frame?",
                                          style=wx.ICON_QUESTION|wx.YES_NO)
        result = warning_dialog.ShowModal()
        if result == wx.ID_YES:
            print("Now closing")
            quit()

if __name__ == "__main__":
    """Implement the wxPython loop."""
    SCREEN_APP = wx.App()
    MAIN_FRAME = MainFrame(parent=None, title="Warning dialog")
    SCREEN_APP.MainLoop()
