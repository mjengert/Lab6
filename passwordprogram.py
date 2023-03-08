# Maralynn Engert
# Prints the password menu.
def password_menu():
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    print('')


'''Takes in string password input, then iterates over the string to create an integer of each individual number 
within a list. Then adds 3 to each number within the list and adds it to a separate list (enc_password) to separate 
the encoded from the decoded version. Last it joins each value within the (enc_password) list to return the final 
encoded password.'''


def encode(password):
    og_password = []
    for num in password:
        og_password.append(int(num))
    enc_password = []
    for value in og_password:
        value += 3
        if value == 10:
            value = 0
        if value == 11:
            value = 1
        if value == 12:
            value = 2
        enc_password.append(str(value))
    password_encoded = ''.join(enc_password)
    return password_encoded

def decode(password_encoded):
    ogdeepass = []
    for i in password_encoded:
        ogdeepass.append(int(i))
    depassword = []
    for x in ogdeepass:
        x -= 3
        if x == 0:
            x = 10
        if x == 1:
            x = 11
        if x == 12:
            x = 2
        depassword.append(str(x))
    password_de = ''.join(depassword)
    return password_de

# Begins password encoding and decoding program
if __name__ == '__main__':
    menu_on = True
    while menu_on:
        password_menu()
        op_choice = int(input('Please enter an option: '))
        '''Runs through encode function, stores the final encoded product as password_encoded variable. Then prints 
        statement after completion.'''
        if op_choice == 1:
            password_og = input('Please enter your password to encode: ')
            password_encoded = encode(password_og)
            print('Your password has been encoded and stored!')
            print('')
        '''Runs through decode function, stores the final decoded product as password_decoded variable. Then prints 
        statement with the encoded and decoded password.'''
        if op_choice == 2:
            password_decoded = decode(password_encoded)
            print(f'The encoded password is {password_encoded}, and the original password is {password_decoded}')
            print('')
        # Exits the program.
        if op_choice == 3:
            menu_on = False
