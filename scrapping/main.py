from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
from libScrappingtipocambio import scrapping_tipocambio, grabarMonedas
class TipoCambio:

    def __init__(self,window):
        self.wind = window
        self.wind.title('Tipos de cambios')
        self.wind.geometry('600x300')

        #FRAME
        frame = LabelFrame(self.wind, text='Tipos de Cambios')
        frame.grid(row=0,column=0,columnspan=9,pady=20,padx=20)

        #TREVIEW
        self.TrvData= ttk.Treeview(height=10,columns=3)

        self.TrvData['columns'] = ('moneda', 'compra', 'venta')

        self.TrvData.column('#0',width=0,stretch='NO')
        self.TrvData.column('moneda')
        self.TrvData.column('compra')
        self.TrvData.column('venta')  

        self.TrvData.heading('#0', text='ID')
        self.TrvData.heading('moneda',text='moneda')
        self.TrvData.heading('compra',text='compra')
        self.TrvData.heading('venta',text='venta')

        self.TrvData.grid(row=0,column=0)
        self.btnExportar = Button(self.wind,text='Descargar',command=self.descargarData)
        self.btnExportar.grid(row=2,columnspan=2,sticky=W+E)

        self.TrvData.grid(row=0,column=0)
        self.btnExportar = Button(self.wind,text='Exportar',command=self.exportarData)
        self.btnExportar.grid(row=3,columnspan=2,sticky=W+E)

    def descargarData(self):
            #Limpiar data
            for item in self.TrvData.get_children():
                self.TrvData.delete(item)

            #Obteniendo data de SBS
            data = scrapping_tipocambio() 
            id=1

            #Insertar data a Treeview 
            for row in data: 
                self.TrvData.insert('',END, str(id), values=list(row.values()),text='0'+str(id),tags=("even"))
                id+=1
            self.TrvData.tag_configure("even",foreground="white", background="black")

    def exportarData(self):
        data=[]
        #Obteniendo data de Treeview
        for child in  self.TrvData.get_children():
                value_dict={}
                for col, item in zip(self.TrvData["columns"], self.TrvData.item(child)["values"]):
                    value_dict[col] = item
                    if not value_dict in data:
                        data.append(value_dict)

        #Validando data de Treeview
        if len(data):
            strMonedas = grabarMonedas(data)
            file =  filedialog.asksaveasfile(filetypes=[("All Files", "*.*")],initialfile = 'Untitled.csv', mode='w', defaultextension=".csv")
            if file:
                file.write(strMonedas)
                file.close()
                messagebox.showinfo("Mensaje","Se ha exportado correctamente")
        else:
            messagebox.showinfo("Mensaje","No hay información para exportar")

if __name__ == "__main__":

    window = Tk()
    app = TipoCambio(window)
    window.mainloop()
