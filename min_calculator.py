import tkinter as tk


def add_digit(digit):
    """Добавляет число при нажатии на кнопку на калькуляторе.
       Число передается в виде str.
    """
    value = calc.get()
    if value[0] == '0':
        value = value[1:]
    calc.delete(0, tk.END)
    calc.insert(0, value + digit)


def add_operation(operation):
    """Добавляет оператор (+, -, *, /) при нажатии на кнопку на калькуляторе.
       Оператор передается в виде str.
       Если задан уже один оператор, то при нажатии на другой оператор предыдущий заменяется.
    """
    value = calc.get()
    if value[-1] in '-+/*':
        value = value[:-1]
    calc.delete(0, tk.END)
    calc.insert(0, value + operation)


def make_digit_button(digit):
    """Возвращает кнопку.
       Кнопка задается в виде str.
    """
    return tk.Button(text=digit, bd=5, font=('Arial', 13), command=lambda: add_digit(digit))


def make_operation_button(operation):
    """Возвращает оператор(Сложение: +,
                           Вычитание -,
                           Умножение: *,
                           Деление: /).
       Оператор задается в виде str.
    """
    return tk.Button(text=operation, bd=5, font=('Arial', 13), fg='red', command=lambda: add_operation(operation))


def make_calc_button(operation):
    """Кнопка, которая выполняет вычисления."""
    return tk.Button(text=operation, bd=5, font=('Arial', 13), fg='red', command=lambda: add_digit(operation))


win = tk.Tk()
win.geometry(f'240x270+100+200')
win['bg'] = '#33ffe6'
win.title('Калькулятор')  # Заголовок

calc = tk.Entry(win, justify=tk.RIGHT, font=('Arial', 15), width=15)
calc.insert(0, '0')
calc.grid(row=0, column=0, columnspan=4, sticky='we', padx=5)

make_digit_button('1').grid(row=1, column=0, stick='wens', padx=5, pady=5)
make_digit_button('2').grid(row=1, column=1, stick='wens', padx=5, pady=5)
make_digit_button('3').grid(row=1, column=2, stick='wens', padx=5, pady=5)
make_digit_button('4').grid(row=2, column=0, stick='wens', padx=5, pady=5)
make_digit_button('5').grid(row=2, column=1, stick='wens', padx=5, pady=5)
make_digit_button('6').grid(row=2, column=2, stick='wens', padx=5, pady=5)
make_digit_button('7').grid(row=3, column=0, stick='wens', padx=5, pady=5)
make_digit_button('8').grid(row=3, column=1, stick='wens', padx=5, pady=5)
make_digit_button('9').grid(row=3, column=2, stick='wens', padx=5, pady=5)
make_digit_button('0').grid(row=4, column=0, stick='wens', padx=5, pady=5)

make_operation_button('+').grid(row=1, column=3, stick='wens', padx=5, pady=5)
make_operation_button('-').grid(row=2, column=3, stick='wens', padx=5, pady=5)
make_operation_button('/').grid(row=3, column=3, stick='wens', padx=5, pady=5)
make_operation_button('*').grid(row=4, column=2, stick='wens', padx=5, pady=5)

make_calc_button('=').grid(row=4, column=3, stick='wens', padx=5, pady=5)

win.grid_columnconfigure(0, minsize=60)
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=60)
win.grid_columnconfigure(3, minsize=60)

win.grid_rowconfigure(1, minsize=60)
win.grid_rowconfigure(2, minsize=60)
win.grid_rowconfigure(3, minsize=60)
win.grid_rowconfigure(4, minsize=60)

win.mainloop()




























"""В этой программе происходят простейшие вычисления, простой калькулятор."""


def m_calculator(first_num, second_num, operator):
    try:
        opps = '-+*/'
        if operator == '/' and second_num == 0:
            return 'На ноль делить нельзя!'

        if operator not in opps:
            return 'Введите один из операторов (-, +, *, /)'

        if operator == '-':
            return first_num - second_num
        if operator == '+':
            return first_num + second_num
        if operator == '*':
            return first_num * second_num
        if operator == '/':
            return first_num / second_num
    except ValueError:
        return 'Ошибка: введите числовое значение!'


try:
    x = int(float(input('Введите первое число: ')))
    y = int(float(input('Введите второе число: ')))
    op = input('Введите оператор (-, +, *, /): ')
    result = m_calculator(x, y, op)
    print('Результат:', result)
except ValueError:
    print('Ошибка: введите числовое значение!')
































