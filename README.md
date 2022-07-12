# Criar arquivos de entrada de dados meteorológicos para Delft3D4

## Baixar os dados meteorológicos do ERA5

Ver como baixar os dados [aqui](https://github.com/Dilello/BaixarDadosERA5no-Win10) usando o código [ERA5_request.py](https://github.com/Dilello/BaixarDadosERA5no-Win10/blob/main/ERA5_request.py) 

## Executando o código de conversão de arquivos .nc para os formatos .amp, .amv e .amu  aceitos pelo Deflt3D4

Salvar o código [convert.py](https://github.com/Dilello/CriarArquivosMeteoDelft3D4/blob/main/convert.py) no seu diretório de trabalho onde se encontram os arquivos .nc de dados meteorológicos (Exemplo: pressão e componentes da velocidade do vento a 10 m).

Abrir o terminal do Anaconda, ir até o diretório de trabalho e executar o código:

```python
# python convert.py
```

Digitar o nome do arquivo .nc que deseja converter:

```python
# Input netcdf file name: MeuAquivo.nc
```

Digitar a variável de interesse (exemplo: componente u da velocidade do vento - u10)

```python
# write the variables you want to read (through the gap): u10
```

Criar grid e arquivo e digitar o mês inicial em inglês (ex.: jan, feb, mar, ...):

```python
# write wind grid? y/n y
# start create meteo files? y/n y
# Using month: jan
```

Digitar a contagem do passo do tempo:

```python
# time to write u10(time size (120,)): 120
```


