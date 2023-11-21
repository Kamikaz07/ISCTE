agenda = [
    ["Segunda", {"10h": None, "11h": None, "12h": None, "13h": None, "14h": None, "15h": None}],
    ["Terça", {"10h": None, "11h": None, "12h": None, "13h": None, "14h": None, "15h": None}],
    ["Quarta", {"10h": None, "11h": None, "12h": None, "13h": None, "14h": None, "15h": None}],
    ["Quinta", {"10h": None, "11h": None, "12h": None, "13h": None, "14h": None, "15h": None}],
    ["Sexta", {"10h": None, "11h": None, "12h": None, "13h": None, "14h": None, "15h": None}],
    ["Sábado", {"10h": None, "11h": None, "12h": None, "13h": None, "14h": None, "15h": None}],
    ["Domingo", {"10h": None, "11h": None, "12h": None, "13h": None, "14h": None, "15h": None}]
]

def inserir_evento(dia, horario, evento):
    dia = dia.capitalize()
    for item in agenda:
        if item[0] == dia:
            item[1][horario] = evento
            return
    print(f"Dia inválido: {dia}")

def imprimir_agenda():
    for dia, horarios in agenda:
        print(dia)
        for horario, evento in horarios.items():
            print(f"{horario}: {evento}")

def main():
    dia = input("Dia da Semana:\n")
    hora = input("Hora:\n")
    evento = input("Evento:\n")
    inserir_evento(dia, hora, evento)
    imprimir_agenda()

if __name__ == "__main__":
    main()