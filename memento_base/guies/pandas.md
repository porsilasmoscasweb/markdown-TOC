<!-- TOC INICIO -->
- [PANDAS](#pandas)
  - [TREBALLA AMB DATAFRAMES](#treballa-amb-dataframes)
  - [FUNCTIONS](#functions)
  - [ERRORS](#errors)
    - [NO CARREGAR ELS CANVIS](#no-carregar-els-canvis)
<!-- TOC FIN -->

# PANDAS

## TREBALLA AMB DATAFRAMES

La millor forma de treballa amb Pandas a és amb un jupyter.

## FUNCTIONS

* Canviar de type una `column`
pp.curve.index.astype(int)

* Substiruir `NaN` > `False`
pp.curve['cch_fact'].fillna(False)

* Rename `column`
pp.curve.rename({'timestamp': 'utc_datetime'}, axis=1)

* Drop `column`
pp.curve.drop('utc_datetime', axis=1)

## ERRORS

### NO CARREGAR ELS CANVIS

Per recargar els canvis de local, s'ha de reiniciar el `kernel`.