import flet as ft
from flet_core.elevated_button import ElevatedButton


def calc_suma(txt1,txt2,labresul):
    try:
        num1=float(txt1.value.strip())
        num2=float(txt2.value.strip())
        resultado=num1+num2
        labresul.value=f"resultado: {resultado}"
    except ValueError:
        labresul.value="Error, ingresa valores correctos"

def calc_resta(txt1,txt2,labresul):
    try:
        num1=float(txt1.value.strip())
        num2=float(txt2.value.strip())
        resultado=num1-num2
        labresul.value=f"resultado: {resultado}"
    except ValueError:
        labresul.value="Error, ingresa valores correctos"

def calc_multi(txt1,txt2,labresul):
    try:
        num1=float(txt1.value.strip())
        num2=float(txt2.value.strip())
        resultado=num1*num2
        labresul.value=f"resultado: {resultado}"
    except ValueError:
        labresul.value="Error, ingresa valores correctos"

def calc_divicion(txt1,txt2,labresul):
    try:
        num1=float(txt1.value.strip())
        num2=float(txt2.value.strip())
        resultado=num1/num2
        labresul.value=f"resultado: {resultado}"
    except ValueError:
        labresul.value="Error, ingresa valores correctos"


def main(page: ft.Page):
    page.title="caulculadora"
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.bgcolor="#f59c3d"
    
    txt1=ft.TextField(label="primer numero")
    txt2=ft.TextField(label="segundo numero")
    
    labresul=ft.Text("resultado:")
    
    def on_calc_suma(e):
        calc_suma(txt1,txt2,labresul)
        page.update()
        
    def on_calc_resta(e):
        calc_resta(txt1,txt2,labresul)
        page.update()
    def on_calc_divicion(e):
        calc_divicion(txt1,txt2,labresul)
        page.update()
        
    def on_calc_multiplicacion(e):
        calc_multi(txt1,txt2,labresul)
        page.update()
    
    def limpiar(e):
        txt1.value=""
        txt2.value=""
        labresul.value="resultado:"
        page.update()
    
    btnsuma=ElevatedButton("+",on_click=on_calc_suma)
    btnresta=ElevatedButton("-",on_click=on_calc_resta)
    btndivicion=ElevatedButton("/",on_click=on_calc_divicion)
    btnmulti=ElevatedButton("*",on_click=on_calc_multiplicacion )
    btnlimpiar=ElevatedButton("limpiar",on_click=limpiar)
    
    page.add(
        ft.Row([txt1,txt2],alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([labresul],alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([btnsuma,btnresta,btndivicion,btnmulti,btnlimpiar],alignment=ft.MainAxisAlignment.CENTER)
    )



ft.app(main)
