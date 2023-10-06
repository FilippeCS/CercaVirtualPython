import cv2

# Carregue o arquivo de vídeo
video_filename = 'pessoas.mp4'
cap = cv2.VideoCapture(video_filename)

# Crie o objeto do subtrator de fundo
fgbg = cv2.createBackgroundSubtractorMOG2()

# Defina a posição da cerca virtual (linha horizontal) na metade do quadro (ajuste conforme necessário)
y_cerca = cap.get(cv2.CAP_PROP_FRAME_HEIGHT) // 2

while True:
    # Leia o próximo quadro
    ret, frame = cap.read()

    # Se o vídeo terminar, saia
    if not ret:
        break

    # Aplique a subtração de fundo no quadro atual
    fgmask = fgbg.apply(frame)

    # Aplique um limiar para obter as áreas de movimento
    _, thresh = cv2.threshold(fgmask, 25, 255, cv2.THRESH_BINARY)

    # Encontre os contornos das áreas de movimento
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Desenhe a cerca virtual (linha horizontal) no quadro
    cv2.line(frame, (0, int(y_cerca)), (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(y_cerca)), (0, 0, 255), 2)

    for contour in contours:
        # Calcule a área do contorno
        area = cv2.contourArea(contour)

        # Se a área for maior que um valor específico (ajuste conforme necessário)
        if area > 500:
            # Obtenha os limites do retângulo ao redor do contorno
            x, y, w, h = cv2.boundingRect(contour)

            # Verifique se o objeto em movimento cruza a cerca virtual (linha horizontal)
            if y < y_cerca:
                # Se cruzar, desenhe um retângulo vermelho ao redor do objeto
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            else:
                # Caso contrário, desenhe um retângulo verde ao redor do objeto
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Mostre o quadro resultante com os retângulos
    cv2.imshow("Video", frame)

    # Se a tecla 'q' for pressionada, saia
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libere o vídeo e feche a janela
cap.release()
cv2.destroyAllWindows()
