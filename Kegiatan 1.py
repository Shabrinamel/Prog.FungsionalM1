# Fungsi penambahan (add), Anda mungkin sudah memiliki ini
def add(a, b):
    return a + b

# Fungsi pengurangan
def minus(a, b):
    return a - b

# Fungsi perkalian
def mult(a, b):
    return a * b

# Fungsi pembagian
def div(a, b):
    if b == 0:
        raise ValueError("Pembagian oleh nol tidak diizinkan")
    return a / b

# Fungsi tree yang mengolah pohon ekspresi
def tree(expression_tree):
    if isinstance(expression_tree, tuple):
        left_operand, operator, right_operand = expression_tree
        if operator == '+':
            return add(tree(left_operand), tree(right_operand))
        elif operator == '-':
            return minus(tree(left_operand), tree(right_operand))
        elif operator == '*':
            return mult(tree(left_operand), tree(right_operand))
        elif operator == '/':
            return div(tree(left_operand), tree(right_operand))
        else:
            raise ValueError("Operator tidak valid: " + operator)
    else:
        return expression_tree

# Contoh penggunaan
expression_tree = ((2, '+', 3), '*', (5, "-", 1))

result = tree(expression_tree)

print("Hasil evaluasi pohon ekspresi: ", result)
