"""
Estruturas condicionais
if (Se), else, elfi (else if)
"""

idade = 26

"""
# Estrutura condicional if, em C

if(idade < 18){
    printf("Menor de idade");
} else{
    printf("Menor de idade");
}
"""

"""
# Estrutura condicional if, em Java

if(idade < 18){
    System.out.println("Menor de idade");
} else{
    System.out.println("Menor de idade");
}
"""

if idade < 18:
    print('Menor de idade')
elif idade == 18:
    print('Tem 18 anos')
elif idade == 26:
    print('Tem 26 anos')
else:
    print('Maior de idade')
