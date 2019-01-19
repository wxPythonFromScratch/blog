"""Demonstrate the use of wxPython in a larger application."""


from datetime import datetime
import wx


class MainFrame(wx.Frame):
    """Create and show the frame for the application."""
    def __init__(self, *args, **kwargs):
        """Initialise the MainFrame class."""
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
        file_menu = self.create_file_menu()
        help_menu = self.create_help_menu()
        self.Append(file_menu, '&File')
        self.Append(help_menu, '&Help')

    def create_file_menu(self):
        menu = wx.Menu()
        clear_menu_item = wx.MenuItem(parentMenu=menu, id=wx.ID_CLEAR)
        save_menu_item = wx.MenuItem(parentMenu=menu, id=wx.ID_SAVE)
        quit_menu_item = wx.MenuItem(parentMenu=menu, id=wx.ID_EXIT)
        menu.Append(clear_menu_item)
        menu.Append(save_menu_item)
        menu.Append(quit_menu_item)
        return menu

    def create_help_menu(self):
        help_menu = wx.Menu()
        return help_menu


class MainPanel(wx.Panel):
    """Create a panel to hold application widgets."""
    def __init__(self, parent, *args, **kwargs):
        """Initialise the MainPanel class."""
        super(MainPanel, self).__init__(parent, *args, **kwargs)
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

        person_sizer = self.create_person_sizer()
        extras_sizer = self.create_extras_sizer()
        room_sizer = self.create_room_sizer()
        city_sizer = self.create_city_sizer()
        date_sizer = self.create_date_sizer()
        button_sizer = self.create_button_sizer()

        preferences_sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        preferences_sizer.Add(extras_sizer, flag=wx.RIGHT, border=10)
        preferences_sizer.Add(room_sizer)
        sizer = wx.GridBagSizer(10, 10)
        sizer.Add(person_sizer, pos=(0, 0), flag=wx.TOP|wx.LEFT, border=10)
        sizer.Add(preferences_sizer, pos=(0, 1), flag=wx.TOP, border=10)
        sizer.Add(city_sizer, pos=(1, 0), flag=wx.LEFT, border=10)
        sizer.Add(date_sizer, pos=(1, 1), flag=wx.RIGHT, border=10)
        sizer.Add(button_sizer, pos=(2, 0), span=(1, 2),
                  flag=wx.LEFT|wx.BOTTOM|wx.RIGHT|wx.EXPAND,
                  border=10)
        self.SetSizer(sizer)
        self.clear_controls()

    def clear_controls(self):
        """Reset all controls to their default values."""
        self.txt_first_name.SetValue('')
        self.txt_last_name.SetValue('')
        self.txt_email.SetValue('')
        for cb_extra in self.cb_extras_list:
            cb_extra.SetValue(False)
        self.room_box.SetSelection(0)
        self.lst_cities.SetSelection(0)
        self.lst_cities.SetSelection(-1)
        self.cmb_day.SetValue('Day')
        self.cmb_month.SetValue('Month')
        self.cmb_year.SetValue('Year')

    def on_cmd_clear_click(self, event):
        """Handle the cmd_clear click event."""
        del event
        self.clear_controls()

    def on_cmd_save_click(self, event):
        """Print the values of all controls."""
        del event
        print('First name: %s' % self.txt_first_name.GetValue())
        print('Last name: %s' % self.txt_first_name.GetValue())
        print('Email: %s' % self.txt_first_name.GetValue())
        for index, cb_extra in enumerate(self.cb_extras_list):
            print(self.extras_list[index]+': %s' % str(cb_extra.GetValue()))
        print('Room type: %s' % self.room_types[self.room_box.GetSelection()])
        print('City: %s' % self.cities[self.lst_cities.GetSelection()])
        date_string = 'Date: {day} {month} {year}'
        print(date_string.format(day=self.cmb_day.GetValue(),
                                 month=self.cmb_month.GetValue(),
                                 year=self.cmb_year.GetValue()))
        print('----------------')
        self.clear_controls()

    @staticmethod
    def on_cmd_quit_click(event):
        """Tear down processes and quit the application."""
        del event
        quit()

    def create_person_sizer(self):
        """Return a sizer containing all controls relating to personal details."""
        lbl_first_name = wx.StaticText(parent=self, label="First name")
        lbl_last_name = wx.StaticText(parent=self, label="Last name")
        lbl_email = wx.StaticText(parent=self, label="Email")
        self.txt_first_name = wx.TextCtrl(parent=self, size=(150, -1))
        self.txt_last_name = wx.TextCtrl(parent=self, size=(150, -1))
        self.txt_email = wx.TextCtrl(parent=self, size=(250, -1))
        sizer = wx.GridBagSizer(5, 5)
        sizer.Add(lbl_first_name, pos=(0, 0))
        sizer.Add(lbl_last_name, pos=(1, 0))
        sizer.Add(lbl_email, pos=(2, 0))
        sizer.Add(self.txt_first_name, pos=(0, 1))
        sizer.Add(self.txt_last_name, pos=(1, 1))
        sizer.Add(self.txt_email, pos=(2, 1))
        return sizer

    def create_extras_sizer(self):
        """Return a sizer containing all controls relating to extras details."""
        extras_box = wx.StaticBox(parent=self, label="Extras")
        sizer = wx.StaticBoxSizer(box=extras_box, orient=wx.VERTICAL)
        self.cb_extras_list = []
        for extras in self.extras_list:
            cb_extras = wx.CheckBox(parent=extras_box, label=extras, name=extras)
            sizer.Add(cb_extras, flag=wx.ALL, border=0)
            self.cb_extras_list.append(cb_extras)
        return sizer

    def create_room_sizer(self):
        """Return a sizer containing all controls relating to room details."""
        self.room_box = wx.RadioBox(parent=self, label="Room",
                                    choices=self.room_types,
                                    style=wx.RA_SPECIFY_ROWS)
        sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        sizer.Add(self.room_box)
        return sizer

    def create_city_sizer(self):
        """Return a sizer containing all controls relating to city selection."""
        city_box = wx.StaticBox(parent=self, label="Destination")
        sizer = wx.StaticBoxSizer(box=city_box, orient=wx.HORIZONTAL)
        self.lst_cities = wx.ListBox(parent=self, size=(300, 150), choices=self.cities)
        sizer.Add(self.lst_cities)
        return sizer

    def create_date_sizer(self):
        """Return a sizer containing all controls relating to date selection."""
        date_box = wx.StaticBox(parent=self, label="Booking date")
        sizer = wx.StaticBoxSizer(box=date_box, orient=wx.HORIZONTAL)
        self.cmb_day = wx.ComboBox(parent=self, size=(100, -1), choices=self.days)
        self.cmb_month = wx.ComboBox(parent=self, size=(100, -1), choices=self.months)
        self.cmb_year = wx.ComboBox(parent=self, size=(100, -1), choices=self.years)
        sizer.Add(self.cmb_day, flag=wx.ALL, border=10)
        sizer.Add(self.cmb_month, flag=wx.TOP|wx.BOTTOM, border=10)
        sizer.Add(self.cmb_year, flag=wx.ALL, border=10)
        return sizer

    def create_button_sizer(self):
        """Return a sizer containing the main buttons."""
        cmd_clear = wx.Button(parent=self, id=wx.ID_CLEAR)
        cmd_save = wx.Button(parent=self, id=wx.ID_SAVE)
        cmd_quit = wx.Button(parent=self, id=wx.ID_EXIT)

        cmd_clear.Bind(wx.EVT_BUTTON, self.on_cmd_clear_click)
        cmd_save.Bind(wx.EVT_BUTTON, self.on_cmd_save_click)
        cmd_quit.Bind(wx.EVT_BUTTON, self.on_cmd_quit_click)

        sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        sizer.Add(cmd_clear)
        sizer.Add(cmd_save)
        sizer.Add((0, 0), proportion=1)
        sizer.Add(cmd_quit, flag=wx.ALIGN_RIGHT)
        return sizer


if __name__ == "__main__":
    """Implement the wxPython loop."""
    SCREEN_APP = wx.App()
    MAIN_FRAME = MainFrame(parent=None, title="Hotel booking")
    SCREEN_APP.MainLoop()
