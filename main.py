#Made By Willian
#Made In Brazil
#This probram is a way to know your anual grades, you just have to write the notes and it'll tell you the average!

#Heading Info
nome    = str(input('Nome: '))
materia = str(input('Matéria: '))
ano     = str(input('Ano: 20'))
serie   = str(input('Série: '))
print ('=' * 16)

#Heading Title
print ()
print ('NOTAS DO ALUNO ' + nome + ' NO ANO DE 20' + ano)
print (materia)
print ('=' * 16)

#1st period
print ()
print ('1º TRIMESTRE')
print ('=' * 16)
av11  = float(input('AV1: '))
av21  = float(input('AV2: '))
av31  = float(input('AV3: '))
av41  = float(input('AV4: '))
rec1  = float(input('RECUPERAÇÃO TRIMESTRAL: '))

#About Recuperation
if rec1 < 7:
    medt1 = (av11 + av21 + av31 + av41) / 4
else:
    medt1 = (av11 + av21 + av31 + av41 + rec1) / 5

print ('A média do 1º Trimestre é: ', medt1)
print ('=' * 16)

#2nd period
print()
print ('2º TRIMESTRE')
print ('=' * 16)
av12  = float(input('AV1: '))
av22  = float(input('AV2: '))
av32  = float(input('AV3: '))
av42  = float(input('AV4: '))
rec2  = float(input('RECUPERAÇÃO TRIMESTRAL: '))

#About Recuperation
if rec2 < 7:
    medt2 = (av12 + av22 + av32 + av42) / 4
else:
    medt2 = (av12 + av22 + av32 + av42 + medt2) / 5

print ('A média do 2º Trimestre é: ', medt2)
print ('=' * 16)

#3rd period
print ()
print ('3º TRIMESTRE')
print ('=' * 16)
av13  = float(input('AV1: '))
av23  = float(input('AV2: '))
av33  = float(input('AV3: '))
av43  = float(input('AV4: '))
rec3  = float(input('RECUPERAÇÃO TRIMESTRAL: '))

#About Recuperation
if rec3 < 7:
    medt3 = (av13 + av23 + av33 + av43) / 4
else:
    medt3 = (av13 + av23 + av33 + av43 + rec3) / 5
    
print ('A média do 3º Trimestre é: ', medt3)
print ('=' * 16)

#final Recuperation + final grades
print ()
recf = float(input('RECUPERAÇÃO FINAL: '))
if recf < 7:
    medf = (medt1 + medt2 + medt3) / 3
else:
    medf = (medt1 + medt2 + medt3 + recf) / 4

print ('SUA NOTA FINAL DE ' + materia + ' FOI: ', medf)

if medf <= 7:
    resultado = 'REPROVADO'
else:
    resultado = 'APROVADO'
    
print (resultado)