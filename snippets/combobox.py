"""Demonstrate the creation of a wxComboBox widget."""


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
        self.months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                       "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        month_sizer = self.create_month_sizer()
        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        sizer.Add(month_sizer, flag=wx.ALL, border=10)
        self.SetSizer(sizer)

    def create_month_sizer(self):
        """Return a sizer containing the month combobox."""
        date_box = wx.StaticBox(parent=self, label="Expiry date")
        sizer = wx.StaticBoxSizer(box=date_box, orient=wx.HORIZONTAL)
        cmb_month = wx.ComboBox(parent=self, size=(100, -1), value="Month", choices=self.months)
        sizer.Add(cmb_month, flag=wx.ALL, border=10)
        return sizer

if __name__ == "__main__":
    """Implement the wxPython loop."""
    SCREEN_APP = wx.App()
    MAIN_FRAME = MainFrame(parent=None, title="Frame with a combobox")
    SCREEN_APP.MainLoop()
