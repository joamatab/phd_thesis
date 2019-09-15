import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec


plt.figure(0)


gs = GridSpec(3, 3,
        width_ratios=[1,1,1],
        height_ratios=[1,0.5,1]
        )

ax1 = plt.subplot(gs[0, :])
ax2 = plt.subplot(gs[1,0])
ax3 = plt.subplot(gs[1,1])
ax4 = plt.subplot(gs[1,2])
ax5 = plt.subplot(gs[2,0])
ax6 = plt.subplot(gs[2,1])
ax7 = plt.subplot(gs[2,2])


#ax_main = plt.subplot2grid((3,3), (0,0), colspan=3)
#ax_table1 = plt.subplot2grid((3,3), (1,0))
#ax_table2 = plt.subplot2grid((3,3), (1,1))
#ax_table3 = plt.subplot2grid((3,3), (1,2))
#ax_peak1 = plt.subplot2grid((3,3), (2,0))
#ax_peak2 = plt.subplot2grid((3,3), (2,1))
#ax_peak3 = plt.subplot2grid((3,3), (2,2))


plt.show()


