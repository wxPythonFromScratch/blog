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
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.contact_panel = ContactPanel(self)
        sizer.Add(self.contact_panel, flag=wx.ALL, border=10)
        self.SetSizer(sizer)

    def on_cb_contact_click(self, event):
        del event
        contact_string = ""
        for cb_contact in self.contact_panel.cb_contacts:
            if cb_contact.GetValue():
                contact_string = ", ".join([contact_string, cb_contact.GetName()])
        print("Contact methods: {}".format(contact_string[2:]))

    def on_cmd_cancel_click(self, event):
        del event
        quit()


class ContactPanel(wx.Panel):
    def __init__(self, parent, *args, **kwargs):
        wx.Panel.__init__(self, parent, *args, **kwargs)
        contact_box = wx.StaticBox(self, label="Contact method")
        sizer = wx.StaticBoxSizer(contact_box, wx.HORIZONTAL)
        self.cb_contacts = []
        contacts = ["Home phone", "Mobile", "Email"]
        for contact in contacts:
            cb_contact = wx.CheckBox(contact_box, label=contact, name=contact)
            cb_contact.Bind(wx.EVT_CHECKBOX, parent.on_cb_contact_click)
            sizer.Add(cb_contact, flag=wx.ALL, border=10)
            self.cb_contacts.append(cb_contact)
        self.SetSizer(sizer)

if __name__ == "__main__":
    SCREEN_APP = wx.App()
    MAIN_FRAME = MainFrame(None, title="Frame with StaticBox")
    SCREEN_APP.MainLoop()
