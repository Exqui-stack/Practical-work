import tkinter as extic

from tkinter import messagebox

def display_label_frame():
    header_label_frame.grid(row=0, column=0, padx=25, pady=15)
    body_label_frame.grid(row=1, column=0, padx=25, pady=15)
    foot_label_frame.grid(row=2, column=0, padx=25, pady=10)



def button_clicked(b):
    global clicking, count
    

    if b["text"] ==" " and clicking == True:
        b["text"] = "X"
        count += 1
        clicking = False
        checkwin()
        
    elif b["text"] ==" " and clicking == False:
        b["text"] = "O"
        count += 1
        clicking = True
        checkwin()
    else:
         messagebox.showerror("That box has already been occupied\n Select another box")

def display_body_widget():
    global button1, button2, button3, button4, button5, button6, button7, button8, button9, clicking
    button1= extic.Button(body_label_frame, text=" ", font=('Arial', 12, 'bold'), width=7 , height=3, background='yellow', command=lambda: button_clicked(button1))
    button1.grid(row=0, column=0)
    button2= extic.Button(body_label_frame, text=" ", font=('Arial', 12, 'bold'), width=7 , height=3, background='yellow', command=lambda: button_clicked(button2))
    button2.grid(row=0, column=1)
    button3= extic.Button(body_label_frame, text=" ", font=('Arial', 12, 'bold'), width=7 , height=3, background='yellow', command=lambda: button_clicked(button3))
    button3.grid(row=0, column=2)
    button4= extic.Button(body_label_frame, text=" ", font=('Arial', 12, 'bold'), width=7 , height=3, background='yellow', command=lambda: button_clicked(button4))
    button4.grid(row=1, column=0)
    button5= extic.Button(body_label_frame, text=" ", font=('Arial', 12, 'bold'), width=7 , height=3, background='yellow', command=lambda: button_clicked(button5))
    button5.grid(row=1, column=1)
    button6= extic.Button(body_label_frame, text=" ", font=('Arial', 12, 'bold'), width=7 , height=3, background='yellow', command=lambda: button_clicked(button6))
    button6.grid(row=1, column=2)
    button7= extic.Button(body_label_frame, text=" ", font=('Arial', 12, 'bold'), width=7 , height=3, background='yellow', command=lambda: button_clicked(button7))
    button7.grid(row=2, column=0)
    button8= extic.Button(body_label_frame, text=" ", font=('Arial', 12, 'bold'), width=7 , height=3, background='yellow', command=lambda: button_clicked(button8))
    button8.grid(row=2, column=1)
    button9= extic.Button(body_label_frame, text=" ", font=('Arial', 12, 'bold'), width=7 , height=3, background='yellow', command=lambda: button_clicked(button9))
    button9.grid(row=2, column=2)




def restart():
    global button1, button2, button3, button4, button5, button6, button7, button8, button9
    global clicking, count
    clicking = True
    count = 0
    button1= extic.Button(body_label_frame, text=" ", font=('Arial', 12, 'bold'), width=7 , height=3, background='yellow', command=lambda: button_clicked(button1))
    button1.grid(row=0, column=0)
    button2= extic.Button(body_label_frame, text=" ", font=('Arial', 12, 'bold'), width=7 , height=3, background='yellow', command=lambda: button_clicked(button2))
    button2.grid(row=0, column=1)
    button3= extic.Button(body_label_frame, text=" ", font=('Arial', 12, 'bold'), width=7 , height=3, background='yellow', command=lambda: button_clicked(button3))
    button3.grid(row=0, column=2)
    button4= extic.Button(body_label_frame, text=" ", font=('Arial', 12, 'bold'), width=7 , height=3, background='yellow', command=lambda: button_clicked(button4))
    button4.grid(row=1, column=0)
    button5= extic.Button(body_label_frame, text=" ", font=('Arial', 12, 'bold'), width=7 , height=3, background='yellow', command=lambda: button_clicked(button5))
    button5.grid(row=1, column=1)
    button6= extic.Button(body_label_frame, text=" ", font=('Arial', 12, 'bold'), width=7 , height=3, background='yellow', command=lambda: button_clicked(button6))
    button6.grid(row=1, column=2)
    button7= extic.Button(body_label_frame, text=" ", font=('Arial', 12, 'bold'), width=7 , height=3, background='yellow', command=lambda: button_clicked(button7))
    button7.grid(row=2, column=0)
    button8= extic.Button(body_label_frame, text=" ", font=('Arial', 12, 'bold'), width=7 , height=3, background='yellow', command=lambda: button_clicked(button8))
    button8.grid(row=2, column=1)
    button9= extic.Button(body_label_frame, text=" ", font=('Arial', 12, 'bold'), width=7 , height=3, background='yellow', command=lambda: button_clicked(button9))
    button9.grid(row=2, column=2)


def display_footer_widget():
    global restart
    restart= extic.Button(foot_label_frame, text="Restart ", font=('Arial', 12, 'bold'), width=7 , height=2, background='yellow', command=restart)
    restart.grid(row=3, column=1)



   

def checkwin():
    global winner, player1_score, player2_score, player1_label, player2_label
    winner = False

    if  button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X":
        button1.config(bg="blue")
        button2.config(bg="blue")
        button3.config(bg="blue")
        winner = True
        player1_score +=1
        player1_label.config(text=f'player1 Score{player1_score}')
        messagebox.showinfo("Exquisite game!!!", "User X Wins")
        disable_all_buttons()
    elif button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X":
        button4.config(bg="blue")
        button5.config(bg="blue")
        button6.config(bg="blue")
        winner = True
        player1_score +=1
        player1_label.config(text=f'player1 Score{player1_score}')

        messagebox.showinfo("Exquisite game!!!", "User X Wins")
        disable_all_buttons()
    elif button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X":
        button7.config(bg="blue")
        button8.config(bg="blue")
        button9.config(bg="blue")
        winner = True
        player1_score +=1
        player1_label.config(text=f'player1 Score{player1_score}')

        messagebox.showinfo("Exquisite game!!!", "User X Wins")
        disable_all_buttons()
    elif button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X":
        button1.config(bg="blue")
        button4.config(bg="blue")
        button7.config(bg="blue")
        winner = True
        player1_score +=1
        player1_label.config(text=f'player1 Score{player1_score}')

        messagebox.showinfo("Exquisite game!!!", "User X Wins")
        disable_all_buttons()

    elif button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X":
        button2.config(bg="blue")
        button5.config(bg="blue")
        button8.config(bg="blue")
        winner = True
        player1_score +=1
        player1_label.config(text=f'player1 Score{player1_score}')

        messagebox.showinfo("Exquisite game!!!", "User X Wins")
        disable_all_buttons()
    
    elif button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X":
        button3.config(bg="blue")
        button6.config(bg="blue")
        button9.config(bg="blue")
        winner = True
        player1_score +=1
        player1_label.config(text=f'player1 Score{player1_score}')
        messagebox.showinfo("Exquisite game!!!", "User X Wins")
        disable_all_buttons()

    elif button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X":
        button1.config(bg="blue")
        button5.config(bg="blue")
        button9.config(bg="blue")
        winner = True
        player1_score +=1
        player1_label.config(text=f'player1 Score{player1_score}')
        messagebox.showinfo("Exquisite game!!!", "User X Wins")
        disable_all_buttons()

    elif button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X":
        button3.config(bg="blue")
        button5.config(bg="blue")
        button7.config(bg="blue")
        winner = True
        player1_score +=1
        player1_label.config(text=f'player1 Score{player1_score}')
        messagebox.showinfo("Exquisite game!!!", "User X Wins") 
        disable_all_buttons()  


        
    elif  button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O":
        button1.config(bg="blue")
        button2.config(bg="blue")
        button3.config(bg="blue")
        winner = True
        player2_score +=1
        player2_label.config(text=f'player2 Score{player2_score}')

        messagebox.showinfo("Exquisite game!!!", "User O Wins")
        disable_all_buttons()
    elif button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O":
        button4.config(bg="blue")
        button5.config(bg="blue")
        button6.config(bg="blue")
        winner = True
        player2_score +=1
        player2_label.config(text=f'player2 Score{player2_score}')
        messagebox.showinfo("Exquisite game!!!", "User O Wins")
        disable_all_buttons()
    elif button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O":
        button7.config(bg="blue")
        button8.config(bg="blue")
        button9.config(bg="blue")
        winner = True
        player2_score +=1
        player2_label.config(text=f'player2 Score{player2_score}')
        messagebox.showinfo("Exquisite game!!!", "User O Wins")
        disable_all_buttons()
    elif button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O":
        button1.config(bg="blue")
        button4.config(bg="blue")
        button7.config(bg="blue")
        winner = True
        player2_score +=1
        player2_label.config(text=f'player2 Score{player2_score}')
        messagebox.showinfo("Exquisite game!!!", "User O Wins")
        disable_all_buttons()

    elif button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O":
        button2.config(bg="blue")
        button5.config(bg="blue")
        button8.config(bg="blue")
        winner = True
        player2_score +=1
        player2_label.config(text=f'player2 Score{player2_score}')
        messagebox.showinfo("Exquisite game!!!", "User O Wins")
        disable_all_buttons()
    elif button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O":
        button3.config(bg="blue")
        button6.config(bg="blue")
        button9.config(bg="blue")
        winner = True
        player2_score +=1
        player2_label.config(text=f'player2 Score{player2_score}')
        messagebox.showinfo("Exquisite game!!!", "User O Wins")
        disable_all_buttons()

    elif button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O":
        button1.config(bg="blue")
        button5.config(bg="blue")
        button9.config(bg="blue")
        winner = True
        player2_score +=1
        player2_label.config(text=f'player2 Score{player2_score}')

        messagebox.showinfo("User Y Wins!!!")
        disable_all_buttons()

    elif button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O":
        button3.config(bg="blue")
        button5.config(bg="blue")
        button7.config(bg="blue")
        winner = True
        player2_score +=1
        player2_label.config(text=f'player2 Score{player2_score}')
        messagebox.showinfo("Exquisite game!!!", "User O Wins") 
        disable_all_buttons()

    
def display_header_widget():
    global player1_label, player2_label
    player1_label = extic.Label(header_label_frame, text= f'Player1 Score:{player1_score}')
    player2_label = extic.Label(header_label_frame, text= f'Player2 Score:{player2_score}')

    player1_label.grid(row=0, column= 0)
    player2_label.grid(row=0, column= 1)  

   

def disable_all_buttons():
    button1.config(state="disabled")
    button2.config(state="disabled")
    button3.config(state="disabled")
    button4.config(state="disabled")
    button5.config(state="disabled")
    button6.config(state="disabled")
    button7.config(state="disabled")
    button8.config(state="disabled")
    button9.config(state="disabled")


def menu():
    display_label_frame()
    display_header_widget()
    display_body_widget()
    display_footer_widget()


if __name__ == "__main__":

    main_window = extic.Tk()
    main_window.title('Exquisite TicTacToe')
    main_window.geometry('290x360')
    main_window.resizable(0,0)
    main_window.config(bg='Blue')

    clicking = True
    count = 0
    player1_score = 0
    player2_score = 0

    

    header_label_frame = extic.LabelFrame (main_window, background='yellow', borderwidth=0)
    body_label_frame = extic.LabelFrame(main_window, borderwidth=0)
    foot_label_frame = extic.LabelFrame(main_window, borderwidth=0)



    menu()
    
    
    #checkwin()
    #disable_all_buttons()
    #button_clicked()
    
   





    main_window.mainloop()