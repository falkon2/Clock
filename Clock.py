
from time import strftime
from tkinter import ttk,messagebox
from tkinter import *
from datetime import datetime
import pytz
import time


root = Tk()
root.title("Clock")
root.geometry("498x608")

def International_time():
    #timezone list: https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568
    countries = [
        #African cities
        'Lagos',
        'Kinshasa',
        'Cairo',
        'Khartoum',
        #South American cities
        'Buenos_Aires',
        'Salta',
        #American cities
        'Los Angeles',
        'Mexico City',
        'New York',
        #Asian cities
        'Bangkok',
        'Calcutta',
        'Dacca',
        'Dubai',
        'Gaza',
        'Hong Kong',
        'Kabul',
        'Kolkata',
        'Kuwait',
        'Qatar',
        'Seoul',
        'Shanghai',
        'Singapore',
        'Tokyo',
        'Hong Kong',
        # OCE cities
        'Melbourne',
        'Perth',
        'Queensland',
        'Sydney',
        #European cities
        'Greenwich',
        'Amsterdam',
        'Berlin',
        'Dublin',
        'Kiev',
        'London',
        'Luxembourg',
        'Madrid',
        'Moscow',
        'Rome',
        ]
    def destroy():
        question = messagebox.askquestion('exit','Are you sure?')
        if question == 'yes':
            root.destroy()    
    def Search():
        time = International_countries_time.get()
        print(time)
            
        match time:
            case('Lagos'):
                time = datetime.now(pytz.timezone('Africa/Lagos'))
                display = time.strftime("%D, %H:%M:%S")
                print(display)
                mylabel2.config(text=display)
                mylabel2.after(1000,Search)
            case('Kinshasa'):
                time = datetime.now(pytz.timezone('Africa/Kinshasa'))
                display = time.strftime("%D, %H:%M:%S")
                print(display)
                mylabel2.config(text=display)
                mylabel2.after(1000,Search)
            case('Cairo'):
                time = datetime.now(pytz.timezone('Africa/Cairo'))
                display = time.strftime("%D, %H:%M:%S")
                print(display)
                mylabel2.config(text=display)
                mylabel2.after(1000,Search)
            case('Khartoum'):
                time = datetime.now(pytz.timezone('Africa/Khartoum'))
                display = time.strftime("%D, %H:%M:%S")
                print(display)
                mylabel2.config(text=display)
                mylabel2.after(1000,Search)
            case('Buenos_Aires'):
                time = datetime.now(pytz.timezone('America/Argentina/Buenos_Aires'))
                display = time.strftime("%D, %H:%M:%S")
                print(display)
                mylabel2.config(text=display)
                mylabel2.after(1000,Search)
            case('Salta'):
                time = datetime.now(pytz.timezone('America/Argentina/Salta'))
                display = time.strftime("%D, %H:%M:%S")
                print(display)
                mylabel2.config(text=display)
                mylabel2.after(1000,Search)
            case('Los Angeles'):
                time = datetime.now(pytz.timezone('America/Los_Angeles'))
                display = time.strftime("%D, %H:%M:%S")
                print(display)
                mylabel2.config(text=display)
                mylabel2.after(1000,Search)
            case('Mexico City'):
                time = datetime.now(pytz.timezone('America/Mexico_City'))
                display = time.strftime("%D, %H:%M:%S")
                print(display)
                mylabel2.config(text=display)
                mylabel2.after(1000,Search)
            case('New York'):
                time = datetime.now(pytz.timezone('America/New_York'))
                display = time.strftime("%D, %H:%M:%S")
                print(display)
                mylabel2.config(text=display)
                mylabel2.after(1000,Search)
            case('Bangkok'):
                time = datetime.now(pytz.timezone('Asia/Bangkok'))
                display = time.strftime("%D, %H:%M:%S")
                print(display)
                mylabel2.config(text=display)
                mylabel2.after(1000,Search)
            case('Calcutta'):
                time = datetime.now(pytz.timezone('Asia/Calcutta'))
                display = time.strftime("%D, %H:%M:%S")
                print(display)
                mylabel2.config(text=display)
                mylabel2.after(1000,Search)
            case('Dacca'):
                time = datetime.now(pytz.timezone('Asia/Dacca'))
                display = time.strftime("%D, %H:%M:%S")
                print(display)
                mylabel2.config(text=display)
                mylabel2.after(1000,Search)
            case('Dubai'):
                time = datetime.now(pytz.timezone('Asia/Dubai'))
                display = time.strftime("%D, %H:%M:%S")
                print(display)
                mylabel2.config(text=display)
                mylabel2.after(1000,Search)
            case('Gaza'):
                time = datetime.now(pytz.timezone('Asia/Gaza'))
                display = time.strftime("%D, %H:%M:%S")
                print(display)
                mylabel2.config(text=display)
                mylabel2.after(1000,Search)
            case('Hong Kong'):
                time = datetime.now(pytz.timezone('Asia/Hong_Kong'))
                display = time.strftime("%D, %H:%M:%S")
                print(display)
                mylabel2.config(text=display)
                mylabel2.after(1000,Search)
            case('Kabul'):
                time = datetime.now(pytz.timezone('Asia/Kabul'))
                display = time.strftime("%D, %H:%M:%S")
                print(display)
                mylabel2.config(text=display)
                mylabel2.after(1000,Search)
            case('Kolkata'):
                time = datetime.now(pytz.timezone('Asia/Kolkata'))
                display = time.strftime("%D, %H:%M:%S")
                print(display)
                mylabel2.config(text=display)
                mylabel2.after(1000,Search)
            case('Kuwait'):
                time = datetime.now(pytz.timezone('Asia/Kuwait'))
                display = time.strftime("%D, %H:%M:%S")
                print(display)
                mylabel2.config(text=display)
                mylabel2.after(1000,Search)
            case('Qatar'):
                time = datetime.now(pytz.timezone('Asia/Qatar'))
                display = time.strftime("%D, %H:%M:%S")
                print(display)
                mylabel2.config(text=display)
                mylabel2.after(1000,Search)
            case('Seoul'):
                time = datetime.now(pytz.timezone('Asia/Seoul'))
                display = time.strftime("%D, %H:%M:%S")
                print(display)
                mylabel2.config(text=display)
                mylabel2.after(1000,Search)
            case('Shanghai'):
                time = datetime.now(pytz.timezone('Asia/Shanghai'))
                display = time.strftime("%D, %H:%M:%S")
                print(display)
                mylabel2.config(text=display)
                mylabel2.after(1000,Search)
            case('Singapore'):
                time = datetime.now(pytz.timezone('Asia/Singapore'))
                display = time.strftime("%D, %H:%M:%S")
                print(display)
                mylabel2.config(text=display)
                mylabel2.after(1000,Search)
            case('Tokyo'):
                time = datetime.now(pytz.timezone('Asia/Kabul'))
                display = time.strftime("%D, %H:%M:%S")
                print(display)
                mylabel2.config(text=display)
                mylabel2.after(1000,Search)
            case('Hong Kong'):
                time = datetime.now(pytz.timezone('Asia/Hong_Kong'))
                display = time.strftime("%D, %H:%M:%S")
                print(display)
                mylabel2.config(text=display)
                mylabel2.after(1000,Search)
            case('Melbourne'):
                time = datetime.now(pytz.timezone('Australia/Melbourne'))
                display = time.strftime("%D, %H:%M:%S")
                print(display)
                mylabel2.config(text=display)
                mylabel2.after(1000,Search)
            case('Perth'):
                time = datetime.now(pytz.timezone('Australia/Perth'))
                display = time.strftime("%D, %H:%M:%S")
                print(display)
                mylabel2.config(text=display)
                mylabel2.after(1000,Search)
            case('Queensland'):
                time = datetime.now(pytz.timezone('Australia/Queensland'))
                display = time.strftime("%D, %H:%M:%S")
                print(display)
                mylabel2.config(text=display)
                mylabel2.after(1000,Search)
            case('Sydney'):
                time = datetime.now(pytz.timezone('Australia/Sydney'))
                display = time.strftime("%D, %H:%M:%S")
                print(display)
                mylabel2.config(text=display)
                mylabel2.after(1000,Search)
            case('Greenwich'):
                time = datetime.now(pytz.timezone('Greenwich'))
                display = time.strftime("%D, %H:%M:%S")
                print(display)
                mylabel2.config(text=display)
                mylabel2.after(1000,Search)
            case('Berlin'):
                time = datetime.now(pytz.timezone('Europe/Berlin'))
                display = time.strftime("%D, %H:%M:%S")
                print(display)
                mylabel2.config(text=display)
                mylabel2.after(1000,Search)
            case('Amsterdam'):
                time = datetime.now(pytz.timezone('Europe/Amsterdam'))
                display = time.strftime("%D, %H:%M:%S")
                print(display)
                mylabel2.config(text=display)
                mylabel2.after(1000,Search)
            case('Dublin'):
                time = datetime.now(pytz.timezone('Europe/Dublin'))
                display = time.strftime("%D, %H:%M:%S")
                print(display)
                mylabel2.config(text=display)
                mylabel2.after(1000,Search)
            case('Kiev'):
                time = datetime.now(pytz.timezone('Europe/Kiev'))
                display = time.strftime("%D, %H:%M:%S")
                print(display)
                mylabel2.config(text=display)
                mylabel2.after(1000,Search)
            case('London'):
                time = datetime.now(pytz.timezone('Europe/London'))
                display = time.strftime("%D, %H:%M:%S")
                print(display)
                mylabel2.config(text=display)
                mylabel2.after(1000,Search)
            case('Luxembourg'):
                time = datetime.now(pytz.timezone('Europe/Luxembourg'))
                display = time.strftime("%D, %H:%M:%S")
                print(display)
                mylabel2.config(text=display)
                mylabel2.after(1000,Search)
            case('Madrid'):
                time = datetime.now(pytz.timezone('Europe/Madrid'))
                display = time.strftime("%D, %H:%M:%S")
                print(display)
                mylabel2.config(text=display)
                mylabel2.after(1000,Search)
            case('Moscow'):
                time = datetime.now(pytz.timezone('Europe/Moscow'))
                display = time.strftime("%D, %H:%M:%S")
                print(display)
                mylabel2.config(text=display)
                mylabel2.after(1000,Search)
            case('Rome'):
                time = datetime.now(pytz.timezone('Europe/Rome'))
                print(type(time))
                display = time.strftime("%D, %H:%M:%S")
                print(display)
                mylabel2.config(text=display)
                mylabel2.after(1000,Search)
    International_countries_time = ttk.Combobox(root,value= countries)
    International_countries_time.config(width=40)
    International_countries_time.current(32)
    International_countries_time.pack()
    
    Time_Search_button = ttk.Button(root, text='Search', command=Search)
    Time_Search_button.config(width=40)
    Time_Search_button.pack()
    
    Initial_button_Alarm.forget()
    Initial_button_international_clock.forget()
    Initial_button_Stop_watch.forget()
    Initial_button_timer.forget()
    Back_to_home = ttk.Button(root, text='exit', command=destroy)
    Back_to_home.config(width=40)
    Back_to_home.pack()
    mylabel2 = ttk.Label(root)
    mylabel2.pack()

def Stop_watch():
    seconds, minutes, hours = 0,2,1
    time = str(hours) + str(minutes) + ':' + str(seconds)
    stop_watch_label = ttk.Label(root,text= time)
    Start_button = ttk.Button(root, text='Start')
    Stop_button = ttk.Button(root,text='Stop')
    if seconds<60:
        while seconds<60:
            print(seconds, time.sleep(1))
            seconds = seconds + 1
            print(seconds)
            if seconds == 60:
                seconds = 0
                minutes = 1
                print(minutes)
                print(seconds)
                
                
                
    
    Stop_button.config(width=40)
    Start_button.config(width=40)
    stop_watch_label.pack()
    Start_button.pack()
    Stop_button.pack()
    
    Back_to_home = ttk.Button(root, text='back')
    Back_to_home.config(width=40)
    Back_to_home.pack()
    
    Initial_button_Alarm.forget()
    Initial_button_international_clock.forget()
    Initial_button_Stop_watch.forget()
    Initial_button_timer.forget()
    

def Alarm(width=40):
    class EntryWithPlaceholder(Entry):
        def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey', width=40):
            super().__init__(master)
            self.placeholder = placeholder; self.placeholder_color = color
            self.default_fg_color = self['fg']; self.config(width=width)
            self.bind("<FocusIn>", self.foc_in); self.bind("<FocusOut>", self.foc_out)
            self.put_placeholder()
        def put_placeholder(self):
            self.insert(0, self.placeholder); self['fg'] = self.placeholder_color
        def foc_in(self, *args):
            if self['fg'] == self.placeholder_color:
                self.delete('0', 'end'); self['fg'] = self.default_fg_color
        def foc_out(self, *args):
            if not self.get(): self.put_placeholder()
    def destroy():
        question = messagebox.askquestion('exit','Are you sure you want to exit?')
        if question == 'yes':
            root.destroy()
    def save():
        time = datetime.today()
        display = time.strftime("%H:%M:%S")
        mylabel2.config(text=display)
        mylabel2.after(1000,save)
        compare = Alarm_time.get()
        print(compare)
        print(display)
        if compare == display:
            messagebox.showinfo("Alarm", "Times up")
            print(compare)
    mylabel2 = ttk.Label(root)
    Alarm_time = EntryWithPlaceholder(root, placeholder="Enter your time in hours:mins:seconds format.")
    Alarm_time.pack()
    Alarm_time.config()
    save_to_home = ttk.Button(root, text='Save', command=save)
    save_to_home.config(width=width)
    save_to_home.pack()
    exit = ttk.Button(root, text= 'exit', command=destroy)
    exit.config(width=width)
    exit.pack()
    mylabel2.pack()
    Initial_button_Alarm.forget()
    Initial_button_international_clock.forget()
    Initial_button_Stop_watch.forget()
    Initial_button_timer.forget()

#timer will be the last one to be made
def Timer():
    '''def start_timer():
        return
    global text
    '''
    #Once ctime
    text = 'a'
    timer_label = ttk.Label(root, text=text)
    start_button = ttk.Button(root, text='Start')
    timer_label.config(width=40)
    timer_label.pack()
    start_button.config(width=40)
    start_button.pack()
    Back_to_home = ttk.Button(root, text='back')
    Back_to_home.config(width=40)
    Back_to_home.pack()
    Initial_button_Alarm.forget()
    Initial_button_international_clock.forget()
    Initial_button_Stop_watch.forget()
    Initial_button_timer.forget()

Initial_button_international_clock = ttk.Button(root, text='International time',command=International_time)
Initial_button_Alarm = ttk.Button(root, text='Alarm', command=Alarm)
Initial_button_Stop_watch = ttk.Button(root, text='Stop Watch',command=Stop_watch)
Initial_button_timer = ttk.Button(root, text='Timer',command=Timer)


Initial_button_international_clock.pack(ipadx=200, ipady=65)
Initial_button_Alarm.pack(ipadx=250, ipady=65)
Initial_button_Stop_watch.pack(ipadx=2200, ipady=65)
Initial_button_timer.pack(ipadx=250, ipady=65)
root.mainloop()
