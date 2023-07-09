import mplcyberpunk
import yfinance
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np

#Extrair dados da PETR4 desde 2010
symbol = "PETR4.SA"
dados = yfinance.download(symbol, '2010-12-31')["Adj Close"]

#Calcular os retornos mensais
retornos = dados.pct_change()

#Calculando a volatilidade e removendos dados faltantes
volatilidade = retornos.rolling(252).std().dropna()
volatilidade = volatilidade * np.sqrt(252)

#Estilo do gráfico titulo e ajustando o eixo Y
plt.style.use("cyberpunk")
ax = volatilidade.plot(title = f"Volatilidade {symbol}")
ax.yaxis.set_major_formatter(mtick.PercentFormatter(1))
plt.show()