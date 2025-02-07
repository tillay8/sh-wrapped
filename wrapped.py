from modules import *

setheadercolor("cyan")
clear()
printtotal()
print_stats("Top 10 used commands", Counter(first_words).most_common(10), "magenta", "green", "used")
print_stats("Top 10 misspelled commands", Counter(misspelled).most_common(10), "red", "green", "run")
mostargs("git", 5, "yellow")
mostargs("cd", 5, "red")
mostargs("rm", 12, "green")
sudopercent("red")
firstcommand("green", "magenta")
byweekday("magenta", "blue")
hourly("green", "magenta")
