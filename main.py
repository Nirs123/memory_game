import random
from time import perf_counter, time
import tkinter as tk

win = tk.Tk()
win.title("Memory")
win.geometry("960x780")
win.minsize(960,780)
win.maxsize(960,780)

frame_1 = tk.Frame(win)
frame_2 = tk.Frame(win)

def set_countdown():
    global colors_easy,memory_color_easy,colors_medium,memory_color_medium,colors_hard,memory_color_hard,time_start
    colors_easy = ["red","green","yellow","blue","pink","orange"]
    memory_color_easy = {"red":0,"green":0,"yellow":0,"blue":0,"pink":0,"orange":0}

    colors_medium = ["#ff0000","#ff0079","#ff00ff","#8300ff","#0000ff","#00ffff","#00ff7e","#00ff00","#ffff00","#ff8400"]
    memory_color_medium = {"#ff0000":0,"#ff0079":0,"#ff00ff":0,"#8300ff":0,"#0000ff":0,"#00ffff":0,"#00ff7e":0,"#00ff00":0,"#ffff00":0,"#ff8400":0}

    colors_hard = ["#ff0000","#ff0079","#ff00ff","#8300ff","#0000ff","#0089ff","#00ffff","#00ff7e","#00ff00","#81ff00","#ffff00","#ff8400","#fcb7f4","#4e7e4e","#9893e6"]
    memory_color_hard = {"#ff0000":0,"#ff0079":0,"#ff00ff":0,"#8300ff":0,"#0000ff":0,"#0089ff":0,"#00ffff":0,"#00ff7e":0,"#00ff00":0,"#81ff00":0,"#ffff00":0,"#ff8400":0,"#fcb7f4":0,"#4e7e4e":0,"#9893e6":0}

    time_start = perf_counter()

def countdown(d):
    global b_list,b_start
    b_list = []

    set_countdown()

    title.grid_forget()
    subtitle.grid_forget()
    b_easy.grid_forget()
    b_medium.grid_forget()
    b_hard.grid_forget()

    if d =="easy":
        for i in range(0,4):
            for j in range(0,3):
                color = colors_easy[random.randint(0,5)]
                while memory_color_easy[color] > 1:
                    color = colors_easy[random.randint(0,5)]
                memory_color_easy[color] += 1
                b_tmp = tk.Button(frame_1,bg=color,command=None,width=34,height=15)
                b_list.append([b_tmp,color])
                b_tmp.grid(row=j,column=i)

    elif d =="medium":
        for i in range(0,5):
            for j in range(0,4):
                color = colors_medium[random.randint(0,9)]
                while memory_color_medium[color] > 1:
                    color = colors_medium[random.randint(0,9)]
                memory_color_medium[color] += 1
                b_tmp = tk.Button(frame_1,bg=color,command=None,width=26,height=11)
                b_list.append([b_tmp,color])
                b_tmp.grid(row=j,column=i)

    elif d =="hard":
        for i in range(0,6):
            for j in range(0,5):
                color = colors_hard[random.randint(0,14)]
                while memory_color_hard[color] > 1:
                    color = colors_hard[random.randint(0,14)]
                memory_color_hard[color] += 1
                b_tmp = tk.Button(frame_1,bg=color,command=None,width=22,height=9)
                b_list.append([b_tmp,color])
                b_tmp.grid(row=j,column=i)

    b_start = tk.Button(frame_2,text="START",font=('Segoe UI Black',"18"),command= lambda diff = d:start_game(diff))
    b_start.grid(row=0,column=0, pady=8)

def start_game(d):
    b_start.grid_forget()
    for button, color in b_list:
        button['bg'] = "grey"
        button['command'] = lambda b = button,c = color : inter_reveal(b,c,d)

s_set = False
def set_reveal():
    global count,memory_button,memory_color,s_t_right,s_t_wrong,count_errors,count_right,diff_count,b_right,memory_wrong
    count = 0
    memory_color = None
    memory_button = None
    memory_wrong = None
    s_t_wrong = False
    s_t_right = False
    count_right = 0
    count_errors = 0
    diff_count = {"easy":6,"medium":10,"hard":15}
    b_right = []
def inter_reveal(b,c,d):
    global s_set
    if s_set == False:
        set_reveal()
        s_set = True
    if b not in b_right:
        reveal(b,c,d)
def reveal(button,color,diff):
    global end_text,b_end,b_new_game,s_t_right,s_t_wrong,memory_button,memory_color,count,count_right,count_errors,diff_count,b_right,t_right,t_wrong,memory_wrong,time_start
    if s_t_wrong:
        t_wrong.destroy()
    if s_t_right:
        t_right.destroy()
    if count == 0:
        if memory_wrong != None:
            memory_wrong['bg'] = "grey"
            memory_button['bg'] = "grey"
            memory_wrong = None
        button['bg'] = color
        button['command'] = None
        memory_color = color
        memory_button = button
        count += 1
    elif count == 1:
        if memory_color == color:
            button['bg'] = color
            button['command'] = None
            t_right = tk.Label(frame_2,text="GOOD JOB !",font=('Segoe UI Black',"18"))
            t_right.grid(row=0,column=0,pady=8)
            s_t_right = True
            count_right += 1
            b_right.append(memory_button)
            b_right.append(button)
            if count_right == diff_count[diff]:
                end_text = tk.Label(frame_2,text=f"Well done ! You made it in {round(perf_counter() - time_start,2)}s with {count_errors} errors !",font=('Segoe UI Black',"18"))
                b_end = tk.Button(frame_2,text="QUIT",font=('Segoe UI Black',"18"),command=win.destroy)
                b_new_game = tk.Button(frame_2,text="New Game",font=('Segoe UI Black',"18"),command=new_game)
                end_text.grid(row=0,column=0,pady=8)
                b_end.grid(row=0,column=1,padx=10,pady=8)
                b_new_game.grid(row=0,column=2)
        else:
            memory_wrong = button
            button['bg'] = color
            s_t_wrong = True
            t_wrong = tk.Label(frame_2,text="WRONG",font=('Segoe UI Black',"18"))
            t_wrong.grid(row=0,column=0,pady=8)
            count_errors += 1
        count = 0

def new_game():
    global s_set,b_list,end_text
    s_set = False
    for button,color in b_list:
        button.destroy()
    t_right.destroy()
    end_text.destroy()
    b_end.destroy()
    b_new_game.destroy()
    set_countdown()
    set_reveal()
    main()

def main():
    global title,subtitle,b_easy,b_medium,b_hard
    title = tk.Label(frame_1,text="Welcome to the Memory Game !",font=('Segoe UI Black',"38"))
    subtitle = tk.Label(frame_1,text="Choose your difficulty:",font=('Segoe UI Black',"28"))
    b_easy = tk.Button(frame_2,text="Easy",font=('Segoe UI Black',"18"),command= lambda d="easy":countdown(d))
    b_medium = tk.Button(frame_2,text="Medium",font=('Segoe UI Black',"18"),command= lambda d="medium":countdown(d))
    b_hard = tk.Button(frame_2,text="Hard",font=('Segoe UI Black',"18"),command= lambda d="hard":countdown(d))

    title.grid(row=0,column=0,pady=100,padx=50)
    subtitle.grid(row=1,column=0,padx=50)
    b_easy.grid(row=0,column=0,pady=100)
    b_medium.grid(row=0,column=1,padx=20)
    b_hard.grid(row=0,column=2)

if __name__ == "__main__":
    main()

frame_1.pack()
frame_2.pack()

win.mainloop()