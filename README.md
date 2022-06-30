# statusERP
Script criado com a finalidade de atualizar dados e os mostrar em uma tela


Script feito para rodar determinada tarefa com um cronograma, tarefa 1 executa sempre em uma determinada hora, tarefa 2 executa a cada 10 minutos

Tarefa 1 - trocaData() criada para ser executada todo dia as 08:00 horas e 13:00 horas serve para alterar a data no sistema inserindo a data atual deixando sempre as buscas atualizadas do dia.

Tarefa 2 - buscar() criada para ser exucatda em 10 minutos basicamente é um autoclick que atualiza a o relatorio

Criado uma maquinba virtual no windows 10 via Hyper-V, essa VM executa o sistema e o script e nao precisa ser delisgada a vm pois esta junto ao servidor.

Criando tambem um VENV (ambiemnte virtual) - para que os pacotes nao se misture junto ao sistema, .venv incluido no gitignore.