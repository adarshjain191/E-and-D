
#importing tkinter libary and its module which are used to creat GUI
from tkinter import messagebox, simpledialog, Tk


#function to check length of string is even or odd
def is_even(number):
    return number % 2 == 0 #returns True if number is even otherwise returns false


#function to seprate charaters which are at even index
def get_even_letters(message):
    even_letters = []
    for counter in range(0, len(message)):
        if is_even(counter):
            even_letters.append(message[counter])
    return even_letters #returns the list of charactes at even index


#function to seprate charaters which are at odd index
def get_odd_letters(message):
    odd_letters = []
    for counter in range(0, len(message)):
        if not is_even(counter):
            odd_letters.append(message[counter])
    return odd_letters #returns the list of charactes at odd index


#this function genrates the encrypted message from the 
#message entered by the user
def swap_letters(message):
    letter_list = []
    if not is_even(len(message)): #calling is_even function to check length of message is even or odd
        message = message + '@'   #if length is odd then it added "@" at the last of message
    #here we are calling get_even_letters function
    even_letters = get_even_letters(message) 
    #here we are calling get_odd_letters function
    odd_letters = get_odd_letters(message)
    for counter in range(0, int(len(message)/2)):
        letter_list.append(odd_letters[counter])
        letter_list.append(even_letters[counter])
    return letter_list #returns the encoded or decoded message


#this function ask user if he/she want to encrypt or decrypt 
##it will show a dialog box 
def get_task():
    task = simpledialog.askstring('Task', 'Do you want to encrypt or decrypt?')
    return task  #return task(i.e encrypt or decrypt)


#this function ask user to enter their message for encrypt
#it will show a dialog box 
def get_message():
    message = simpledialog.askstring('Message', 'Enter the secret message: ')
    return message #return message enter by user



#the exectution of program start from here
if __name__=="__main__":
    #create an instance of tkinter frame or window
    root = Tk()
    #an infinite while loop
    while True:
        #calling get_task function
        task = get_task()  

        #if user want to encrypt
        if task == 'encrypt'or task=="Encrypt" or task=="ENCRYPT":
            #calling get_message function
            message = get_message() 
            #calling swap_letter function to rearrange charaters 
            #or to encrypt message
            encrypted = swap_letters(message)
            #it will show the encrypted message in messagebox
            messagebox.showinfo('Ciphertext of the secret message is:', ''.join(encrypted))
        
        #if user want to decrypt
        elif task == 'decrypt'or task == 'Decrypt' or task == 'DECRYPT':
            #calling get_message function 
            message = get_message()
            #calling swap_letter function to again rearranging charaters and obtaining orignal message
            #or to decrypt message
            decrypted = swap_letters(message)
            decrypted.pop()
            #it will show the decrypted message in messagebox
            messagebox.showinfo('Plaintext of the secret message is:', "".join(decrypted))
        #to break infinte loop
        else:
            break

    #calling method mainloop() which is used to run application in infinite loop
    root.mainloop()