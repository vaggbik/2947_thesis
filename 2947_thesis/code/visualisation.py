plt.plot(x, y, 'co')
a_scale = float(max(x))/float(100)
for i in range(0,len(x)):
    plt.arrow(x[best[i]], y[best[i]], (x[best[i+1]] - x[best[i]]), (y[best[i+1]] - y[best[i]]), head_width = a_scale, color = 'grey', length_includes_head = True)
plt.xlim(0, max(x)*1.1)
plt.ylim(0, max(y)*1.1)
plt.show()