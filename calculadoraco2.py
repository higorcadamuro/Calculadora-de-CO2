import tkinter as tk
from tkinter import ttk

# emissões de CO2
emissao_co2_verde = 0.0385  # Emissão de CO2 para a bandeira verde (kg CO2 por kWh)
emissao_co2_amarela = 0.045  # Emissão de CO2 para a bandeira amarela (kg CO2 por kWh)
emissao_co2_vermelha_1 = 0.055  # Emissão de CO2 para a bandeira vermelha patamar 1 (kg CO2 por kWh)
emissao_co2_vermelha_2 = 0.06  # Emissão de CO2 para a bandeira vermelha patamar 2 (kg CO2 por kWh)
emissao_co2_gasolina = 2.3  # Emissão de CO2 por litro de gasolina (kg CO2 por litro)
emissao_co2_diesel = 2.7  # Emissão de CO2 por litro de diesel (kg CO2 por litro)
emissao_co2_etanol = 1.5  # Emissão de CO2 por litro de etanol (kg CO2 por litro)
emissao_co2_por_km = 0.14  # Emissão de CO2 por quilômetro rodado (kg CO2 por km)

# Custo do reflorestamento em dólares
custo_reflorestamento_dolar = 5  # Custo de reflorestamento por tonelada de CO2 (em dólares)

# Taxa de câmbio (1 dólar = 5,74 reais - 10/11/2024 às 23:00)
taxa_cambio = 5.74  # Conversão de dólar para real

# Função para calcular a emissão de CO2 com base no consumo de energia e bandeira tarifária
def calcular_emissao_energia(consumo, bandeira):
    if bandeira == "amarela":
        return consumo * emissao_co2_amarela
    elif bandeira == "vermelha_1":
        return consumo * emissao_co2_vermelha_1
    elif bandeira == "vermelha_2":
        return consumo * emissao_co2_vermelha_2
    else:  # Caso padrão: bandeira verde
        return consumo * emissao_co2_verde

# Função para calcular a emissão de CO2 com base no tipo e volume de combustível
def calcular_emissao_combustivel(litros, tipo_combustivel):
    if tipo_combustivel == "gasolina":
        return litros * emissao_co2_gasolina
    elif tipo_combustivel == "diesel":
        return litros * emissao_co2_diesel
    elif tipo_combustivel == "etanol":
        return litros * emissao_co2_etanol

# Função para calcular a emissão de CO2 com base na distância percorrida
def calcular_emissao_viagem(distancia):
    return distancia * emissao_co2_por_km

# Função para calcular o custo em reais para compensar as emissões de CO2
def calcular_custo_em_reais(creditos):
    custo_dolar = creditos * custo_reflorestamento_dolar  # Custo em dólares
    return custo_dolar * taxa_cambio  # Conversão para reais

# Função principal para calcular os resultados e exibir na interface
def calcular_resultados():
    consumo = float(entry_kwh.get())  # Consumo de energia elétrica (kWh)
    bandeira = combo_bandeira.get().lower()  # Bandeira tarifária selecionada
    litros_gasolina = float(entry_gasolina.get())  # Litros de gasolina consumidos
    litros_diesel = float(entry_diesel.get())  # Litros de diesel consumidos
    litros_etanol = float(entry_etanol.get())  # Litros de etanol consumidos
    distancia = float(entry_km.get())  # Distância percorrida (km)

    # Calcula as emissões de CO2 para cada categoria
    emissao_energia = calcular_emissao_energia(consumo, bandeira)
    emissao_gasolina = calcular_emissao_combustivel(litros_gasolina, "gasolina")
    emissao_diesel = calcular_emissao_combustivel(litros_diesel, "diesel")
    emissao_etanol = calcular_emissao_combustivel(litros_etanol, "etanol")
    emissao_viagem = calcular_emissao_viagem(distancia)

    # Soma as emissões totais
    emissao_total = (
        emissao_energia
        + emissao_gasolina
        + emissao_diesel
        + emissao_etanol
        + emissao_viagem
    )

    # Calcula os créditos de carbono necessários e o custo para compensar
    creditos = emissao_total / 1000  # Converte kg CO2 para toneladas
    custo = calcular_custo_em_reais(creditos)

    # Gera o texto do resultado
    resultado = f"Emissões totais: {emissao_total:.2f} kg CO2\n"
    resultado += f"Créditos de carbono necessários: {creditos:.2f} toneladas\n"
    resultado += f"Custo para compensar: R$ {custo:.2f}"

    # Atualiza o rótulo de resultado na interface
    label_resultado.config(text=resultado)

# Interface TKinter
janela = tk.Tk()  # Cria a janela principal
janela.title("Calculadora de Crédito de Carbono")  # Define o título da janela

# Entrada de dados e exibição de resultados
label_kwh = tk.Label(janela, text="Consumo de energia (kWh):")
entry_kwh = tk.Entry(janela)
label_bandeira = tk.Label(janela, text="Bandeira tarifária:")
combo_bandeira = ttk.Combobox(janela, values=["Verde", "Amarela", "Vermelha1", "Vermelha2"])
combo_bandeira.set("Verde")  # Define a opção padrão
label_gasolina = tk.Label(janela, text="Gasolina (litros):")
entry_gasolina = tk.Entry(janela)
label_diesel = tk.Label(janela, text="Diesel (litros):")
entry_diesel = tk.Entry(janela)
label_etanol = tk.Label(janela, text="Etanol (litros):")
entry_etanol = tk.Entry(janela)
label_km = tk.Label(janela, text="Distância (km):")
entry_km = tk.Entry(janela)
botao_calcular = tk.Button(janela, text="Calcular", command=calcular_resultados)
label_resultado = tk.Label(janela, text="")

# Organiza colunas e linhas da janela
label_kwh.grid(row=1, column=0)
entry_kwh.grid(row=1, column=1)
label_bandeira.grid(row=0, column=0)
combo_bandeira.grid(row=0, column=1)
label_gasolina.grid(row=2, column=0)
entry_gasolina.grid(row=2, column=1)
label_diesel.grid(row=3, column=0)
entry_diesel.grid(row=3, column=1)
label_etanol.grid(row=4, column=0)
entry_etanol.grid(row=4, column=1)
label_km.grid(row=5, column=0)
entry_km.grid(row=5, column=1)
botao_calcular.grid(row=7, column=1)
label_resultado.grid(row=8, column=1)

# Inicia o loop principal da interface
janela.mainloop()
