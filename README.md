# Criar arquivos de entrada de dados meteorológicos para Delft3D4

## Baixar os dados meteorológicos do ERA5

Ver como baixar os dados [aqui](https://github.com/Dilello/BaixarDadosERA5no-Win10) usando o código [ERA5_request.py](https://github.com/Dilello/BaixarDadosERA5no-Win10/blob/main/ERA5_request.py) e o código [ERA5_convert.py](https://github.com/Dilello/BaixarDadosERA5no-Win10/blob/main/ERA5_convert.py)

## Executando o código de conversão de arquivos .nc para os formatos .amp, .amv e .amu  aceitos pelo Deflt3D4

Salvar o código [convertv2.py](https://github.com/Dilello/CriarArquivosMeteoDelft3D4/blob/main/convertv2.py) no seu diretório de trabalho onde se encontram os arquivos .nc de dados meteorológicos (Exemplo: pressão ao nível do mar (Pa) e as componentes da velocidade (m/s) do vento a 10 m). O nome dos arquivos devem vir da seguinte maneira:

MSL_Y2020M2.nc

U10M_Y2021M10.

V10M_y2024M9.nc

Abrir o terminal do Anaconda, ir até o diretório de trabalho e executar o código:

```python
# python convertv2.py
```

Digitar o ano do Reference Date do arquivo.mdf (Time frame: Delft3d4 FLOW):

```python
# Input year from Reference Date - Delft3D4 (YYYY): 2018
```
IMPORTANTE: Crie SEMPRE uma data no Reference Date do arquivo.mdf que comece no primeiro instante do ano de interesse (Exemplo: 01 01 2018 00 00 00).

Digitar o ano inicial relativo ao período de modelagem:
Nesse caso, o ano de início da modelagem pode ser posterior ao ano definido no Reference Date do arquivo.mdf

```python
# Input year start run (YYYY): 2020
```

Digitar o ano final relativo ao período de modelagem:

```python
# Input year end run (YYYY): 2024
```

Digitar o mês incial relativo ao período de modelagem:
IMPORTANTE: Baixe SEMPRE uma série temporal começando no primeiro instante do mês de interesse (Exemplo: 2020-7-1 00:00).

```python
# Input month start run (number: 1, 2, ..., 11, 12): 7
```

Digitar o mês final relativo ao período de modelagem:

```python
# Input month end run (number: 1, 2, ..., 11, 12): 9
```

Digitar o dia final relativo ao período de modelagem:

```python
# Input day end run (number: 1, 2, ..., 30, 31): 30
```

Informar o número de variáveis meteorológicas:

```python
# Enter number of variables: 3
```

Informar quais variáveis meteorológicas são:

```python
# Enter variables (MSL, U10M, V10M, ...): MSL
# Enter variables (MSL, U10M, V10M, ...): U10M
# Enter variables (MSL, U10M, V10M, ...): V10M
# [MSL, U10M, V10M]
```
Os arquivos serão salvos na mesma pasta dos arquivos de inputs, porém com os seguintes nomes:

MSL_202002.amp

U10M_202110.amu

V10M_202409.amv
