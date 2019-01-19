"""Demonstrate the creation of a wxPython DatePicker."""

import wx
import wx.adv
from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL,'en_GB.UTF-8')


class MainFrame(wx.Frame):
    """Create and show the frame for the application."""
    def __init__(self, *args, **kwargs):
        """Initialise the MainFrame class."""
        super(MainFrame, self).__init__(*args, **kwargs)
        panel = MainPanel(parent=self)
        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        sizer.Add(panel)
        self.SetSizerAndFit(sizer)
        self.Show()


class MainPanel(wx.Panel):
    """Create a panel to hold application widgets."""
    def __init__(self, parent, *args, **kwargs):
        """Initialise the MainPanel class."""
        super(MainPanel, self).__init__(parent, *args, **kwargs)

        now = datetime.today()
        day_one = wx.DateTime(year=now.year, month=0, day=1)
        self.dte_required = wx.adv.DatePickerCtrl(parent=self, dt=day_one)
        self.dte_required.Bind(wx.adv.EVT_DATE_CHANGED, self.on_dte_required_change)

        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        sizer.Add(self.dte_required, flag=wx.ALL, border=10)
        self.SetSizer(sizer)

    def on_dte_required_change(self, event):
        """Print date on DatePickerCtrl date change."""
        date = self.dte_required.GetValue()
        pydate = self.wxdate2pydate(date)
        print(pydate.strftime("%d %b %Y"))

    @staticmethod
    def wxdate2pydate(date):
        """Return a python dattime object from wxPython datetime object."""
        assert isinstance(date, wx.DateTime)
        if date.IsValid():
            ymd = list(map(int, date.FormatISODate().split('-')))
            year = int(ymd[0])
            month = int(ymd[1])
            day = int(ymd[2])
            return datetime(year, month, day)
        else:
            return None



if __name__ == "__main__":
    """Implement the wxPython loop."""
    SCREEN_APP = wx.App()
    MAIN_FRAME = MainFrame(parent=None, title="Datepicker")
    SCREEN_APP.MainLoop()
