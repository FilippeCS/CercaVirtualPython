# CercaVirtualPython

Em resumo, este código detecta objetos em movimento em um vídeo, desenha uma cerca virtual e identifica se esses objetos cruzam a cerca ou não, marcando-os com retângulos vermelhos ou verdes, respectivamente. É uma aplicação básica de detecção de movimento usando OpenCV.

Primeiro, é definido o nome do arquivo de vídeo que você deseja processar, no exemplo é 'pessoas.mp4'. O código cria um objeto cap para carregar esse vídeo.

Em seguida, é criado um objeto fgbg usando cv2.createBackgroundSubtractorMOG2(). Esse objeto é usado para subtrair o fundo do vídeo e detectar áreas em movimento.

O código define a posição da cerca virtual como uma linha horizontal, que é colocada na metade do quadro do vídeo. Você pode ajustar essa posição conforme necessário.

Entra em um loop infinito que continuará até que o vídeo termine ou a tecla 'q' seja pressionada.

Dentro do loop, o código lê o próximo quadro do vídeo usando cap.read().

Ele aplica a subtração de fundo no quadro atual, o que significa que ele tenta isolar as áreas em movimento no quadro.

Em seguida, é aplicado um limiar para destacar as áreas de movimento no quadro.

O código encontra os contornos das áreas de movimento. Um contorno é basicamente a forma do objeto em movimento.

Ele desenha a cerca virtual como uma linha horizontal vermelha no quadro.

O código passa por todos os contornos encontrados e calcula a área de cada um. Se a área do contorno for maior que 500 (ajustável), ele considera que é um objeto em movimento.

Dependendo se o objeto em movimento cruzar a cerca virtual ou não (linha horizontal), ele desenha um retângulo vermelho ao redor do objeto se cruzar a linha e um retângulo verde se não cruzar.

O quadro resultante com os retângulos é exibido em uma janela com o título "Video".

O loop continuará até que o vídeo termine ou até que a tecla 'q' seja pressionada.

Após sair do loop, o código libera o vídeo e fecha a janela.
