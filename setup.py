
DISTNAME = "new-pkg"
DESCRIPTION = "new-pkg test project for setuptools"

VERSION = robo_clocks.__version__  # gets from init??

# import a restricted version of roboclocks
# does not need the compiled code??

#mk what this to work after pip install
import new_pkg as newpkg

