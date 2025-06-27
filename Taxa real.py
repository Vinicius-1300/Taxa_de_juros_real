import Funções

j = Funções.inflacao()

def taxa_real(jn):
    te = (1 + (jn / 100)) / (1 + (j / 100))
    ir = (te - 1) * 100
    return ir

print('=-' * 5 + '=','TAXA REAL','=' + '-=' * 5)
rend_ef = Funções.validacao_float('\33[4;37mRendimento efetivo: ')
t_real = taxa_real(rend_ef)
print(f'\33[mA taxa real será de \33[0;34m{t_real:.1f}%')

"""
jn = juros nominal
te = taxa efetiva
ir = inflaçõa no período
"""