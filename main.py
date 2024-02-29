# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
import game
from ai import *
from game import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from  random import randint
root=Tk()
style=ttk.Style()
root.title("TIC TAC TOY : Player 1")
style.theme_use('classic')

board = []
for _ in range(25):
    board.append(' ')
board[0] = 'X'
board[1] = 'O'
board[2] = 'O'
board[3] = 'X'
board[7] = 'X'
board[8] = 'O'
board[9] = 'X'
board[11] = 'O'
board[12] = 'O'
board[13] = 'X'

button1=Button(root,text=' ',bg='#ffb3fe')
button1.grid(row=0,column=0,sticky='snew',ipadx=40,ipady=40)
button1.config(text=board[0])
#button1.config(command=lambda:hala(1))

button2=Button(root,text=' ', bg='#ffb3fe')
button2.grid(row=0,column=1,sticky='snew',ipadx=40,ipady=40)
button2.config(text=board[1])
#button2.config(command=lambda:hala(2))

button3=Button(root,text=' ', bg='#ffb3fe')
button3.grid(row=0,column=2,sticky='snew',ipadx=40,ipady=40)
button3.config(text=board[2])
#button3.config(command=lambda:hala(3))

button4=Button(root,text=' ', bg='#ffb3fe')
button4.grid(row=0,column=3,sticky='snew',ipadx=40,ipady=40)
button4.config(text=board[3])
#button4.config(command=lambda:hala(4))

button5=ttk.Button(root,text=' ')
button5.grid(row=0,column=4,sticky='snew',ipadx=40,ipady=40)
button5.config(text=board[4])
#button5.config(command=lambda:hala(5))
####################################################################################
button6=ttk.Button(root,text=' ')
button6.grid(row=1,column=0,sticky='snew',ipadx=40,ipady=40)
button6.config(text=board[5])

#button6.config(command=lambda:hala(6))

button7=ttk.Button(root,text=' ')
button7.grid(row=1,column=1,sticky='snew',ipadx=40,ipady=40)
button7.config(text=board[6])

#button7.config(command=lambda:hala(7))

button8=Button(root,text=' ', bg='#ffb3fe')
button8.grid(row=1,column=2,sticky='snew',ipadx=40,ipady=40)
button8.config(text=board[7])

#button8.config(command=lambda:hala(8))

button9=Button(root,text=' ', bg='#ffb3fe')
button9.grid(row=1,column=3,sticky='snew',ipadx=40,ipady=40)
button9.config(text=board[8])

button10=Button(root,text=' ', bg='#ffb3fe')
button10.grid(row=1,column=4,sticky='snew',ipadx=40,ipady=40)
button10.config(text=board[9])

####################################################################################
button11=ttk.Button(root,text=' ')
button11.grid(row=2,column=0,sticky='snew',ipadx=40,ipady=40)
button11.config(text=board[10])
#button9.config(command=lambda:hala(9))

button12=Button(root,text=' ', bg='#ffb3fe')
button12.grid(row=2,column=1,sticky='snew',ipadx=40,ipady=40)
button12.config(text=board[11])
#button9.config(command=lambda:hala(9))

button13=Button(root,text=' ', bg='#ffb3fe')
button13.grid(row=2,column=2,sticky='snew',ipadx=40,ipady=40)
button13.config(text=board[12])
#button9.config(command=lambda:hala(9))

button14=Button(root,text=' ', bg='#ffb3fe')
button14.grid(row=2,column=3,sticky='snew',ipadx=40,ipady=40)
button14.config(text=board[13])
#button9.config(command=lambda:hala(9))

button15=ttk.Button(root,text=' ')
button15.grid(row=2,column=4,sticky='snew',ipadx=40,ipady=40)
button15.config(text=board[14])
#button9.config(command=lambda:hala(9))

#############################################################################

button16=ttk.Button(root,text=' ')
button16.grid(row=3,column=0,sticky='snew',ipadx=40,ipady=40)
button16.config(text=board[15])
#button9.config(command=lambda:hala(9))

button17=ttk.Button(root,text=' ')
button17.grid(row=3,column=1,sticky='snew',ipadx=40,ipady=40)
button17.config(text=board[16])
#button9.config(command=lambda:hala(9))

button18=ttk.Button(root,text=' ')
button18.grid(row=3,column=2,sticky='snew',ipadx=40,ipady=40)
button18.config(text=board[17])
#button9.config(command=lambda:hala(9))

button19=ttk.Button(root,text=' ')
button19.grid(row=3,column=3,sticky='snew',ipadx=40,ipady=40)
button19.config(text=board[18])
#button9.config(command=lambda:hala(9))

button20=ttk.Button(root,text=' ')
button20.grid(row=3,column=4,sticky='snew',ipadx=40,ipady=40)
button20.config(text=board[19])
#######################################################################
button21=ttk.Button(root,text=' ')
button21.grid(row=4,column=0,sticky='snew',ipadx=40,ipady=40)
button21.config(text=board[20])
#button9.config(command=lambda:hala(9))

button22=ttk.Button(root,text=' ')
button22.grid(row=4,column=1,sticky='snew',ipadx=40,ipady=40)
button22.config(text=board[21])
#button9.config(command=lambda:hala(9))

button23=ttk.Button(root,text=' ')
button23.grid(row=4,column=2,sticky='snew',ipadx=40,ipady=40)
button23.config(text=board[22])
button23.config(command=lambda:SetLayout(22,'X'))
#button9.config(command=lambda:hala(9))

button24=ttk.Button(root,text=' ')
button24.grid(row=4,column=3,sticky='snew',ipadx=40,ipady=40)
button24.config(text=board[23])
button24.config(command=lambda:SetLayout(23,'X'))



button25=ttk.Button(root,text=' ')
button25.grid(row=4,column=4,sticky='snew',ipadx=40,ipady=40)
button25.config(text=board[24])
button25.config(command=lambda:SetLayout(24,'X'))
################################################################
root.rowconfigure(0,weight=1)
root.rowconfigure(1,weight=1)
root.rowconfigure(2,weight=1)
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)
root.columnconfigure(2,weight=1)
#
def main():
    """
    The main function holds the main UI for the tictactoe module.
    """
    while True:

        path = ""


        print("Would you like to play against:")
        print("[1] A human player.")
        print("[2] An AI player.")
        print("[3] two AI players play.")
        player = input("Please choose either 1, 2, 3 : ")
        if player not in ('1', '2', '3'):
            print("Please choose again.")
            continue

        algorithm_one = ""
        algorithm_two = ""
        if player == '2' or player == '3':
            print("Which algorithm would you like the AI to use?")
            print("[1] Easy")
            print("[2] Hard")
            algorithm_one = input("Please choose either 1 or 2: ")
            if algorithm_one not in ('1', '2'):
                print("Please choose again.")
                continue

        if player == '3':
            print("Which algorithm would you like the AI to use?")
            print("[1] Easy")
            print("[2] Hard")
            algorithm_two = input("Please choose either 1 or 2: ")
            if algorithm_two not in ('1', '2'):
                print("Please choose again.")
                continue

        algorithm_one = "Easy" if algorithm_one == '1' else "Hard"
        algorithm_two = "Easy" if algorithm_two == '1' else "Hard"

        game(board, path, player, algorithm_one, algorithm_two)

    print("Goodbye.")


def SetLayout(id,text):
    #id,text,=gettt()
    if(id==23):
        # button24.config(text=text)
        # button24.state(['disabled'])
        board[23]=text
        #ggg(board)
        #game(board, "", 'O', "Easy", "")
    # elif (id==6):
    #      button7.config(text=text)
    #      button7.state(['disabled'])
    # elif (id==10):
    #      button11.config(text=text)
    #      button11.state(['disabled'])
    # elif (id==4):
    #      button4.config(text=text)
    #      button4.state(['disabled'])
    # elif (id==5):
    #      button5.config(text=text)
    #      button5.state(['disabled'])
    # elif (id==6):
    #      button6.config(text=text)
    #      button6.state(['disabled'])
    # elif (id==7):
    #      button7.config(text=text)
    #      button7.state(['disabled'])
    # elif (id==8):
    #      button8.config(text=text)
    #      button8.state(['disabled'])
    # elif (id==9):
    #      button9.config(text=text)
    #      button9.state(['disabled'])




if __name__ == '__main__':
    main()
root.mainloop()