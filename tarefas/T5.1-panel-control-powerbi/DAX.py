medida_diferenza_poboacion = VAR ano_anterior = SELECTEDVALUE('poboacion_galicia'[ano]) - 1
VAR poboacion_ano_anterior = CALCULATE(SUM('poboacion_galicia'[num_poboacion]), FILTER('poboacion_galicia', 'poboacion_galicia'[ano] = ano_anterior))
RETURN SUM('poboacion_galicia'[num_poboacion]) - poboacion_ano_anterior


