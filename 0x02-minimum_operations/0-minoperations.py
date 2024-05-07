def minOperations(n: int) -> int:
    if n == 1:
        return 0  # No operations needed for n = 1

    operations = 0
    current = 1
    clipboard = ""

    while current < n:
        if n % current == 0:
            # Perform "Paste" operation
            operations += n // current
            current += clipboard.count("H")
        else:
            # Perform "Copy All" operation
            clipboard = "H" * current
            operations += 1
            current += current

    return operations if current == n else 0
