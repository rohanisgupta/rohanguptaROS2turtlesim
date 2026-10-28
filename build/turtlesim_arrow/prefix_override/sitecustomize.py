import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/rohan/rohanguptaROS2turtlesim/install/turtlesim_arrow'
