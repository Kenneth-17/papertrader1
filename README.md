# Diegetic Gaze Control

<p align="center">
  <img src="./doc/images/DiegeticGazeControlLogo.png" alt="Diegetic Gaze Control Logo" width="400">
</p>

<a href="https://www.youtube.com/watch?v=hrXuNYLDFds&feature=youtu.be">
  <img src="https://img.shields.io/badge/youtube-d95652.svg?style=flat-square&logo=youtube" alt="youtube" style="height: 20px;">
</a>

[![Docker Image Version (latest semver)](https://img.shields.io/docker/v/enunezs/diegetic_gaze_control/1.0?logo=docker)](https://hub.docker.com/repository/docker/enunezs/diegetic_gaze_control/general)

---

## Introduction

Diegetic Gaze Control is an innovative system designed to enable intuitive interaction with printed paper interfaces, physical environments, and robots using only your eye-gaze. This project aims to empower individuals, particularly those with disabilities, by providing a natural and seamless way to control assistive devices without the constraints of traditional screens or complex hardware.

At the core of Diegetic Gaze Control is the use of gaze-tracking glasses such as Pupil Neon Glasses or Tobii Glasses Pro 2. These glasses capture the user’s eye movements and translate them into control signals for interacting with printed interfaces or everyday objects. The system utilizes ArUco markers for precise detection and interaction, ensuring that users can effortlessly engage with their surroundings.

This project leverages several powerful technologies, including ROS2 for robotic control, Docker for easy deployment, and OpenCV for image processing. By integrating these tools, Diegetic Gaze Control provides a robust and flexible platform for research and practical applications in assistive technology.

### Key Features

- **Intuitive Interaction**: Control interfaces and objects with eye-gaze, maintaining a natural and comfortable user experience.
- **Versatile Hardware**: Compatible with Pupil Neon Glasses, Tobii Glasses Pro 2, or a standard USB webcam.
- **Flexible Interfaces**: Use printed paper interfaces that are easy to create, customize, and replace.
- **Safe and Practical**: Keeps the user’s gaze on the task, enhancing safety and ease of use without causing VR sickness.
- **Robust Technology Stack**: Built on ROS2, Docker, and OpenCV for reliability and ease of deployment.

Diegetic Gaze Control is ideal for researchers, developers, and practitioners in the fields of assistive technology, human-computer interaction, and robotics. It provides a foundation for developing new applications that leverage eye-gaze for control and interaction, opening up new possibilities for empowering users and enhancing accessibility.

# Table of Contents

- [Introduction](#introduction)
- [Why?](#why)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
  - [Cloning](#cloning)
  - [Setting Up the Environment](#setting-up-the-environment)
- [Running](#running)
  - [Docker Setup](#docker-setup)
  - [Configuration](#configuration)
  - [Starting the Application](#starting-the-application)
- [How Does It Work?](#how-does-it-work)
  - [Code Structure](#code-structure)
  - [Launch Files](#launch-files)
- [Contribution Guidelines](#contribution-guidelines)

# Why?

<p align="center">
Our goal is to empower people with disabilities to interact with the world without constraining them to a screen.
</p>

## Motivation

The primary motivation behind Diegetic Gaze Control is to enhance the accessibility and usability of assistive technologies. Traditional control methods often rely on touchscreens, keyboards, or mouse devices, which can be cumbersome or even unusable for individuals with physical disabilities. By leveraging eye-gaze as a natural and intuitive input method, we aim to provide a more inclusive solution that enables users to interact with their environment seamlessly and independently.

## Key Advantages

### Intuitive and Natural Interaction
Diegetic Gaze Control keeps the user's gaze focused on the task at hand. Unlike screen-based interfaces, where attention is divided between the screen and the environment, our system allows for direct interaction with physical objects and printed interfaces. This approach not only enhances user experience but also reduces cognitive load and improves task efficiency.

### Versatility and Flexibility
- **Hardware Compatibility**: The system supports a range of gaze-tracking devices, including Pupil Neon Glasses, Tobii Glasses Pro 2, and even standard USB webcams. This flexibility ensures that users can choose the hardware that best fits their needs and budget.
- **Printed Interfaces**: Using printed paper interfaces provides a cost-effective and easily customizable solution. Users can create and modify their own control interfaces without the need for expensive equipment or software.

### Safety and Comfort
By keeping the user’s gaze on the robot or task, Diegetic Gaze Control enhances safety and usability. This is particularly beneficial in environments where situational awareness is crucial. Additionally, the system avoids the discomfort and potential VR sickness associated with wearing large VR headsets.

### Open and Extensible
Built on robust and widely-used technologies like ROS2, Docker, and OpenCV, Diegetic Gaze Control is designed to be easily extensible. Researchers and developers can build upon this platform to create new applications and functionalities, fostering innovation in the field of assistive technology.

## Real-World Applications

Diegetic Gaze Control has numerous potential applications:
- **Assistive Devices**: Empower individuals with disabilities to control various assistive devices, enhancing their independence and quality of life.
- **Human-Robot Interaction**: Facilitate more natural and efficient interactions between humans and robots in both industrial and domestic settings.
- **Education and Training**: Provide accessible learning tools and interfaces for students and trainees with physical limitations.

In summary, Diegetic Gaze Control represents a significant step forward in making assistive technology more intuitive, versatile, and accessible. By leveraging eye-gaze as a primary input method, we aim to bridge the gap between users and their environments, empowering them to interact more freely and effectively.

- [FAQs/Troubleshooting](#faqs--troubleshooting)
- [Citing This Work](#citing-this-work)
