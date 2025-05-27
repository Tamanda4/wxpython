import wx

class MyFrame(wx.Frame):
    def _init_(self):
        super()._init_(parent=None, title='Hello World')
        panel = wx.Panel(self)
        fgs=wx.FlexGridSizer(rows=5,cols=2,hgap=5,vgap=5)

        # text control widget
        fgs.Add(wx.TextCtrl(panel, value='initial text'))
        fgs.Add(wx.TextCtrl(panel, style=wx.TE_PASSWORD))

        #radiobutton widget
        fgs.Add(wx.RadioButton(panel, label='Male',style=wx.RB_GROUP))
        fgs.Add(wx.RadioButton(panel, label='Female'))

        #STATICTEXT widget
        fgs.Add(wx.StaticText(panel, label="Enter your name:"))

        #checkbox widget
        fgs.Add(wx.CheckBox(panel, label="Black"))

        #combobox widget
        items=["Apple", "Rice", "Cheese cake"]
        fgs.Add(wx.ComboBox(panel, choices= items))

        #slider widget
        fgs.Add(wx.Slider(panel, value= 50, minValue=0, maxValue=100))

        # button widget
        fgs.Add(wx.Button(panel, label='Press Me'))

        panel.SetSizer(fgs)
        self.Show()

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()