#class Parameters:
#def __init__(self, paramfile):
#	self.file = paramfile # Parameters file
#	self.params = {} # inicializar estrutura de dados

from ast import literal_eval

def readParams(parFile):
	param_list = []
	params = {}
	with open(parFile, 'r') as cfg:
		for linha in cfg.readlines():
			# apagar espacos em branco no inicio e fim
			linha = linha.strip()
			# a linha eh um comentario ou esta vazia, passar a proxima
			if not linha or linha.startswith('#') or linha.startswith('}'):
				continue
			# criar method
			if linha.endswith('{'):
				group = linha.split('{')[0]
				params[group] = {}
			elif linha.endswith(':'):
				method = linha.split(':')[0]
				params[group][method] = {}
			# criar parametro
			else:
				param, valor = linha.split('=')
				# guardar parametro
				params[group][method][param] = literal_eval(valor)

	return params
