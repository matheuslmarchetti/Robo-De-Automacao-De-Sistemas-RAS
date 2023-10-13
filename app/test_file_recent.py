import os

caminho = r'C:\Users\lungu\OneDrive\Documentos\dev\EMS'
lista_arquivos = os.listdir(caminho)
print(lista_arquivos)

lista_datas_arquivos = []
for arquivo in lista_arquivos:
    data_arquivo = os.path.getmtime(rf'{caminho}\{arquivo}')
    # print(arquivo, data_arquivo)
    lista_datas_arquivos.append((data_arquivo, arquivo))
lista_datas_arquivos.sort(reverse=True)
print(lista_datas_arquivos)
arquivos_mais_recente = lista_datas_arquivos[0]
print(arquivos_mais_recente)
print(arquivos_mais_recente[1])