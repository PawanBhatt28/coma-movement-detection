
# Coma Patient Facial Movement Detection

This project addresses a critical need in healthcare, focusing on the often overlooked aspect of continuous monitoring for patients in comatose states. Comatose patients require meticulous observation as even subtle changes in their condition can have significant implications for their care and recovery.

## Problem statement

The care and recovery of comatose patients are heavily reliant on consistent and accurate monitoring. However, traditional monitoring techniques often fall short, missing important cues that could signal changes in the patient's condition. This project aims to bridge this gap by providing a reliable and comprehensive monitoring solution.
# Solution
Our solution utilizes the "Mediapipe" framework for computer vision developed by Google, to address the unique challenges of monitoring comatose patients. By harnessing the power of Mediapipe, we are able to track and analyze facial movements with unparalleled accuracy and precision.

## Monitoring
![alt text](https://github.com/PawanBhatt28/coma-movement-detection/blob/master/temp/eye_blink.png)
![alt text](https://github.com/PawanBhatt28/coma-movement-detection/blob/master/temp/lip_ration.png)
![alt text](https://github.com/PawanBhatt28/coma-movement-detection/blob/master/temp/head_vertical_changes.png)

## Facial Movement Tracking with Mediapipe
The Mediapipe framework is indispensable in the context of monitoring a comatose patient's facial movements. It provides robust capabilities for detecting and supplying facial landmarks, including 3D coordinates, enabling us to monitor even the most subtle changes in a patient's face.

## Landmark Categorization and Feature Extraction
To effectively monitor facial movements, we have developed techniques to categorize landmarks into groups such as eyes, lips, contour, and others. This allows us to extract specific facial features and analyze them in real-time. For instance, the Eye Aspect Ratio derived from Mediapipe landmarks can accurately identify changes in eye states, indicating whether a patient's eyes are open or closed.

## 3D Head Movement Tracking
Tracking head movement in a 3D perspective presents unique challenges. Our solution addresses this complexity by employing Mediapipe to track two carefully selected landmarks and determine the head's rotation and position. We have developed algorithms that evaluate these landmarks to identify any significant head movements, providing valuable insights into the patient's condition.

## Conclusion
In conclusion, our digital solution leverages the robust capabilities of the Mediapipe framework to extract and analyze facial landmarks in real-time, enabling continuous monitoring of facial expressions, eye movements, and head rotations in comatose patients. By detecting even minute changes in the patient's condition, our solution has the potential to assist healthcare professionals in making timely assessments and implementing appropriate treatments.

![alt text](https://github.com/PawanBhatt28/coma-movement-detection/blob/master/temp/front.png?)
![alt text](https://github.com/PawanBhatt28/coma-movement-detection/blob/master/temp/far_front.png?raw=true)
![alt text](https://github.com/PawanBhatt28/coma-movement-detection/blob/master/temp/left_side.png?raw=true)
![alt text](https://github.com/PawanBhatt28/coma-movement-detection/blob/master/temp/right_side.png?)
