def Linear_Eq():
    print("\ny = m*x + b", "\n↑          ")
    y = input("Enter 'y' or 'x': ").strip().lower()
    
    if y not in ("x", "y"):
        print("Error: Enter only 'y' or 'x'.")
        return None, None, None, None

    m = input("Enter m (or 'm' if unknown): ").strip()
    x = input("Enter x (or 'x' if unknown): ").strip()
    b = input("Enter b (or 'b' if unknown): ").strip()

    # Check if the entered values are numbers -- Проверяем, являются ли введённые значения числами
    m = float(m) if m.replace('.', '', 1).lstrip('-').isdigit() else m
    x = float(x) if x.replace('.', '', 1).lstrip('-').isdigit() else x
    b = float(b) if b.replace('.', '', 1).lstrip('-').isdigit() else b

    # Generate the equation result -- Формируем уравнение
    if isinstance(m, float) and isinstance(x, float):
        result = m * x + b if isinstance(b, float) else f"{m} * {x} + {b}"
    else:
        result = f"{m} * {x} + {b}"

    print(f"\nResult: {y} = {result}\n")
    return y, m, x, b


def Convert_Linear_Eq(y, m, x, b):
    if y is None:
        return

    # If m is a number, convert it to float and adjust the equation -- Если коэффициент m - число, домножаем обе стороны уравнения на -1
    if isinstance(m, float) or (isinstance(m, str) and m.lstrip('-').replace('.', '', 1).isdigit()):
        m = float(m)  # Преобразуем в число
        term_x = f"{-m}x" if m != 0 else "0"
    else:
        term_x = f"-{m}x" if m != "m" else "-m*x"

    # If b is a number, adjust its sign when moving to the left side -- Если b - число, меняем знак при переносе в левую часть
    if isinstance(b, float) or (isinstance(b, str) and b.lstrip('-').replace('.', '', 1).isdigit()):
        b = float(b)  # Преобразуем в число
        term_b = f"{-b}" if b != 0 else "0"
    else:
        term_b = f"-{b}"

    # Print the normal form of the equation: ax + by + c = 0 -- Выводим нормальное уравнение в виде ax + by + c = 0
    print(f"Normal equation: {term_x} + 1y {term_b} = 0")


# Example:
y, m, x, b = Linear_Eq()
Convert_Linear_Eq(y, m, x, b)