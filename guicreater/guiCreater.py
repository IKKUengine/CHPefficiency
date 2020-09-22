
from tkinter import *
from connections import internetConnection
from datacollector import gpsModul
from datacollector import temperatureSensor
from datacollector import weatherServer
import parameter
import time

class Gui(Frame):
    textPower = 'Hallo GenLab!'
    textSignal = 'Hallo GenLab!'
    textFeedback = 'Server Feedback!'

    def __init__(self):
        self.cloudConnection = internetConnection.CloudConnection()
        self.weather = weatherServer.Weather(self.cloudConnection)
        self.temperatureInside = temperatureSensor.TemperatureSensor(self.cloudConnection)        
        self.gpsData = gpsModul.GpsModul(self.cloudConnection)
        # subject.notify_observers('done')
        # GUI Init
        # self.requestPowerAnalyzer()
        master = Tk()
        menu_bar = Menu(master)
        self.infoText = Label(master, text=self.textPower, fg="red")
        self.infoText.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.signalText = Label(master, text=self.textSignal, bg="yellow")
        self.signalText.place(relx=0.99, rely=0.001, anchor=NE)
        self.textFeedback = Label(master, text=self.textFeedback, fg="blue")
        self.textFeedback.place(relx=0.8, rely=0.001, anchor=NE)
 
        main_menu = Menu(menu_bar, tearoff=0)
        measure_menu = Menu(menu_bar, tearoff=0)
        controlling_menu = Menu(menu_bar, tearoff=0)
        measure_menu.add_command(label="Stop Measure", command=self.stopMeasure)
        measure_menu.add_command(label="Start Measure", command=self.startMeasure)
        #measure_menu.add_command(label="Stop Transfer", command=self.netConn.setStop)
        #measure_menu.add_command(label="Start Transfer", command=self.netConn.setStart)
        #controlling_menu.add_command(label="On/Off CHP", command=self.relais.setGPIOPinOnOff)
        main_menu.add_command(label="Quit", command=master.destroy)
        
        self.label = Label(master, text = "IP-Address Server:")
        self.label.grid(row = 0, column = 0, sticky = W,  padx = 5, pady = 30)
        
        self.entry = Entry(master)
        self.entry.grid(row = 1, column = 0, sticky = W,  padx = 5, pady = 5)
        self.entry.focus_set()
        #self.entry.insert(0, self.cloudConnection.getIP())
        
        self.button = Button(master, text="Set Server IP", command =self.connect)
        self.button.grid(row = 2, column = 0, sticky = W, padx = 5, pady = 5)

        menu_bar.add_cascade(label="Menu", menu=main_menu)
        menu_bar.add_cascade(label="Measurement", menu=measure_menu)
        menu_bar.add_cascade(label="Controlling", menu=controlling_menu)
        master.config(menu=menu_bar)
        if parameter.fullscreen:
            master.attributes('-fullscreen', True)
        Frame.__init__(self, master)
        
    def connect(self):
        ipAddr = self.entry.get()
        
        try:
            #self.cloudConnection.setIP(ipAddr)
            #print (ipAddr)
            pass
        except:
            if parameter.printMessages:
                print ("Please switch on the Server-App!")
            self.messageServer = "NO SERVER CONNECTED!"
            print("NO SERVER CONNECTED!")


    def stopMeasure(self):
        self.weather.setStop()
        self.temperatureInside.setStop()
        self.gpsData.setStop()
        
    def startMeasure(self):
        self.weather.setStart()
        self.temperatureInside.setStart()
        self.gpsData.setStart()
        
    def __exit__(self):
        self.temperatureInside.setExit()
        self.temperatureInside.__exit__()
        self.weather.setExit()
        self.gpsData.setExit()
        self.cloudConnection.setExit()
        self.cloudConnection.__exit__()
        pass
        
    def visualizationData(self):
        self.infoText['text'] = self.adaptDataList()
        self.signalText['text'] = self.cloudConnection.getMessageServer()
        self.textFeedback['text'] = self.cloudConnection.getFeedback()
        self.after(parameter.timeTriggervisualData, self.visualizationData)
        
    def adaptDataList(self):
        
        adaptData = "Fernando at home!"
        #adaptData = "{}\n{}\n\n{}\n{}\n\n{}\n{}\n\n{}\n{}\n\n{}\n{}\n\n{}\n{}".format(self.temperatureInside.getHeader(), self.weather.getData(), self.gpsData.getHeader(), self.relais.getData(), self.massFlow.getHeader(), self.massFlow.getData(), self.heatMeaters.getHeader1(), self.heatMeaters.getData1(), self.heatMeaters.getHeader2(), self.heatMeaters.getData2(), self.heatMeaters.getHeader3(), self.heatMeaters.getData3())
        return adaptData
    
    def switchOffHysteresis(self):
        #if  self.heatMeater1.getTreturn() >= parameter.switchOffMaxT and self.relais.getCHPOnOffStatus() == 1:
        #    self.relais.setRelaisCHPOff()
        #if self.heatMeater1.getTreturn() <= parameter.switchOffMinT and self.relais.getCHPOnOffStatus() == 0:
        #    self.relais.setRelaisCHPOn()
        self.after( 100, self.switchOffHysteresis)
        

