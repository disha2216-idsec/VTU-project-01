import cv2


def open_camera(index=0):
    cap = cv2.VideoCapture(index)
    if not cap.isOpened():
        raise RuntimeError("Camera not found or already in use.")
    return cap


def main():
    try:
        cap = open_camera()
    except RuntimeError as error:
        print(error)
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Could not read from the camera.")
            break

        frame = cv2.flip(frame, 1)
        cv2.imshow("Live Webcam Feed", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
