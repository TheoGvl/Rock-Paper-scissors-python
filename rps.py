import flet as ft
import random

def main(page: ft.Page):
    # Βασικές ρυθμίσεις
    page.title = "Rock, Paper, Scissors !!!"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 450
    page.window.height = 600
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 30

    # Μεταβλητές για το σκορ
    skor_paikti = 0
    skor_ypologisti = 0

    # Οι πιθανές επιλογές
    epiloges = ["Rock 🪨", "Scissors ✂️", "Paper 📜"]

    # --- Η Λογική του Παιχνιδιού ---
    def paixe(e):
        nonlocal skor_paikti, skor_ypologisti
        
        # Διαβάζουμε τι διάλεξε ο παίκτης
        paiktis = e.control.data
        
        # Ο υπολογιστής διαλέγει στην τύχη
        ypologistis = random.choice(epiloges)
        
        # Ενημερώνουμε την οθόνη για το τι διάλεξε ο υπολογιστής
        keimeno_ypologisti.value = f"The computer chose:\n{ypologistis}"

        # Ελέγχουμε ποιος κέρδισε
        if paiktis == ypologistis:
            apotelesma.value = "It's a tie! 🤝"
            apotelesma.color = ft.Colors.YELLOW_400
            
        elif (paiktis == "Rock 🪨" and ypologistis == "Scissors ✂️") or \
             (paiktis == "Scissors ✂️" and ypologistis == "Paper 📜") or \
             (paiktis == "Paper 📜" and ypologistis == "Rock 🪨"):
            
            apotelesma.value = "You win! 🎉"
            apotelesma.color = ft.Colors.GREEN_400
            skor_paikti += 1 # Αυξάνουμε το σκορ
            
        else:
            apotelesma.value = "You lost! 😢"
            apotelesma.color = ft.Colors.RED_400
            skor_ypologisti += 1 # Αυξάνουμε το σκορ του υπολογιστή

        # Ανανεώνουμε το σκορ στην οθόνη
        keimeno_skor.value = f"You: {skor_paikti}  |  Computer: {skor_ypologisti}"
        page.update()

    # --- Στήσιμο Οθόνης ---
    titlos = ft.Text("Rock, Paper, Scissors !!!", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_400)
    
    keimeno_skor = ft.Text("You: 0  |  Computer: 0", size=22, weight=ft.FontWeight.BOLD)
    
    keimeno_ypologisti = ft.Text("The computer is thinking...", size=20, text_align=ft.TextAlign.CENTER)
    
    apotelesma = ft.Text("Make your choice!", size=26, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE)

    # Τα τρία κουμπιά
    btn_petra = ft.Button("Rock 🪨", data="Rock 🪨", on_click=paixe)
    btn_psalidi = ft.Button("Scissors ✂️", data="Scissors ✂️", on_click=paixe)
    btn_xarti = ft.Button("Paper 📜", data="Paper 📜", on_click=paixe)

    koumpia_row = ft.Row(
        [btn_petra, btn_psalidi, btn_xarti], 
        alignment=ft.MainAxisAlignment.CENTER
    )

    # Προσθήκη όλων στη σελίδα
    page.add(
        titlos,
        ft.Divider(height=20, color="transparent"),
        keimeno_skor,
        ft.Divider(height=30, color="grey"),
        keimeno_ypologisti,
        ft.Divider(height=20, color="transparent"),
        apotelesma,
        ft.Divider(height=40, color="transparent"),
        ft.Text("Make your choice:", size=16, color=ft.Colors.GREY_400),
        koumpia_row
    )
ft.run(main)