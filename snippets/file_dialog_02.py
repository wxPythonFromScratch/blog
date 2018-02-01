import wx
import os


class MainFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        panel = MainPanel(self)
        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        sizer.Add(panel)
        self.SetSizerAndFit(sizer)
        self.Show()


class MainPanel(wx.Panel):
    def __init__(self, parent, *args, **kwargs):
        wx.Panel.__init__(self, parent, *args, **kwargs)
        self.path = "/home/jeff/"

        path_sizer = self.create_path_sizer()
        button_sizer = self.create_button_sizer()

        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        sizer.Add(path_sizer, flag=wx.ALL, border=10)
        sizer.Add(button_sizer, flag=wx.LEFT|wx.RIGHT|wx.BOTTOM|wx.EXPAND, border=10)
        self.SetSizer(sizer)

    def on_cmd_path_click(self, event):
        del event
        self.path = self.get_file_path()
        self.txt_path.SetValue(self.path)

    def on_cmd_quit_click(self, event):
        del event
        quit()

    def create_path_sizer(self):
        lbl_path = wx.StaticText(parent=self, label="Path:")
        self.txt_path = wx.TextCtrl(parent=self, size=(300, -1))
        cmd_path = wx.Button(parent=self, id=wx.ID_OPEN)
        cmd_path.Bind(wx.EVT_BUTTON, self.on_cmd_path_click)

        sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        sizer.Add(lbl_path, flag=wx.RIGHT, border=10)
        sizer.Add(self.txt_path, flag=wx.RIGHT, border=10)
        sizer.Add(cmd_path)
        return sizer

    def create_button_sizer(self):
        cmd_quit = wx.Button(parent=self, id=wx.ID_EXIT)
        cmd_quit.Bind(wx.EVT_BUTTON, self.on_cmd_quit_click)
        sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        sizer.Add((0, 0), proportion=1)
        sizer.Add(cmd_quit)
        return sizer

    def get_file_path(self):
        path = self.path
        file_types = 'txt files (*.txt)| All files (*.*)|*.*|'
        file_dialog = wx.FileDialog(parent=self,
                                    message = 'Open file',
                                    defaultDir=os.path.dirname(path),
                                    defaultFile=os.path.basename(path),
                                    wildcard=file_types,
                                    style=wx.FD_OPEN)
        if file_dialog.ShowModal() == wx.ID_OK:
            path = file_dialog.GetPath()
        else:
            path = ''
        file_dialog.Destroy()
        return path

if __name__ == "__main__":
    SCREEN_APP = wx.App()
    MAIN_FRAME = MainFrame(parent=None, title="Open file dialog")
    SCREEN_APP.MainLoop()
