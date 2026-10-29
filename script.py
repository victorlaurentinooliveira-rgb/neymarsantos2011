def calcular_media(notas):
    """Calcula a média aritmética de uma lista de notas."""
    return sum(notas) / len(notas)

def verificar_status(media):
    """Define se o aluno está aprovado, em recuperação ou reprovado."""
    if media >= 7.0:
        return "Aprovado(a)! Parabéns! 🎉"
    elif 5.0 <= media < 7.0:
        return "Em Recuperação. Precisa estudar mais um pouco! 📚"
    else:
        return "Reprovado(a). ❌"

def executar_sistema():
    print("=== Sistema de Gerenciamento de Notas Escolares ===")
    
    try:
        qtd_notas = int(input("Quantas notas deseja inserir para o aluno? "))
        if qtd_notas <= 0:
            print("Erro: A quantidade de notas deve ser maior que zero.")
            return
            
        notas = []
        for i in range(qtd_notas):
            nota = float(input(f"Digite a nota {i + 1}: "))
            if nota < 0 or nota > 10:
                print("Erro: A nota deve ser um valor entre 0 e 10.")
                return
            notas.append(nota)
            
        # Executa a lógica
        media_final = calcular_media(notas)
        status_aluno = verificar_status(media_final)
        
        # Mostra os resultados
        print("\n================ RESULTADO ================")
        print(f"Média Final do Aluno: {media_final:.2f}")
        print(f"Status do Aluno: {status_aluno}")
        print("===========================================")
        
    except ValueError:
        print("Erro: Por favor, digite apenas números válidos.")

if __name__ == "__main__":
    executar_sistema()

