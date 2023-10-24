def eval_loop():
    while True:
        user_value = input('Type your maths expression to evaluate: ')
        if user_value == 'done':
            break

        print(eval(user_value))
       
eval_loop()