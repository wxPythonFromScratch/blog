from datetime import datetime
import wx


class MainFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        panel = MainPanel(self)
        self.SetMenuBar(MenuBar())
        self.status_bar = self.CreateStatusBar()
        self.status_bar.SetStatusText('New client')
        sizer = wx.BoxSizer()
        sizer.Add(panel)
        self.SetSizerAndFit(sizer)
        self.Show()


class MenuBar(wx.MenuBar):
    def __init__(self):
        wx.MenuBar.__init__(self)
        file_menu = FileMenu()
        help_menu = HelpMenu()
        self.Append(file_menu, '&File')
        self.Append(help_menu, '&Help')


class FileMenu(wx.Menu):
    def __init__(self):
        wx.Menu.__init__(self)
        clear_menu_item = wx.MenuItem(self, wx.ID_CLEAR)
        save_menu_item = wx.MenuItem(self, wx.ID_SAVE)
        quit_menu_item = wx.MenuItem(self, wx.ID_EXIT)
        self.Append(clear_menu_item)
        self.Append(save_menu_item)
        self.Append(quit_menu_item)


class HelpMenu(wx.Menu):
    def __init__(self):
        wx.Menu.__init__(self)


class MainPanel(wx.Panel):
    def __init__(self, *args, **kwargs):
        wx.Panel.__init__(self, *args, **kwargs)
        self.days = [str(day) for day in range(1, 32)]
        this_year = datetime.now().year
        self.years = [str(year) for year in range(this_year, this_year+10)]
        self.months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                       "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        self.extras_list = ["Breakfast", "Newpaper", "Flowers"]
        self.room_types = ["Single", "Twin", "Double"]
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

        self.person_panel = PersonPanel(self)
        self.extras_panel = ExtrasPanel(self)
        self.room_panel = RoomPanel(self)
        self.city_panel = CityPanel(self)
        self.date_panel = DatePanel(self)
        button_panel = ButtonPanel(self)

        preferences_sizer = wx.BoxSizer(wx.HORIZONTAL)
        preferences_sizer.Add(self.extras_panel, flag=wx.RIGHT, border=10)
        preferences_sizer.Add(self.room_panel)
        sizer = wx.GridBagSizer(10, 10)
        sizer.Add(self.person_panel, pos=(0, 0), flag=wx.TOP|wx.LEFT, border=10)
        sizer.Add(preferences_sizer, pos=(0, 1), flag=wx.TOP, border=10)
        sizer.Add(self.city_panel, pos=(1, 0), flag=wx.LEFT, border=10)
        sizer.Add(self.date_panel, pos=(1, 1), flag=wx.RIGHT, border=10)
        sizer.Add(button_panel, pos=(2, 0), span=(1, 2),
                  flag=wx.LEFT|wx.BOTTOM|wx.RIGHT|wx.EXPAND,
                  border=10)
        self.SetSizer(sizer)
        self.clear_controls()

    def clear_controls(self):
        self.person_panel.txt_first_name.SetValue('')
        self.person_panel.txt_last_name.SetValue('')
        self.person_panel.txt_email.SetValue('')
        for cb_extra in self.extras_panel.cb_extras_list:
            cb_extra.SetValue(False)
        self.room_panel.room_box.SetSelection(0)
        self.city_panel.lst_cities.SetSelection(0)
        self.city_panel.lst_cities.SetSelection(-1)
        self.date_panel.cmb_day.SetValue('Day')
        self.date_panel.cmb_month.SetValue('Month')
        self.date_panel.cmb_year.SetValue('Year')

    def on_cmd_clear_click(self, event):
        del event
        self.clear_controls()

    def on_cmd_save_click(self, event):
        del event
        print('First name: %s' % self.person_panel.txt_first_name.GetValue())
        print('Last name: %s' % self.person_panel.txt_first_name.GetValue())
        print('Email: %s' % self.person_panel.txt_first_name.GetValue())
        for index, cb_extra in enumerate(self.extras_panel.cb_extras_list):
            print(self.extras_list[index]+': %s' % str(cb_extra.GetValue()))
        print('Room type: %s' % self.room_types[self.room_panel.room_box.GetSelection()])
        print('City: %s' % self.cities[self.city_panel.lst_cities.GetSelection()])
        date_string = 'Date: {day} {month} {year}'
        print(date_string.format(day=self.date_panel.cmb_day.GetValue(),
                                 month=self.date_panel.cmb_month.GetValue(),
                                 year=self.date_panel.cmb_year.GetValue()))
        print('----------------')
        self.clear_controls()

    @staticmethod
    def on_cmd_quit_click(event):
        del event
        quit()


class PersonPanel(wx.Panel):
    def __init__(self, parent, *args, **kwargs):
        wx.Panel.__init__(self, parent, *args, **kwargs)
        lbl_first_name = wx.StaticText(self, label="First name")
        lbl_last_name = wx.StaticText(self, label="Last name")
        lbl_email = wx.StaticText(self, label="Email")
        self.txt_first_name = wx.TextCtrl(self, size=(150, -1))
        self.txt_last_name = wx.TextCtrl(self, size=(150, -1))
        self.txt_email = wx.TextCtrl(self, size=(250, -1))
        sizer = wx.GridBagSizer(5, 5)
        sizer.Add(lbl_first_name, pos=(0, 0))
        sizer.Add(lbl_last_name, pos=(1, 0))
        sizer.Add(lbl_email, pos=(2, 0))
        sizer.Add(self.txt_first_name, pos=(0, 1))
        sizer.Add(self.txt_last_name, pos=(1, 1))
        sizer.Add(self.txt_email, pos=(2, 1))
        self.SetSizer(sizer)


class ExtrasPanel(wx.Panel):
    def __init__(self, parent, *args, **kwargs):
        wx.Panel.__init__(self, parent, *args, **kwargs)
        extras_box = wx.StaticBox(self, label="Extras")
        sizer = wx.StaticBoxSizer(extras_box, wx.VERTICAL)
        self.cb_extras_list = []
        cb_extras_list = []
        for extras in parent.extras_list:
            cb_extras = wx.CheckBox(extras_box, label=extras, name=extras)
            cb_extras_list.append(cb_extras)
            sizer.Add(cb_extras, flag=wx.ALL, border=0)
            self.cb_extras_list.append(cb_extras)
        self.SetSizer(sizer)


class RoomPanel(wx.Panel):
    def __init__(self, parent, *args, **kwargs):
        wx.Panel.__init__(self, parent, *args, **kwargs)
        self.room_box = wx.RadioBox(self, label="Room",
                                    choices=parent.room_types,
                                    style=wx.RA_SPECIFY_ROWS)
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(self.room_box)
        self.SetSizer(sizer)


class CityPanel(wx.Panel):
    def __init__(self, parent, *args, **kwargs):
        wx.Panel.__init__(self, parent, *args, **kwargs)
        city_box = wx.StaticBox(self, label="Destination")
        sizer = wx.StaticBoxSizer(city_box, wx.HORIZONTAL)
        self.lst_cities = wx.ListBox(self, size=(300, 150), choices=parent.cities)
        sizer.Add(self.lst_cities)
        self.SetSizer(sizer)


class DatePanel(wx.Panel):
    def __init__(self, parent, *args, **kwargs):
        wx.Panel.__init__(self, parent, *args, **kwargs)
        date_box = wx.StaticBox(self, label="Booking date")
        sizer = wx.StaticBoxSizer(date_box, wx.HORIZONTAL)
        self.cmb_day = wx.ComboBox(self, size=(100, -1), choices=parent.days)
        self.cmb_month = wx.ComboBox(self, size=(100, -1), choices=parent.months)
        self.cmb_year = wx.ComboBox(self, size=(100, -1), choices=parent.years)
        sizer.Add(self.cmb_day, flag=wx.ALL, border=10)
        sizer.Add(self.cmb_month, flag=wx.TOP|wx.BOTTOM, border=10)
        sizer.Add(self.cmb_year, flag=wx.ALL, border=10)
        self.SetSizer(sizer)


class ButtonPanel(wx.Panel):
    def __init__(self, parent, *args, **kwargs):
        wx.Panel.__init__(self, parent, *args, **kwargs)
        cmd_clear = wx.Button(self, wx.ID_CLEAR)
        cmd_save = wx.Button(self, wx.ID_SAVE)
        cmd_quit = wx.Button(self, wx.ID_EXIT)

        cmd_clear.Bind(wx.EVT_BUTTON, parent.on_cmd_clear_click)
        cmd_save.Bind(wx.EVT_BUTTON, parent.on_cmd_save_click)
        cmd_quit.Bind(wx.EVT_BUTTON, parent.on_cmd_quit_click)

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(cmd_clear)
        sizer.Add(cmd_save)
        sizer.Add((0, 0), proportion=1)
        sizer.Add(cmd_quit, flag=wx.ALIGN_RIGHT)
        self.SetSizer(sizer)


if __name__ == "__main__":
    SCREEN_APP = wx.App()
    MAIN_FRAME = MainFrame(None, title="Hotel booking")
    SCREEN_APP.MainLoop()
