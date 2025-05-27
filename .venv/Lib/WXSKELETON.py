import wx

class MyFrame(wx.Frame):
    def _init_(self):
        super()._init_(parent=None, title='Hello World')
        panel = wx.Panel(self)
        grid = wx.GridSizer(5, 2, 10, 10)

        # text control widget
        grid.Add(wx.TextCtrl(panel, value='initial text'))
        grid.Add(wx.TextCtrl(panel, style=wx.TE_PASSWORD))

        #radiobutton widget
        grid.Add(wx.RadioButton(panel, label='Male',style=wx.RB_GROUP))
        grid.Add(wx.RadioButton(panel, label='Female'))

        #STATICTEXT widget
        grid.Add(wx.StaticText(panel, label="Enter your name:"))

        #checkbox widget
        grid.Add(wx.CheckBox(panel, label="Black"))

        #combobox widget
        items=["Apple", "Rice", "Cheese cake"]
        grid.Add(wx.ComboBox(panel, choices= items))

        #slider widget
        grid.Add(wx.Slider(panel, value= 50, minValue=0, maxValue=100))

        # button widget
        grid.Add(wx.Button(panel, label='Press Me'))

        panel.SetSizer(grid)
        self.Show()

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()