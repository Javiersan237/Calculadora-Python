import tkinter as tk

class Calculadora:
    def __init__(self, root):

        #Variables de la Ventana
        self.root = root
        self.root.title("Calculadora")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        
        # Variables de estado
        self.current_number = "0"
        self.previous_number = None
        self.operation = None
        self.result = None
        self.waiting_for_operand = False
        self.last_action = None  # 'numero' or 'operación'
        self.max_digits = 8
        self.max_decimals = 3
        self.display_value = "0"
        self.is_dark_mode = False
        self.error_state = False
        
        # Colores
        self.colors = {
            'light': {
                'bg': '#FFFFFF',
                'display_bg': '#F5F5F5',
                'display_fg': '#000000',
                'button_bg': '#E0E0E0',
                'button_fg': '#000000',
                'operator_bg': '#FF9500',
                'operator_fg': '#FFFFFF',
                'function_bg': '#A5A5A5',
                'function_fg': '#000000',
                'equal_bg': '#FF9500',
                'equal_fg': '#FFFFFF',
                'border': '#D0D0D0'
            },
            'dark': {
                'bg': '#1C1C1E',
                'display_bg': '#1C1C1E',
                'display_fg': '#FFFFFF',
                'button_bg': '#333333',
                'button_fg': '#FFFFFF',
                'operator_bg': '#FF9500',
                'operator_fg': '#FFFFFF',
                'function_bg': '#A5A5A5',
                'function_fg': '#000000',
                'equal_bg': '#FF9500',
                'equal_fg': '#FFFFFF',
                'border': '#3A3A3C'
            }
        }
        
        self.setup_ui()
        
    def setup_ui(self):
        # Frame principal
        self.main_frame = tk.Frame(self.root, bg=self.colors['light']['bg'])
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Pantalla
        self.display_frame = tk.Frame(self.main_frame, bg=self.colors['light']['display_bg'], height=150)
        self.display_frame.pack(fill=tk.X, padx=10, pady=(20, 10))
        self.display_frame.pack_propagate(False)
        
        self.display_label = tk.Label(
            self.display_frame,
            text="0",
            font=('Arial', 48, 'bold'),
            bg=self.colors['light']['display_bg'],
            fg=self.colors['light']['display_fg'],
            anchor='e',
            padx=20
        )
        self.display_label.pack(fill=tk.BOTH, expand=True)
        
        # Botones
        self.buttons_frame = tk.Frame(self.main_frame, bg=self.colors['light']['bg'])
        self.buttons_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Configurar grid de botones
        buttons = [
            ('AC', 0, 0), ('+/-', 0, 1), ('C', 0, 2), ('÷', 0, 3),
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('×', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('+', 3, 3),
            ('0', 4, 0), ('.', 4, 2), ('=', 4, 3)
        ]
        
        # Hacer que el botón 0 ocupe 2 columnas
        self.btn_0 = None
        
        for text, row, col in buttons:
            if text == '0':
                btn = tk.Button(
                    self.buttons_frame,
                    text=text,
                    font=('Arial', 18, 'bold'),
                    bg=self.colors['light']['button_bg'],
                    fg=self.colors['light']['button_fg'],
                    relief=tk.RAISED,
                    bd=1,
                    command=lambda t=text: self.button_click(t)
                )
                btn.grid(row=row, column=col, columnspan=2, sticky='nsew', padx=2, pady=2)
                self.btn_0 = btn
            else:
                if text in ['+', '-', '×', '÷', '=']:
                    bg_color = self.colors['light']['operator_bg']
                    fg_color = self.colors['light']['operator_fg']
                elif text in ['AC', '+/-', 'C']:
                    bg_color = self.colors['light']['function_bg']
                    fg_color = self.colors['light']['function_fg']
                else:
                    bg_color = self.colors['light']['button_bg']
                    fg_color = self.colors['light']['button_fg']
                
                btn = tk.Button(
                    self.buttons_frame,
                    text=text,
                    font=('Arial', 18, 'bold'),
                    bg=bg_color,
                    fg=fg_color,
                    relief=tk.RAISED,
                    bd=1,
                    command=lambda t=text: self.button_click(t)
                )
                btn.grid(row=row, column=col, sticky='nsew', padx=2, pady=2)
        
        # Configurar pesos del grid
        for i in range(5):
            self.buttons_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.buttons_frame.grid_columnconfigure(i, weight=1)
        
        # Tecla para modo oscuro (Ctrl+D o Cmd+D)
        self.root.bind('<Control-d>', self.toggle_dark_mode)
        self.root.bind('<Command-d>', self.toggle_dark_mode)
        
        # Teclas para operaciones
        self.root.bind('<Key>', self.key_press)
        
    def toggle_dark_mode(self, event=None):
        self.is_dark_mode = not self.is_dark_mode
        colors = self.colors['dark'] if self.is_dark_mode else self.colors['light']
        
        # Actualizar colores
        self.main_frame.config(bg=colors['bg'])
        self.buttons_frame.config(bg=colors['bg'])
        self.display_frame.config(bg=colors['display_bg'])
        self.display_label.config(bg=colors['display_bg'], fg=colors['display_fg'])
        
        # Actualizar botones
        for widget in self.buttons_frame.winfo_children():
            if isinstance(widget, tk.Button):
                text = widget['text']
                if text in ['+', '-', '×', '÷', '=']:
                    widget.config(bg=colors['operator_bg'], fg=colors['operator_fg'])
                elif text in ['AC', '+/-', 'C']:
                    widget.config(bg=colors['function_bg'], fg=colors['function_fg'])
                else:
                    widget.config(bg=colors['button_bg'], fg=colors['button_fg'])
    
    def key_press(self, event):
        key = event.char
        if key in '0123456789':
            self.button_click(key)
        elif key in '+-*/':
            if key == '*':
                self.button_click('×')
            elif key == '/':
                self.button_click('÷')
            else:
                self.button_click(key)
        elif key == '=' or key == '\r':
            self.button_click('=')
        elif key == '.':
            self.button_click('.')
        elif key in 'cC':
            self.button_click('C')
        elif key in 'aA':
            self.button_click('AC')
    
    def format_number(self, num):
        """Formatea el número para mostrar en pantalla"""
        if isinstance(num, float):
            # Si es float, truncar a max_decimals
            num_str = f"{num:.{self.max_decimals}f}"
            # Eliminar ceros innecesarios
            num_str = num_str.rstrip('0').rstrip('.') if '.' in num_str else num_str
            return num_str
        return str(num)
    
    def validate_number(self, num_str):
        """Valida que el número no exceda los límites"""
        if self.error_state:
            self.clear_all()
            self.error_state = False
        
        # Si contiene punto decimal, verificar decimales
        if '.' in num_str:
            int_part, dec_part = num_str.split('.')
            if len(int_part) + len(dec_part) > self.max_digits:
                return False
            if len(dec_part) > self.max_decimals:
                return False
        else:
            if len(num_str) > self.max_digits:
                return False
        return True
    
    def get_display_value(self):
        return self.display_label['text']
    
    def set_display_value(self, value):
        if value == 'ERR':
            self.error_state = True
            self.display_label.config(text='ERR')
            self.current_number = "0"
            return
        
        # Si el valor es un número, formatearlo
        if isinstance(value, (int, float)):
            formatted = self.format_number(value)
            self.display_label.config(text=formatted)
            self.current_number = str(value)
        else:
            self.display_label.config(text=value)
            self.current_number = value if value != '0' else "0"
    
    def button_click(self, value):
        if self.error_state and value not in ['AC', 'C']:
            return
        
        if value.isdigit():
            self.handle_digit(value)
        elif value == '.':
            self.handle_decimal()
        elif value == '+/-':
            self.handle_negate()
        elif value in ['+', '-', '×', '÷']:
            self.handle_operation(value)
        elif value == '=':
            self.handle_equal()
        elif value == 'C':
            self.handle_clear()
        elif value == 'AC':
            self.clear_all()
    
    def handle_digit(self, digit):
        if self.waiting_for_operand:
            self.current_number = "0"
            self.waiting_for_operand = False
        
        if self.current_number == "0" and digit != '0':
            self.current_number = digit
        elif self.current_number != "0":
            new_number = self.current_number + digit
            if self.validate_number(new_number):
                self.current_number = new_number
        
        self.set_display_value(self.current_number)
        self.last_action = 'number'
    
    def handle_decimal(self):
        if self.waiting_for_operand:
            self.current_number = "0"
            self.waiting_for_operand = False
        
        if '.' not in self.current_number:
            self.current_number += '.'
            self.set_display_value(self.current_number)
            self.last_action = 'number'
    
    def handle_negate(self):
        if self.current_number != "0":
            if self.current_number.startswith('-'):
                self.current_number = self.current_number[1:]
            else:
                self.current_number = '-' + self.current_number
            self.set_display_value(self.current_number)
    
    def handle_operation(self, op):
        if self.last_action == 'operation' and self.operation is not None:
            # Cambiar la operación pendiente
            self.operation = op
            return
        
        current = float(self.current_number) if '.' in self.current_number else int(self.current_number)
        
        if self.operation is not None and self.previous_number is not None and not self.waiting_for_operand:
            # Realizar operación pendiente
            result = self.calculate(self.previous_number, current, self.operation)
            if result is None:
                return
            self.current_number = str(result)
            self.set_display_value(result)
            self.previous_number = result
        else:
            self.previous_number = current
        
        self.operation = op
        self.waiting_for_operand = True
        self.last_action = 'operation'
    
    def handle_equal(self):
        if self.operation is None:
            if self.result is not None:
                self.set_display_value(self.result)
            return
        
        current = float(self.current_number) if '.' in self.current_number else int(self.current_number)
        
        if self.previous_number is not None:
            result = self.calculate(self.previous_number, current, self.operation)
            if result is None:
                return
            self.result = result
            self.current_number = str(result)
            self.set_display_value(result)
            self.previous_number = result
            self.operation = None
            self.waiting_for_operand = True
            self.last_action = 'operation'
    
    def calculate(self, num1, num2, operation):
        try:
            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '×':
                result = num1 * num2
            elif operation == '÷':
                if num2 == 0:
                    self.set_display_value('ERR')
                    return None
                result = num1 / num2
            else:
                return None
            
            # Verificar límite de dígitos
            if isinstance(result, float):
                # Para floats, verificar si la parte entera excede el límite
                int_part = str(int(result))
                if len(int_part) > self.max_digits:
                    self.set_display_value('ERR')
                    return None
                # Redondear a max_decimals
                result = round(result, self.max_decimals)
            else:
                if len(str(result)) > self.max_digits:
                    self.set_display_value('ERR')
                    return None
            
            return result
        except:
            self.set_display_value('ERR')
            return None
    
    def handle_clear(self):
        if self.last_action == 'operation' and self.operation is not None:
            # Restaurar al valor anterior
            self.operation = None
            self.waiting_for_operand = False
            if self.previous_number is not None:
                self.set_display_value(self.previous_number)
                self.current_number = str(self.previous_number)
            else:
                self.set_display_value("0")
                self.current_number = "0"
        else:
            # Borrar último número
            self.current_number = "0"
            self.set_display_value("0")
            self.waiting_for_operand = False
        
        self.last_action = None
    
    def clear_all(self):
        self.current_number = "0"
        self.previous_number = None
        self.operation = None
        self.result = None
        self.waiting_for_operand = False
        self.last_action = None
        self.error_state = False
        self.set_display_value("0")

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculadora(root)
    root.mainloop()