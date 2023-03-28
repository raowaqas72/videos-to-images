import os
import cv2
import numpy as np

# Get current directory
current_dir = os.getcwd()

# Loop through all files in current directory
for filename in os.listdir(current_dir):
    # Check if file is a video
    if filename.endswith(".mp4") or filename.endswith(".avi") or filename.endswith(".mov"):
        # Create folder for extracted frames with same name as video file
        folder_name = os.path.splitext(filename)[0]
        os.makedirs(folder_name, exist_ok=True)
        
        # Open video file
        video_capture = cv2.VideoCapture(filename)
        
        # Loop through all frames in video
        frame_count = 0
        write_count=0
        while True:
            # Read next frame
            ret, frame = video_capture.read()
            gray1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            array1 = np.array(gray1)
            try:
                mse = np.mean((array1 - array2) ** 2)
                
                if mse>10:
                    write_count=write_count+1
                    print(mse)
                    print(write_count)
                    frame_name = os.path.join(folder_name, f"frame_{frame_count:04d}.jpg")
                    cv2.imwrite(frame_name, frame)
            except:
                pass

            # Check if frame was successfully read
            if not ret:
                break
            img2 = frame
            gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
            array2 = np.array(gray2)
            
            # Save frame as image file in folder
            
            frame_count += 1
        
        # Release video capture
        video_capture.release()
