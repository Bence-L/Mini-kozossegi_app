from tkinter import Tk, Label, Entry, Button

def aron_ablak():
    def megnyomva():
        uzenet = ide_irjon.get()
        elkuldve = Label(aron_ablak, text="Elküldve", bg="black", fg="#ed735a", font=('Times', 10, 'bold'))
        elkuldve.grid(row=5, pady=10, padx=(0, 550))
        
        def eltavolit():
            elkuldve.destroy()
        
        aron_ablak.after(2000, eltavolit)
        
        try:
            with open("uzenetek.txt", 'a', encoding="utf-8") as fajl:
                fajl.write(uzenet + "; ÁRON\n")
        except Exception as e:
            print('Nem találjuk az adatokat', e)
        
        ide_irjon.delete(0, 'end')
        beszelgetni()
        iras()
    
    def beszelgetni():
        global kiuzent
        kiuzent = []
        
        try:
            with open("uzenetek.txt", 'r', encoding="utf-8") as fajl:
                for sor in fajl:
                    adat = sor.strip().split(';')
                    if len(adat) == 2:
                        kiuzent.append({
                            'Üzenet': adat[0],
                            'Kiküldte': adat[1]
                        })
        except FileNotFoundError:
            print("Az uzenetek.txt fájl nem található.")

    def iras():
        sorkoz = 6  
        for widget in aron_ablak.grid_slaves():
            if int(widget.grid_info()["row"]) >= 6:
                widget.grid_forget()
        
        for i in kiuzent:
            if i['Kiküldte'].strip() == "ÁRON":  #ÁRON
                uzenetlabel = Label(aron_ablak, text=f"Én: {i['Üzenet']}", font="Times 20",fg="black", bg="#28e8fa")
                uzenetlabel.grid(row=sorkoz, column=0, pady=5, padx=(400,0)) 
            else:  #BENCE
                uzenetlabel = Label(aron_ablak, text=f"Bence: {i['Üzenet']}", font="Times 20",fg="black", bg="#285cfa")
                uzenetlabel.grid(row=sorkoz, column=0, pady=5, padx=(0,160))
            sorkoz += 1

    aron_ablak = Tk()
    aron_ablak.geometry("700x900")
    aron_ablak.configure(bg="black")
    aron_ablak.title("Áron profilja")
    aron_cim = Label(aron_ablak, text="Áron profilja🎁", fg="#28e8fa", bg="black", font=('Times', 50, 'bold'))
    aron_cim.grid(row=0, columnspan=1, pady=10, padx=60)

    chatfal = Label(aron_ablak, text="Írja ide az üzenetét:", bg="black", fg="#28e8fa", font=('Helvetica', 15, 'bold'))
    chatfal.grid(row=3, pady=10, padx=(0, 550))
    ide_irjon = Entry(aron_ablak, width=20, bg="#285cfa")
    ide_irjon.grid(row=4, pady=0, padx=(0, 560))

    bekuldesgomb = Button(aron_ablak, text="=>", bg="#285cfa", font="Times 8", borderwidth=3, command=megnyomva)
    bekuldesgomb.grid(row=4, pady=0, padx=(0, 440))

    beszelgetni()
    iras()
    
    aron_ablak.mainloop()

#aron_ablak()
#egyik szín #285cfa
#masik szín #28e8fa
#gomb szín #ed735a
