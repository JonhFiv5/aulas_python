# Manipulação de arquivos PDF
# Unindo e dividindo arquivos PDF

# Documentação-> https://pythonhosted.org/PyPDF2/
# Exemplos-> http://www.blog.pythonlibrary.org/2018/06/07/an-intro-to-pypdf2/

# Dependendo da versão do nosso PDF podemos ter alguns erros

import PyPDF2
import os

# Unindo PDFs em um único arquivo
"""
caminho_pdfs = 'aulas_python'

# PdfFileMerger para unir PDFs em um único
novo_pdf = PyPDF2.PdfFileMerger()

for root, dirs, files in os.walk(caminho_pdfs):
    for file in sorted(files):
        if '.pdf' in file:
            caminho_completo = os.path.join(root, file)
            # Abrimos o arquivo em modo de bytes (rb)
            arquivo_pdf = open(caminho_completo, 'rb')
            novo_pdf.append(arquivo_pdf)

# Abrimos no modo de escrita de bytes (wb)
with open(f'{caminho_pdfs}/aula_98_parte_unica.pdf', 'wb') as pdf_unico:
    novo_pdf.write(pdf_unico)
"""

# Separando páginas de um PDF em arquivos diferentes
with open('aulas_python/aula_98_parte_unica.pdf', 'rb') as arquivo_pdf:
    leitor = PyPDF2.PdfFileReader(arquivo_pdf)
    num_paginas = leitor.getNumPages()
    
    for pag in range(num_paginas):
        escritor = PyPDF2.PdfFileWriter()
        pagina_atual = leitor.getPage(pag)
        escritor.addPage(pagina_atual)

        with open(f'aulas_python/aula_98_copia{pag + 1}.pdf', 'wb') as novo_pdf:
            escritor.write(novo_pdf)
