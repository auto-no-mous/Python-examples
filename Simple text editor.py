#simple text editor, written on python 3.4, still works on 3.7.5
#GUI via tkinter

from tkinter import filedialog
from tkinter import messagebox
from tkinter import *


root=Tk()
root.title("Без имени - Текстовый редактор")
file = ''
fontColor = StringVar(value='black')
fontSize = StringVar(value="12")
fontName = StringVar(value='Arial')

def colorBtn():
   global fontColor
   rgb, color = colorchooser.askcolor(title="Color")
   if color!=None:
      fontColor.set(color)

def apply():
   global mainText, fontColor, fontName, fontSize
   mainText.configure(foreground=fontColor.get(), font=(fontName.get(), int(fontSize.get())))
   

def options():
   global fontSize, fontName
   top = Toplevel()
   top.focus()
   fontNameOpt = OptionMenu(top, fontName, 'Arial', 'Book Antiqua', 'Verdana')
   faceDescr = Label(top, text="Шрифт: ")
   faceDescr.grid(row=0, column=0)
   top.columnconfigure(1, weight=1)
   fontNameOpt.grid(row=0, column=1, sticky=N+E+W)

   fontSizeOpt = OptionMenu(top, fontSize, '8', '12', '16')
   sizeDescr = Label(top, text="Размер: ")
   sizeDescr.grid(row=1, column=0)
   fontSizeOpt.grid(row=1, column=1, sticky=N+E+W)
   
   selectColor = Button(top, text="Выбрать цвет", command=colorBtn)
   colorDescr = Label(top, text="Цвет текста:")
   colorDescr.grid(row=2, column=0)
   selectColor.grid(row=2, column=1, sticky=N+E+W)
   
   line = Label (top, text="---------------------")
   line.grid(row=3, column=0, columnspan=2, sticky=N+E+W+S)
   
   okBtn = Button (top, text="Применить", width=25, command=apply)
   okBtn.grid(row = 4, column=0, columnspan=2, pady=10)
   cancelBtn = Button (top, text="Отмена", width=25)
   cancelBtn.grid(row = 5, column=0, columnspan=2,pady=10)
   top.attributes('-topmost', 'true')
   top.geometry('300x200')

   
def cut ():
   mainText.event_generate("<<Cut>>")

def copy ():
   mainText.event_generate("<<Copy>>")

def paste ():
   mainText.event_generate("<<Paste>>") 

def fileWrite():
   t = open(file, 'w')
   t.write (mainText.get(1.0, END))
   t.close()
   path = file.split('/')[-1]
   root.title(path+' - Текстовый редактор')

def fileSave ():
   if file =='':
      fileSaveAs()
   else:
     fileWrite()
      

def fileSaveAs():
   global file
   oldfile = file
   file = filedialog.asksaveasfilename(initialfile='Без имени.txt',
                                       defaultextension = '*.txt',
                                          filetypes=[('Тексовые файлы', '*.txt'),
                                                     ('Все файлы', '*.*')])
   if file !='': fileWrite()
   else:
      file = oldfile
         

def fileOpen ():
   global file
   file = filedialog.askopenfilename (filetypes=
                                [("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")])
   if file !='':
      mainText.delete(1.0, END)
      path = file.split('/')[-1]
      root.title(path+' - Текстовый редактор')
      t = open(file, "r")
      mainText.insert(1.0, t.read())
      t.close()

def newFile ():
    mainText.delete(1.0, END)
    root.title("Без имени - Текстовый редактор")
    file = ''
    

def close ():
    root.destroy()


def about():
    messagebox.showinfo(title = "О программе",
                        message="Простой текстовый редактор.\nРазработчик: Александр Киселев\nautonomous@bk.ru")

def updSt(arg):
   global status, mainText
   t = mainText.get(1.0, END)
   status.configure(text='Всего символов: '+str(len(t)))
   mainText.edit_modified(False)

   
mainMenu = Menu(root)
fileMenu = Menu (mainMenu)
fileMenu.add_command(label="Новый", command=newFile)
fileMenu.add_command(label="Открыть", command=fileOpen)
fileMenu.add_command(label="Сохранить", command = fileSave)
fileMenu.add_command(label="Сохранить как", command=fileSaveAs)
fileMenu.add_command(label="Выход", command=close)


editMenu = Menu(mainMenu)
editMenu.add_command(label="Копировать", command=copy)
editMenu.add_command(label="Вырезать", command=cut)
editMenu.add_command(label="Вставить", command=paste)
editMenu.add_command(label="Настройки", command=options)


helpMenu = Menu(mainMenu)
helpMenu.add_command(label="О программе", command=about)

mainMenu.add_cascade(menu=fileMenu, label="Файл")
mainMenu.add_cascade(menu=editMenu, label="Правка")
mainMenu.add_cascade(menu=helpMenu, label="Справка")

root.config(menu = mainMenu)

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)


mainText = Text(root)
mainText.bind("<<Modified>>", updSt)

mainText.grid(sticky = N + W + E + S)

status = Label(root, text="Всего символов:", bd=1, relief=SUNKEN, anchor='w')
status.grid(sticky = E + S + W)

scroll = Scrollbar(mainText)
scroll.pack(side=RIGHT,fill=Y)                     
          
      
scroll.config(command=mainText.yview)      
mainText.config(yscrollcommand=scroll.set)
root.geometry('450x500')

if (len(sys.argv)>1):
   path = sys.argv[1].split('\\')[-1]
   root.title(path+' - Текстовый редактор')
   t = open(sys.argv[1], "r")
   mainText.insert(1.0, t.read())
   t.close()
   
root.mainloop()
