import tkinter as tk
from modelo import Apuesta

class Ventana(tk.Tk):
    """
    Parte visual de una aplicación, con botones y menús para que el usuario seleccione la opción deseada.
    """
    def __init__(self, apuesta):
        super().__init__()
        self.apuesta = apuesta
        self.title("Apuestas")
        self.geometry("478x208")
        
        menu_bar = tk.Menu(self)
        self.config(menu=menu_bar)
        
        menu_opciones = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Opciones", menu=menu_opciones)
        
        menu_opciones.add_command(label="Incrementar")
        menu_opciones.add_command(label="Cancelar")

        content_pane = tk.Frame(self, bd=5)
        content_pane.pack(expand=True, fill="both")
        
        self.btn_incrementar = tk.Button(content_pane, text="Incrementar", command=self.incrementar)
        self.btn_incrementar.pack(side="left", padx=10, pady=10)
        
        self.btn_cancelar = tk.Button(content_pane, text="Cancelar", command=self.cancelar)
        self.btn_cancelar.pack(side="left", padx=10, pady=10)
        
        self.text_area = tk.Text(content_pane, state="disabled")
        self.text_area.pack(side="left", padx=10, pady=10)
        
        self.nuevaApuesta(apuesta)
        
    def incrementar(self):
        self.apuesta.incrementar()
        self.text_area.configure(state="normal")
        self.text_area.delete("1.0", "end")
        self.text_area.insert("end", str(self.apuesta))
        self.text_area.configure(state="disabled")
        
    def cancelar(self):
        self.apuesta.cancelar()
        self.text_area.configure(state="normal")
        self.text_area.delete("1.0", "end")
        self.text_area.insert("end", str(self.apuesta))
        self.text_area.configure(state="disabled")
        
    def nuevaApuesta(self, apuesta):
        self.apuesta = apuesta
        self.text_area.configure(state="normal")
        self.text_area.delete("1.0", "end")
        self.text_area.insert("end", str(self.apuesta))
        self.text_area.configure(state="disabled")
        
if __name__ == "__main__":
    ventana = Ventana(Apuesta())
    ventana.mainloop()
	