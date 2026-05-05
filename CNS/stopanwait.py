import random

def receiver(frame):
    if random.random() < 0.2:  # 20% chance of loss
        print("Frame lost!")
        return -1

    print(f"Frame {frame} received.")
    return frame

def sender(frames):
    for i in range(len(frames)):
        while True:
            print(f"Sending: {frames[i]}")
            ack = receiver(i)

            if ack == i:
                print("ACK received. Moving to next frame.\n")
                break
            else:
                print("No ACK. Retransmitting...\n")

frames = ["Data1", "Data2", "Data3"]
sender(frames)