<!-- TOC INICIO -->
- [MARKDOWN](#markdown)
  - [COMMENT](#comment)
  - [DETAILS](#details)
    - [SUMMARY](#summary)
  - [SEPERADOR](#seperador)
  - [TABLE](#table)
      - [WITH IMAGES](#with-images)
  - [ICONS (Github)](#icons-github)
  - [INFO BOX (Github)](#info-box-github)
  - [TASKLIST (Github)](#tasklist-github)
  - [NOTES (Github)](#notes-github)
  - [HTML](#html)
<!-- TOC FIN -->

# MARKDOWN

## COMMENT

This will not appear:
```markdown
[//]: <> (order:asc)
```

## DETAILS

<details>
...

Test Details

...
</details>

### SUMMARY

<details>
<summary>Summary</summary>
...

Test Summary

...
</details>   

## SEPERADOR

***

---

___

## TABLE

| HEAD 1 | HEAD 2 |
|--------|--------|
| VAL 1  | VAL 2  |


#### WITH IMAGES

| ![Imagen 1](imagen1.jpg) | ![Imagen 2](imagen2.jpg) |
|--------------------------|--------------------------|


## ICONS (Github)

:warning:


## INFO BOX (Github)

!!! Info "Nota"
    Descripció de la nota ....

## TASKLIST (Github)

Aquest apart de generar un llistat de `tasques` afegeix un botó per afegit tasques

```[tasklist]
### Llistat 
- [ ] Note
```

## NOTES (Github)

> [!TIP]
> 
> :tips:
> 
> [!NOTE]
> 
> :warning:


## HTML

<div style="display: flex; justify-content: space-between;">
    <img src="imagen1.jpg" alt="Imagen 1" width="45%" />
    <img src="imagen2.jpg" alt="Imagen 2" width="45%" />
</div>
