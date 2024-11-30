while True:
    # خطوة 1: قراءة الرقم الأول والتحقق من صحته
    while True:
        try:
            num1 = float(input("Enter a number 1: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # خطوة 2: قراءة العملية الحسابية والتحقق من صحتها
    while True:
        operation = input("Enter an operation (+, -, *, /): ")
        if operation in ['+', '-', '*', '/']:
            break
        else:
            print("Invalid input. Please enter an operation (+, -, *, /).")

    # خطوة 3: قراءة الرقم الثاني والتحقق من صحته
    while True:
        try:
            num2 = float(input("Enter a number 2: "))
            if operation == '/' and num2 == 0:
                print("Error! Division by zero is not allowed.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # خطوة 4: تنفيذ العملية الحسابية وعرض النتيجة
    if operation == "+":
        result = f"{num1} + {num2} = {num1 + num2}"
    elif operation == "-":
        result = f"{num1} - {num2} = {num1 - num2}"
    elif operation == "*":
        result = f"{num1} * {num2} = {num1 * num2}"
    elif operation == "/":
        result = f"{num1} / {num2} = {num1 / num2}"

    print(result)

    # خطوة 5: سؤال المستخدم إذا كان يريد إجراء عملية حسابية أخرى
    again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
    if again in ['yes', 'y']:
        continue
    elif again in ['no', 'n']:
        print("Goodbye!")
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
