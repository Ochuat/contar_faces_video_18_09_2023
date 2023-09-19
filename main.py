import cv2

# Inicializar o detector de rosto
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Capturar o vídeo
#"C:\\003_Fresenius\\Curtes IA\\Av Paulista ‐ Feito com o Clipchamp.mp4")  # Substitua "seu_video.mp4" pelo caminho para o seu arquivo de vídeo
#'/content/drive/MyDrive/Engenharia de Software/Machine Learning_Luiz/2023_09_18_Visao computacional_contador de pessoas/Av Paulista ‐ Feito com o Clipchamp.mp4')
video_capture = cv2.VideoCapture("C:\\003_Fresenius\\Curtes IA\\Sala de aula_720.mp4")

while True:
    # Capturar frame a frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Contar o número de rostos
    face_count = len(faces)

    # Desenhar um retângulo ao redor das faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Exibir o número de rostos no frame
    cv2.putText(frame, f'Faces: {face_count}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    # Exibir o frame resultante
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Quando tudo estiver feito, liberar a captura
video_capture.release()
cv2.destroyAllWindows()