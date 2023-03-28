from pyspark.sql import SparkSession
from pyspark import SparkContext
import cv2
import os
from pyspark import SparkConf

conf = SparkConf().set("spark.driver.bindAddress", "127.0.0.1").set("spark.driver.port", "4042")
print(conf)
def extract_frames(filename):
    # Check if file is a video
    if filename.endswith(".mp4") or filename.endswith(".avi") or filename.endswith(".mov"):
        # Create folder for extracted frames with same name as video file
        folder_name = filename.split(".")[0]
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
    #Create a SparkSession
    
    os.environ['SPARK_HOME'] = '/mnt/spark'
    print(os.environ['SPARK_HOME'])
#     spark = SparkSession.builder \
#    .master("local") \
#    .appName("MyApp") \
#    .getOrCreate()
#     print("hi")
    # try:
    #     #spark = SparkSession.builder.appName("ExtractFrames").getOrCreate()
        
    # except:
    #     pass
    SparkContext.getOrCreate().stop()
    # active_contexts = SparkContext._active_spark_context
    # print(active_contexts)

# Stop all active Spark contexts
    # for context in active_contexts:
    #      context.stop()
    spark = SparkSession.builder.appName("ExtractFrames").config(conf=conf).getOrCreate()
    
          # stop the SparkContext

    # print("Hi")
    # #Get list of video files
    video_files = [filename for filename in os.listdir(".")
                   if filename.endswith((".mp4", ".avi", ".mov"))]

    # Parallelize the processing of video files
    sc = spark.sparkContext
    video_files_rdd = sc.parallelize(video_files)
    video_files_rdd.foreach(extract_frames)
