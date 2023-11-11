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
ball_count=0
wicket_count=0
def user_bat():

    
    def runs(bat_value):

        global ball_count,wicket_count
        over=dict["over"]
        total_balls=over*6
        total_wicket=dict["wicket"]
        total_runs=dict["runs"]["user"]
        target_run=dict["runs"]["bot"] + 1
        wicket=0

        
        ball_count += 1#------------ball_counting--------------#

        balls_left=total_balls - ball_count

        user_ball_count_text.configure(state=NORMAL)
        user_ball_count_text.delete('1.0',END)
        user_ball_count_text.insert(END,balls_left)
        user_ball_count_text.configure(state=DISABLED)
            
        ball_val = random.randint(0,6)
        bat_val_text.configure(state=NORMAL)
        bat_val_text.delete('1.0',END)
        bat_val_text.insert(END,bat_value)
        bat_val_text.configure(state=DISABLED)

        ball_val_text.configure(state=NORMAL)
        ball_val_text.delete('1.0',END)
        ball_val_text.insert(END,ball_val)
        ball_val_text.configure(state=DISABLED)
                
        print("bat ----",bat_value)
        print("bal------",ball_val)


        if bat_value==ball_val: #------------------------wicket -------------------------#
            print(wicket)
            
            wicket_count +=1     #-------------wicket count-------------#
            wicket_left=total_wicket - wicket_count

            wicket_gone_label=Label(user_bat_frame, text=f"Wicket No. - {wicket_count}", fg="red")
            wicket_gone_label.grid(row=12, column=0, columnspan=5, padx=10, pady=20)

            wicket_count_text.configure(state=NORMAL)
            wicket_count_text.delete('1.0',END)
            wicket_count_text.insert(END,wicket_left)
            wicket_count_text.configure(state=DISABLED)

            if wicket_count == total_wicket:
              
                wicket_gone_label=Label(user_bat_frame, text=f"Your Batting is over, Your total Score is {total_runs} ",fg="red", font=('Times New Roman', 15))
                wicket_gone_label.grid(row=13, column=0, columnspan=5, padx=10, pady=20)

                button_0.config(state=DISABLED)
                button_1.config(state=DISABLED)
                button_2.config(state=DISABLED)
                button_3.config(state=DISABLED)
                button_4.config(state=DISABLED)
                button_5.config(state=DISABLED)
                button_6.config(state=DISABLED)

                batting_over_next_button=Button(user_bat_frame,text="Next")
                batting_over_next_button.grid(row=14, column=0, columnspan=5, padx=10, pady=20)
                
        
        elif ball_count==total_balls:

            over_completed_label=Label(user_bat_frame, text=f"Your Batting is over, Your total Score is {total_runs} ",fg="red", font=('Times New Roman', 15))
            over_completed_label.grid(row=12, column=0, columnspan=5, padx=10, pady=20)

            button_0.config(state=DISABLED)
            button_1.config(state=DISABLED)
            button_2.config(state=DISABLED)
            button_3.config(state=DISABLED)
            button_4.config(state=DISABLED)
            button_5.config(state=DISABLED)
            button_6.config(state=DISABLED)
        


        else:
            if bat_value==0:
                bat_value=ball_val
            total_runs += bat_value

            your_score_text.configure(state=NORMAL)  #-------- Your total score ---------#
            your_score_text.delete('1.0',END)
            your_score_text.insert(END,total_runs) 
            your_score_text.configure(state=DISABLED)

            print("score = ",total_runs)
            print()
            dict["runs"]["user"]=total_runs
            if dict["toss"]["user"]=="ball":
                target_run=target_run-bat_value
                print("Target ",target_run)
            if target_run<=0:
                pass

    
    user_bat_frame = main_frame()
    user_bat_frame.grid(row=1,column=0, columnspan=5, padx=10, pady=10) 

  #------------- your score text -----------------------#

    your_score_label=Label(user_bat_frame, text="Your score", font=('Times New Roman', 12))
    your_score_label.grid(row=1, column=0, padx=10)

    your_score_text=Text(user_bat_frame,state=DISABLED,height=1,width=5)
    your_score_text.grid(row=2,column=0)
    
#-----------------Target score text -------------------------#

    if dict["toss"]["user"]=="ball":
        user_bat_target_label=Label(user_bat_frame, text="Target", font=('Times New Roman', 12))
        user_bat_target_label.grid(row=1, column=4, padx=10)

        user_bat_target_text=Text(user_bat_frame,state=DISABLED,height=1,width=5)
        user_bat_target_text.grid(row=2,column=4)

        # user_bat_target_text.configure(state=NORMAL)
        # user_bat_target_text.insert(END,target_run)

        # print(f"user target is {target_run} from {total_balls} balls in {total_wicket} wickets ")

    #----------------ball count text ----------------#

    over=dict["over"]
    total_balls=over*6

    user_ball_count_label=Label(user_bat_frame,text="Balls left")
    user_ball_count_label.grid(row=10, column=0, padx=10, pady=10)

    user_ball_count_text=Text(user_bat_frame,state=DISABLED, height=1, width=5)
    user_ball_count_text.grid(row=11, column=0)

    user_ball_count_text.configure(state=NORMAL)
    user_ball_count_text.delete('1.0',END)
    user_ball_count_text.insert(END,total_balls)
    user_ball_count_text.configure(state=DISABLED)
    

    #------------------Wicket Count text --------------------#

    total_wicket=dict["wicket"]

    wicket_count_label=Label(user_bat_frame,text="Wickets left")
    wicket_count_label.grid(row=10, column=4, padx=10, pady=10)

    wicket_count_text=Text(user_bat_frame,state=DISABLED, height=1, width=5)
    wicket_count_text.grid(row=11, column=4)

    wicket_count_text.configure(state=NORMAL)
    wicket_count_text.delete('1.0',END)
    wicket_count_text.insert(END,total_wicket)
    wicket_count_text.configure(state=DISABLED)

    #-------------------batting score text --------------------#

    you_are_batting_label=Label(user_bat_frame,text="You are Batting", font=('Times New Roman', 15,'bold'))
    you_are_batting_label.grid(row=3, column=0, columnspan=5, padx=10, pady=20)

    bat_val_label=Label(user_bat_frame,text="YOU",font=('Times New Roman', 13))
    bat_val_label.grid(row=4, column=1, padx=10, pady=4)

    bat_val_text=Text(user_bat_frame,state=DISABLED,height=1,width=5)
    bat_val_text.grid(row=5, column=1, padx=10 ,pady=4)

#------------------------bowling score text---------------#        

    ball_val_label=Label(user_bat_frame,text="BOT",font=('Times New Roman', 13))
    ball_val_label.grid(row=4, column=3, padx=10, pady=4)

    ball_val_text=Text(user_bat_frame,state=DISABLED,height=1,width=5)
    ball_val_text.grid(row=5, column=3, padx=10 ,pady=4)

    #------buttons---------------#      
    button_0 = Button(user_bat_frame, text="0", command=lambda:runs(0),padx=10)
    button_0.grid(row=7, column=2, padx=10, pady=10 )

    button_1 = Button(user_bat_frame, text="1", command=lambda:runs(1),padx=10)
    button_1.grid(row=8, column=1, padx=10, pady=10 )

    button_2 = Button(user_bat_frame, text="2", command=lambda:runs(2),padx=10)
    button_2.grid(row=8, column=2, padx=10, pady=10 )
    
    button_3 = Button(user_bat_frame, text="3", command=lambda:runs(3),padx=10)
    button_3.grid(row=8, column=3, padx=10, pady=10 )
        
    button_4 = Button(user_bat_frame, text="4", command=lambda:runs(4),padx=10)
    button_4.grid(row=9, column=1, padx=10, pady=10 )

    button_5 = Button(user_bat_frame, text="5", command=lambda:runs(5),padx=10)
    button_5.grid(row=9, column=2, padx=10, pady=10 )

    button_6 = Button(user_bat_frame, text="6", command=lambda:runs(6),padx=10)
    button_6.grid(row=9, column=3, padx=10, pady=10 )





def match(choice):
    if choice == "batting":
        dict["toss"]["user"]="bat"
        dict["toss"]["bot"]="ball"
        print("user win the Toss and choose batting ")
    else:
        dict["toss"]["user"]="ball"
        dict["toss"]["bot"]="bat"
        print("user win the Toss and choose balling")
    print(dict)
    if dict["toss"]["user"]=="bat":
    
        user_bat()
        


def bat_ball_choose():

    bat_ball_choose_frame=main_frame()
    bat_ball_choose_frame.grid(row=1,column=0, columnspan=2, padx=10, pady=10)

    if dict["toss_win"]["user"]==1:
        user_bat_ball_choice_label=Label(bat_ball_choose_frame,text="Select your Choice" ,font=('Times New Roman', 12, 'bold')) 
        user_bat_ball_choice_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        batting_button=Button(bat_ball_choose_frame, text=" Batting ", command=lambda:match("batting"))
        batting_button.grid(row=2, column=0, padx=10, pady=10)

        bowling_button=Button(bat_ball_choose_frame, text="Bowling", command=lambda:match("bowling"))
        bowling_button.grid(row=2, column=1, padx=10, pady=10)

    else:
        bot_bat_ball_choice=random.randint(0,1)
        print(f"bot put {bot_bat_ball_choice}")  
        if bot_bat_ball_choice==0:
            bot_choice_label=Label(bat_ball_choose_frame, text="bot choose batting and you have to ball" ,font=('Times New Roman', 13,))
            bot_choice_label.grid(row=1, column=0, columnspan=2, padx=10,pady=10)

            bat_ball_choosed_next=Button(bat_ball_choose_frame, text="Next",command=lambda:match("bowling"))
            bat_ball_choosed_next.grid(row=2, column=1, padx=10, pady=10)

            print("bot win the Toss and choose batting and you have to ball")
                    
        elif bot_bat_ball_choice==1:

            bot_choice_label=Label(bat_ball_choose_frame, text="bot choose bowling and you have to bat" ,font=('Times New Roman', 13))
            bot_choice_label.grid(row=1, column=0, columnspan=2, padx=10,pady=10)

            bat_ball_choosed_next=Button(bat_ball_choose_frame, text="Next",command=lambda:match("batting"))
            bat_ball_choosed_next.grid(row=2, column=1, padx=10, pady=10)

            print("bot win the toss and choose balling and you have to bat")

            

def toss_time(user_tossing):

    toss_time_frame=main_frame()
    toss_time_frame.grid(row=1,column=0,columnspan=2,padx=10,pady=10)

    bot_tossing=random.randint(1,6)
    print(bot_tossing)
    total=user_tossing+bot_tossing

    toss_time_label=Label(toss_time_frame,text=f"You Choose {user_tossing} and Bot put {bot_tossing}",font=('Times New Roman', 13))
    toss_time_label.grid(row=1,column=0,columnspan=2,padx=10,pady=10)

    if total & 1==0:
        for key,value in dict["toss_choose"].items():
                            
            if value=="even":
                dict["toss_win"][key]=1
                toss_result_label=Label(toss_time_frame,text=f"it is Even and {key} Won the Toss",font=('Times New Roman', 13))
                toss_result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    else:
        for key,value in dict["toss_choose"].items():
                            
            if value=="odd":
                dict["toss_win"][key]=1
                toss_result_label=Label(toss_time_frame,text=f"it is Odd and {key} Won the Toss",font=('Times New Roman', 13))
                toss_result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)  

    toss_time_button=Button(toss_time_frame, text=" Next ", command=bat_ball_choose)
    toss_time_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10 )
    

def odd_even_click(user_select_toss_option):

    if user_select_toss_option == "odd":
        dict["toss_choose"]["user"]="odd"
        dict["toss_choose"]["bot"]="even"
    elif user_select_toss_option == "even":
        dict["toss_choose"]["user"]="even"
        dict["toss_choose"]["bot"]="odd"

    odd_even_toss_frame=main_frame()
    odd_even_toss_frame.grid(row=1,column=0,columnspan=2,padx=10,pady=10)

    user_select_option_view_label=Label(odd_even_toss_frame,text=f"You Choose {user_select_toss_option}",font=('Times New Roman', 15, 'bold'))
    user_select_option_view_label.grid(row=1,column=0,columnspan=2,padx=10,pady=10)

    user_toss_number_label=Label(odd_even_toss_frame,text="Select a number Between 1 to 6 for Tossing" ,font=('Times New Roman', 13))
    user_toss_number_label.grid(row=2,column=0,columnspan=2,padx=10,pady=10)

    toss_val= IntVar()
    toss_val.set(1)

    user_toss_number_optionmenu=OptionMenu(odd_even_toss_frame, toss_val, *toss_list)
    user_toss_number_optionmenu.grid(row=3,column=0,padx=10,pady=10,columnspan=2)

    toss_submit_button=Button(odd_even_toss_frame,text="Next", command=lambda:toss_time(toss_val.get()))
    toss_submit_button.grid(row=4,column=0,columnspan=2,padx=10,pady=10)

    
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


exit_button=Button(exit_frame,text="Exit",fg="white", bg="red", width=50, command=window.quit,pady=3,font=('Times New Roman', 11))
exit_button.grid(row=10, column=0, columnspan=5 )

#------------------------Title Frame----------------#
game_title_label=Label(title_frame,text="ODD OR EVEN GAME", font=('Times New Roman', 19, 'bold'))
game_title_label.grid(row=0, column=0, columnspan=5, padx=20, pady=10)

window.mainloop()