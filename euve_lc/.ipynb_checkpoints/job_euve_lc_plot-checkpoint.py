import numpy as np
import scipy.signal
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

#plots small version of the EUVE lightcurve 

plt.figure('gd394_euve',figsize=(7,5))
#plt.subplots_adjust(top=0.99, right=0.99, left=0.07, bottom=0.08, wspace=0.1, hspace=0.09)


lcs = ['ds_5760_ltc_obs2.ascii', 'gd394_sca_lex_nov96', 'gd394_scb_alc_nov96']
dates = ['1995 October\n65--180\,\AA','1996 November\n58--174\,\AA','1996 November\n156--234\,\AA']

t, c, e = np.loadtxt(lcs[0], unpack=True)
plt.errorbar((t-t[0])/86400, c, yerr=e, marker='o', ls='none', label = 'EUVE 1995 October')
#plt.xlabel('Time (d)', size=20)
plt.ylabel('Counts (s$^{-1}$)', size=20)
#plt.annotate(dates[0], (0.85, 0.85), xycoords='axes fraction', size=15)
plt.ylim(2.05,3.15)
plt.xlim(-0.2, 4.5)
plt.legend(fontsize=20)
plt.xlabel('Time (d)', size=20)
plt.tight_layout()
plt.savefig('job_euve.png', dpi=150)
plt.show()
