print('''Linear Kinematic Calculator''')
print('''v_f = v_i + a * t''')

print('''
Variable Key:
''')
print('''
Final velocity = v_f 
Initital velocity = v_i 
Acceleration = a 
Time = t
    ''')

while True:
    try:
        initial_input = input('Are 3 of the 4 variables known (yes / no)? ')
        if initial_input.upper() == 'YES':
            second_input = input('Which of the variables is unknown? ')
            if second_input.lower() == 'v_f':
                # print('Final velocity is the unknown variable.')
                print('Solving for final velocity...')
                try:
                    v_f_initial = float(input('Enter the initial velocity (m/s): '))
                    v_f_accel = float(input('Enter the acceleration (m/s^2): '))
                    v_f_time = float(input('Enter the time (s): '))
                except:
                    print('Invalid input.')
                    try_again = input('Try again (yes / no)? ')
                    if try_again.upper() == 'YES':
                        continue
                    else:
                        break
                v_f_solution = v_f_initial + v_f_accel * v_f_time
                print(f'Final velocity: {v_f_solution} meters per second.')
                v_f_continue = input('Try again or quit (try / quit)? ')
                if v_f_continue.lower() == 'try':
                    continue
                else:
                    break
            elif second_input.lower() == 'v_i':
                # print('Initial velocity is the unknown variable.')
                print('Solving for initial velocity...')
                try:
                    v_i_final = float(input('Enter the final velocity (m/s): '))
                    v_i_accel = float(input('Enter the acceleration (m/s^2): '))
                    v_i_time = float(input('Enter the time (s): '))
                except:
                    print('Invalid input.')
                    try_again = input('Try again (yes / no)? ')
                    if try_again.upper() == 'YES':
                        continue
                    else:
                        break
                v_i_solution = v_i_final / (v_i_accel * v_i_time)
                print(f'Initial velocity: {v_i_solution} meters per second.')
                v_i_continue = input('Try again or quit (try / quit)? ')
                if v_i_continue.lower() == 'try':
                    continue
                else:
                    break
            elif second_input.lower() == 'a':
                # print('Acceleration is the unknown variable.')
                print('Solving for acceleration...')
                try:
                    a_initial = float(input('Enter the initial velocity (m/s): '))
                    a_final = float(input('Enter the final velocity (m/s): '))
                    a_time = float(input('Enter the time (s): '))
                except:
                    print('Invalid input.')
                    try_again = input('Try again (yes / no)? ')
                    if try_again.upper() == 'YES':
                        continue
                    else:
                        break
                a_solution = (a_final - a_initial) / a_time
                print(f'Acceleration: {a_solution} meters per second squared.')
                a_continue = input('Try again or quit (try / quit)? ')
                if a_continue.lower() == 'try':
                    continue
                else:
                    break
            elif second_input.lower() == 't':
                # print('Time is the unknown variable.')
                print('Solving for time...')
                try:
                    t_initial = float(input('Enter the initial velocity (m/s): '))
                    t_final = float(input('Enter the final velocity (m/s): '))
                    t_accel = float(input('Enter the acceleration (m/s^2): '))
                except:
                    print('Invalid input.')
                    try_again = input('Try again (yes / no)? ')
                    if try_again.upper() == 'YES':
                        continue
                    else:
                        break
                t_solution = (t_final - t_initial) / t_accel
                print(f'Time: {t_solution} seconds.')
                a_continue = input('Try again or quit (try / quit)? ')
                if a_continue.lower() == 'try':
                    continue
                else:
                    break
            else:
                print('Invalid input.')
                try_again = input('Try again (yes / no)? ')
                if try_again.upper() == 'YES':
                    continue
                else:
                    break
        else:
            print('Must know at least 3 of the 4 variables to execute...')
            quit_choice = input('Choose to quit (yes / no)? ')
            if quit_choice.upper() == 'YES':
                break
            else:
                continue
    except:
        print('Invalid input.')
        try_again = input('Try again (yes / no)? ')
        if try_again.upper() == 'YES':
                continue
        else:
            break