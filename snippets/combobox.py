import wx


class MainFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        panel = MainPanel(self)
        sizer = wx.BoxSizer()
        sizer.Add(panel)
        self.SetSizerAndFit(sizer)
        self.Show()


class MainPanel(wx.Panel):
    def __init__(self, parent, *args, **kwargs):
        wx.Panel.__init__(self, parent, *args, **kwargs)
        self.months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                       "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.month_panel = MonthPanel(self)
        sizer.Add(self.month_panel, flag=wx.ALL, border=10)
        self.SetSizer(sizer)


class MonthPanel(wx.Panel):
    def __init__(self, parent, *args, **kwargs):
        wx.Panel.__init__(self, parent, *args, **kwargs)
        date_box = wx.StaticBox(self, label="Expiry date")
        sizer = wx.StaticBoxSizer(date_box, wx.HORIZONTAL)
        cmb_month = wx.ComboBox(self, size=(100, -1), value="Month", choices=parent.months)
        sizer.Add(cmb_month, flag=wx.ALL, border=10)
        self.SetSizer(sizer)

if __name__ == "__main__":
    SCREEN_APP = wx.App()
    MAIN_FRAME = MainFrame(None, title="Frame with a combobox")
    SCREEN_APP.MainLoop()
