import miniaudio
from time import sleep


if __name__ == "__main__":
    def pass_through():
        data = yield b""
        while True:
            print(".", end="", flush=True)
            data = yield data

    def on_stop():
        print("Stopped!")
        print("")

    duplex = miniaudio.DuplexStream(buffersize_msec=0, sample_rate=48000)
    generator = pass_through()
    next(generator)
    print("Starting duplex stream. Press Ctrl + C to exit.")
    duplex.start(generator, on_stop)

    interrupt = False
    while duplex.running and not interrupt:
        try:
            sleep(1)
        except KeyboardInterrupt:
            interrupt = True
    duplex.stop()
