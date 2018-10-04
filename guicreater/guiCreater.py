
from tkinter import *
from connections import networkConnection as etaNet
from datacollector import powerAnalyzer

class Gui(Frame):
    # Members
    textPower = 'Hallo IKKUengine!'
    textSignal = ''

    def __init__(self):
        self.subject = etaNet.NetworkConnection('', 5006)
        self.powerAn = powerAnalyzer.PowerAnalyzer(self.subject)
        # subject.notify_observers('done')
        # GUI Init
        # self.requestPowerAnalyzer()
        master = Tk()
        menu_bar = Menu(master)
        self.infoText = Label(master, text=self.textPower, fg="red")
        self.infoText.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.signalText = Label(master, text=self.textSignal, bg="yellow")
        self.signalText.place(relx=0.99, rely=0.001, anchor=NE)
        Button(master, text='Datan abholen', width=20, command=self.subject.notify_observers).place(relx=0.2, rely=0.98,anchor=SE)
        Button(master, text='PA Messen beenden', width=20, command=self.powerAn.setStop).place(relx=0.8, rely=0.98, anchor=SE)
        Button(master, text='PA Messen starten', width=20, command=self.powerAn.setStart).place(relx=0.5, rely=0.98, anchor=SE)
        Button(master, text='Schließen', width=20, command=master.destroy).place(relx=0.98, rely=0.98, anchor=SE)

        main_menu = Menu(menu_bar, tearoff=0)
        measure_menu = Menu(menu_bar, tearoff=0)
        controlling_menu = Menu(menu_bar, tearoff=0)
        # measure_menu.add_command(label="Power Analyzer", command=window.requestPowerAnalyzer)
        # measure_menu.add_command(label="Gas Mass Flow", command=window.requestGasMassFlow)
        # measure_menu.add_command(label="Heat Meter 1", command=self.requestHeatMeterHeatingWater)
        # measure_menu.add_command(label="Heat Meter 2", command=window.requestHeatMeterHotWater)
        # measure_menu.add_command(label="Weather Data", command=self.requestWeatherData)
        # measure_menu.add_command(label="Time/Date", command=self.requestTimeDate)
        #controlling_menu.add_command(label="On/Off CHP", command=self.setOnOffCHP)
        #main_menu.add_command(label="Save Data", command=self.saveData)
        main_menu.add_command(label="Quit", command=master.destroy)

        menu_bar.add_cascade(label="Menu", menu=main_menu)
        menu_bar.add_cascade(label="Single Measurement", menu=measure_menu)
        menu_bar.add_cascade(label="Controlling", menu=controlling_menu)
        master.config(menu=menu_bar)
        #master.attributes('-fullscreen', True)
        Frame.__init__(self, master)

    def __exit__(self):
        self.powerAn.setExit()
        self.subject.__exit__()