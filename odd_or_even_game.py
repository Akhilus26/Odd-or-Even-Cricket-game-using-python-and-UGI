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

def win_decision():
    
    if dict["toss"]["user"]=="bat":

        user_total_runs=dict["runs"]["user"] 
        bot_total_runs=dict["runs"]["bot"]
        if user_total_runs>bot_total_runs:
            wining_secision_label=Label(user_ball_frame, text=f"Congratulations!, You Won The Match by {user_total_runs-bot_total_runs} runs",fg="red", font=('Times New Roman', 15))
            wining_secision_label.grid(row=14, column=0, columnspan=5, padx=10, pady=20)
            print(f"Congratulations!, You Won The Match by {user_total_runs-bot_total_runs} runs")
        elif user_total_runs<bot_total_runs:
            total_wicket=dict["wicket_count"]["bot"]
            total_wicket_have=dict["wicket"]-total_wicket
            wining_secision_label=Label(user_ball_frame, text=f"bot won the match by {total_wicket_have} wickets, better luck Next time",fg="red", font=('Times New Roman', 15))
            wining_secision_label.grid(row=14, column=0, columnspan=5, padx=10, pady=20)
            print(f"bot won the match by {total_wicket_have} wickets, better luck Next time")
        else:
            wining_secision_label=Label(user_ball_frame, text="draw",fg="red", font=('Times New Roman', 15))
            wining_secision_label.grid(row=14, column=0, columnspan=5, padx=10, pady=20)
            print("draw")

    elif dict["toss"]["user"]=="ball":
          
        bot_total_runs=dict["runs"]["bot"]
        user_total_runs=dict["runs"]["user"]

        if user_total_runs>bot_total_runs:
            total_wicket=dict["wicket_count"]["user"]
            total_wicket_have=dict["wicket"]-total_wicket
            wining_secision_label=Label(user_bat_frame, text=f"Congratulations!, You Won The Match by {total_wicket_have} wickets",fg="red", font=('Times New Roman', 15))
            wining_secision_label.grid(row=14, column=0, columnspan=5, padx=10, pady=20)
            print(f"Congratulations!, You Won The Match by {total_wicket_have} wickets")
        elif user_total_runs<bot_total_runs:
            wining_secision_label=Label(user_bat_frame, text=f"bot won the match by {bot_total_runs-user_total_runs} runs",fg="red", font=('Times New Roman', 15))
            wining_secision_label.grid(row=14, column=0, columnspan=5, padx=10, pady=20)
            print(f"bot won the match by {bot_total_runs-user_total_runs} runs, better luck Next time")
        else:
            wining_secision_label=Label(user_bat_frame, text="draw",fg="red", font=('Times New Roman', 15))
            wining_secision_label.grid(row=14, column=0, columnspan=5, padx=10, pady=20)
            print("draw")


user_ball_count=0
user_ball_wicket_count=0


def user_ball():
    global user_ball_frame

    def ball(ball_value):
        print(ball_value)
        global user_ball_count,user_ball_wicket_count,target_run
        target_run=dict["runs"]["user"]

        over=dict["over"]
        total_balls=over*6
        
        total_wicket=dict["wicket"]
        
        total_runs=dict["runs"]["bot"]
        print("total_target - ",target_run)


        user_ball_count += 1
        balls_left=total_balls - user_ball_count

        user_ball_count_text.configure(state=NORMAL)
        user_ball_count_text.delete('1.0',END)
        user_ball_count_text.insert(END,balls_left)
        user_ball_count_text.configure(state=DISABLED)

        ball_val_text.configure(state=NORMAL)
        ball_val_text.delete('1.0',END)
        ball_val_text.insert(END,ball_value)
        ball_val_text.configure(state=DISABLED)

        bat_value = random.randint(0,6)
        bat_val_text.configure(state=NORMAL)
        bat_val_text.delete('1.0',END)
        bat_val_text.insert(END,bat_value)
        bat_val_text.configure(state=DISABLED)
        print("bat val------", bat_value)
        print('ball val----',ball_value)

        if bat_value == ball_value:
            print("wicket")
            user_ball_wicket_count +=1
            wicket_left = total_wicket - user_ball_wicket_count

            wicket_count_text.configure(state=NORMAL)
            wicket_count_text.delete('1.0',END)
            wicket_count_text.insert(END,wicket_left)
            wicket_count_text.configure(state=DISABLED)

            wicket_gone_label=Label(user_ball_frame, text=f"Wicket No. - {user_ball_wicket_count}", fg="red", font=('Times New Roman', 12))
            wicket_gone_label.grid(row=12, column=0, columnspan=5, padx=10, pady=20)

            if user_ball_wicket_count == total_wicket:

                button_0.config(state=DISABLED)
                button_1.config(state=DISABLED)
                button_2.config(state=DISABLED)
                button_3.config(state=DISABLED)
                button_4.config(state=DISABLED)
                button_5.config(state=DISABLED)
                button_6.config(state=DISABLED)
                if dict["toss"]["user"]=="bat":
                    win_decision()
                elif dict["toss"]["user"]=="ball":
                    wicket_full_gone_label=Label(user_ball_frame, text=f"bot Batting is over, Your bot Score is {total_runs} \nYou need to chasse",fg="red", font=('Times New Roman', 15))
                    wicket_full_gone_label.grid(row=13, column=0, columnspan=5, padx=10, pady=20)

                    batting_over_next_button=Button(user_ball_frame,text="Next",command=user_bat)
                    batting_over_next_button.grid(row=14, column=0, columnspan=5, padx=10, pady=20)
                    

        elif balls_left+1 == 0:
            user_ball_count_text.configure(state=NORMAL)
            user_ball_count_text.delete('1.0',END)
            user_ball_count_text.insert(END,0)
            user_ball_count_text.configure(state=DISABLED)

            bat_val_text.configure(state=NORMAL)
            bat_val_text.delete('1.0',END)
            bat_val_text.configure(state=DISABLED)

            ball_val_text.configure(state=NORMAL)
            ball_val_text.delete('1.0',END)
            ball_val_text.configure(state=DISABLED)

            button_0.config(state=DISABLED)
            button_1.config(state=DISABLED)
            button_2.config(state=DISABLED)
            button_3.config(state=DISABLED)
            button_4.config(state=DISABLED)
            button_5.config(state=DISABLED)
            button_6.config(state=DISABLED)
            if dict["toss"]["user"]=="bat":
                    win_decision()
            elif dict["toss"]["user"]=="ball":
                    wicket_full_gone_label=Label(user_ball_frame, text=f"bot Batting is over, Your bot Score is {total_runs} \nYou need to chasse",fg="red", font=('Times New Roman', 15))
                    wicket_full_gone_label.grid(row=13, column=0, columnspan=5, padx=10, pady=20)

                    batting_over_next_button=Button(user_ball_frame,text="Next",command=user_bat)
                    batting_over_next_button.grid(row=14, column=0, columnspan=5, padx=10, pady=20)
               

        else:
            print("elses")
            if bat_value==0:
                bat_value=ball_value
            total_runs += bat_value

            bot_score_text.configure(state=NORMAL)  #-------- Your total score ---------#
            bot_score_text.delete('1.0',END)
            bot_score_text.insert(END,total_runs) 
            bot_score_text.configure(state=DISABLED)
            
            dict["runs"]["bot"]=total_runs
            
            if dict["toss"]["user"]=="bat":
                target_run=target_run-bat_value
                print("Target ",target_run)
                if target_run<=0:
                    win_decision()
                                              


        


    user_ball_frame = main_frame()
    user_ball_frame.grid(row=1,column=0, columnspan=5, padx=10, pady=10) 

  #------------- bot score text -----------------------#

    bot_score_label=Label(user_ball_frame, text="bot score", font=('Times New Roman', 12))
    bot_score_label.grid(row=1, column=0, padx=10)

    bot_score_text=Text(user_ball_frame,state=DISABLED,height=1,width=5)
    bot_score_text.grid(row=2,column=0)
    
    #-----------------Target score text -------------------------#

    if dict["toss"]["user"]=="bat":

        target_run=dict["runs"]["user"] + 1

        bot_bat_target_label=Label(user_ball_frame, text="Target", font=('Times New Roman', 12))
        bot_bat_target_label.grid(row=1, column=4, padx=10)

        bot_bat_target_text=Text(user_ball_frame,state=DISABLED,height=1,width=5)
        bot_bat_target_text.grid(row=2,column=4)

        bot_bat_target_text.configure(state=NORMAL)
        bot_bat_target_text.delete('1.0',END)
        bot_bat_target_text.insert(END,target_run)
        bot_bat_target_text.configure(state=DISABLED)

        # print(f"user target is {target_run} from {total_balls} balls in {total_wicket} wickets ")

    #----------------ball count text ----------------#

    over=dict["over"]
    total_balls=over*6

    user_ball_count_label=Label(user_ball_frame,text="Balls left")
    user_ball_count_label.grid(row=10, column=0, padx=10, pady=10)

    user_ball_count_text=Text(user_ball_frame,state=DISABLED, height=1, width=5)
    user_ball_count_text.grid(row=11, column=0)

    user_ball_count_text.configure(state=NORMAL)
    user_ball_count_text.delete('1.0',END)
    user_ball_count_text.insert(END,total_balls)
    user_ball_count_text.configure(state=DISABLED)
    

    #------------------Wicket Count text --------------------#

    total_wicket=dict["wicket"]

    wicket_count_label=Label(user_ball_frame,text="Wickets left")
    wicket_count_label.grid(row=10, column=4, padx=10, pady=10)

    wicket_count_text=Text(user_ball_frame,state=DISABLED, height=1, width=5)
    wicket_count_text.grid(row=11, column=4)

    wicket_count_text.configure(state=NORMAL)
    wicket_count_text.delete('1.0',END)
    wicket_count_text.insert(END,total_wicket)
    wicket_count_text.configure(state=DISABLED)

    #-------------------batting score text --------------------#

    you_are_balling_label=Label(user_ball_frame,text="You are Bowling", font=('Times New Roman', 15,'bold'))
    you_are_balling_label.grid(row=3, column=0, columnspan=5, padx=10, pady=20)

    ball_val_label=Label(user_ball_frame,text="YOU",font=('Times New Roman', 13))
    ball_val_label.grid(row=4, column=1, padx=10, pady=4)

    ball_val_text=Text(user_ball_frame,state=DISABLED,height=1,width=5)
    ball_val_text.grid(row=5, column=1, padx=10 ,pady=4)

    #------------------------bowling score text---------------#        

    bat_val_label=Label(user_ball_frame,text="BOT",font=('Times New Roman', 13))
    bat_val_label.grid(row=4, column=3, padx=10, pady=4)

    bat_val_text=Text(user_ball_frame,state=DISABLED,height=1,width=5)
    bat_val_text.grid(row=5, column=3, padx=10 ,pady=4)

    #------buttons---------------#      
    button_0 = Button(user_ball_frame, text="0", command=lambda:ball(0),padx=10)
    button_0.grid(row=7, column=2, padx=10, pady=10 )

    button_1 = Button(user_ball_frame, text="1", command=lambda:ball(1),padx=10)
    button_1.grid(row=8, column=1, padx=10, pady=10 )

    button_2 = Button(user_ball_frame, text="2", command=lambda:ball(2),padx=10)
    button_2.grid(row=8, column=2, padx=10, pady=10 )
    
    button_3 = Button(user_ball_frame, text="3", command=lambda:ball(3),padx=10)
    button_3.grid(row=8, column=3, padx=10, pady=10 )
        
    button_4 = Button(user_ball_frame, text="4", command=lambda:ball(4),padx=10)
    button_4.grid(row=9, column=1, padx=10, pady=10 )

    button_5 = Button(user_ball_frame, text="5", command=lambda:ball(5),padx=10)
    button_5.grid(row=9, column=2, padx=10, pady=10 )

    button_6 = Button(user_ball_frame, text="6", command=lambda:ball(6),padx=10)
    button_6.grid(row=9, column=3, padx=10, pady=10 )
    


user_bat_ball_count=1
user_bat_wicket_count=0
def user_bat():
    global user_bat_frame
    
    def runs(bat_value):

        global user_bat_ball_count,user_bat_wicket_count
        over=dict["over"]
        total_balls=over*6+1
        total_wicket=dict["wicket"]
        total_runs=dict["runs"]["user"]
        target_run=dict["runs"]["bot"] + 1
        wicket=0

        
        user_bat_ball_count += 1#------------ball_counting--------------#

        balls_left=total_balls - user_bat_ball_count

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
            
            user_bat_wicket_count +=1     #-------------wicket count-------------#
            wicket_left=total_wicket - user_bat_wicket_count

            wicket_gone_label=Label(user_bat_frame, text=f"Wicket No. - {user_bat_wicket_count}", fg="red",font=('Times New Roman', 12))
            wicket_gone_label.grid(row=12, column=0, columnspan=5, padx=10, pady=20)

            wicket_count_text.configure(state=NORMAL)
            wicket_count_text.delete('1.0',END)
            wicket_count_text.insert(END,wicket_left)
            wicket_count_text.configure(state=DISABLED)

            if user_bat_wicket_count == total_wicket:
              
                button_0.config(state=DISABLED)
                button_1.config(state=DISABLED)
                button_2.config(state=DISABLED)
                button_3.config(state=DISABLED)
                button_4.config(state=DISABLED)
                button_5.config(state=DISABLED)
                button_6.config(state=DISABLED)
                
                if dict["toss"]["user"]=="bat":

                    wicket_full_gone_label=Label(user_bat_frame, text=f"Your Batting is over, Your total Score is {total_runs} \nbot need to chasse",fg="red", font=('Times New Roman', 15))
                    wicket_full_gone_label.grid(row=13, column=0, columnspan=5, padx=10, pady=20)

                    batting_over_next_button=Button(user_bat_frame,text="Next",command=user_ball)
                    batting_over_next_button.grid(row=14, column=0, columnspan=5, padx=10, pady=20)

                elif dict["toss"]["user"]=="ball":

                    win_decision()

                
        
        elif balls_left+1==0:
            
            user_ball_count_text.configure(state=NORMAL)
            user_ball_count_text.delete('1.0',END)
            user_ball_count_text.insert(END,0)
            user_ball_count_text.configure(state=DISABLED)

            bat_val_text.configure(state=NORMAL)
            bat_val_text.delete('1.0',END)
            bat_val_text.configure(state=DISABLED)

            ball_val_text.configure(state=NORMAL)
            ball_val_text.delete('1.0',END)
            ball_val_text.configure(state=DISABLED)



            button_0.config(state=DISABLED)
            button_1.config(state=DISABLED)
            button_2.config(state=DISABLED)
            button_3.config(state=DISABLED)
            button_4.config(state=DISABLED)
            button_5.config(state=DISABLED)
            button_6.config(state=DISABLED)

            if dict["toss"]["user"]=="bat":

                over_completed_label=Label(user_bat_frame, text=f"Your Batting is over, Your total Score is {total_runs} \nbot need to chasse ",fg="red", font=('Times New Roman', 15))
                over_completed_label.grid(row=12, column=0, columnspan=5, padx=10, pady=20)

                batting_over_next_button=Button(user_bat_frame,text="Next",command=user_ball)
                batting_over_next_button.grid(row=14, column=0, columnspan=5, padx=10, pady=20)

            elif dict["toss"]["user"]=="ball":

                win_decision()



        else:
            if bat_value==0:
                bat_value=ball_val
            total_runs += bat_value
            print(total_runs)

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
                    win_decision()
    
    
    user_bat_frame = main_frame()
    user_bat_frame.grid(row=1,column=0, columnspan=5, padx=10, pady=10) 

  #------------- your score text -----------------------#

    your_score_label=Label(user_bat_frame, text="Your score", font=('Times New Roman', 12))
    your_score_label.grid(row=1, column=0, padx=10)

    your_score_text=Text(user_bat_frame,state=DISABLED,height=1,width=5)
    your_score_text.grid(row=2,column=0)
    
    #-----------------Target score text -------------------------#

    if dict["toss"]["user"]=="ball":
        target_run=dict["runs"]["bot"] + 1

        user_bat_target_label=Label(user_bat_frame, text="Target", font=('Times New Roman', 12))
        user_bat_target_label.grid(row=1, column=4, padx=10)

        user_bat_target_text=Text(user_bat_frame,state=DISABLED,height=1,width=5)
        user_bat_target_text.grid(row=2,column=4)

        user_bat_target_text.configure(state=NORMAL)
        user_bat_target_text.insert(END,target_run)
        user_bat_target_text.configure(state=DISABLED)

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
        

    if dict["toss"]["user"]== "ball":
        user_ball()
        


def bat_ball_choose():

    bat_ball_choose_frame=main_frame()
    bat_ball_choose_frame.grid(row=1,column=0, columnspan=2, padx=10, pady=10)

    if dict["toss_win"]["user"]==1:
        user_bat_ball_choice_label=Label(bat_ball_choose_frame,text="Select your Choice" ,font=('Times New Roman', 18)) 
        user_bat_ball_choice_label.grid(row=1, column=0, columnspan=2, padx=10, pady=20)

        batting_button=Button(bat_ball_choose_frame, text=" Batting ", command=lambda:match("batting"), font=('Times New Roman', 15))
        batting_button.grid(row=2, column=0, padx=10, pady=30)

        bowling_button=Button(bat_ball_choose_frame, text="Bowling", command=lambda:match("bowling"), font=('Times New Roman', 15))
        bowling_button.grid(row=2, column=1, padx=10, pady=30)

    else:
        bot_bat_ball_choice=random.randint(0,1)
        print(f"bot put {bot_bat_ball_choice}")  
        if bot_bat_ball_choice==0:
            bot_choice_label=Label(bat_ball_choose_frame, text="bot choose batting and you have to ball", font=('Times New Roman', 18))
            bot_choice_label.grid(row=1, column=0, padx=10, pady=10)

            bat_ball_choosed_next=Button(bat_ball_choose_frame, text="Next",command=lambda:match("bowling"), font=('Times New Roman', 15))
            bat_ball_choosed_next.grid(row=2, column=0, padx=10, pady=10, columnspan=2)

            print("bot win the Toss and choose batting and you have to ball")
                    
        elif bot_bat_ball_choice==1:

            bot_choice_label=Label(bat_ball_choose_frame, text="bot choose bowling and you have to bat" ,font=('Times New Roman', 18))
            bot_choice_label.grid(row=1, column=0, padx=10,pady=10)

            bat_ball_choosed_next=Button(bat_ball_choose_frame, text="Next",command=lambda:match("batting"), font=('Times New Roman', 15))
            bat_ball_choosed_next.grid(row=2, column=0, padx=10, pady=10, columnspan=2)

            print("bot win the toss and choose balling and you have to bat")

            

def toss_time(user_tossing):

    toss_time_frame=main_frame()
    toss_time_frame.grid(row=1,column=0,columnspan=2,padx=10,pady=10)

    bot_tossing=random.randint(1,6)
    print(bot_tossing)
    total=user_tossing+bot_tossing

    toss_time_label=Label(toss_time_frame,text=f"You put {user_tossing} and Bot put {bot_tossing},",font=('Times New Roman', 18))
    toss_time_label.grid(row=1,column=0,columnspan=2,padx=10,pady=20)

    if total & 1==0:
        for key,value in dict["toss_choose"].items():
                            
            if value=="even":
                dict["toss_win"][key]=1
                toss_result_label=Label(toss_time_frame,text=f"it is Even and {key} Won the Toss",font=('Times New Roman', 15))
                toss_result_label.grid(row=2, column=0, columnspan=2, padx=10,pady=10)

    else:
        for key,value in dict["toss_choose"].items():
                            
            if value=="odd":
                dict["toss_win"][key]=1
                toss_result_label=Label(toss_time_frame,text=f"it is Odd and {key} Won the Toss",font=('Times New Roman', 15))
                toss_result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)  

    toss_time_button=Button(toss_time_frame, text=" Next ", command=bat_ball_choose, font=('Times New Roman', 15))
    toss_time_button.grid(row=3, column=0, columnspan=2, padx=10, pady=20 )
    

def odd_even_click(user_select_toss_option):

    if user_select_toss_option == "odd":
        dict["toss_choose"]["user"]="odd"
        dict["toss_choose"]["bot"]="even"
    elif user_select_toss_option == "even":
        dict["toss_choose"]["user"]="even"
        dict["toss_choose"]["bot"]="odd"

    odd_even_toss_frame=main_frame()
    odd_even_toss_frame.grid(row=1,column=0,columnspan=2,padx=10,pady=10)

    user_select_option_view_label=Label(odd_even_toss_frame,text=f"You Choose {user_select_toss_option}\nSelect a number Between 1 to 6 for Tossing",font=('Times New Roman', 18 ))
    user_select_option_view_label.grid(row=1,column=0,columnspan=2,padx=10,pady=10)

    toss_val= IntVar()
    toss_val.set(1)

    user_toss_number_optionmenu=OptionMenu(odd_even_toss_frame, toss_val, *toss_list)
    user_toss_number_optionmenu.grid(row=3,column=0,padx=10,pady=10,columnspan=2)

    toss_submit_button=Button(odd_even_toss_frame,text="Next", command=lambda:toss_time(toss_val.get()), font=('Times New Roman', 15))
    toss_submit_button.grid(row=4,column=0,columnspan=2,padx=10,pady=10)

    
def toss(over,wicket):

    dict["over"]=over
    dict["wicket"]=wicket

    odd_even_choose_frame=main_frame()
    odd_even_choose_frame.grid(row=1,column=0,columnspan=2,padx=10,pady=10)

    title_label_for_odd_even_choose=Label(odd_even_choose_frame,text="Odd/Even choose ",font=('Times New Roman', 22))
    title_label_for_odd_even_choose.grid(row=1,column=0,columnspan=2,padx=20,pady=20)

    odd_button=Button(odd_even_choose_frame,text="ODD", command=lambda:odd_even_click("odd"), font=('Times New Roman', 15), padx=10)
    odd_button.grid(row=2,column=0,padx=20,pady=20)

    even_button=Button(odd_even_choose_frame,text="EVEN", command=lambda:odd_even_click("even"), font=('Times New Roman', 15))
    even_button.grid(row=2,column=1,padx=20,pady=20)



wicket_over_select_frame=main_frame()
wicket_over_select_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

over_select_label=Label(wicket_over_select_frame, text="Over", font=('Times New Roman', 18))
over_select_label.grid(row=1, column=0, padx=10, pady=2)

wicket_select_label=Label(wicket_over_select_frame, text="Wicket", font=('Times New Roman', 18))
wicket_select_label.grid(row=1, column=1, padx=10, pady=2)


over_menu=IntVar()
over_menu.set(1)

over_option_menu=OptionMenu(wicket_over_select_frame, over_menu, *over_list)
over_option_menu.grid(row=2,column=0,padx=10,pady=2)

wicket_menu=IntVar()
wicket_menu.set(1)

wicket_option_menu=OptionMenu(wicket_over_select_frame, wicket_menu, *wicket_list)
wicket_option_menu.grid(row=2,column=1,padx=10,pady=2)

wicket_over_select_button=Button(wicket_over_select_frame, text="Next", command=lambda:toss(over_menu.get(),wicket_menu.get()), padx=10, font=('Times New Roman', 15))
wicket_over_select_button.grid(row=3, column=0, columnspan=2, padx=10, pady=30)




#------------------------Exit frame-----------------#


exit_button=Button(exit_frame,text="Exit",fg="white", bg="red", width=50, command=window.quit, font=('Times New Roman', 18))
exit_button.grid(row=10, column=0, columnspan=5 )

#------------------------Title Frame----------------#
game_title_label=Label(title_frame,text="ODD OR EVEN GAME", font=('Times New Roman', 29, 'bold'))
game_title_label.grid(row=0, column=0, columnspan=5, padx=20, pady=20)

window.mainloop()