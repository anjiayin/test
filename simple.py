#----------------------------------------------------------------------
# A very simple wxPython example.  Just a wx.Frame, wx.Panel,
# wx.StaticText, wx.Button, and a wx.BoxSizer, but it shows the basic
# structure of any wxPython application.
#----------------------------------------------------------------------

import wx

USE_WIT = False

AppBaseClass = wx.App
if USE_WIT:
    from wx.lib.mixins.inspection import InspectableApp
    AppBaseClass = InspectableApp


class MyFrame(wx.Frame):
    """
    This is MyFrame.  It just shows a few controls on a wxPanel,
    and has a simple menu.
    """
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, -1, title, size=(800,200), pos=(200,200))

        # Create the menubars
        menuBar = wx.MenuBar()

        # and a menu
        menu = wx.Menu()

        # add an item to the menu, using \tKeyName automatically
        # creates an accelerator, the third param is some help text
        # that will show up in the statusbar
        menu.Append(wx.ID_EXIT, "E&xit\tAlt-X", "Exit this simple sample")

        # bind the menu event to an event handler
        self.Bind(wx.EVT_MENU, self.OnTimeToClose, id=wx.ID_EXIT)

        # and put the menu on the menubar
        menuBar.Append(menu, "&File")
        self.SetMenuBar(menuBar)

        self.CreateStatusBar()


        # Now create the Panel to put the other controls on.
        panel = wx.Panel(self)

        # and a few controls
        text = wx.StaticText(panel, -1, "欢迎使用车车数据提供的微信助手")
        text.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD))
        #text.SetSize(text.GetBestSize())
        btnConfigKey = wx.Button(panel, -1, "配置Key")

        # bind the button events to handlers
        self.Bind(wx.EVT_BUTTON, self.OnClickConfigKey, btnConfigKey)

        # Use a sizer to layout the controls, stacked vertically and with
        # a 10 pixel border around each
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(text, 0, wx.ALL, 10)
        sizer.Add(btnConfigKey, 0, wx.ALL, 10)
        panel.SetSizer(sizer)
        panel.Layout()

        # And also use a sizer to manage the size of the panel such
        # that it fills the frame
        sizer = wx.BoxSizer()
        sizer.Add(panel, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.Fit()
        self.CenterOnScreen(wx.BOTH)

    def OnClickConfigKey(self, evt):
        print("配置Key")


    def OnTimeToClose(self, evt):
        """Event handler for the button click."""
        print("See ya later!")
        self.Close()


class MyApp(AppBaseClass):
    def OnInit(self):
        frame = MyFrame(None, "车车数据微信助手")
        self.SetTopWindow(frame)

        print("Print statements go to this stdout window by default.")
        if USE_WIT:
            print("Press Ctrl-Alt-I (Cmd-Opt-I on Mac) to launch the WIT.")
            self.InitInspection()

        frame.Show(True)
        return True

app = MyApp(redirect=False)
app.MainLoop()

