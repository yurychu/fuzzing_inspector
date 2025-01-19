import subprocess as sp

# Debug funcs:
def _log(input):
    pass

if __name__ == "__main__": _log = print


# Public

# Handle 'strace' utility commands
class StraceTool:
    """
    Sequrity Danger Zone!
    Make attachable by 'UID == UID process (non root):'
        # sysctl kernel.yama.ptrace_scope=0
    """

    def __init__(self) -> None:
        self.alias = "strace"

    def strace_exists(self) -> bool:
        try:
            ret = sp.run([self.alias, "--version"],
                        capture_output=True, text=True)
            _log(ret)
            return True if ret.returncode == 0 else False
        except FileNotFoundError as ex:
            _log(ex)
            return False


    def intercept(self, pid=None) -> object:
        ret = None

        if pid:
            command = [self.alias] + \
                    f"-e write=1 -p {int(pid)} \
                        -e trace=write \
                        -s 1024 \
                        -qqq".split()
            _log(command)

            compl_proc = sp.run(command)
            # TODO: work in progress

        return ret


def main():
    pid = 15184
    st = StraceTool()
    if st.strace_exists():
        _log("Ok, let's intercept")
        handler = st.intercept(pid=pid)
    else:
        _log("strace check fail")


if __name__ == "__main__": main()
