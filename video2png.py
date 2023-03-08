import cv2
import os

path_videos = '/Users/Oseas/Documents/nestle-safety/noite/'
videos = os.listdir(path_videos)
for video in videos:
        # verificar se o arquivo é um vídeo no formato avi
        if video.endswith(".avi"):
            video_folder = os.path.join(path_videos, os.path.splitext(video)[0])
            os.makedirs(video_folder, exist_ok=True)
            cap = cv2.VideoCapture(os.path.join(path_videos, video))
            
            #percorrer cada quadro do vídeo
            frame_count = 0
            #contagem em segundos
            count = 0
            while True:
                cap.set(cv2.CAP_PROP_POS_MSEC,(count*1000)) 
                ret, frame = cap.read()
                if not ret:
                    break
                #salvar imagem
                frame_path = os.path.join(video_folder, "frame"+str(frame_count)+".png")
                cv2.imwrite(frame_path, frame)
                # atualizar os contadores de quadros e segundos
                frame_count += 1
                count = count + 1
                # liberar o objeto de captura de vídeo
            cap.release()
print("Extração de quadros concluída.")