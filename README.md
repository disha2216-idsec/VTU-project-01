# Webcam-Based Fall Detection System

A first-semester engineering mini-project that uses a laptop webcam to detect when a person appears to fall and shows an alert on screen.

> This is a student prototype, not a medical or emergency safety system.

---

## Table of Contents

1. [Overview](#overview)
2. [Objective](#objective)
3. [Tech Stack](#tech-stack)
4. [How It Works](#how-it-works)
5. [Team and Responsibilities](#team-and-responsibilities)
6. [Project Structure](#project-structure)
7. [Getting Started](#getting-started)
8. [Testing Plan](#testing-plan)
9. [Privacy and Data Handling](#privacy-and-data-handling)
10. [Limitations](#limitations)
11. [Safety Disclaimer](#safety-disclaimer)
12. [Future Scope](#future-scope)
13. [Acknowledgements](#acknowledgements)

---

## Overview

Falls are a major risk, especially for older adults who live alone. This project explores a low-cost approach to the problem: a standard webcam, pose estimation and simple rules.

The system reads live video, finds the body landmarks of the person in view, analyses posture and movement, and displays a status of **Normal** or **Possible Fall Detected**.

## Objective

Use a webcam to detect when a person appears to fall and display an alert on the screen, using beginner-friendly tools.

| | |
|---|---|
| **Input** | Live laptop webcam feed |
| **Output** | On-screen status: `Normal` or `Possible Fall Detected` |
| **Scope** | Student prototype |

## Tech Stack

| Tool | Purpose |
|---|---|
| **Python** | Core language that ties all modules together |
| **OpenCV** | Webcam access, frame capture and live video display |
| **MediaPipe** | Pose model that finds 33 body landmarks per person |
| **Rule-based logic** | Angles, speed and frame counts decide Normal or Possible Fall |

## How It Works

```
Webcam  ->  Frames  ->  Pose landmarks  ->  Features  ->  Fall rules  ->  Status / Alert
 (M1)                       (M2)             (M3)           (M3)             (M4)
```

1. **Capture:** OpenCV reads frames from the webcam and displays the live feed.
2. **Detect:** MediaPipe finds body landmarks such as shoulders, hips and knees in each frame.
3. **Features:** The system calculates simple values from the landmarks, such as torso angle and body shape.
4. **Rules:** The values are compared with fall conditions to separate falls from normal movement.
5. **Alert:** The result is shown on screen as a status message, with an optional sound alert.

### Detection signals

A person lying down is not necessarily falling, so the system combines several signals instead of relying on one:

- **Body orientation:** torso angle along the shoulder-to-hip line.
- **Body shape:** width of the detected pose compared with its height.
- **Sudden movement:** a fast drop of the hips or shoulders between frames.
- **Persistence:** the condition must hold for several frames before an alert is raised.

An alert is raised only when several signals agree. Exact thresholds are tuned during testing.

## Team and Responsibilities

| Member | Module | Deliverable |
|---|---|---|
| 1 | Webcam and video processing | Working live webcam window |
| 2 | Human pose detection | Live skeleton overlay on the video |
| 3 | Fall detection logic | Function that flags a possible fall from pose data |
| 4 | Alerts, testing and documentation | Alert interface, test records and report |

### Task details

**Member 1: Webcam and video processing**
- Set up Python and OpenCV.
- Access the laptop webcam and display the live feed.
- Handle camera errors and close the application cleanly.

**Member 2: Human pose detection**
- Install and configure MediaPipe.
- Detect shoulders, hips and knees, and draw the pose over the video.
- Test pose detection while standing, sitting and lying down.

**Member 3: Fall detection logic**
- Study how body posture changes during a fall.
- Calculate torso angle and body orientation.
- Write and test rules that separate possible falls from normal movement.

**Member 4: Alerts, testing and documentation**
- Display `Normal` and `Possible Fall Detected` status messages.
- Add an on-screen warning or sound alert.
- Record test cases and results, and prepare the report, diagram and slides.

## Project Structure

Only `webcam_feed.py` exists so far. The other file names below are suggestions, so rename them to match your own files.

```
fall-detection/
├── webcam_feed.py       # Member 1: webcam capture and live feed
├── pose_detection.py    # Member 2: MediaPipe landmarks (planned)
├── fall_logic.py        # Member 3: fall rules (planned)
├── alerts.py            # Member 4: status and alert display (planned)
├── main.py              # Integration of all modules (planned)
├── docs/                # Report, diagram and slides
└── README.md
```

## Getting Started

### Prerequisites

- A laptop or PC with a working webcam
- A recent version of Python 3 that MediaPipe supports

### Installation

```bash
pip install opencv-python mediapipe
```

### Run the webcam module

```bash
python webcam_feed.py
```

A window titled **Live Webcam Feed** opens with a mirrored view of the camera.

| Key | Action |
|---|---|
| `q` | Quit and release the camera |

### Troubleshooting

| Problem | What to try |
|---|---|
| "Camera not found or already in use" | Close other apps using the camera and check the connection |
| Black or frozen window | Re-run the program; try camera index `1` if you have more than one camera |
| "Could not read from the camera" | Check camera permissions in your operating system settings |

## Testing Plan

Test only with safe, controlled movements. Use a mat for any controlled drop.

| Test case | How to test | Expected result |
|---|---|---|
| Standing normally | Stand in front of the webcam | Normal |
| Sitting on a chair | Sit down and shift position | Normal |
| Lying down slowly | Lie on a mat at a slow pace | Normal |
| Bending to pick up | Bend, then stand back up | Normal |
| Sudden drop to a mat | Controlled drop, stays down | Possible Fall Detected |

Record the actual results for each case in `docs/`.

## Privacy and Data Handling

The system does **not store any video**. Each frame is processed live in memory, checked, and then discarded. Nothing is saved to disk, which protects privacy and keeps the prototype lightweight.

## Limitations

- Lying down is not always a fall, so false alarms are possible.
- Lighting and camera angle affect accuracy.
- A partly hidden body can break pose detection.
- Designed for one person and one laptop webcam.

## Safety Disclaimer

This is a student prototype. It must **not** be relied on as an emergency or medical safety system.

## Future Scope

- A mobile application using the phone camera with the same approach.
- Saving a short clip or timestamp only when a possible fall is detected, instead of recording everything.
- Sending notifications to a caregiver.
- Support for multiple people and different camera angles.
- Tuning thresholds with more test data.

## Acknowledgements

- [OpenCV](https://opencv.org/) for video capture and display.
- [MediaPipe](https://developers.google.com/mediapipe) for pose estimation.
