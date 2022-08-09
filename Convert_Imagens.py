from PIL import Image
import os
from colorama import init
from termcolor import colored

init()

pastaImagens = input('[ ? ] Qual o diretório onde as imagens a serem convertidas estão?\nR: ')
extensoes = {
	'1' : 'bmp',
	'2' : 'png',
	'3' : 'jpg',
	'4' : 'jpeg'
}
extensaoArquivos = input('\n[ ? ] Deseja converter as imagens para qual formato ?\n[ 1 ] BMP\n[ 2 ] PNG\n[ 3 ] JPG\n[ 4 ] JPEG\nR: ')

formatoValido = False

while not formatoValido:
	_IdExtensoes = [chave for chave in extensoes.keys()]
	if extensaoArquivos not in _IdExtensoes:
		print('\n\n')
		print('[ ! ] Por favor inserir uma das opções. SOMENTE O NÚMERO !')
		extensaoArquivos = input('[ ? ] Deseja converter as imagens para qual formato ?\n[ 1 ] BMP\n[ 2 ] PNG\n[ 3 ] JPG\n[ 4 ] JPEG\nR: ')
	else:
		formatoValido = True

# Pedir diretório
while not os.path.isdir(pastaImagens):
	print('[ ! ] O caminho passado não é um diretório. Por favor inserir um diretório válido.\n')
	pastaImagens = input('[ ? ] Qual o diretório onde as imagens a serem convertidas para BMP estão?\nR: ')

pastaBmp = pastaImagens + '\\' + "pastaImagensConvertidas_" + extensoes[extensaoArquivos].upper()

print('='*20)
print('ATENÇÃO')
print(f'[ + ] As imagens convertidas serão salvas no caminho: {pastaBmp}')
print('='*20)

# Listar todos os arquivos
arquivos = os.listdir(pastaImagens)
imagens = [imagem for imagem in arquivos if imagem.lower().endswith('jpg') or imagem.lower().endswith('png') or imagem.lower().endswith('jpeg')]
erro = []

if not os.path.isdir(pastaBmp):
	os.mkdir(pastaBmp)

sucesso = 0

for contador, imagem in enumerate(imagens, start=1):
	imagemPadrao = pastaImagens + '\\' + imagem
	#novaImagem = imagem.split('.')[0] + '.bmp'
	novaImagem = imagem.split('.')[0] + '.' + extensoes[extensaoArquivos]
	#input(novaImagem)
	try:
		if not os.path.isfile(pastaBmp + '\\' + novaImagem):
			Image.open(imagemPadrao).convert('RGB').save(pastaBmp + '\\' + novaImagem)
			print(colored(pastaBmp + '\\' + novaImagem + ' - OK', 'green'))
			sucesso += 1
		else:
			print(colored(pastaBmp + '\\' + novaImagem + ' - JÁ EXISTE', 'cyan'))
	except Exception as erroConverterImagem:
		print('\n\n')
		print(colored(pastaBmp + '\\' + novaImagem + ' - ERRO', 'red'))
		print(f'Erro: ' + colored(f'{erroConverterImagem}', 'grey', 'on_red'))
		print('\n\n')
		erro.append(imagem)

	if contador == len(imagens):
		print(f'[ ! ] Conversão concluída com sucesso ! Foram convertidas {sucesso} imagens no total !')
		print(f'Imagens com erro em sua conversão:\n {", ".join(erro)}')