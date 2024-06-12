# Telemanipulation of Robot Hand using Human Gesture
This project aims to telemanipulate a robot hand using human gestures, controlling the gripper over a socket server

## Required Tools
Tools and libraries are installed and accessible:
- Mediapipe :  popular framework for building machine learning pipelines to process perceptual data, such as audio and video.
- OpenCV :  a widely used library for computer vision tasks, including image and video processing.
- Ur_rtde : Python library for communicating with Universal Robots using the Real-Time Data Exchange (RTDE) interface.

## Tracking Module
Using the Mediapipe library for hand tracking, it enables the tracking of hand positions. The library provides more than 21 landmarks on the hand. The positions of these landmarks are normalized, meaning they are represented as values between 0 and 1. Therefore, when comparing these positions with images captured by a camera, it is necessary to scale or resize the image to ensure that the positions align with the resolution or level of detail of the image.

<img src="https://github.com/tanutb/Telemanipulation-of-Robot-Hand-using-Human-Gesture/blob/main/image/MediaPipe.png">

From the positions of landmarks visible in the image, they are used to detect the characteristics or gestures made by measuring the closing of fingers. The closing or opening of fingers is measured by comparing the positions of landmarks at the fingertips to the positions of landmarks at the base of each finger. For example, for the index finger, the position of the landmark at the tip, which is landmark number 8, is compared to the position of the landmark at the base of the index finger, which corresponds to landmark position 5. When the position of landmark 8 has a lower y-coordinate than the position of landmark 5, we can infer that the user is closing their index finger at that moment. This principle is applied to compare all fingers to determine the characteristics of the hand at that specific moment.

## System Scenario
![HCI](https://user-images.githubusercontent.com/72074422/200872546-035e7495-8b3f-4bb4-9f39-8182e573f793.jpg)
## Usage
### 1. Setup IP Address
Before running the server and client scripts, ensure that the IP address for communication is properly configured. This step is crucial for establishing a connection between the client (hand tracking) and the server (robot control).
### 2. Start Server for Robot Control
Run the provided Python script URSever.py to initiate the server responsible for controlling the robot hand. This script should handle incoming commands from the client and execute corresponding actions on the robot hand.
```
python URSever.py
```
### 3. Start Client for Hand Tracking 
Execute the URClient.py script to start the client application responsible for hand tracking and sending gesture data to the server for robot control. This script should utilize computer vision techniques, possibly leveraging tools like OpenCV for hand tracking.
```
python URClient.py
```

## Testing
From user observations during testing, it was found that moving forward and backward compared to controlling with finger gestures can confuse users about the direction of control. Additionally, due to the relatively delayed response of the robot arm, grasping objects becomes challenging and imprecise. Therefore, one possible solution may involve indicating the current position of the robot arm and adjusting its forward and backward movements to minimize confusion. Additionally, reducing the delay in the robot arm's response could improve the precision of grasping objects.

<img src="https://github.com/tanutb/Telemanipulation-of-Robot-Hand-using-Human-Gesture/blob/main/image/u1.png" width="500" height="300">

## Document :
https://hcilab.net/class-project/human-robotics-interface/2022/11/09/class-project-telemanipulation-of-robot-hand-using-human-gesture

## Video demo :
https://m.youtube.com/watch?v=4Dewh1Q_nFE&embeds_referring_euri=https%3A%2F%2Fhcilab.net%2F&source_ve_path=Mjg2NjY&feature=emb_logo

