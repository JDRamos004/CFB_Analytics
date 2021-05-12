import matplotlib
import matplotlib.pyplot as plt
import numpy as np

plt.plot(range(100))
plt.show()

matplotlib.use('Qt5Agg')
# This should be done before `import matplotlib.pyplot`
# 'Qt4Agg' for PyQt4 or PySide, 'Qt5Agg' for PyQt5

t = np.linspace(0, 20, 500)
plt.plot(t, np.sin(t))
plt.show()
