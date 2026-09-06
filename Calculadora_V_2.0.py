"""
CALCULADORA PROFESIONAL - 8 DÍGITOS
Con repetición automática de la última operación al presionar "="
"""

import tkinter as tk
from tkinter import messagebox
import re

class CalculadoraProfesional:
    """
    Clase principal de la calculadora con interfaz gráfica profesional
    """
    
    def __init__(self):
        """Inicializa la calculadora y la interfaz gráfica"""
        # Estado de la calculadora
        self.display_text = "0"
        self.current_number = "0"
        self.previous_number = None
        self.operation = None
        self.result = None
        self.new_number = True
        self.error = False
        self.memory = 0
        self.history = []
        
        # Variables para repetición automática
        self.last_operation = None      # Última operación realizada
        self.last_operand = None        # Último operando usado
        self.last_result = None         # Último resultado
        self.repeat_ready = False       # Indica si está listo para repetir
        
        # Configurar ventana principal
        self.root = tk.Tk()
        self.root.title("Calculadora Profesional")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        self.root.configure(bg='#1a1a2e')
        
        # Configurar estilo
        self.setup_styles()
        
        # Crear interfaz
        self.create_display()
        self.create_buttons()
        self.create_menu()
        
        # Atajos de teclado
        self.setup_keyboard_shortcuts()
        
    def setup_styles(self):
        """Configura los estilos profesionales de la calculadora"""
        self.colors = {
            'bg_dark': '#1a1a2e',
            'bg_display': '#0f0f1f',
            'text_primary': '#ffffff',
            'text_secondary': '#a0aec0',
            'btn_number': '#2d3748',
            'btn_number_hover': '#4a5568',
            'btn_operator': '#ed8936',
            'btn_operator_hover': '#dd6b20',
            'btn_function': '#4a5568',
            'btn_function_hover': '#718096',
            'btn_equal': '#48bb78',
            'btn_equal_hover': '#38a169',
            'btn_clear': '#fc8181',
            'btn_clear_hover': '#f56565',
            'btn_memory': '#9f7aea',
            'btn_memory_hover': '#805ad5'
        }
        
        # Configurar fuente personalizada
        self.font_display = ('Segoe UI', 36, 'bold')
        self.font_buttons = ('Segoe UI', 18, 'bold')
        self.font_small = ('Segoe UI', 12)
        
    def create_display(self):
        """USER STORY 1: Crea el display profesional"""
        display_frame = tk.Frame(self.root, bg=self.colors['bg_dark'], height=120)
        display_frame.pack(fill='x', padx=20, pady=(20, 10))
        display_frame.pack_propagate(False)
        
        # Indicador de operación
        self.operation_label = tk.Label(
            display_frame,
            text="",
            font=self.font_small,
            bg=self.colors['bg_display'],
            fg=self.colors['text_secondary'],
            anchor='e'
        )
        self.operation_label.pack(fill='x', padx=10, pady=(5, 0))
        
        # Display principal
        self.display = tk.Label(
            display_frame,
            text="0",
            font=self.font_display,
            bg=self.colors['bg_display'],
            fg=self.colors['text_primary'],
            anchor='e',
            relief='flat',
            padx=15,
            pady=5
        )
        self.display.pack(fill='both', expand=True, padx=10, pady=(0, 10))
        
        # Configurar el frame del display con borde
        display_frame.configure(bg=self.colors['bg_display'])
        
    def create_buttons(self):
        """USER STORY 2: Crea el panel de botones profesional"""
        buttons_frame = tk.Frame(self.root, bg=self.colors['bg_dark'])
        buttons_frame.pack(fill='both', expand=True, padx=20, pady=(10, 20))
        
        # Configuración del grid
        for i in range(6):
            buttons_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            buttons_frame.grid_columnconfigure(i, weight=1)
        
        # Botones - Fila 1 (Memoria y funciones)
        self.create_button(buttons_frame, "MC", 0, 0, self.memory_clear, 'function')
        self.create_button(buttons_frame, "MR", 1, 0, self.memory_recall, 'function')
        self.create_button(buttons_frame, "M+", 2, 0, self.memory_add, 'function')
        self.create_button(buttons_frame, "M-", 3, 0, self.memory_subtract, 'function')
        
        # Botones - Fila 2 (Funciones especiales)
        self.create_button(buttons_frame, "AC", 0, 1, self.reset_all, 'clear')
        self.create_button(buttons_frame, "C", 1, 1, self.clear_last, 'clear')
        self.create_button(buttons_frame, "±", 2, 1, self.toggle_sign, 'function')
        self.create_button(buttons_frame, "÷", 3, 1, lambda: self.set_operation("÷"), 'operator')
        
        # Botones - Fila 3
        self.create_button(buttons_frame, "7", 0, 2, lambda: self.append_digit(7), 'number')
        self.create_button(buttons_frame, "8", 1, 2, lambda: self.append_digit(8), 'number')
        self.create_button(buttons_frame, "9", 2, 2, lambda: self.append_digit(9), 'number')
        self.create_button(buttons_frame, "×", 3, 2, lambda: self.set_operation("×"), 'operator')
        
        # Botones - Fila 4
        self.create_button(buttons_frame, "4", 0, 3, lambda: self.append_digit(4), 'number')
        self.create_button(buttons_frame, "5", 1, 3, lambda: self.append_digit(5), 'number')
        self.create_button(buttons_frame, "6", 2, 3, lambda: self.append_digit(6), 'number')
        self.create_button(buttons_frame, "-", 3, 3, lambda: self.set_operation("-"), 'operator')
        
        # Botones - Fila 5
        self.create_button(buttons_frame, "1", 0, 4, lambda: self.append_digit(1), 'number')
        self.create_button(buttons_frame, "2", 1, 4, lambda: self.append_digit(2), 'number')
        self.create_button(buttons_frame, "3", 2, 4, lambda: self.append_digit(3), 'number')
        self.create_button(buttons_frame, "+", 3, 4, lambda: self.set_operation("+"), 'operator')
        
        # Botones - Fila 6
        self.create_button(buttons_frame, "0", 0, 5, lambda: self.append_digit(0), 'number', colspan=2)
        self.create_button(buttons_frame, ".", 2, 5, self.append_decimal, 'number')
        self.create_button(buttons_frame, "=", 3, 5, self.calculate_result, 'equal')
        
    def create_button(self, parent, text, col, row, command, style, colspan=1):
        """Crea un botón con estilo profesional"""
        # Configurar colores según estilo
        if style == 'number':
            bg = self.colors['btn_number']
            hover = self.colors['btn_number_hover']
            fg = self.colors['text_primary']
        elif style == 'operator':
            bg = self.colors['btn_operator']
            hover = self.colors['btn_operator_hover']
            fg = 'white'
        elif style == 'function':
            bg = self.colors['btn_function']
            hover = self.colors['btn_function_hover']
            fg = self.colors['text_primary']
        elif style == 'equal':
            bg = self.colors['btn_equal']
            hover = self.colors['btn_equal_hover']
            fg = 'white'
        elif style == 'clear':
            bg = self.colors['btn_clear']
            hover = self.colors['btn_clear_hover']
            fg = 'white'
        else:
            bg = self.colors['btn_function']
            hover = self.colors['btn_function_hover']
            fg = self.colors['text_primary']
        
        # Crear botón
        btn = tk.Button(
            parent,
            text=text,
            font=self.font_buttons,
            bg=bg,
            fg=fg,
            relief='flat',
            borderwidth=0,
            command=command,
            cursor='hand2',
            activebackground=hover,
            activeforeground=fg
        )
        btn.grid(row=row, column=col, columnspan=colspan, sticky='nsew', padx=4, pady=4)
        
        # Efecto hover
        def on_enter(e):
            btn.configure(bg=hover)
        
        def on_leave(e):
            btn.configure(bg=bg)
        
        btn.bind('<Enter>', on_enter)
        btn.bind('<Leave>', on_leave)
        
        return btn
    
    def create_menu(self):
        """Crea el menú superior"""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # Menú Archivo
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Archivo", menu=file_menu)
        file_menu.add_command(label="Historial", command=self.show_history)
        file_menu.add_separator()
        file_menu.add_command(label="Salir", command=self.root.quit)
        
        # Menú Editar
        edit_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Editar", menu=edit_menu)
        edit_menu.add_command(label="Copiar resultado", command=self.copy_result)
        edit_menu.add_command(label="Pegar número", command=self.paste_number)
        
        # Menú Ayuda
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Ayuda", menu=help_menu)
        help_menu.add_command(label="Acerca de", command=self.show_about)
        help_menu.add_command(label="Atajos de teclado", command=self.show_shortcuts)
    
    def setup_keyboard_shortcuts(self):
        """Configura atajos de teclado"""
        self.root.bind('<Key>', self.key_press)
        self.root.bind('<Return>', lambda e: self.calculate_result())
        self.root.bind('<Escape>', lambda e: self.reset_all())
        self.root.bind('<BackSpace>', lambda e: self.clear_last())
    
    def key_press(self, event):
        """Maneja la entrada desde el teclado"""
        key = event.char
        
        if key.isdigit():
            self.append_digit(int(key))
        elif key == '.':
            self.append_decimal()
        elif key in '+':
            self.set_operation('+')
        elif key == '-':
            self.set_operation('-')
        elif key == '*':
            self.set_operation('×')
        elif key == '/':
            self.set_operation('÷')
        elif key.lower() == 'c':
            self.clear_last()
        elif key.lower() == 'a':
            self.reset_all()
    
    # ============ FUNCIONES DE LA CALCULADORA ============
    
    def update_display(self):
        """Actualiza el display con el valor actual"""
        if self.error:
            self.display.config(text="ERR", fg='#fc8181')
            return
        
        # USER STORY 1: Mostrar número actual o resultado
        text = self.display_text
        if len(text) > 12:
            text = text[:12] + "..."
        self.display.config(text=text, fg=self.colors['text_primary'])
        
        # Actualizar indicador de operación
        if self.operation:
            op_text = f"{self.previous_number} {self.operation} "
            self.operation_label.config(text=op_text)
        else:
            self.operation_label.config(text="")
    
    # USER STORY 3: Ingresar números de hasta 8 dígitos
    def append_digit(self, digit):
        """Agrega un dígito al número actual (máx 8 dígitos)"""
        if self.error:
            self.reset_all()
            return
        
        # Al ingresar un número, desactivar repetición
        self.repeat_ready = False
        
        if self.new_number:
            self.current_number = "0"
            self.new_number = False
        
        # Verificar límite de 8 dígitos
        clean_number = self.current_number.replace("-", "").replace(".", "")
        if len(clean_number) >= 8:
            return
        
        if self.current_number == "0" and digit != ".":
            self.current_number = str(digit)
        else:
            self.current_number += str(digit)
        
        self.display_text = self.current_number
        self.update_display()
    
    def append_decimal(self):
        """Agrega punto decimal"""
        if self.error:
            self.reset_all()
            return
        
        self.repeat_ready = False
        
        if self.new_number:
            self.current_number = "0."
            self.new_number = False
        elif "." not in self.current_number:
            # Verificar límite antes de agregar decimal
            clean_number = self.current_number.replace("-", "")
            if len(clean_number) >= 8:
                return
            self.current_number += "."
        
        self.display_text = self.current_number
        self.update_display()
    
    def toggle_sign(self):
        """Cambia el signo del número actual (permite números negativos)"""
        if self.error:
            return
        
        self.repeat_ready = False
        
        if self.current_number != "0":
            if self.current_number.startswith("-"):
                self.current_number = self.current_number[1:]
            else:
                self.current_number = "-" + self.current_number
            self.display_text = self.current_number
            self.update_display()
    
    # USER STORY 2: Operaciones +, -, ×, ÷
    def set_operation(self, op):
        """Establece la operación a realizar"""
        if self.error:
            self.reset_all()
            return
        
        # Si hay una operación pendiente y no es un nuevo número, calcular primero
        if self.previous_number is not None and not self.new_number:
            self.calculate_result()
        
        try:
            self.previous_number = float(self.current_number) if self.current_number else 0
        except ValueError:
            self.previous_number = 0
        
        self.operation = op
        self.new_number = True
        self.repeat_ready = False  # Desactivar repetición al establecer nueva operación
        self.update_display()
    
    # USER STORY 4: Operaciones encadenadas con resultado anterior
    # USER STORY 7: Mostrar "ERR" si excede 8 dígitos
    def calculate_result(self):
        """
        Calcula el resultado de la operación actual.
        Si se presiona "=" repetidamente, repite la última operación.
        """
        # ============ MODO REPETICIÓN ============
        # Si está listo para repetir y hay una operación guardada
        if self.repeat_ready and self.last_operation is not None and self.last_operand is not None:
            self.repeat_last_operation()
            return
        
        # ============ CÁLCULO NORMAL ============
        if self.previous_number is None or self.operation is None:
            # Si no hay operación, solo mostrar el número actual
            try:
                self.result = float(self.current_number)
                self.display_text = self.format_number(self.result)
                self.update_display()
                return
            except:
                return
        
        try:
            current = float(self.current_number)
            
            # Guardar operación para repetición
            self.last_operation = self.operation
            self.last_operand = current
            
            # Realizar operación
            if self.operation == "+":
                self.result = self.previous_number + current
            elif self.operation == "-":
                self.result = self.previous_number - current
            elif self.operation == "×":
                self.result = self.previous_number * current
            elif self.operation == "÷":
                if current == 0:
                    self.error = True
                    self.display_text = "ERR"
                    self.update_display()
                    return
                self.result = self.previous_number / current
            
            # Verificar límite de 8 dígitos
            formatted = self.format_number(self.result)
            clean_formatted = formatted.replace("-", "").replace(".", "")
            if len(clean_formatted) > 8:
                self.error = True
                self.display_text = "ERR"
                self.update_display()
                return
            
            # Guardar en historial
            self.history.append(f"{self.previous_number} {self.operation} {current} = {formatted}")
            
            # Actualizar estado
            self.display_text = formatted
            self.current_number = str(self.result)
            self.previous_number = None
            self.operation = None
            self.new_number = True
            
            # Activar modo repetición
            self.repeat_ready = True
            
            self.update_display()
            
        except Exception as e:
            self.error = True
            self.display_text = "ERR"
            self.update_display()
    
    def repeat_last_operation(self):
        """
        Repite la última operación con el mismo operando.
        Ejemplo: 2 + 2 = 4, luego "=" → 6, luego "=" → 8
        """
        try:
            # El número actual es el resultado anterior
            current = float(self.current_number)
            
            # Guardar el valor actual para el historial
            previous_value = current
            
            # Aplicar la última operación con el último operando
            if self.last_operation == "+":
                self.result = current + self.last_operand
            elif self.last_operation == "-":
                self.result = current - self.last_operand
            elif self.last_operation == "×":
                self.result = current * self.last_operand
            elif self.last_operation == "÷":
                if self.last_operand == 0:
                    self.error = True
                    self.display_text = "ERR"
                    self.update_display()
                    return
                self.result = current / self.last_operand
            else:
                return
            
            # Formatear resultado
            formatted = self.format_number(self.result)
            clean_formatted = formatted.replace("-", "").replace(".", "")
            if len(clean_formatted) > 8:
                self.error = True
                self.display_text = "ERR"
                self.update_display()
                return
            
            # Guardar en historial con indicador de repetición
            self.history.append(f"[REP] {previous_value} {self.last_operation} {self.last_operand} = {formatted}")
            
            # Actualizar estado
            self.display_text = formatted
            self.current_number = str(self.result)
            self.previous_number = None
            self.operation = None
            self.new_number = True
            
            # Mantener modo repetición activo
            self.repeat_ready = True
            
            self.update_display()
            
        except Exception as e:
            self.error = True
            self.display_text = "ERR"
            self.update_display()
    
    def format_number(self, num):
        """Formatea un número para mostrar (máx 8 dígitos)"""
        if num is None:
            return "0"
        
        # Si es entero, mostrar sin decimales
        if isinstance(num, float) and num.is_integer():
            return str(int(num))
        
        # Formatear con precisión limitada
        s = f"{num:.10f}".rstrip("0").rstrip(".")
        
        # Si es muy largo, usar notación científica
        if len(s.replace("-", "").replace(".", "")) > 8:
            s = f"{num:.6e}"
        
        return s
    
    # USER STORY 5: Botón C - Limpiar último número u operación
    def clear_last(self):
        """Limpia el último número u operación (C)"""
        if self.error:
            self.reset_all()
            return
        
        # Desactivar repetición
        self.repeat_ready = False
        
        if self.operation is not None and self.new_number:
            # Cancelar operación pendiente
            self.operation = None
            self.previous_number = None
            self.current_number = "0"
            self.display_text = "0"
        else:
            # Limpiar número actual
            self.current_number = "0"
            self.display_text = "0"
            self.new_number = True
        
        self.update_display()
    
    # USER STORY 6: Botón AC - Limpiar todo el estado
    def reset_all(self):
        """Limpia todo el estado (AC)"""
        self.display_text = "0"
        self.current_number = "0"
        self.previous_number = None
        self.operation = None
        self.result = None
        self.new_number = True
        self.error = False
        self.repeat_ready = False
        self.last_operation = None
        self.last_operand = None
        self.update_display()
    
    # ============ FUNCIONES DE MEMORIA ============
    
    def memory_clear(self):
        """Limpia la memoria"""
        self.memory = 0
        self.show_temporary_message("MC")
    
    def memory_recall(self):
        """Recupera el valor de memoria"""
        self.current_number = str(self.memory)
        self.display_text = str(self.memory)
        self.new_number = True
        self.repeat_ready = False
        self.update_display()
        self.show_temporary_message("MR")
    
    def memory_add(self):
        """Suma el número actual a la memoria"""
        try:
            self.memory += float(self.current_number)
            self.show_temporary_message(f"M+ = {self.memory}")
        except:
            pass
    
    def memory_subtract(self):
        """Resta el número actual de la memoria"""
        try:
            self.memory -= float(self.current_number)
            self.show_temporary_message(f"M- = {self.memory}")
        except:
            pass
    
    def show_temporary_message(self, message):
        """Muestra un mensaje temporal en la etiqueta de operación"""
        original = self.operation_label.cget('text')
        self.operation_label.config(text=message, fg='#48bb78')
        self.root.after(1500, lambda: self.operation_label.config(text=original, fg=self.colors['text_secondary']))
    
    # ============ FUNCIONES DEL MENÚ ============
    
    def show_history(self):
        """Muestra el historial de operaciones"""
        if not self.history:
            messagebox.showinfo("Historial", "No hay operaciones en el historial")
            return
        
        history_text = "\n".join(self.history[-10:])  # Últimas 10 operaciones
        messagebox.showinfo("Historial de operaciones", 
                           f"Últimas {len(self.history)} operaciones:\n\n{history_text}")
    
    def copy_result(self):
        """Copia el resultado al portapapeles"""
        self.root.clipboard_clear()
        self.root.clipboard_append(self.display_text)
        self.show_temporary_message("¡Copiado!")
    
    def paste_number(self):
        """Pega un número del portapapeles"""
        try:
            text = self.root.clipboard_get()
            # Validar que sea un número
            if re.match(r'^-?\d*\.?\d*$', text):
                if len(text.replace("-", "").replace(".", "")) <= 8:
                    self.current_number = text
                    self.display_text = text
                    self.new_number = True
                    self.repeat_ready = False
                    self.update_display()
        except:
            pass
    
    def show_about(self):
        """Muestra información sobre la calculadora"""
        messagebox.showinfo(
            "Acerca de",
            "Calculadora Profesional v3.0\n\n"
            "Desarrollada con Python y Tkinter\n"
            "Características:\n"
            "• Display de 8 dígitos\n"
            "• Operaciones encadenadas\n"
            "• Repetición automática al presionar '='\n"
            "• Números negativos\n"
            "• Memoria (MC, MR, M+, M-)\n"
            "• Historial de operaciones\n"
            "• Atajos de teclado\n\n"
            "© 2024 - Todos los derechos reservados"
        )
    
    def show_shortcuts(self):
        """Muestra los atajos de teclado"""
        messagebox.showinfo(
            "Atajos de teclado",
            "Teclas rápidas disponibles:\n\n"
            "0-9    → Ingresar dígitos\n"
            ".      → Punto decimal\n"
            "+ - * / → Operaciones\n"
            "Enter  → Calcular (=)\n"
            "C      → Limpiar último (C)\n"
            "A      → Limpiar todo (AC)\n"
            "Esc    → Limpiar todo (AC)"
        )
    
    def run(self):
        """Inicia la aplicación"""
        self.root.mainloop()


# ============ PUNTO DE ENTRADA ============

if __name__ == "__main__":
    # Crear y ejecutar la calculadora
    app = CalculadoraProfesional()
    app.run()