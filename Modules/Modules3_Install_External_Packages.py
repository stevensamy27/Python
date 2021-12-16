# ------------------------------------------
# -- Modules => Install External Packages --
# ------------------------------------------
# [1] Module vs Package
# [2] External Packages Downloaded From The Internet
# [3] You Can Install Packages With Python Package Manager PIP
# [4] PIP Install the Package and Its Dependencies
# [5] Modules List "https://docs.python.org/3/py-modindex.html"
# [6] Packages and Modules Directory "https://pypi.org/"
# [7] PIP Manual "https://pip.pypa.io/en/stable/reference/pip_install/"
# ---------------------------------------------------------------------

import termcolor
import pyfiglet

print(dir(pyfiglet))
print("#" * 50)
print(pyfiglet.figlet_format("Steven"))
print("#" * 50)
print(termcolor.colored("Stiiiv", color="green"))
print("#" * 50)
print(termcolor.colored(pyfiglet.figlet_format("Stiiiv"), color="yellow"))


########OUTPUT######

'''

##################################################
 ____  _
/ ___|| |_ _____   _____ _ __
\___ \| __/ _ \ \ / / _ \ '_ \
 ___) | ||  __/\ V /  __/ | | |
|____/ \__\___| \_/ \___|_| |_|


##################################################
Stiiiv    >>>with green color<<<
##################################################
 ____  _   _ _ _       
/ ___|| |_(_|_|_)_   __
\___ \| __| | | \ \ / /
 ___) | |_| | | |\ V /
|____/ \__|_|_|_| \_/




'''