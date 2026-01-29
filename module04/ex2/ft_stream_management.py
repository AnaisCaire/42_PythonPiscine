
import sys

def treechannels():
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")

    id = input("Input Stream active. Enter archivist ID: ")
    status = input("Input Stream active. Enter status report: ")

    sys.stdout.write(f"[ STANDARD ] Archive status from {id}: {status}.\n")
    sys.stderr.write("[ ALERT ] System diagnostic: Communication channels verified\n")
    sys.stdout.write("[ STANDARD] Data transmission complete\n")


if __name__ == "__main__":
    treechannels()