import os
import glob

files = glob.glob('./hyper-test-pics/kim/*')

for i, f in enumerate(files):
    ftitle, fext = os.path.splitext(f)
<<<<<<< HEAD
    os.rename(f, './/hyper-test-pics/kim/1_kim' + '{0:d}'.format(i) + fext)
=======
    os.rename(f, './downloads/renamed/other' + '{0:d}'.format(i) + fext)
    
>>>>>>> fe666f71a469d3e634a49cc33bcdea0303a82e12
