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
        cities_raw = ["London", "Birmingham", "Glasgow", "Leeds", "Bristol",
                      "Liverpool", "Manchester", "Sheffield", "Edinburgh",
                      "Cardiff", "Leicester", "Stoke-on-Trent", "Bradford",
                      "Coventry", "Nottingham", "Kingston-upon-Hull",
                      "Belfast", "Newcastle-upon-Tyne", "Sunderland",
                      "Brighton", "Derby", "Plymouth", "Wolverhampton",
                      "Southampton", "Swansea ", "Salford", "Portsmouth",
                      "Milton Keynes", "Aberdeen", "Reading", "Northampton",
                      "Luton", "Swindon", "Warrington", "Dudley", "York"]
        self.cities = sorted(cities_raw)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.city_panel = CityPanel(self)
        sizer.Add(self.city_panel, flag=wx.ALL, border=10)
        self.SetSizer(sizer)

    def on_lst_cities_click(self, event):
        lst_cities = event.GetEventObject()
        print(self.cities[lst_cities.GetSelection()])


class CityPanel(wx.Panel):
    def __init__(self, parent, *args, **kwargs):
        wx.Panel.__init__(self, parent, *args, **kwargs)
        city_box = wx.StaticBox(self, label="Destination")
        sizer = wx.StaticBoxSizer(city_box, wx.HORIZONTAL)
        lst_cities = wx.ListBox(self, size=(300, 150), choices=sorted(parent.cities))
        lst_cities.Bind(wx.EVT_LISTBOX, parent.on_lst_cities_click)
        sizer.Add(lst_cities, flag=wx.ALL, border=10)
        self.SetSizer(sizer)

if __name__ == "__main__":
    SCREEN_APP = wx.App()
    MAIN_FRAME = MainFrame(None, title="Frame with a listbox")
    SCREEN_APP.MainLoop()
