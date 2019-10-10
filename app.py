from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import random
import numpy as np

import timeit


def main():

    root = tk.Tk()
    # root.geometry('800x500')
    root.resizable(width=False, height=False)
    root.title('Tugas Algoritma')

    canvas = tk.Canvas(root, height=500, width=800)
    canvas.pack()

    bg = tk.PhotoImage(file='bg.png')
    bl = tk.Label(root, image=bg)
    bl.place(relwidth=1, relheight=1)

    # root.iconbitmap('icons/pypad.ico')

    ########################################################################

    def about():
        messagebox.showinfo("About", "Simulasi Algoritma Sorting")

    def help_box(event=None):
        messagebox.showinfo(
            "Help", "For help email to hai@irfnrdh.com", icon='question')

    def exit_editor():
        if messagebox.askokcancel("Quti", "Do you really want to quit?"):
            root.destroy()
    root.protocol('WM_DELETE_WINDOW', exit_editor)

    def donothing():
        print("Nothing to do :v")

    ########################################################################
    # Bubble Sort
    def bbsort(angka):
        for i in range(len(angka)-1, 0, -1):
            # swap = False
            for j in range(i):
                if angka[j] > angka[j+1]:
                    tampung = angka[j]
                    angka[j] = angka[j+1]
                    angka[j+1] = tampung
                #     swap = True
                # if not swap:
                #     break

    # Selection Sort

    def sssort(angka):
        for i in range(len(angka)):
            min_idx = i
            for j in range(i, len(angka)):
                if angka[j] < angka[min_idx]:
                    min_idx = j
            tampung = angka[i]
            angka[i] = angka[min_idx]
            angka[min_idx] = tampung

    # Insertion Sort

    def issort(angka):
        for i in range(1, len(angka)):
            idx = angka[i]
            for j in range(i-1, 0, -1):
                if angka[j] > idx:
                    angka[j+1] = angka[j]
                else:
                    angka[j+1] = idx
                    break

    # Bubble+Insertion+Selection Sort Optimize

    def bisort(angka):
        for i in range(len(angka)):
            min_idx = i
        for j in range(i, len(angka)):
            if angka[j] < angka[min_idx]:
                min_idx = j
        tampung = angka[i]
        angka[i] = angka[min_idx]
        angka[min_idx] = tampung

    ########################################################################

    def bbs_respon():
        if len(listbox_widget.get(0, tk.END)) == 0:
            print("Data Lu mane?")
        else:
            print("#################################################### BUBLE SORT ")
            hasil_listbox_widget.delete(0, tk.END)
            angka = list(listbox_widget.get(0, tk.END))
            print("Data Sample \n", angka)
            start = timeit.default_timer()
            bbsort(angka)
            stop = timeit.default_timer()
            runtime = stop - start
            print("\n Hasil Sorting  \n", angka)
            print('RunTime : ', runtime)
            print('Jumlah data : ', len(angka))

            for hasil_entry in angka:
                hasil_listbox_widget.insert(tk.END, hasil_entry)

            bbs_time.config(text="% .12f" % runtime)
            bbs_time.place(x=420, y=185)

    def iss_respon():
        if len(listbox_widget.get(0, tk.END)) == 0:
            print("Data Lu mane?")
        else:
            print("#################################################### INSERTION SORT ")
            hasil_listbox_widget.delete(0, tk.END)
            angka = list(listbox_widget.get(0, tk.END))
            print("Data Sample \n", angka)
            start = timeit.default_timer()
            issort(angka)
            stop = timeit.default_timer()
            runtime = stop - start
            print("\n Hasil Sorting  \n", angka)
            print('RunTime : ', runtime)
            print('Jumlah data : ', len(angka))

            for hasil_entry in angka:
                hasil_listbox_widget.insert(tk.END, hasil_entry)

            iss_time.config(text="% .12f" % runtime)
            iss_time.place(x=545, y=185)

    def sss_respon():
        if len(listbox_widget.get(0, tk.END)) == 0:
            print("Data Lu mane?")
        else:
            print("#################################################### SELECTION SORT ")
            hasil_listbox_widget.delete(0, tk.END)
            angka = list(listbox_widget.get(0, tk.END))
            print("Data Sample \n", angka)
            start = timeit.default_timer()
            sssort(angka)
            stop = timeit.default_timer()
            runtime = stop - start
            print("\n Hasil Sorting  \n", angka)
            print('RunTime : ', runtime)
            print('Jumlah data : ', len(angka))

            for hasil_entry in angka:
                hasil_listbox_widget.insert(tk.END, hasil_entry)

            sss_time.config(text="% .12f" % runtime)
            sss_time.place(x=670, y=185)

    def bsi_respon():
        if len(listbox_widget.get(0, tk.END)) == 0:
            print("Data Lu mane?")
        else:
            print("#################################################### BSI")
            hasil_listbox_widget.delete(0, tk.END)
            angka = list(listbox_widget.get(0, tk.END))
            print("Data Sample \n", angka)
            start = timeit.default_timer()
            bisort(angka)
            stop = timeit.default_timer()
            runtime = stop - start
            print("\n Hasil Sorting  \n", angka)
            print('RunTime : ', runtime)
            print('Jumlah data : ', len(angka))

            for hasil_entry in angka:
                hasil_listbox_widget.insert(tk.END, hasil_entry)

            bsi_time.config(text="% .12f" % runtime)
            bsi_time.place(x=570, y=333)

    def generate(entry):

        listbox_widget.delete(0, tk.END)

        l = int(entry)
        listrandom = []
        for i in range(l):
            value = random.randint(1, 1000)
            listrandom.append(value)
            listbox_widget.insert(tk.END, value)

        angka = listrandom
        # print(listrandom)

        # listbox_entries = random.sample(range(100), int(entry))
        # for entry in listbox_entries:
        #     listbox_widget.insert(tk.END, entry)
        #angka = listbox_widget.get(0, tk.END)

    def cls():
        hasil_listbox_widget.delete(0, tk.END)
        print("\n" * 100)
        # print [ listbox_widget.get(i) for i in listbox_widget.curselection()]

    ########################################################################
    menubar = Menu(root)

    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Generate Random Number", command=donothing)
    filemenu.add_command(label="Close", command=exit_editor)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)

    menubar.add_cascade(label="File", menu=filemenu)

    aboutmenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="About", menu=aboutmenu)
    aboutmenu.add_command(label="About", command=about)
    aboutmenu.add_command(label="Help", command=help_box)

    root.config(menu=menubar)

    ########################################################################

    # DATA SAMPLING ------------------------------
    frame_data = tk.Frame(root)
    frame_data.place(relx=0.128, rely=0.140, relwidth=0.18,
                     relheight=0.65, anchor='n')

    listbox_widget = tk.Listbox(
        frame_data, selectmode="BROWSE", height=20, width=20, background='white')
    listbox_widget_scrl = Scrollbar(frame_data, orient=VERTICAL)
    listbox_widget.config(yscrollcommand=listbox_widget_scrl.set)
    listbox_widget_scrl.configure(command=listbox_widget.yview)

    listbox_widget.grid(row=1, sticky=W)
    listbox_widget_scrl.grid(row=1, column=1, sticky=NS)

    # DATA HASIL ------------------------------
    frame_hasil = tk.Frame(root)
    frame_hasil.place(relx=0.34, rely=0.140, relwidth=0.18,
                      relheight=0.65, anchor='n')

    hasil_listbox_widget = tk.Listbox(
        frame_hasil, selectmode="BROWSE", height=20, width=20, background='white')
    hasil_listbox_widget_scrl = Scrollbar(frame_hasil, orient=VERTICAL)
    hasil_listbox_widget.config(yscrollcommand=hasil_listbox_widget_scrl.set)
    hasil_listbox_widget_scrl.configure(command=hasil_listbox_widget.yview)
    # hasil_listbox_entries = random.sample(range(100), 10)
    # for hasil_entry in hasil_listbox_entries:
    #     hasil_listbox_widget.insert(tk.END, hasil_entry)
    hasil_listbox_widget.grid(row=1, sticky=W)
    hasil_listbox_widget_scrl.grid(row=1, column=1, sticky=NS)

    # Entry
    entry = tk.Entry(root, font=40, width=7)
    entry.place(x=105, y=450)

    # BUTTON
    bbs_button = tk.Button(root, text="START", font=40,
                           command=bbs_respon).place(x=434, y=140)
    iss_button = tk.Button(root, text="START", font=40,
                           command=iss_respon).place(x=555, y=140)
    sss_button = tk.Button(root, text="START", font=40,
                           command=sss_respon).place(x=680, y=140)
    bsi_button = tk.Button(root, text="START", font=40,
                           command=bsi_respon).place(x=466, y=330)
    # GENERATE DATA SAMPLING
    gen_button = tk.Button(root, text="GENERATE", font=40,
                           command=lambda: generate(entry.get()))
    gen_button.place(x=180, y=447)
    cls_button = tk.Button(root, text="CLEAN", font=40,
                           command=cls).place(x=295, y=447)

    # RESPON TIME
    bbs_time = ttk.Label(root, background="#6367c8",
                         foreground="#fff")
    bbs_time['text'] = "Respon Time"
    bbs_time.place(x=429, y=185)

    iss_time = tk.Label(root,
                        background="#6367c8", foreground="#fff")
    iss_time['text'] = "Respon Time"
    iss_time.place(x=555, y=185)

    sss_time = tk.Label(root,
                        background="#6367c8", foreground="#fff")
    sss_time['text'] = "Respon Time"
    sss_time.place(x=680, y=185)

    bsi_time = tk.Label(root,
                        background="#6367c8", font=40, foreground="#fff")
    bsi_time['text'] = "Respon Time"
    bsi_time.place(x=570, y=333)

    ########################################################################

    root.mainloop()


main()
