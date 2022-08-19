import matplotlib.pyplot as plt
import os
path = os.path.join(os.path.dirname(__file__), 'research_default.mplstyle')
plt.style.use(path)

# Alternatively, import via an environment variable
# mtlb = os.getenv('MYPYTHON')
# plt.style.use(os.path.join(mtlb, 'research_default.mplstyle'))

fig, ax = plt.subplots(figsize=(4,1))
ax.plot([1, 2, 3], label='test')
ax.set_ylabel("y-label")
ax.set_xlabel('x-label')

ax.legend()
plt.show()