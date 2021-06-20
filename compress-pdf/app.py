import os
inFile = input('Input pdf: ')
outFile = input('Output pdf: ')
os.system(f'gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/printer -dNOPAUSE -dQUIET -dBATCH -sOutputFile={outFile} {inFile}')
