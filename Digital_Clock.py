from tkinter import *
import datetime
from tkinter import messagebox

def date_time():
    time=datetime.datetime.now()
    hr=time.strftime('%I')
    min=time.strftime('%M')
    sec=time.strftime('%S')
    am=time.strftime('%p')
    date=time.strftime('%d')
    month=time.strftime('%m')
    year=time.strftime('%y')
    day=time.strftime('%a')


    lab_hr.config(text=hr)
    lab_min.config(text=min)
    lab_sec.config(text=sec)
    lab_am.config(text=am)
    lab_hr.after(200,date_time)
    lab_date.config(text=date)
    lab_month.config(text=month)
    lab_year.config(text=year)
    lab_day.config(text=day.upper())





clock=Tk()
clock.title('Digital Clock')
clock.geometry('1000x600')
clock.config(bg='black')    #301934
# filename=PhotoImage(file='zigzag.png')
# background=Label(clock,image=filename)
# background.place(x=0,y=0,relheight=1,relwidth=1)

#**************************** create block for numbers **************************************

lab_hr=Label(clock,text='00',font=('Algerian',60,'bold'),bg='#000000',fg='#EADDCA')
lab_hr.place(x=112,y=105,height=120,width=110)

lab_min=Label(clock,text='00',font=('Algerian',60,'bold'),bg='Black',fg='#EADDCA')
lab_min.place(x=334,y=105,height=120,width=110)

lab_sec=Label(clock,text='00',font=('Algerian',60,'bold'),bg='black',fg='#EADDCA')
lab_sec.place(x=546,y=105,height=120,width=110)

lab_am=Label(clock,text='AM',font=('Bell MT',45,'bold'),bg='black',fg='#EADDCA')
lab_am.place(x=758,y=105,height=120,width=110)

# **************************** create text for time ***********************************

txt_hr=Label(clock,text='HOUR',font=('Bell MT',17),bg='black',fg='#EADDCA')
txt_hr.place(x=112,y=255,height=30,width=110)

txt_min=Label(clock,text='MINUTE',font=('Bell MT',17),bg='black',fg='#EADDCA')
txt_min.place(x=334,y=255,height=30,width=110)

txt_sec=Label(clock,text='SECOND',font=('Bell MT',17),bg='black',fg='#EADDCA')
txt_sec.place(x=546,y=255,height=30,width=110)

txt_am=Label(clock,text='PERIOD',font=('Bell MT',17),bg='black',fg='#EADDCA')
txt_am.place(x=758,y=255,height=30,width=110)

#***************************************** create block for date *****************************

lab_date=Label(clock,text='00',font=('Algerian',60,'bold'),bg='black',fg='#EADDCA')
lab_date.place(x=112,y=335,height=120,width=110)

lab_month=Label(clock,text='00',font=('Algerian',60,'bold'),bg='black',fg='#EADDCA')
lab_month.place(x=334,y=335,height=120,width=110)

lab_year=Label(clock,text='00',font=('Algerian',60,'bold'),bg='black',fg='#EADDCA')
lab_year.place(x=546,y=335,height=120,width=110)

lab_day=Label(clock,text='DAY',font=('Bell MT',40,'bold'),bg='black',fg='#EADDCA')
lab_day.place(x=758,y=335,height=120,width=130)

# write text for date

txt_date=Label(clock,text='DATE',font=('Bell MT',17),bg='black',fg='#EADDCA')
txt_date.place(x=112,y=475,height=30,width=110)

txt_month=Label(clock,text='MONTH',font=('Bell MT',17),bg='black',fg='#EADDCA')
txt_month.place(x=334,y=475,height=30,width=110)

txt_year=Label(clock,text='YEAR',font=('Bell MT',17),bg='black',fg='#EADDCA')
txt_year.place(x=546,y=475,height=30,width=110)

txt_day=Label(clock,text='DAY',font=('Bell MT',17),bg='black',fg='#EADDCA')
txt_day.place(x=758,y=475,height=30,width=110)


date_time()
clock.mainloop()

