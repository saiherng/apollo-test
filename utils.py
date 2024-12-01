class Colors:
    RESET = "\033[0m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"

def printFail():
    print(f"{Colors.RED}FAIL{Colors.RESET}")

def printPass():
    print(f"{Colors.GREEN}PASS{Colors.RESET}")
