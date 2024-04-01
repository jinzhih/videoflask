import cv2
import numpy as np
import os
from datetime import datetime

def video_gen(id,act_topic,dialogues):
    
    # Directory to save the video
    output_dir = './content'

    # Video properties
    frame_width = 1920
    frame_height = 1080
    fps = 30

    # Texts to display
    texts = [act_topic]
    for dialogue in dialogues:
        str_list = [dialogue["Character"],": ", dialogue["Line"]]
        con_dialogue = "".join(str_list)
        #texts = np.concatenate(texts,dialogue.)
        texts.append(con_dialogue)  # Add your texts here

    # Font properties
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_thickness = 2
    font_color = (255, 255, 255)  # White color

    # Create a VideoWriter object
    current_timestamp = datetime.now().timestamp()
    video_file_name = f'video_{current_timestamp}_{id}.mp4'
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(os.path.join(output_dir, video_file_name), fourcc, fps, (frame_width, frame_height))

    # Generate frames with text
    for text in texts:
        # Create a black background
        # Generate a blue background frame
        frame = np.zeros((frame_height, frame_width, 3), dtype=np.uint8)
        frame[ :, :, 2] = np.ones([frame_height, frame_width])*25
        frame[ :, :, 1] = np.ones([frame_height, frame_width])*25
        frame[ :, :, 0] = np.ones([frame_height,frame_width])*112 

        # Get text size and position
        text_size = cv2.getTextSize(text, font, font_scale, font_thickness)[0]
        segments = [text[i:i+100] for i in range(0, len(text), 100)]
        #text_x = int((frame_width - text_size[0]))
        #text_y = int((frame_height + text_size[1]))
        text_x = 150
        text_y = 200
        for segment in segments:
            cv2.putText(frame, segment, (text_x,text_y),font, font_scale, font_color, font_thickness, cv2.LINE_AA)
            text_y += 30

        # Put text on the frame
        #cv2.putText(frame, text, (text_x, text_y), font, font_scale, font_color, font_thickness, cv2.LINE_AA)

        # Write frame to video
        for n in range(150):
          video.write(frame)
      

    # Release VideoWriter object
    video.release()
    return video_file_name
