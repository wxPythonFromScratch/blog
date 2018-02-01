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
        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        contact_sizer = self.create_contact_sizer()
        sizer.Add(contact_sizer, flag=wx.ALL, border=10)
        self.SetSizer(sizer)

    def on_cb_contact_click(self, event):
        del event
        contact_string = ""
        for cb_contact in self.cb_contacts:
            if cb_contact.GetValue():
                contact_string = ", ".join([contact_string, cb_contact.GetName()])
        print("Contact methods: {}".format(contact_string[2:]))

    def on_cmd_cancel_click(self, event):
        del event
        quit()

    def create_contact_sizer(self):
        contact_box = wx.StaticBox(parent=self, label="Contact method")
        sizer = wx.StaticBoxSizer(box=contact_box, orient=wx.HORIZONTAL)
        self.cb_contacts = []
        contacts = ["Home phone", "Mobile", "Email"]
        for contact in contacts:
            cb_contact = wx.CheckBox(parent=contact_box, label=contact, name=contact)
            cb_contact.Bind(wx.EVT_CHECKBOX, self.on_cb_contact_click)
            sizer.Add(cb_contact, flag=wx.ALL, border=10)
            self.cb_contacts.append(cb_contact)
        return sizer

if __name__ == "__main__":
    SCREEN_APP = wx.App()
    MAIN_FRAME = MainFrame(parent=None, title="Frame with StaticBox")
    SCREEN_APP.MainLoop()
