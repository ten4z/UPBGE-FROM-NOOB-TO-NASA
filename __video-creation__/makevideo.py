import cv2
import os
image_folder = 'pictures'


images = ["frame" + str(i) + ".png" for i in range(175, 280)] 
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter('video-render.mp4',cv2.VideoWriter_fourcc(*'mp4v'), 25, (width,height))


for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))


cv2.destroyAllWindows()
video.release()