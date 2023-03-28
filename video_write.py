import os
import cv2
import multiprocessing

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
            
            # Check if frame was successfully read
            if not ret:
                break
            
            # Save frame as image file in folder
            frame_name = os.path.join(folder_name, f"frame_{frame_count:04d}.jpg")
            cv2.imwrite(frame_name, frame)
            frame_count += 1
        
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
