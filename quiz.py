print("Seja muito bem vindo ao quiz da Giovana")
answer_user = input("Quer começar? (S/N)")

if answer_user != "S":
   quit()

score = 0

print("Iniciando...")
print("(1) Quem é o atual dono do Twitter? \n (A) Mark Z. \n (B) Elon M. \n (C) John S. \n (D) Clark H. \n")
answer_1 = input("Resposta: \n")

if (answer_1 == "B"):
   print("Correto!\n")
   score = score + 1
else:
   print("Incorreto! Resposta correta: Elon M. \n")


print("(2) Quem eliminou o Brasil da Copa do Mundo de 2022? \n (A) Argentina \n (B) Espanha \n (C) Croácia \n (D) Alemanha \n")

answer_2 = input("Resposta: \n")

if (answer_2 == "C"):
   print("Correto!\n")
   score = score + 1
else:
   print("Incorreto! Resposta Correta: Croácia \n")

print(f"Final do game! Pontuação: {score}/2 \n\n")
