def br(qty):
    """
    this function will produce a line break
    """
    return print("-"*qty)

def ctitle(title_name):
    """
    Prints a formatted comment title with underline
    """
    print(f"# {title_name}")
    print("#" + "-" * 60)