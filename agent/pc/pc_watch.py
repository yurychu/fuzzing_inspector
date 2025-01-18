import subprocess as sp

from pc_pointer import ProcessPointer


def start_process(command: str) -> ProcessPointer:
    print(command)
    sp.run(command)
    return ProcessPointer()


if __name__ == "__main__":
    start_process("./runner")
