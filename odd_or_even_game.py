from tkinter import *
import random



window=Tk()

window.title("Odd or Even Game")

dict={
    "toss_choose":{"user":0,"bot":0},
    "toss_win":{"user":0,"bot":0},
    "toss":{"user":0,"bot":0},
    "runs":{"user":0,"bot":0},
    "over":0,
    "wicket":0,
    "wicket_count":{"bot":0,"user":0}
    }

toss_list=[1,2,3,4,5,6]
bat_ball_list=[0,1,2,3,4,5,6]
over_list=[1,2,3,4,5,6,7,8,9,10]
wicket_list=[1,2,3,4,5]

#--------------------frames--------------------------------------#
container_frame=Frame(window)
container_frame.pack()

title_frame=Frame(container_frame)
title_frame.grid(row=0,column=0)

exit_frame=Frame(container_frame)
exit_frame.grid(row=10,column=0)


main_frame_list=[]
def main_frame():
    global frame
    if len(main_frame_list)>0:
        main_frame_destroyer()
    frame=Frame(container_frame)
    main_frame_list.append(frame)

    return frame

def main_frame_destroyer():
    frame.destroy()
    main_frame_list.clear()






#-------------------ODD/EVEN Toss------------------------------#

def toss_time(user_tossing):

    toss_time_label=Label(toss_time_frame,text=f"You Choose {user_tossing} and Bot put {bot_tossing}",font=('Times New Roman', 12, 'bold'))
    toss_time_label.grid(row=1,column=0,columnspan=2,padx=10,pady=10)

    toss_time_frame=main_frame()
    toss_time_frame.grid(row=1,column=0,columnspan=2,padx=10,pady=10)

    bot_tossing=random.randint(1,6)
    total=user_tossing+bot_tossing
    
    
    if total & 1==0:
        for key,value in dict["toss_choose"].items():
                            
            if value=="even":
                dict["toss_win"][key]=1
                toss_result_label=Label(toss_time_frame,text=f"it is Even and {key} Won the Toss",font=('Times New Roman', 12, 'bold'))
                toss_result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    else:
        for key,value in dict["toss_choose"].items():
                            
            if value=="odd":
                dict["toss_win"][key]=1
                toss_result_label=Label(toss_time_frame,text=f"it is Odd and {key} Won the Toss",font=('Times New Roman', 12, 'bold'))
                toss_result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)  

    
    

def odd_even_click(user_select_toss_option):

    if user_select_toss_option == "odd":
        dict["toss_choose"]["user"]="odd"
        dict["toss_choose"]["bot"]="even"
    elif user_select_toss_option == "even":
        dict["toss_choose"]["user"]="even"
        dict["toss_choose"]["bot"]="odd"

    print(dict)

    odd_even_toss_frame=main_frame()
    odd_even_toss_frame.grid(row=1,column=0,columnspan=2,padx=10,pady=10)

    user_select_option_view_label=Label(odd_even_toss_frame,text=f"You Choose {user_select_toss_option}",font=('Times New Roman', 15, 'bold'))
    user_select_option_view_label.grid(row=1,column=0,columnspan=2,padx=10,pady=10)

    user_toss_number_label=Label(odd_even_toss_frame,text="Select a number Between 1 to 6 for Tossing")
    user_toss_number_label.grid(row=2,column=0,columnspan=2,padx=10,pady=10)

    toss_val= IntVar()
    toss_val.set(1)

    user_toss_number_optionmenu=OptionMenu(odd_even_toss_frame, toss_val, *toss_list)
    user_toss_number_optionmenu.grid(row=3,column=0,padx=10,pady=10,columnspan=2)

    toss_submit_button=Button(odd_even_toss_frame,text="Next", command=lambda:toss_time(toss_val.get()))
    toss_submit_button.grid(row=4,column=0,columnspan=2)

    
def toss(over,wicket):

    dict["over"]=over
    dict["wicket"]=wicket

    odd_even_choose_frame=main_frame()
    odd_even_choose_frame.grid(row=1,column=0,columnspan=2,padx=10,pady=10)

    title_label_for_odd_even_choose=Label(odd_even_choose_frame,text="Odd/Even choose ",font=('Times New Roman', 15, 'bold',UNDERLINE))
    title_label_for_odd_even_choose.grid(row=1,column=0,columnspan=2,padx=20,pady=20)

    odd_button=Button(odd_even_choose_frame,text="ODD", command=lambda:odd_even_click("odd"))
    odd_button.grid(row=2,column=0,padx=20,pady=10)

    even_button=Button(odd_even_choose_frame,text="EVEN", command=lambda:odd_even_click("even"))
    even_button.grid(row=2,column=1,padx=20,pady=10)



wicket_over_select_frame=main_frame()
wicket_over_select_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

over_select_label=Label(wicket_over_select_frame, text="Over")
over_select_label.grid(row=1, column=0, padx=10, pady=2)

wicket_select_label=Label(wicket_over_select_frame, text="Wicket")
wicket_select_label.grid(row=1, column=1, padx=10, pady=2)


over_menu=IntVar()
over_menu.set(1)

over_option_menu=OptionMenu(wicket_over_select_frame, over_menu, *over_list)
over_option_menu.grid(row=2,column=0,padx=10,pady=2)

wicket_menu=IntVar()
wicket_menu.set(1)

wicket_option_menu=OptionMenu(wicket_over_select_frame, wicket_menu, *wicket_list)
wicket_option_menu.grid(row=2,column=1,padx=10,pady=2)

wicket_over_select_button=Button(wicket_over_select_frame, text="Next", command=lambda:toss(over_menu.get(),wicket_menu.get()))
wicket_over_select_button.grid(row=3, column=0, columnspan=2, padx=10, pady=20)




#------------------------Exit frame-----------------#


exit_button=Button(exit_frame,text="Exit",fg="white", bg="red", width=50, command=window.quit)
exit_button.grid(row=10,column=0,columnspan=2)

#------------------------Title Frame----------------#
game_title_label=Label(title_frame,text="ODD OR EVEN GAME", font=('Times New Roman', 19, 'bold'))
game_title_label.grid(row=0, column=0, columnspan=2, padx=20, pady=10)

window.mainloop()