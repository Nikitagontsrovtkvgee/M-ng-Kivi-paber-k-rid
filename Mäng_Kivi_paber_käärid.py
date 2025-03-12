import random

print("Tere tulemast m‰ngule 'Kivi-paber-k‰‰rid'.")

choices = ["Kivi", "Paber", "K‰‰rid"]

rules = [["Tasav‰gise", "Arvuti vıidab!", "Sa vıidad!"],
         ["Sa vıidad!", "Tasav‰gise", "Arvuti vıidab!"],
         ["Arvuti vıidab!", "Sa vıidad!", "Tasav‰gise"]]

m‰ngija_choice = input("Vali (Kivi, paber, k‰‰rid): ").capitilize()
if m‰ngija_choice not in choices:
    print("Vale sisestus, proovi uuesti.")
else:
    computer_choice = random.choice(choices)
    print(f"Arvuti valis: {computer_choice}")
