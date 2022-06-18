from tkinter import *
# from tkinter.ttk import Treeview
from tkinter import ttk
from libScrappingtipocambio import scrapping_tipocambio

class TipoCambio:
    
    def __init__(self,window):
        self.wind = window
        self.wind.title('Tipos de cambios')
        self.wind.geometry('680x380')

        #FRAME
        frame = LabelFrame(self.wind, text='Tipos de Cambios')
        frame.grid(row=0,column=0,columnspan=3,pady=20,padx=20)

        #TREVIEW
        self.TrvData= ttk.Treeview(height=10,columns=3)

        self.TrvData['columns'] = ('Moneda', 'Compra', 'Venta')

        self.TrvData.column('#0',width=0,stretch=NO)
        self.TrvData.column('Moneda')
        self.TrvData.column('Compra')
        self.TrvData.column('Venta')  

        self.TrvData.heading('#0', text='id')
        self.TrvData.heading('Moneda',text='Moneda')
        self.TrvData.heading('Compra',text='Compra')
        self.TrvData.heading('Venta',text='Venta')

        self.TrvData.grid(row=0,column=0)
        self.btnExportar = Button(self.wind,text='Descargar',command=self.listarData)
        self.btnExportar.grid(row=2,columnspan=2,sticky=W+E)

        self.TrvData.grid(row=0,column=0)
        self.btnExportar = Button(self.wind,text='Exportar',command=self.listarData)
        self.btnExportar.grid(row=3,columnspan=2,sticky=W+E)
        

        # btnExportar.grid(row=2,columnspan=2,sticky=W+E)
        # self.TrvData.pack(fill=BOTH, expand=1)
        # self.TrvAlumno.grid(row=5,column=0, columnspan=2,padx=10)
        # self.TrvAlumno.heading('#0',text='Nombre',anchor=CENTER)
        # self.TrvAlumno.heading('#1',text='Email',anchor=CENTER)

    def listarData(self):
        data = scrapping_tipocambio() 
        print(data)  
        # for row in data:
        #     self.TrvData.insert('', '1',END, values=row,text='01')

window = Tk()
app = TipoCambio(window)
window.mainloop()
