define s = Character("Steve")
define i = Character("Igor")
define st = Character("Stella")
define e = Character("Elli")
define m = Character("Garota Misteriosa")
define z = Character("Garoto Perdido")

label start:

    play music "audio/romantico.mp3" fadein 1.0

    scene escola

    "Era o primeiro dia de aula do último ano do Ensino Médio para Steve."
    "Ele passou 2 anos apaixonado por sua melhor amiga, Stella."
    "Até então, ele nunca conseguiu declarar-se para ela"
    "Mas esse ano será diferente..."
    "Finalmente ele se sente confiante!"

    show steve
    with dissolve

    s "Estou bastante animado para este ano!!"

    hide steve

    scene sala de aula

    show stella
    with dissolve

    st "E aí Steve, como você está hoje?"
    st "Tudo certo?"

    hide stella

    show steve

    s "Tudo sim, só estou me acostumando a acordar cedo novamente."
    s "Sério, acordar antes das 7 da matina é algo desumano e cruel!"

    hide steve

    s "Stella dá uma leve risada."

    show stella

    st "Você é um bobinho!"

    hide stella

    st "Steve não consegue conter sua felicidade e dá um sorriso de volta."

    scene portaigor

    play sound "audio/somdeporta.mp3"

    "De repente, a porta da sala se abre e por ela entra Igor."

    scene sala de aula

    show igor
    with dissolve

    i "Olá pessoal, qual é a boa?"
    i "Cês viram que a tia da merenda tá dando coxinha?"

    hide igor

    show steve

    s "Demorô, vou lá fazer a boa!!"

    hide steve

    show igor

    i "Mas mudando de assunto, vocês já decidiram em qual clube vão entrar este ano?"

    hide igor

    i "Enquanto igor falava, uma pessoa misteriosa estava atenta a conversa..."

    show stella

    st "Eu já me decidi. Eu quero muito fazer parte do clube de vôlei!"
    st "Acho que pode ser uma ótima oportunidade para eu entrar na equipe de torcida da escola."

    hide stella

    "Steve mostra-se interessado pelo comentário de Stella."

    show igor

    i "Que legal Stella! Eu pretendo fazer parte do clube de futebol, pois é meu esporte favorito."
    i "VAI MENGÃO!"
    i "E você, Steve? Pretende fazer parte de qual clube esse ano?"

    hide igor

    menu:

        "Hum, Stella vai fazer parte do clube de vôlei..."
        "Mas Igor vai fazer parte do de futebol..."

        "Entrar para o clube de vôlei":

            jump volei

        "Entrar para o clube de futebol":

            jump futebol

label volei:

    scene sala de aula

    show steve

    s "Eu acho que vou escolher participar do clube de vôlei."
    s "Eu assisti recentemente a seleção olímpica e fiquei bastante inspirado!"

    hide steve

    show stella

    st "Que legal Steve, é bom que nós vamos poder passar mais tempo juntos!"

    hide stella

    "Steve fica bastante feliz ao ouvir essas palavras."

    show steve

    s "É verdade Stella, eu pensei nisso antes de tomar essa decisão."

    hide steve

    play audio "audio/hit.mp3"

    "Nesse momento, uma garota esbarra em Steve."

    show elli
    with dissolve

    m "Opa, me desculpa..."

    hide elli

    "Disse a garota com a cabeça abaixada e o rosto vermelho."

    show steve

    s "Não, tudo be-"

    hide steve

    play sound "audio/correndo.mp3"
    "Antes que terminasse de falar, a garota saiu correndo da sala."

    show igor

    i "Ué, que menina estranha!"

    hide igor

    show steve

    s "Pois é, eu acho que ela deve estar doida para ir na cantina comprar coxinha."
    s "Pior que é, a gente ficou conversando fiado aqui e a cantina está quase fechando."
    s "Falou pessoal, a gente sê ve por aí!"

    hide steve

    scene escuridao

    "Um tempo se passou, e os jogos escolares estavam quase chegando."
    "Nosso herói se encontra cada vez mais decidido a declarar seu amor."

    scene quadra

    show steve
    with dissolve

    s "Nossa, hoje o treino foi bem cansativo!"
    s "Minhas pernas estão doendo de tanto pular!"

    hide steve

    show stella

    st "Nem me fale, eu também fiquei toda quebrada com essa aula."
    st "Mas e aí, você acha que está pronto para a interclasse desse ano?"
    st "Porque falta só um mês!"

    hide stella

    show steve

    s "Talvez..."
    s "Acredito que esse mês eu consiga melhorar o tanto que preciso."
    s "Aqui Stella, mudando de assunto, queria saber se você está livre esse fim de semana?"

    hide steve

    "Falou Steve com o rosto um pouco tímido."

    show stella

    st "Acredito que sim, por que?"

    "Antes que pudesse responder à pergunta Igor chega e interrompe a conversa..."

    show igor2
    with moveinright

    i "Fala galera, tudo certo?"
    i "Cansados?"

    st "Oii, Igor!"
    st "Nós estamos bem cansados mesmo!"
    st "Pelo jeito, você não. (risos)"

    i "hahaha, eu sou incansável!"
    i "Aí Stella, tá ligada aquele filme que você queria ver, que lançou semana passada?"

    st "Sim, estou..."

    i "Pois bem, arrangei dois ingressos para assistir no cinema."
    i "Tá afim de ir comigo esse fim de semana?"

    st "Sério? Com certeza que eu tô!!!"

    i "Fechado então!"
    i "Ah, se quiser ir também Steve, é só falar que eu te arrumo um ingresso também."

    "Nesse momento, Steve começou a sentir muita raiva, mas resolveu guardar para si."

    hide stella

    hide igor2

    show steve

    s "Tranquilo, precisa não!"
    s "Eu vou passar esse final de semana tentando subir de ranque no LOL."

    hide steve

    show igor

    i "Poxa cara, tem certeza?"

    hide igor

    show steve

    s "Sim, obrigado pelo convite!"

    hide steve

    scene escuridao

    "Aquele final de semana foi um saco."
    "Steve passou jogando LOL enquanto chorava de tristeza e raiva."

    scene vestiario
    play music "audio/suspense.mp3" fadein 1.0

    "Chegou o primeiro dia de interclasse. Steve começara a se preparar para a partida."

    show igor
    with dissolve

    i "Oi Steve!"
    i "Preparado para sua primeira partida?"

    hide igor

    show steve

    i "Por que você está aqui, você não tem o seu jogo também?"
    "Questionou com um tom de voz grosseiro."

    hide steve

    show igor

    i "Poxa, vim aqui só para te desejar sorte. Pra que toda essa grosseria?"
    i "Por um acaso, algo de ruim aconteceu?"

    hide igor

    menu:

        "O fato de Stella e Igor estarem saindo te enche de raiva."

        "Se entregar ao ódio e arrumar uma briga com Igor":

            jump brigouvolei

        "Pedir desculpas pela grosseria":

            jump apoiouvolei

label apoiouvolei:

    play music "audio/romantico.mp3" fadein 1.0

    show steve

    s "Me desculpe Igor, eu estava com a cabeça um pouco quente."
    s "Me perdoe se soei arrogante."

    hide steve

    show igor

    i "Não, de boa, eu entendo..."
    i "Os jogos nos deixam assim mesmo."
    i "Aqui, eu tava combinando com a Stella da gente sair para comer uma coxinha."
    i "Você gostaria de ir com a gente?"

    hide igor

    show steve

    s "Não, obrigado. Estou tentando subir para diamante!"
    s "Falta só um pouco..."
    s "Bom passeio para vocês dois!"

    "Steve aparentava estar bem, mas na verdade estava bem triste com essa situação."
    "Mas não chegaria ao ponto de arrumar uma briga com seu melhor amigo por conta disso."

    hide steve

    scene corredor

    "Algumas horas depois, após a partida de vôlei, Steve acabara se encontrando com a garota misteriosa."

    show elli

    m "Oii Steve! Assisti sua partida, você jogou muito bem!"

    hide elli

    show steve

    s "Obrigado! Eu acho que poderia ter jogado melhor, mas tudo bem."
    s "Mas espera... Como você sabe meu nome?"

    hide steve

    show elli

    m "A gente estuda na mesma sala!"
    m "E eu gosto de você..."
    "Disse bem baixinho."

    hide elli

    show steve

    s "O que você disse?"

    hide steve

    show elli

    m "Nada não! (risos)"
    m "Mas aqui, você e seu amigo estão bem?"
    m "Não querendo me intrometer..."

    hide elli

    show steve

    s "Estamos bem sim... Mas como é que você sabe que nós discutimos?"

    hide steve

    show elli

    m "Eu tenho meus metódos... (risos)"
    m "Se não for incômodo perguntar, por que você estava tão nervoso?"

    hide elli

    show steve

    s "Ah sim, não era nada demais!"
    s "Eu estava passando por alguns problemas pessoais em relação ao meu amigo."
    s "Mas depois eu pensei melhor e achei que não valia a pena brigar por isso."

    hide steve

    show elli

    m "Entendo..."
    m "Respeito sua atitude, não podemos deixar os nervos à flor da pele!"

    hide elli

    show steve

    s "É tenso..."

    hide steve

    show elli

    e "Ah, onde estão meus modos?! Prazer, me chamo Elli, sou sua colega de sala, sento atrás de você!"

    hide elli

    show steve

    s "Ah sim! Prazer, me chamo Steve, mas pelo jeito você já sabia. (risos)"

    hide steve

    show elli

    e "Pois é..."
    "Disse dando uma leve risada."
    e "Mas Steve, mudando de assunto, eu e alguns estamos criando um grupo de estudos para se preparar para a semana de provas."
    e "Você teria vontade de se juntar a nós?"

    hide elli

    menu:

        "Será que vale a pena se juntar a Elli?"

        "Se juntar ao grupo de estudos com Elli":

            jump grupodeestudosapoiou

        "Rejeitar":

            jump limbo

label futebol:

    scene sala de aula

    show steve

    s "Eu acho que vou escolher participar do clube de futebol."
    s "Eu gosto muito de jogar bola!"

    hide steve

    show igor

    i "Aí sim!"
    i "A gente vai poder jogar juntos então."

    hide igor

    show stella

    st "Poxa, vou ficar sozinha..."

    hide stella

    show steve

    s "A gente vai te fazer companhia sempre que pudermos."
    s "Fica triste não!"

    hide steve

    show igor

    i "Sim, e você não vai ficar sozinha de fato."
    i "Você ainda vai ter suas amigas com você, não?"

    hide igor

    show stella

    st "Sim, eu tô só zoando com vocês. (risos)"
    st "Não se preocupem!"

    hide stella

    play audio "audio/hit.mp3"
    "Nesse momento, uma garota esbarra em Steve."

    show elli
    with dissolve

    m "Opa, me desculpa..."

    hide elli

    "Disse a garota com a cabeça abaixada e o rosto avermelhado."

    show steve

    s "Não, tudo be-"

    hide steve

    play sound "audio/correndo.mp3"
    "Antes que terminasse de falar, a garota saiu correndo da sala."

    show igor

    i "Ué, que menina estranha!"

    hide igor

    show steve

    s "Pois é, eu acho que ela deve estar doida para ir na cantina comprar coxinha."
    s "Pior que é, a gente ficou conversando fiado aqui e a cantina está quase fechando."
    s "Falou pessoal, a gente sê ve por aí!"

    hide steve

    scene escuridao

    "Um tempo se passou, e os jogos escolares estavam quase chegando."
    "Nosso herói encontrava-se cada vez mais decidido a declarar o seu amor."

    scene campo

    show steve
    with dissolve

    s "Nossa, a partida de hoje foi acirrada!"

    hide steve

    show igor

    i "Nem me fale..."
    i "O cara me deu uma rasteira na maior cara de pau!"
    i "Eu tô todo dolorido agora."

    hide igor

    show steve

    s "Putz, daqui à pouco é hora do lanche e eu deixei minha mochila no vestiário!"
    s "Vou lá buscar correndo e já volto."
    s "Tô faminto por uma coxinha!"

    hide steve

    show igor

    i "Ai ai, você e suas coxinhas. (risos)"
    i "Fique à vontade, eu vou ver como a Stella está."

    hide igor

    show steve

    s "Beleza, depois eu encontro vocês no ginásio."

    hide steve

    play sound "audio/correndo.mp3"
    "Steve sai correndo, louco para poder fazer seu lanche."

    scene corredor

    play audio "audio/hit.mp3"
    "No caminho para o vestiário, Steve sem querer bate de frente com uma garota."
    "Era uma garota familiar..."

    show steve

    s "Nossa, me desculpa!"

    hide steve

    show elli
    with dissolve

    m "Tudo bem, eu que estava distraída."

    hide elli

    show steve

    s "Que isso, a culpa foi minha."
    s "Você tá bem?"
    s "Se machucou?"

    hide steve

    show elli

    m "Estou bem sim, hahaha..."
    "Nesse momento, Steve lembrouse daquela garota."
    hide elli

    show steve

    s "Ah, é você que esbarrou comigo há um tempo atrás correndo para comprar coxinha!"
    "A garota ficou sem entender muito bem a parte da coxinha, mas se lembrava do resto."

    hide steve

    show elli

    m "Sim, eu mesma!"
    "Disse sorridente."
    m "Mas para onde você estava indo com tanta pressa?"

    hide elli

    show steve

    s "Ah, eu tava indo no vestiário do clube de futebol pegar um dinheiro que deixei lá."

    hide steve

    show elli

    m "Você também faz parte do clube de futebol?"
    "A garota parecia já saber desse detalhe, mas talvez quissese desenvolver a conversa..."

    hide elli

    show steve

    s "Sim, eu sou o zagueiro do time da escola."
    s "Você também joga futebol?"

    hide steve

    show elli

    m "Sim, eu jogo no time feminino."
    e "Aliás eu me chamo Elli, prazer!"

    hide elli

    show steve

    s "Prazer, me chamo Steve. Bem legal saber que também curte futebol."
    s "Me desculpe, mas agora eu preciso correr, se não vou perder o horário."
    s "Outra hora a gente pode conversar mais."

    hide steve

    "O semblante de Elli parecia bem feliz."

    scene quadra

    "Após comer sua tão sonhada coxinha, Steve foi correndo encontrar-se com Stella e Igor no ginásio."

    show steve
    with dissolve

    s "Ei gente, cheguei. Como vocês estão?"

    hide steve

    show stella

    st "Eu tô toda quebrada!"
    st "Não aguento mais pular..."

    hide stella

    show steve

    s "Tenso..."
    s "Onde tá o Igor?"
    "Perguntou ao perceber que o mesmo não se fazia presente."

    hide steve

    show stella

    st "Ele foi ao banheiro."

    hide stella

    show steve

    s "Entendi..."
    s "Aqui Stella..."
    s "Gostaria de saber se você está livre este fim de semana..."

    hide steve

    "Steve dissera isso com o rosto envergonhado."

    show stella

    st "Acredito que sim, por que?"

    "Antes que pudesse responder a pergunta Igor chega e interrompe a conversa."

    show igor2
    with moveinright

    i "Fala galera, tudo certo?"
    i "Cansados?"

    st "Oii, Igor!"
    st "Nós estamos bem cansados mesmo."
    st "Pelo jeito, você não. (risos)"

    i "Hahaha, eu sou incansável!"
    i "Aí Stella, tá ligada o filme que lançou semana passada... Que você queria ver?"

    st "Sim, estou..."

    i "Pois bem, arrangei dois ingressos para a seção em IMAX!!"
    i "Tá afim de ir comigo esse fim de semana?"

    st "Sério?! Com certeza que eu tô!!!"

    i "Fechado então!"
    i "Ah, se quiser ir  Steve, é só falar que eu te arrumo um ingresso também."

    "Nesse momento, Steve começou a sentir muita raiva, mas resolveu guardar para si."

    hide stella

    hide igor2

    show steve

    s "Tranquilo, precisa não!"
    s "Eu vou passar esse final de semana tentando subir de ranque no LOL."

    hide steve

    show igor

    i "Poxa cara, tem certeza?"

    hide igor

    show steve

    s "Sim, obrigado pelo convite!"

    hide steve

    scene escuridao

    "Aquele final de semana foi um saco."
    "Steve passou jogando LOL enquanto chorava de tristeza e raiva."

    scene vestiario
    play music "audio/suspense.mp3" fadein 1.0

    "Chegou o primeiro dia de interclasse."
    "Steve começara a se preparar para a partida."

    show igor
    with dissolve

    i "Oi Steve!"
    i "Preparado para sua primeira partida?"

    hide igor

    show steve

    i "Por que você está aqui, você não tem o seu jogo também?"
    "Questionou com um tom de voz grosseiro."

    hide steve

    show igor

    i "Poxa, vim aqui só para te desejar sorte."
    i "Pra que toda essa grosseria?"
    i "Por acaso aconteceu algo de ruim?"

    hide igor

    menu:

        "O fato de Stella e Igor estarem saindo junto te enche de raiva."

        "Se entregar ao ódio e arrumar uma briga com Igor":

            jump brigoufutebol

        "Pedir desculpas pela grosseria":

            jump apoioufutebol

label brigoufutebol:

    show steve

    s "Não se faça de besta, tudo de ruim aconteceu!"
    s "Você é meu melhor amigo, sabe que eu gosto da Stella, como pôde chama-lá para sair?"

    hide steve

    show igor

    i "Ah então é isso..."
    i "Apesar de ser seu amigo eu leio mentes."
    i "Além do mais, você é muito lerdo com esse tipo de coisa!"
    i "E como você não tomava uma atitude resolvi fazer as coisas do meu jeito."
    i "Afinal eu também gosto dela!!"

    hide igor

    show steve

    s "COMO OUSA!"

    hide steve

    play sound "audio/porrada.mp3"
    "Neste momento, impulsionado pela raiva Steve lança-se em cima de Igor e uma briga começa."
    "Elli, que por algum motivo misterioso estava na porta do vestiário, ao perceber a situação, chamou o diretor."
    "Steve e Igor foram levados à diretoria e ambos levaram suspensão de 3 dias pelo ocorrido."

    scene escuridao

    "3 DIAS DEPOIS..."

    scene sala de aula

    show steve

    s "Bom dia, como andaram as coisas por aqui com a minha ausência?"

    hide steve

    show stella

    st "BOM DIA É O ESCAMBAL!!"
    st "O Igor me contou tudo o que aconteceu!"
    st "Como você pôde agredi-lo desta maneira?"
    st "Achei que fôssemos amigos, mas amigos não agem dessa forma!"
    st "Eu e o Igor estamos namorando agora, e eu espero que você nos deixe em paz daqui em diante."

    hide stella

    show steve

    s "Mas Ste-"

    hide steve

    show stella

    st "Mas nada, passar bem Steve!"

    hide stella

    "Stella sai da sala furiosa indicando que a amizade dos dois teria terminado."
    "Steve encontrava-se desolado, e ainda tentava processar tudo o que havia acontecido."

    scene corredor

    play music "audio/musicatriste.mp3" fadein 2.0

    "Durante o intervalo Steve é abordado por Elli, que percebera que ele se encontrava entristecido."

    show elli
    with dissolve

    e "Hey, não pude deixar de notar que você está triste. Aconteceu alguma coisa?"

    hide elli

    show steve

    s "Ah... oi..."
    s "Está tudo bem, estou apenas refletindo um pouco sobre o que têm acontecido na minha vida."

    hide steve

    show elli

    e "Se precisar de um ombro amigo é só falar!"

    hide elli

    show steve

    s "Obrigado, mas acho que só preciso de um tempo sozinho..."

    hide steve

    show elli

    e "Tudo bem então, mas gostaria de deixar uma proposta no ar..."
    e "Eu e alguns amigos estamos criando um grupo de estudos para se preparar para a semana de provas."
    e "Gostaria muito que você participasse conosco!!"
    e "Acredito que pode ser um bom remédio pra você."
    e "Vai estar ocupando a mente com algo produtivo."
    e "O que acha?"

    hide elli

    menu:

        "Será que vale a pena juntar-se a Elli?"

        "Se juntar ao grupo de estudos com Elli":

            jump grupodeestudosbriga

        "Rejeitar":

            jump rejeitar

label brigouvolei:

    show steve

    s "Não se faça de besta, tudo de ruim aconteceu!"
    s "Você é meu melhor amigo, sabe que eu gosto da Stella, como pôde chama-lá para sair?"

    hide steve

    show igor

    i "Ah então é isso..."
    i "Apesar de ser seu amigo eu não leio mentes."
    i "Além do mais, você é muito lerdo com esse tipo de coisa!"
    i "E como você não tomava uma atitude resolvi fazer as coisas do meu jeito."
    i "Afinal eu também gosto dela!!"

    hide igor

    show steve

    s "COMO OUSA!"

    hide steve

    play sound "audio/porrada.mp3"

    "Neste momento, impulsionado pela raiva Steve lança-se em cima de Igor e uma briga começa."
    "Uma garota que estava por perto, ouviu a briga e ao perceber a situação chamou o diretor."
    "Steve e Igor foram levados à diretoria e ambos levaram suspensão de 3 dias pelo ocorrido."

    scene escuridao

    "3 DIAS DEPOIS..."

    scene sala de aula

    show steve
    with dissolve

    s "Bom dia, como andaram as coisas por aqui com a minha ausência?"

    hide steve

    show stella

    st "BOM DIA É O ESCAMBAL!"
    st "O Igor me contou tudo que aconteceu!"
    st "Como você pôde agredi-lo desta maneira?"
    st "Achei que fôssemos amigos, mas amigos não agem dessa forma!"
    st "Eu e o Igor estamos namorando agora, e eu espero que você nos deixe em paz daqui em diante"

    hide stella

    show steve

    s "Mas Ste-"

    hide steve

    show stella

    st "Mas nada, passar bem Steve!"

    hide stella

    "Stella sai da sala furiosa indicando que a amizade dos dois havia terminado."
    "Steve encontrava-se desolado, e ainda tentava processar tudo o que havia acontecido."

    scene corredor

    play music "audio/musicatriste.mp3" fadein 2.0

    "Durante o intervalo, Steve é abordado pela garota misteriosa, que percebera que o mesmo aparentava estar triste."

    show elli
    with dissolve

    m "Hey, não pude deixar de notar que você está triste, aconteceu alguma coisa?"

    hide elli

    show stevetriste

    s "Ah... oi..."
    s "Está tudo bem, estou apenas refletindo um pouco sobre o que vem acontecido na minha vida."

    hide stevetriste

    show elli

    m "Peço desculpas pela sua suspensão, fui eu quem contei ao diretor sobre o ocorrido."

    hide elli

    show stevetriste

    s "Não, tudo bem. Você fez o certo. Eu que errei."
    s "Álias, meu nome é Steve. Acho que nunca nos apresentamos antes."
    s "Você é aquela garota que esbarrou comigo aquele dia, certo?"

    hide stevetriste

    show elli

    m "Sou eu sim...(risos)"
    m "Prazer, me chamo Elii!"
    e "Aquele dia eu estava meio estabanada, e acabei me embananando pra não chegar em última na fila da coxinha!"

    hide elli

    show steve

    s "Ah sim... sendo assim é por um motivo justo."

    hide steve

    show elli

    e "Mas hein, mudando de assunto, eu e um grupo de amigos estamos montando um grupo de estudos."
    e "Gostaria muito que você participasse com a gente. Acredito que será um bom remédio para você!"
    e "Vai estar ocupando a mente com algo produtivo."
    e "O que acha?"

    hide elli

    menu:

        "Será que vale a pena juntar-se a Elli?"

        "Se juntar ao grupo de estudos com Elli":

            jump grupodeestudosbriga

        "Rejeitar":

            jump rejeitar

label grupodeestudosbriga:

    play music "audio/musicafeliz.mp3" fadein 1.0

    show steve

    s "Obrigado Elli, fico muito feliz de receber esse convite!"
    s "É claro que eu aceito!"
    s "Acho que vai ser muito bom para mim!"

    hide steve

    show elli

    e "Que bom que você se animou."
    e "Espero te ver na nossa primeira reunião!"
    "Falou com uma olhar sorridente."

    hide elli

    show steve

    s "Pode deixar!"

    hide steve

    scene biblioteca

    "Alguns dias depois..."
    "Steve e Elli começaram a estudar juntos."

    show steve

    s "Rapaz, essa parada de trigonometria é triste!"
    s "É mais difícil do que subir de ranque no LOL! (risos)"

    hide steve

    show elli

    e "Nossa, então você também é lolzeiro?"

    hide elli

    show steve

    s "Por que? Você também joga?"

    hide steve

    show elli

    e "Sim, meu ranque já é mestre!"
    "Nesse momento, Steve ficata boquiaberto."

    hide elli

    show steve

    s "Cê ta zuando comigo! Eu aqui tô morrendo para subir pro diamante!"

    hide steve

    show elli

    e "Se você quiser, eu posso te ajudar a subir de ranque."

    hide elli

    show steve

    s "Mas é claro, seria uma honra!"
    s "Qual seu nick no jogo?"

    hide steve

    show elli

    e "FotosdeCantorHD."

    hide elli

    show steve

    s "Ah, o meu é ZicaGamesXD."

    hide steve

    "Nesse instante, um garoto aparentemente perdido se aproxima."

    show zoru
    with dissolve

    z "Opa, é aqui que vende coxinha?"
    z "Não consigo encontrar a lanchonete!"

    hide zoru

    show steve

    s "Não, acho que você está perdido, meu amigo."
    s "Aqui na verdade é a biblioteca."

    hide steve

    show zoru

    z "MAS COMO ISSO É POSSÍVEL?!"
    z "JÁ ESTOU ANDANDO A MAIS DE UMA HORA!!!"

    hide zoru

    "O garoto então se irrita e sai correndo em busca da lanchonete."

    show elli

    e "Você conhece esse cara?"

    hide elli

    show steve

    s "Nunca nem vi!"

    hide steve

    scene escuridao

    "Deste dia em diante, Elli e Steve passaram a jogar LOL frequentemente."
    "O relacionamentos dos dois crescia cada dia mais."

    scene escola

    show elli
    with dissolve

    e "Você melhorou bastante desde que começamos a jogar juntos!"

    hide elli

    show steve

    s "Graças a você!"
    s "Meu objetivo agora é virar o melhor do Brasil!"

    play sound "audio/onibus.mp3"

    s "Opa, meu ônibus chegou, acho que vou nessa."
    s "Falou Elli."

    "Antes que Steve atravessase a rua, Elli puxa sua mão."

    hide steve

    show elli

    e "Espere Steve!"
    e "Eu preciso falar uma coisa importante com você."

    hide elli

    show steve

    s "O que foi, está tudo bem com você?"

    hide steve

    show elli

    e "Lembra daquele dia que esbarrei com você na sala, no início do ano?"

    hide elli

    show steve

    s "Lembro sim, por que?"

    hide steve

    show elli

    e "A partir daquele dia, eu comecei a sentir algo por você."
    e "Por isso que eu acabei te seguindo em certos momentos."
    e "Como no dia em que você discutiu com seu amigo."
    e "Eu sei que é estranho, mas o meu coração falou mais alto!"
    e "Eu não suporto mais pensar em você!"
    e "E portanto, finalmente decidi externar isso!"
    e "Você aceita namorar comigo?"

    hide elli

    menu:

        "Que decisão difícil, o que fazer?"

        "Aceitar o pedido de Elli":

            jump finalElli

        "Não corresponder":

            jump assasinato


label rejeitar:

    show stevetriste

    s "Agradeço pelo convite Elli, e também pelo fato de você estar tentando me animar."
    s "Você é uma garota legal, por isso peço que não desperdice seu tempo comigo..."
    s "Você merece amigos mais leais!"
    s "Acho que vou andando..."

    hide stevetriste

    show elli

    e "Ah não diga isso..."

    hide elli

    "Nosso herói não deu ouvidos a Elli que tentou ajudá-lo."

    scene morte

    "Depois daquele dia, Steve ficou um tempo sem ir para a escola."
    "Após brigar com seu melhor amigo, perder a chance de namorar com a garota que amava, e ainda perder a chance de conhecer alguém melhor."
    "Steve acabara por não ter mais esperanças na vida, adentrando numa profunda depressão."
    "Anos depois, os colegas de Steve se encontraram com a mãe dele, e acabaram recebendo a fatídica notícia de que Steve tornara-se {b}INCEL!{/b}"

return

label apoioufutebol:

    play music "audio/romantico.mp3" fadein 1.0

    show steve

    s "Me desculpe Igor, eu estava com a cabeça um pouco quente!"
    s "Me perdoe se soei arrogante..."

    hide steve

    show igor

    i "Não, de boa, eu entendo."
    i "Os jogos nos deixam assim mesmo."
    i "Aqui, eu tava combinando com a Stella da gente sair este fim de semana."
    i "Você gostaria de vir com a gente?"

    hide igor

    show steve

    s "Não, obrigado... Esse fim de semana eu vou tentar subir pra diamante no LOL."
    s "Falta só um pouco."
    s "Bom passeio para vocês dois!"
    "Steve aparentava estar bem, mas na verdade estava bem triste com a situação."
    "Mas não chegaria ao ponto de arrumar uma briga com seu melhor amigo por isso."

    hide steve

    scene corredor

    "Algumas horas depois, após a partida de futebol, Steve acabara se encontrando novamente com Elli."

    show elli

    e "Oii Steve! Assisti sua partida, você jogou muito bem!"

    hide elli

    show steve

    s "Obrigado! Apesar de ter marcado um gol pro time, defensivamente eu fui muito mal!"
    s "O que é ruim para um zagueiro..."

    hide steve

    show elli

    e "Que isso, você arrasou sim!"
    "Disse Elli com o rosto corado."
    e "Mas agora mudando de assunto, você e seu amigo estão bem?"
    e "Não querendo me intrometer..."

    hide elli

    show steve

    s "Estamos bem sim... Mas como é que você sabe que nós discutimos?"

    hide steve

    show elli

    e "Eu tenho meus metódos...(risos)"
    e "Se não for incômodo perguntar, por que você estava tão nervoso?"

    hide elli

    show steve

    s "Ah sim, não era nada demais!"
    s "Eu estava passando por alguns problemas pessoais em relação ao meu amigo."
    s "Mas depois eu pensei melhor e achei que não valeria à pena brigar por isso."

    hide steve

    show elli

    e "Entendo..."
    e "Respeito sua atitude, não podemos deixar os nervos à flor da pele!"

    hide elli

    show steve

    s "É tenso..."

    hide steve

    show elli

    e "Mas hein Steve, eu e alguns estamos criando um grupo de estudos para se preparar para a semana de provas."
    e "Você teria vontade de se juntar a nós?"

    hide elli

    menu:

        "Será que vale a pena juntar-se a Elli?"

        "Se juntar ao grupo de estudos com Elli":

            jump grupodeestudosapoiou

        "Rejeitar":

            jump limbo

label limbo:

    scene corredor

    show steve

    s "Muito obrigado pelo convite, mas eu gosto de estudar sozinho."
    s "Muita gente me desconcentra."

    hide steve

    show elli

    e "Ah... tudo bem eu entendo, mas anota o meu número, caso você mude de ideia!"

    hide elli

    show steve

    s "Claro, anoto sim!"

    hide steve

    scene esperanca

    "Daquele dia em diante Steve e Elli passaram a ser amigos."
    "Steve dessistiu da ideia de ficar com Stella, muito por conta do seu amigo Igor."
    "Começara a focar mais em seus projetos pessoais. Escolhendo um caminho {b}SOLITÁRIO{/b} em se tratando do amor..."

return

label grupodeestudosapoiou:

    scene corredor

    show steve

    s "Depende... Vai rolar coxinha?"

    hide steve

    show elli

    e "Pode apostar que sim!"

    hide elli

    show steve

    s "Então estou dentro!"

    hide steve

    show elli

    e "Legal!"

    hide elli

    scene biblioteca

    "Alguns dias depois..."
    "Steve e Elli começaram a estudar juntos."

    show steve

    s "Rapaz, essa parada de trigonometria é triste!"
    s "É mais difícil do que subir de ranque no LOL."

    hide steve

    show elli

    e "Nossa, então você também é lolzeiro?"

    hide elli

    show steve

    s "Por que? Você também joga?"

    hide steve

    show elli

    e "Sim, meu ranque já é mestre!"
    "Nesse momento, Steve ficara boquiaberto."

    hide elli

    show steve

    s "Cê ta zuando comigo! E eu aqui morrendo para chegar em diamante!"

    hide steve

    show elli

    e "Se você quiser, eu posso te ajudar a subir de ranque."

    hide elli

    show steve

    s "Mas é claro, seria uma honra!"
    s "Qual seu nick no jogo?"

    hide steve

    show elli

    e "FotosdeCantorHD."

    hide elli

    show steve

    s "Ah, o meu é ZicaGamesXD."

    hide steve

    "Nesse instante, um garoto aparentemente perdido se aproxima."

    show zoru
    with dissolve

    z "Opa, é aqui que vende coxinha?"
    z "Não consigo encontrar a lanchonete!"

    hide zoru

    show steve

    s "Não, acho que você está perdido, meu amigo."
    s "Aqui na verdade é a biblioteca."

    hide steve

    show zoru

    z "MAS COMO ISSO É POSSÍVEL?!"
    z "JÁ ESTOU ANDANDO A MAIS DE UMA HORA!!!"

    hide zoru

    "O garoto então se irrita e sai correndo em busca da lanchonete."

    show elli

    e "Você conhece esse cara?"

    hide elli

    show steve

    s "Nunca nem vi!"

    hide steve

    scene escuridao

    "Desse dia em diante, Elli e Steve passaram a jogar LOL frequentemente."
    "O relacionamentos dos dois crescia cada dia mais."

    scene escola

    show elli
    with dissolve

    e "Você melhorou bastante desde que começamos a jogar juntos!"

    hide elli

    show steve

    s "Graças a você!"
    s "Meu objetivo agora é virar o melhor do Brasil!"

    play sound "audio/onibus.mp3"

    s "Opa, meu ônibus chegou, acho que vou nessa."
    s "Falou Elli!"

    "Antes que Steve atravessase a rua, Elli puxa sua mão."

    hide steve

    show elli

    e "Espere Steve!"
    e "Eu preciso falar uma coisa importante com você."

    hide elli

    show steve

    s "O que foi, tá tudo bem com você?"

    hide steve

    show elli

    e "Lembra daquele dia que esbarrei com você na sala, no início do ano?"

    hide elli

    show steve

    s "Lembro sim, por que?"

    hide steve

    show elli

    e "A partir daquele dia, eu comecei a sentir algo por você."
    e "Por isso que eu acabei te seguindo em certos momentos."
    e "Como no dia em que você discutiu com seu amigo."
    e "Eu sei que é estranho, mas o meu coração falou mais alto!"
    e "Eu não suporto mais pensar em você!"
    e "E portanto, decidi finalmente esternar isso."
    e "Você aceita namorar comigo?"

    hide elli

    menu:

        "Que decisão difícil, o que fazer?"

        "Aceitar o pedido de Elli":

            jump finalElli

        "Não corresponder":

            jump assasinato

label finalElli:

    scene escola

    show steve

    play music "audio/ellitheme.mp3" fadein 1.0

    s "Depois da discussão com meu amigo, eu fiquei triste por conta de outra garota."
    s "Mas conhecer você me trouxe alegria novamente!"
    s "É claro que eu aceito!"

    hide steve

    scene pordosol

    "A partir desse dia, Steve e Elli passaram a compartilhar boas tardes jogando LOL e comendo coxinha."
    "Steve finalmente encontrou o amor verdadeiro."
    "E eles se tornaram {b}ETERNOS NAMORADOS{/b}!"

    scene sunset

    show zoru

    z "Sério mesmo que ninguém sabe me dizer onde vende coxinha...?"

    hide zoru
    with dissolve

return

label assasinato:

    play music "audio/sadelli.mp3" fadein 1.0 volume 2.0

    scene escola

    show steve

    s "Uau..."
    s "Foi bastante informação para processar!(risos)"
    s "Olha Elli, eu gosto muito de você."
    s "Mas eu ainda sou muito apaixonado pela Stella e planejo me declarar para ela no dia de hoje!"
    s "Espero que entenda..."

    hide steve

    show elli

    e "Ah...claro..."
    e "Onde eu estava com a cabeça, acabei confundido as coisas...(suando)"

    hide elli

    "Elli dissera aquilo mas em seu íntimo estava devastada."
    "Passara todo aquele tempo com Steve e sentira uma enorme paixão por ele."
    "Agora que este a rejeitara, seu coração ardia em amargura e tristeza..."

    show steve

    s "Tudo bem, acontece! (risos)"
    s "Enfim, agora eu vou indo nessa!"

    hide steve

    show elli

    e "Ah... boa sorte..."
    "Disse Elli furiosa em seu âmago."

    hide elli

    show steve

    s "Tchau, te vejo amanhã!"

    hide steve

    "Steve não sabia, mas sua escolha lhe resultaria em consequências inimagináveis."

    scene lanchonete

    play music "audio/musicafeliz.mp3" fadein 1.0

    "Mais tarde naquele dia..."
    "Steve marcara com Stella para encontrarem-se na lanchonete."
    "Para Steve tratava-se do tão aguardado momento em que se declararia."

    show steve
    with dissolve

    s "Hey Stella, obrigado por ter aceitado o meu convite."
    s "Acredito que você vai gostar, ouvi dizer que nessa lanchonete vende uma coxinha divina!"

    hide steve

    show stella

    st "Sim, ouvi falar também, por isso nem pensei duas vezes antes de aceitar!"

    hide stella

    show steve

    s "Então não vamos perder tempo."
    s "Garçom, manda pra gente a melhor coxinha da casa!"

    hide steve

    "Enquanto saboreavam uma deliciosa coxinha, o papo fluia por um tempo."
    "Até que Steve finalmente encontrou o momento perfeito para falar."

    show steve

    s "Foi muito bom esse momento que tivemos Stella, eu me diverti bastante!"

    hide steve

    show stella

    st "Sim, fazia tempo que eu não tinha um momento tão agradável!"
    st "Ultimamente tenho estado bastante ocupada estudando para as provas..."

    hide stella

    show steve

    s "Sim, eu e a Elli também temos estudado bastante!"
    s "Mas enfim, essa noite eu lhe trouxe aqui Stella, pois na verdade gostaria de lhe contar algo..."

    hide steve

    show stella

    st "Sou toda ouvidos!"

    hide stella

    show steve

    s "Stella, nós já somos amigos antes mesmo do Ensino Médio."
    s "Desde o momento em que eu lhe conheci, eu sabia que seriamos grandes amigos."
    s "Mas o tempo foi passando e o que era uma amizade passou a ser algo a mais para mim."
    s "No início achei que eram apenas coisas da minha cabeça..."
    s "Mas todas as vezes que eu te via o meu coração batia diferente!"
    s "Então... eu lhe trouxe aqui hoje pois gostaria de lhe ped-"

    hide steve

    show stella

    st "Espera Steve!"
    "Interrompeu Stella, antes que nosso herói terminasse de falar."

    st "Olha, eu tive de lhe interromper, pois está óbvio aonde você quer chegar."
    st "Eu achei muito lindo o que você disse Steve..."
    st "Durante todo este tempo em que nos conhecemos, eu nutro o mesmo sentimento por você."
    st "E assim como você, eu também não tive coragem de externar o que estava sentindo."
    st "Eu quero muito responder sim para a sua pergunta."
    st "Mas eu preciso te dizer que o Igor também me pediu em namoro..."

    hide stella

    "Quando Stella pronunciou tais palavras, Steve derrubou sua coxinha no chão."
    "Estava completamente incrédulo."

    show stella

    st "Naquele dia em que fomos ao cinema, ele se declarou para mim."
    st "Planejou toda aquela noite, eu estava confusa e não queria magoá-lo..."
    st "Mas é você que eu realmente amo, Steve!"
    st "O que eu devo fazer?"

    hide stella

    menu:

        "Steve está em uma encruzilhada."
        "Por um lado, deseja ficar com o amor de sua vida. Mas por outro, não quer apunhalar o seu amigo."

        "Propor a Stella que os dois fiquem juntos":

            jump fugircomstella

        "Não corresponder Stella e ficar do lado de seu amigo":

            jump naocorresponder

label fugircomstella:

    scene lanchonete

    show steve

    s "Uau... eu não sei nem o que dizer..."
    s "Nunca passou pela minha cabeça que você também me visse desta forma."
    s "Eu sei que parece loucura Stella, mas vamos fugir juntos!"

    hide steve

    show stella

    st "Como assim, Steve?"
    st "Não temos como fugir, tudo que nós temos está aqui em São Paulo."

    hide stella

    show steve

    s "Eu sei disso Stella, mas meus avós estão planejando se mudare para o Rio Grande do Sul no final do ano."
    s "Podemos ir com eles depois de nos formarmos, e começarmos uma vida juntos."
    s "Eu sei que estou sendo egoísta."
    s "Mas eu te amo Stella! E quero passar o resto da minha vida ao seu lado!"

    hide steve

    "Stella demorara um pouco para se convencer do plano de Steve."
    "Mas o seu amor por ele era tamanho que ela se convencera da ideia."
    "Steve e Stella estavam decididos a fugirem juntos." #S e S = S2
    "Mas nem tudo andaria como o planejado..."

    scene corredormorte

    play music "audio/stevedeath.mp3" fadein 1.0

    "NO DIA SEGUINTE, NA ESCOLA..."

    show igor
    with dissolve

    i "Bom dia Elli, chegou mais cedo hoje?"

    hide igor

    show elli

    e "Sim Igor, e foi justamente para conversar com você!"

    hide elli

    show igor

    i "Comigo?"
    i "O que foi que aconteceu?"

    hide igor

    show elli

    e "Soube que você e a Stella começaram a namorar, certo?"

    hide elli

    "Igor fica surpreso com o interrogamento de Elli."

    show igor

    i "Ah... ainda iriamos esperar o momento certo para falarmos disso..."
    i "Mas sim, começamos a namorar há pouco tempo."
    i "Como você ficou sabendo disso?"

    hide igor

    show elli

    e "Acho que antes, você gostaria de ver isso!"

    hide elli

    "Elli mostra uma filmagem para Igor em seu celular."
    "Tratava-se da conversa que Steve tivera com Stella na noite anterior."

    show igor

    i "Como isso é possível? Só pode ser uma piada!"

    "Igor estava incrédulo com o que acabara de ver."

    i "Como você conseguiu isto?"

    hide igor

    show elli

    e "Eu tenho meus métodos...(risos)"

    "Disse Elli com uma malícia em seu sorriso."

    e "O motivo pelo qual mostrei isso a você, é para desmascarar o tipo de pessoa que o Steve realmente é!"
    e "Da mesma forma que ele traiu à você, ele também feriu o meu coração!"
    e "E por isso, gostaria de lhe propor algo..."

    hide elli

    scene casaigor

    "Passados 3 dias, Igor fez um convite à Steve para jogar videogame em sua casa."
    "Pediu que não contasse a ninguém sobre isso, pois seus pais não sabiam que ele traria amigos em casa."

    show steve
    with dissolve

    s "IGOR, IGOR!"
    "Steve gritava no portão de seu amigo, mas este não atendia."

    s "Por que será que ele não atende?"
    s "Vou verificar a entrada dos fundos..."

    hide steve

    "Steve tentou chamar pela entrada dos fundos, mas novamente ninguém atendia."
    "Até que Steve percebera que a porta dos fundos, que dava acesso à cozinha, estava destrancada."

    play sound "audio/somdeporta.mp3"

    "Steve então decidiu entrar e verificar se seu amigo estava em casa."

    scene cozinha

    show steve

    s "Igor?"
    s "A porta dos fundos estava aberta, decidi entrar tudo bem?"
    s "Tem alguém em casa?"

    hide steve

    "Havia um silêncio absoluto na casa e não havia sinal algum de seu amigo."
    "Até que da janela da cozinha, Steve notara algo."
    #Se sobrar tempo, colocar uma imagem bacana desse momento
    "Era Igor e Elli na janela pelo lado de fora, acenavam para Steve."
    "Parecia haver algo nas mãos de Igor..."

    show steve

    s "Estava te procurando amigo."
    s "Por que não entra para podermos jogar?"
    s "Elli também está aí?"

    hide steve

    "Steve notara que o que Igor carregava tratava-se de um coquetel molotov."

    show steve

    s "O que está fazendo com isso na mão, é perigoso!"

    hide steve

    "Finalmente após um tempo, Igor pora-se a falar..."

    show igor

    i "Você jogou bem Steve."
    i "Mas fez a escolha errada!"

    hide igor

    scene incendio

    "Em um instante não existia mais Steve."
    "Eram apenas Elli e Igor na rua e uma densa paisagem vermelha de fundo..."
    "Todas as memórias e lembranças foram {b}QUEIMADAS{/b} juntas com o fogo..."

return

label naocorresponder:

    scene lanchonete

    play music "audio/musicatriste.mp3" fadein 1.0

    show steve

    s "Uau... eu não sei nem o que dizer!"
    s "Nunca passou pela minha cabeça que você também me visse dessa forma."
    s "Mas eu também não tinha ideia sobre você e o Igor."
    s "Eu fiquei sentido quando ele te chamou para sair aquele dia."
    s "Tivemos até alguns desentendimentos..."

    hide steve

    show stella

    "Stella ficara surpresa com a revelação de Steve."

    st "Como assim? Não sabia que quase chegou a este ponto."
    st "Ainda bem que não aconteceu nada grave!"

    hide stella

    show steve

    s "Sim, isso são águas passadas..."
    s "Não pretendo trair a confiança do meu amigo!"
    s "Você deu a sua palavra pra ele, e acredito que o melhor é que vocês continuem juntos."
    s "Daqui em diante continuaremos sendo apenas amigos, Stella!"

    hide steve

    "Stella e Steve realmente não estavam destinados a ficarem juntos."
    "Steve decidira que o melhor a se fazer era seguir em frente e preservar uma boa amizade."
    "Os dois terminaram aquela noite saboreando mais uma coxinha e parecia ser o início de novos tempos."
    "Mas aquela semana ainda guardava altos momentos..."

    scene corredor

    "NO DIA SEGUINTE NA ESCOLA..."

    show igor
    with dissolve

    i "Bom dia Elli, chegou mais cedo hoje?"

    hide igor

    show elli

    e "Sim Igor e foi justamente para falar com você!"

    hide elli

    show igor

    i "Comigo?"
    i "E qual é a boa?"

    hide igor

    show elli

    e "Soube que você e a Stella começaram a namorar né?"

    hide elli

    "Igor fica surpreso com o interrogamento de Elli."

    show igor

    i "Ah... ainda iriamos esperar o momento certo para falarmos sobre isso."
    i "Mas sim, começamos a namorar esse fim de semana."
    i "Como você ficou sabendo disso?"

    hide igor

    show elli

    e "Acho que antes você gostaria de ver isso!"

    hide elli

    "Elli mostra uma filmagem para Igor em seu celular."
    "Tratava-se da conversa que Igor tivera com Stella na noite anterior. Mas havia algo diferente..."
    "Elli editara o vídeo, dando a entender que Steve e Stella tinham um caso."

    show igor

    i "Como isso é possível? Só pode ser uma piada!"

    "Igor estava incrédulo com o que acabara de ver."

    i "Como você conseguiu isto?"

    hide igor

    show elli

    e "Eu tenho meus métodos...(risos)"

    "Disse Elli com uma malícia em seu sorriso."

    e "O motivo pelo qual mostrei isso a você é para desmascarar o tipo de pessoa que o steve realmente é!"
    e "Da mesma forma que ele traiu à você, ele também feriu o meu coração!"
    e "E por isso gostaria de lhe propor algo..."

    hide elli

    "Enquanto Elli influenciava Igor para algo de que poderia se arrepender, alguém que ouvia a conversa surgira das sombras..."

    show zoru
    with dissolve

    z "Opa! Não pude deixar de ouvir o que vocês estavam falando!"

    hide zoru

    show igor

    i "Quem é você?"
    i "Como surgiu do nada?"

    hide igor

    show zoru

    z "Eu apareço sempre que necessário!"

    "Na realidade, o Garoto Misterioso estava à procura do banheiro."
    "Mas por ter se perdido acabou passando próximo a Igor e Elli por coincidência."

    z "Bem, mas como eu estava dizendo..."
    z "Não acredite no que essa mentirosa está dizendo!"
    z "Eu também estava presente no encontro de Stella e Steve ontem à noite."
    z "E possuo o vídeo com a real conversa que os dois tiveram!"

    hide zoru

    "O Garoto Misterioso mostra o vídeo que tinha em mãos e que agora sim continha a realidade dos fatos."

    show igor

    i "Nossa! realmente, esse vídeo parece bem mais real."
    i "Agora que percebi que o outro vídeo tinha até a marca dágua do QuineMaster."
    i "Você me salvou de fazer uma loucura..."
    i "Onde eu estava com a cabeça?"

    hide igor

    show elli

    e "Não acredite no que ele disse!"
    e "O vídeo que te mostrei é real!"

    "Elli falava furiosamente, deixando transparecer sua frustração com a falha de seu plano."

    hide elli

    show igor

    i "Não me venha com churumelas, Elli!"
    i "Não acredito que quase caí no seu joguinho e estava prestes a cometer um grave erro contra o meu melhor amigo."
    i "Mantenha-se longe de mim!"
    i "Eu achava que você fosse alguém de boa índole, mas por detrás desse rosto fofo está o verdadeiro Diabo!"

    hide igor

    show ellitriste

    "Elli se entristesse com a fala de Igor e sai correndo dali..."
    "Mais tarde Elli sairia da escola, e nunca mais se ouviria falar dela."

    hide ellitriste

    play music "audio/romantico.mp3" fadein 2.0

    show igor
    with dissolve

    i "Nossa, muito obrigado!"
    i "Você me salvou muito hoje!"
    i "Fico te devendo essa!"

    hide igor

    show zoru

    z "Não foi nada, amigos servem pra isso!"

    hide zoru

    show igor

    i "A propósito... o que você estava fazendo ontem à noite?"
    i "E mais... Quem é você?"

    hide igor

    show zoru

    z "Ah... isso é uma longa história..."
    z "Tudo começou porque eu estava procurando aonde vendia coxinha. Acabou que do nada acabei parando naquele lanchonete...HAHAHAHA!"
    z "Mas valeu a pena, a coxinha de lá era LENDÁRIA!"
    z "E sobre a outra pergunta..."
    z "O meu nome é Goro!"
    z "Joronoa Goro. Sou novo aqui!"

    hide zoru

    "E assim Goro e Igor se conheceram e tornaram-se grandes amigos."
    "Aquele dia fora um dia especial para Igor, pois descobrira que os amigos que tinha eram os mais leais do mundo!"

    scene casaigor

    "3 dias depois, Igor chamara seu amigo Steve para jogar videogame em sua casa."

    show steve

    s "IGOR, IGOR!"
    "Steve gritava no portão de seu amigo!"

    hide steve

    show igor

    i "Olá amigo, que bom que veio."
    i "Fiz um lanche para nós comermos, vamos pra cozinha."
    i "Aliás, acabei comprando aquela Visual Novel que lançou recentemente."
    i "Salty Love... Vamos tentar zerar hoje!"

    hide igor

    scene fimigor

    "Igor e Steve passaram a tarde toda jogando videogame e aquele dia ficarIa marcado em suas vidas para sempre!"

    show igor

    i "Você jogou muito bem Steve!"
    i "Fez a escolha {b}CORRETA{/b}!"

    hide igor

return
