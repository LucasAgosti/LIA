import numpy as np

class UF:

	def __init__(self, f, name):
		self.meses = np.zeros((12, 5))
		self.f = f
		self.name = name

	def addView(mes, produto, qtde):
		self.meses[mes - 1][produto.target.index(1)] += qtde

class Produto:

	def __init__(self, n_produto, nome):
		self.target = np.zeros(5)
		self.target[n_produto] = 1
		self.name = name

def create_states():

	states = np.array()
	states.append(UF(0.221, "São Paulo"))
	states.append(UF(0.102, "Minas Gerais"))
	states.append(UF(0.081, "Rio de Janeiro"))
	states.append(UF(0.074, "Bahia"))
	states.append(UF(0.055, "Paraná"))
	states.append(UF(0.055, "Rio Grande do Sul"))
	states.append(UF(0.046, "Pernambuco"))
	states.append(UF(0.044, "Ceará"))
	states.append(UF(0.040, "Pará"))
	states.append(UF(0.034, "Santa Catarina"))
	states.append(UF(0.034, "Maranhão"))
	states.append(UF(0.032, "Goiás"))
	states.append(UF(0.019, "Amazonas"))
	states.append(UF(0.019, "Paraiba"))
	states.append(UF(0.019, "Espirito Santo"))
	states.append(UF(0.017, "Rio Grande do Norte"))
	states.append(UF(0.016, "Mato Groso"))
	states.append(UF(0.016, "Alagoas"))
	states.append(UF(0.016, "Piauí"))
	states.append(UF(0.014, "Distrito Federal"))
	states.append(UF(0.013, "Mato Grosso do Sul"))
	states.append(UF(0.011, "Sergipe"))
	states.append(UF(0.009, "Rondônia"))
	states.append(UF(0.007, "Tocantins"))
	states.append(UF(0.004, "Acre"))
	states.append(UF(0.004, "Amapa"))
	states.append(UF(0.002, "Roraima"))

	return states
