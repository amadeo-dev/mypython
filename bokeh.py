
from mediapipe import solutions
from mediapipe.framework.formats import landmark_pb2
import numpy as np
import cv2  
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision


def draw_landmarks_on_image(rgb_image, detection_result):
  pose_landmarks_list = detection_result.pose_landmarks
  annotated_image = np.copy(rgb_image)

  # Loop through the detected poses to visualize.
  for idx in range(len(pose_landmarks_list)):
    pose_landmarks = pose_landmarks_list[idx]

    # Draw the pose landmarks.
    pose_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
    pose_landmarks_proto.landmark.extend([
      landmark_pb2.NormalizedLandmark(x=landmark.x, y=landmark.y, z=landmark.z) for landmark in pose_landmarks
    ])
    solutions.drawing_utils.draw_landmarks(
      annotated_image,
      pose_landmarks_proto,
      solutions.pose.POSE_CONNECTIONS,
      solutions.drawing_styles.get_default_pose_landmarks_style())
  return annotated_image
 
model_path = "pose_landmarker_heavy.task"
file = "girl.jpg"

def init():
# STEP 2: Create an PoseLandmarker object.
  base_options = python.BaseOptions(model_asset_path=model_path)
  options = vision.PoseLandmarkerOptions(
    base_options=base_options,
    output_segmentation_masks=True)
  detector = vision.PoseLandmarker.create_from_options(options)
  return detector
   

def bokeh(detect, image):
       # STEP 3: Load the input image.
    img = mp.Image.create_from_file(image)
    # STEP 4: Detect pose landmarks from the input image.
    detection_result = detector.detect(img)
    
    # STEP 5: Process the detection result. In this case, visualize it.
    annotated_img = draw_landmarks_on_image(img.numpy_view(), detection_result)
    cv2.imshow("test2",cv2.cvtColor(annotated_img, cv2.COLOR_RGB2BGR))
    
    segmentation_mask = detection_result.segmentation_masks[0].numpy_view()
    visualized_mask = np.repeat(segmentation_mask[:, :, np.newaxis], 3, axis=2) * 255

init()
bokeh(file)

