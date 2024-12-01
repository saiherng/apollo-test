class TestInfo:
    name = ""
    description = ""
    def __init__(self, name, description) -> None:
        self.name = name
        self.description = description

class Colors:
    RESET = "\033[0m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"

def printFail(testInfo: TestInfo):
    print(f"\n{Colors.RED}{testInfo.name} FAIL. {testInfo.description}{Colors.RESET}")
    raise Exception (f"{Colors.RED}{testInfo.name} failed.{Colors.RESET}")

def printPass(testInfo):
    print(f"\n{Colors.GREEN}{testInfo.name} PASS. {testInfo.description}{Colors.RESET}")
