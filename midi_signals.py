import mido

def print_midi_messages(port_name):
    with mido.open_input(port_name) as port:
        print(f"Listening to port: {port_name}")
        print("Press Ctrl+C to exit")

        try:
            for msg in port:
                print(f"Received message: {msg}")
        except KeyboardInterrupt:
            print("\nInterrupted by user.")

if __name__ == "__main__":
    midi_port_name = '2- A-PRO 1 1'

    try:
        print_midi_messages(midi_port_name)
    except KeyboardInterrupt:
        pass
