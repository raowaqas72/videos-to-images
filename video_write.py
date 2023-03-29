import os
import cv2
import multiprocessing
import numpy as np

def extract_frames(filename):
    # Check if file is a video
    if filename.endswith(".mp4") or filename.endswith(".avi") or filename.endswith(".mov"):
        # Create folder for extracted frames with same name as video file
        folder_name = os.path.splitext(filename)[0]
        os.makedirs(folder_name, exist_ok=True)
        
        # Open video file
        video_capture = cv2.VideoCapture(filename)
        
        # Loop through all frames in video
        frame_count = 0
        while True:
            # Read next frame
            ret, frame = video_capture.read()
            gray1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            # Check if frame was successfully read
            if not ret:
                break
            
            # Save frame as image file in folder
            try:
                array1 = np.array(gray1)
                array2 = np.array(gray2)

                # Compute mean squared error (MSE)
                mse = np.mean((array1 - array2) ** 2)
                if mse>5:
                    frame_name = os.path.join(folder_name, f"frame_{frame_count:04d}.jpg")
                    cv2.imwrite(frame_name, frame)
            except: pass
            frame_count += 1
            img2=frame
            gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

        
        # Release video capture
        video_capture.release()

if __name__ == "__main__":
    # Get current directory
    current_dir = os.getcwd()

    # Get list of video files
    video_files = [filename for filename in os.listdir(current_dir)
                   if filename.endswith((".mp4", ".avi", ".mov"))]

    # Process video files in parallel
    with multiprocessing.Pool() as pool:
        pool.map(extract_frames, video_files)
