<!-- TOC INICIO -->
- [VIM](#vim)
  - [TUTORIALS](#tutorials)
  - [MODE](#mode)
  - [Lineas](#lineas)
  - [File](#file)
  - [Commands](#commands)
<!-- TOC FIN -->

# VIM

## TUTORIALS

[OPENVIM](https://openvim.com/)

[GAME](https://vim-adventures.com/)

[GENIUS](http://vimgenius.com/)

[DOC](https://vimschool.netlify.app/introduction/vimtutor/)

[DOC COMMANDS](https://victorhck.gitbook.io/aprende-vim/cap06_modo_insertar)

## MODE

`i`: modo insertar
`v`: modo visual
`ctrl+W`*2: per moure't de finestra


## Lineas

`d`: cut 
`y`: copiar línies seleccionades
`p`: enganxar línies
`x`: borrar char
`u`: undo

`Shift+V`: seleccionar linia
`Ctrl+V`: seleccionar char
`Ctrl+R`: redo
`Ctrl+H`: Borrar un carácter
`Ctrl+W`: Borrar una palabra
`Ctrl+U`: Borrar una línea entera

## File

`:q` to quit (short for :quit)
`:q!` to quit without saving (short for :quit!)
`:wq` to write and quit
`:wq!` to write and quit, attempting to force the write if the file lacks write permission
`:x` to write and quit; like :wq but writes only if modified (short for :exit)
`:qa` to quit all (short for :quitall)
`:cq` to quit, without saving, with a nonzero exit code to indicate failure (short for :cquit)

`i`: Inserta texto antes del cursor
`I`: Inserta texto antes del primer carácter que no sea un espacio en blanco de la línea
`a`: Añadir texto después del cursor
`A`: Añadir texto al final de la línea
`o`: Crea una nueva línea debajo del cursor y cambia al modo insertar
`O`: Crea una nueva línea encima del cursor y cambia al modo insertar
`s`: Elimina el carácter debajo del cursor e inserta texto (sustituye texto)
`S`: Elimina la línea actual e inserta texto (sustituye toda la línea)
`gi`: Inserta texto en la misma posición donde el modo insertar fue detenido por última vez en el *buffer* actual
`gI`: Inserta texto al comienzo de una línea (columna 1)

## Commands

`:<line_number>`: anar a la linea
`:<line_number>+<offset>`: anar a la linea i posició
`:set paste + ENTER` + `:i`: encol·loquem a la línea que volem enganxar el codi en el mateix format i `CTRL+SHIFT+V`
`:%s/article/tutorial/gc`: replace all with confirmation
`:set nu`: Mostrar numero de líneas
