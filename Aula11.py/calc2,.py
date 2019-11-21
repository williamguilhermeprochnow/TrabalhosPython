def calc_mes(valor, rent):
    val_mes = valor * rent
    return val_mes

def calc_ano(valor,rent):
    montante = (valor*(1+rent)**12)-valor
    return montante
