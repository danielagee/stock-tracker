import datetime
from tkinter import *
import analysis.constants as c

background_color = '#eae6ff'
text_color = '#000000'

root = Tk()
root.title('Data Entry')
root.geometry('950x450+300+200')
root.resizable(False, False)
root.configure(bg=background_color)

# Labels
x_align_label = 20
Label(root, text='Stocks Project Folder Path (root):', font=23, bg=background_color, fg=text_color).place(x=x_align_label, y=20)
Label(root, text='Portfolio Folder Name:', font=23, bg=background_color, fg=text_color).place(x=x_align_label, y=70)
Label(root, text='Portfolio File Name:', font=23, bg=background_color, fg=text_color).place(x=x_align_label, y=120)
Label(root, text='Output Folder Name:', font=23, bg=background_color, fg=text_color).place(x=x_align_label, y=170)
Label(root, text='Refresh Tickers?', font=23, bg=background_color, fg=text_color).place(x=x_align_label, y=220)
Label(root, text='Refresh Dividends?', font=23, bg=background_color, fg=text_color).place(x=x_align_label, y=270)
Label(root, text='Generate portfolio plot?', font=23, bg=background_color, fg=text_color).place(x=x_align_label, y=320)
Label(root, text='Generate individual stock plots?', font=23, bg=background_color, fg=text_color).place(x=x_align_label, y=370)

# Entry
root_path_entry = Entry(root, textvariable=c.root_path, width=45, bd=2, font=20)
portfolio_path_entry = Entry(root, textvariable=c.portfolio_path, width=45, bd=2, font=20)
portfolio_file_entry = Entry(root, textvariable=c.portfolio_file, width=45, bd=2, font=20)
output_path_entry = Entry(root, textvariable=c.output_path, width=45, bd=2, font=20)
refresh_tickers_entry = Entry(root, textvariable=c.refresh_tickers, width=45, bd=2, font=20)
refresh_dividends_entry = Entry(root, textvariable=c.refresh_dividends, width=45, bd=2, font=20)
portfolio_plot_entry = Entry(root, textvariable=c.portfolio_plot, width=45, bd=2, font=20)
individual_plot_entry = Entry(root, textvariable=c.individual_plot, width=45, bd=2, font=20)

x_align_entry = 350
root_path_entry.place(x=x_align_entry, y=20)
portfolio_path_entry.place(x=x_align_entry, y=70)
portfolio_file_entry.place(x=x_align_entry, y=120)
output_path_entry.place(x=x_align_entry, y=170)
refresh_tickers_entry.place(x=x_align_entry, y=220)
refresh_dividends_entry.place(x=x_align_entry, y=270)
portfolio_plot_entry.place(x=x_align_entry, y=320)
individual_plot_entry.place(x=x_align_entry, y=370)

# start_delay = 30  # Start timeline xx days before earliest portfolio acquisition
# end_date = datetime.date.today() - datetime.timedelta(days=0)  # End date is today

root.mainloop()


# Add an icon to data entry form
#icon_image=PhotoImage(file='logo.png')
#root.iconphoto(False, icon_image)

#from tkinter.ttk import Combobox
#from tkinter import messagebox
#import tkinter as tk