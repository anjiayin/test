#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'anjiayin'
import wx
import wx.adv


class MyTaskBarIcon(wx.adv.TaskBarIcon):
    ICON = "logo.ico"  # 图标地址
    ID_ABOUT = wx.NewId()  # 菜单选项“关于”的ID
    ID_EXIT = wx.NewId()  # 菜单选项“退出”的ID
    ID_CONFIG_KEY = wx.NewId()  # 菜单选项“显示页面”的ID
    TITLE = "车车数据微信助手" #鼠标移动到图标上显示的文字
    

    def __init__(self):
        wx.adv.TaskBarIcon.__init__(self)
        self.SetIcon(wx.Icon(self.ICON), self.TITLE)  # 设置图标和标题
        self.Bind(wx.EVT_MENU, self.onAbout, id=self.ID_ABOUT)  # 绑定“关于”选项的点击事件
        self.Bind(wx.EVT_MENU, self.onExit, id=self.ID_EXIT)  # 绑定“退出”选项的点击事件
        self.Bind(wx.EVT_MENU, self.onConfigKey, id=self.ID_CONFIG_KEY)  # 绑定“显示页面”选项的点击事件
        self.mainFrame = MainFrame(None, self.TITLE)
    # “关于”选项的事件处理器
    def onAbout(self, event):
        wx.MessageBox('我的车车（北京）网络技术有限公司', "关于")

    # “退出”选项的事件处理器
    def onExit(self, event):
        wx.Exit()

    # “配置Key”选项的事件处理器
    def onConfigKey(self, event):
        if(isinstance(self.mainFrame, MainFrame)):
            self.mainFrame.Show(True)
        else:
            self.mainFrame = MainFrame(None, self.TITLE)
            self.mainFrame.Show(True)
        return

    # 创建菜单选项
    def CreatePopupMenu(self):
        menu = wx.Menu()
        for mentAttr in self.getMenuAttrs():
            menu.Append(mentAttr[1], mentAttr[0])
        return menu

    # 获取菜单的属性元组
    def getMenuAttrs(self):
        return [('配置Key', self.ID_CONFIG_KEY),
                ('关于', self.ID_ABOUT),
                ('退出', self.ID_EXIT)]


class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self)
        MyTaskBarIcon()#显示系统托盘图标

class MainFrame(wx.Frame):
    """
    This is MyFrame.  It just shows a few controls on a wxPanel,
    and has a simple menu.
    """
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, -1, title, (10,10), (600,400))

        # Create the menubar
        menuBar = wx.MenuBar()

        # and a menu
        menu = wx.Menu()

        # add an item to the menu, using \tKeyName automatically
        # creates an accelerator, the third param is some help text
        # that will show up in the statusbar
        menu.Append(wx.ID_EXIT, "退出", "退出配置界面")

        # bind the menu event to an event handler
        self.Bind(wx.EVT_MENU, self.OnTimeToClose, id=wx.ID_EXIT)

        # and put the menu on the menubar
        menuBar.Append(menu, "菜单")
        self.SetMenuBar(menuBar)

        self.CreateStatusBar()


        # Now create the Panel to put the other controls on.
        panel = wx.Panel(self)

        # and a few controls
        text = wx.StaticText(panel, -1, "请输入Key")
        text.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD))
        text.SetSize(text.GetBestSize())
        self.mKey = wx.TextCtrl(panel)
        self.mKey.SetFocus()
        btnConfigKey = wx.Button(panel, -1, "保存")



        # bind the button events to handlers
        self.Bind(wx.EVT_BUTTON, self.OnClickConfigKey, btnConfigKey)

        # bind the frame close events 
        self.Bind(wx.EVT_CLOSE, self.CLOSE)

        # bind the frame iconize events 
        self.Bind(wx.EVT_ICONIZE, self.ICONIZE)

        # Use a sizer to layout the controls, stacked vertically and with
        # a 10 pixel border around each
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(text, 0, wx.ALL, 10)
        sizer.Add(self.mKey, 0, wx.ALL, 10)
        sizer.Add(btnConfigKey, 0, wx.ALL, 10)
        panel.SetSizer(sizer)
        panel.Layout()

        # And also use a sizer to manage the size of the panel such
        # that it fills the frame
        #sizer = wx.BoxSizer()
        #sizer.Add(panel, 1, wx.EXPAND)
        #self.SetSizer(sizer)
        #self.Fit()
        self.CenterOnScreen(wx.BOTH)

    def OnClickConfigKey(self, evt):
        print("配置Key")


    def OnTimeToClose(self, evt):
        """Event handler for the button click."""
        print("点击了菜单中的退出")
        self.Hide()
    
    def CLOSE(self, evt):
        print("点击了窗口关闭")
        self.Hide()
        return False

    def ICONIZE(self, evt):
        print("点击了窗口最小化按钮")
        evt.Skip()
        self.Hide()
        return False

class MyApp(wx.App):
    def OnInit(self):
        self.myFrame = MyFrame()
    #    self.mainFram = MainFram(None, "车车数据微信助手")
        return True


if __name__ == "__main__":
    app = MyApp(redirect=False)
    app.MainLoop()
