


from tkinter import Tk, Button, messagebox

# Initialisation des variables globales
board = [' ' for _ in range(9)]  # Plateau de jeu
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # Cases disponibles
count = 0  # Compteur de coups
mark = 'X'  # Marque du joueur actuel (sera mis à jour)

# Créer la fenêtre principale
root = Tk()
root.title("Tic-Tac-Toe")

# Fonction pour vérifier si quelqu'un a gagné
def win():
    winning_combinations = [
        (0,1,2), (3,4,5), (6,7,8),  # lignes
        (0,3,6), (1,4,7), (2,5,8),  # colonnes
        (0,4,8), (2,4,6)             # diagonales
    ]
    for a,b,c in winning_combinations:
        if board[a] == board[b] == board[c] and board[a] != ' ':
            return board[a]  # Retourne 'X' ou 'O'
    return None
    

# Fonction checker() complète
def checker(digit):
    global count, mark, digits, board

    # Déterminer le joueur actuel
    if count % 2 == 0:
        mark = 'X'
    else:
        mark = 'O'

    # Vérifier chaque chiffre et mettre à jour le plateau et bouton
    if digit == 1 and 1 in digits:
        digits.remove(1)
        board[0] = mark
        button1.config(text=mark)
    if digit == 2 and 2 in digits:
        digits.remove(2)
        board[1] = mark
        button2.config(text=mark)
    if digit == 3 and 3 in digits:
        digits.remove(3)
        board[2] = mark
        button3.config(text=mark)
    if digit == 4 and 4 in digits:
        digits.remove(4)
        board[3] = mark
        button4.config(text=mark)
    if digit == 5 and 5 in digits:
        digits.remove(5)
        board[4] = mark
        button5.config(text=mark)
    if digit == 6 and 6 in digits:
        digits.remove(6)
        board[5] = mark
        button6.config(text=mark)
    if digit == 7 and 7 in digits:
        digits.remove(7)
        board[6] = mark
        button7.config(text=mark)
    if digit == 8 and 8 in digits:
        digits.remove(8)
        board[7] = mark
        button8.config(text=mark)
    if digit == 9 and 9 in digits:
        digits.remove(9)
        board[8] = mark
        button9.config(text=mark)

    # Incrémenter le compteur de coups
    count += 1

    # Vérifier la victoire
    if win() == mark:
        if mark == 'X':
            messagebox.showinfo("Victoire", "Player1 wins")
        else:
            messagebox.showinfo("Victoire", "Player2 wins")
        root.destroy()
        return

    # Vérifier le match nul
    if count > 8 and win() != 'X' and win() != 'O':
        messagebox.showinfo("Match Tied", "Match Tied")
        root.destroy()

# Créer les boutons et les placer sur la grille
button1 = Button(root, text=" ", font="Arial 20", width=5, height=2, command=lambda: checker(1))
button2 = Button(root, text=" ", font="Arial 20", width=5, height=2, command=lambda: checker(2))
button3 = Button(root, text=" ", font="Arial 20", width=5, height=2, command=lambda: checker(3))
button4 = Button(root, text=" ", font="Arial 20", width=5, height=2, command=lambda: checker(4))
button5 = Button(root, text=" ", font="Arial 20", width=5, height=2, command=lambda: checker(5))
button6 = Button(root, text=" ", font="Arial 20", width=5, height=2, command=lambda: checker(6))
button7 = Button(root, text=" ", font="Arial 20", width=5, height=2, command=lambda: checker(7))
button8 = Button(root, text=" ", font="Arial 20", width=5, height=2, command=lambda: checker(8))
button9 = Button(root, text=" ", font="Arial 20", width=5, height=2, command=lambda: checker(9))

# Placer les boutons sur la grille
button1.grid(row=0, column=0)
button2.grid(row=0, column=1)
button3.grid(row=0, column=2)
button4.grid(row=1, column=0)
button5.grid(row=1, column=1)
button6.grid(row=1, column=2)
button7.grid(row=2, column=0)
button8.grid(row=2, column=1)
button9.grid(row=2, column=2)

# Lancer la boucle principale Tkinter
root.mainloop()
