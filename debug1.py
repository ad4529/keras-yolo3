def detect_video(yolo, video_path, output_path="./video1.avi"):
    import cv2
    vid = cv2.VideoCapture(0)
    vid.set(3,640)
    vid.set(4,480)
    if not vid.isOpened():
        raise IOError("Couldn't open webcam or video")
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    isOutput = True if output_path != "" else False
    out = cv2.VideoWriter(output_path, fourcc, 25.0, (640,480))
    accum_time = 0
    curr_fps = 0
    fps = "FPS: ??"
    prev_time = timer()
    while True:
        return_value, frame = vid.read()
        print('Captured frame {}'.format(frame.shape))
        image = Image.fromarray(frame)
        image = yolo.detect_image(image)
        result = np.asarray(image)
        print("Result {}".format(result.shape))
        curr_time = timer()
        exec_time = curr_time - prev_time
        prev_time = curr_time
        accum_time = accum_time + exec_time
        curr_fps = curr_fps + 1
        if accum_time > 1:
            accum_time = accum_time - 1
            fps = "FPS: " + str(curr_fps)
            curr_fps = 0
        cv2.putText(result, text=fps, org=(3, 15), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=0.50, color=(255, 0, 0), thickness=2)
        cv2.namedWindow("result", cv2.WINDOW_NORMAL)
        cv2.imshow("result", result)
        if isOutput:
            out.write(result)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    yolo.close_session()
