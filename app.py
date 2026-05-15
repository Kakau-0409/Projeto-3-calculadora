import streamlit as st

st.set_page_config(page_title="Calculadora", page_icon="🧮")

st.title("Calculadora")

opcao = st.sidebar.selectbox(
    "Escolha uma calculadora:",
    [
        "Soma",
        "Subtração",
        "Multiplicação",
        "Divisão",
        "IMC",
        "Média Escolar",
        "Desconto",
        "Dólar -> Real"
    ]
)

# SOMA-----------------------------------------------

if opcao == "Soma":

    quantidade = st.number_input(
        "Quantos números deseja somar?",
        min_value=2,
        max_value=100,
        step=1
    )

    numeros = []

    for i in range(quantidade):
        numero = st.number_input(f"Número {i+1}", key=f"soma{i}")
        numeros.append(numero)

    if st.button("Somar"):
        resultado = sum(numeros)
        st.success(f"Resultado: {resultado}")

# SUBTRAÇÃO------------------------------------------

elif opcao == "Subtração":

    quantidade = st.number_input(
        "Quantos números deseja subtrair?",
        min_value=2,
        max_value=100,
        step=1
    )

    numeros = []

    for i in range(quantidade):
        numero = st.number_input(f"Número {i+1}", key=f"sub{i}")
        numeros.append(numero)

    if st.button("Subtrair"):

        resultado = numeros[0]

        for numero in numeros[1:]:
            resultado -= numero

        st.success(f"Resultado: {resultado}")

# MULTIPLICAÇÃO--------------------------------------

elif opcao == "Multiplicação":

    quantidade = st.number_input(
        "Quantos números deseja multiplicar?",
        min_value=2,
        max_value=100,
        step=1
    )

    numeros = []

    for i in range(quantidade):
        numero = st.number_input(f"Número {i+1}", key=f"multi{i}")
        numeros.append(numero)

    if st.button("Multiplicar"):

        resultado = 1

        for numero in numeros:
            resultado *= numero

        st.success(f"Resultado: {resultado}")

# DIVISÃO--------------------------------------

elif opcao == "Divisão":

    numero1 = st.number_input("Número dividendo")
    numero2 = st.number_input("Segundo divisor (vai na chave)")

    if st.button("Dividir"):

        if numero2 != 0:

            resultado = numero1 / numero2
            st.success(f"Resultado: {resultado}")

        else:
            st.error("Impossivel dividir por zero.")
# IMC------------------------------------------------

elif opcao == "IMC":

    peso = st.number_input("Peso (kg)")
    altura = st.number_input("Altura (m)")

    if st.button("IMC"):

        if altura > 0:

            imc = peso / (altura ** 2)

            st.success(f"Seu IMC é: {imc:.2f}")

            if imc < 18.5:
                st.warning("Abaixo do peso")
            elif imc < 25:
                st.success("Peso normal!")
            elif imc < 30:
                st.warning("Sobrepeso")
            else:
                st.error("Obesidade")

# MÉDIA ESCOLAR--------------------------------------

elif opcao == "Média Escolar":

    nota1 = st.number_input("Nota 1", min_value=0.0, max_value=10.0)
    nota2 = st.number_input("Nota 2", min_value=0.0, max_value=10.0)
    nota3 = st.number_input("Nota 3", min_value=0.0, max_value=10.0)
    nota4 = st.number_input("Nota 4", min_value=0.0, max_value=10.0)

    if st.button("Calcular Média"):

        media = (nota1 + nota2 + nota3 + nota4) / 4

        st.success(f"Média: {media:.1f}")

        if media >= 6:
            st.success("Aprovado!")
        
        elif media >=5 :
            st.warning("Recuperação")
        elif media <= 5:
            st.error("Reprovado")
        

# DESCONTO-------------------------------------------

elif opcao == "Desconto":

    preco = st.number_input("Preço original")
    desconto = st.number_input("Porcentagem de desconto")

    if st.button("Desconto"):

        valor_desconto = preco * (desconto / 100)
        valor_final = preco - valor_desconto

        st.success(f"Preço final: R${valor_final:.2f}")

# DÓLAR -> REAL--------------------------------------

elif opcao == "Dólar -> Real":

    dolar = st.number_input("Valor em dólar")

    cotacao = 5.67

    if st.button("Converter"):

        real = dolar * cotacao

        st.success(f"Valor em real: R${real:.2f}")