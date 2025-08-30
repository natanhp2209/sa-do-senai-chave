palavras_unicas = set()

while True:
    entrada = input("Digite uma palavra (ou 'sair' para terminar): ").strip()
    
    if entrada() == 'sair':
        break
    
    if entrada:  
        palavras_unicas.add(entrada())  
if palavras_unicas:
    lista_ordenada = sorted(palavras_unicas)
    
    print("\n=== Resultados ===")
    print(f"Total de palavras diferentes digitadas: {len(palavras_unicas)}")
    print("\nPalavras em ordem alfabética:")
    for palavra in lista_ordenada:
        print(f"- {palavra}")
    
    if 'python' in palavras_unicas:
        print("\na palavra 'Python' foi encontrada na lista!")
    else:
        print("\na palavra 'Python' NÃO foi encontrada na lista.")
else:
    print("Nenhuma palavra foi digitada.")