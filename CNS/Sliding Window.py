import random

WINDOW_SIZE = 3

def sender(frames):
    base = 0

    while base < len(frames):

        # Send all frames in window
        for i in range(base, min(base + WINDOW_SIZE, len(frames))):
            print(f"Sending: {frames[i]}")

        # Simulate ACK
        if random.random() > 0.2:
            print(f"ACK received for Frame {base}. Window slides.\n")
            base += 1
        else:
            print(f"ACK lost! Retransmitting from Frame {base}...\n")

frames = ["Data1", "Data2", "Data3", "Data4", "Data5"]
sender(frames)