import tkinter as tk
import datetime


main = tk.Tk()

main.attributes('-fullscreen', True)

########################################
#def exitapp():
#    main.destroy()
#exitb = tk.Button(main, text="Exit")
#exitb.pack()

########################################

screen_w = main.winfo_screenwidth()
screen_h = main.winfo_screenheight()
frame_w = screen_w - screen_w/4
frame_h = screen_h - 100

ticket_time = datetime.datetime.now().strftime('%m-%d-%y %H:%M')
print(ticket_time)

print(screen_w,screen_h)


# Main frames

leftframe = tk.Frame(main, height=frame_h, width=frame_w, bg="lightblue", highlightbackground="blue", highlightthickness=1)
leftframe.pack(side="left")

rightframe = tk.Frame(main, height=frame_h, width=screen_w/4, bg="lightgreen")
rightframe.pack(side="right")


# Buttons

ticket1 = tk.Button(main, text='Jimmy Tang \n Account lockdown\n' + ticket_time)
ticket1.place(x=100, y=100)


main.mainloop()
