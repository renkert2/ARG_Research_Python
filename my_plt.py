import weekly_reports
from slugify import slugify
import matplotlib.pyplot as plt
import os
import pickle

mtlb = os.getenv('MYPYTHON')
plt.style.use(os.path.join(mtlb, 'research_default.mplstyle'))

wkly_dir = os.path.join(weekly_reports.WEEKLY_REPORTS, weekly_reports.LATEST_WEEKLY_REPORT)

def export(fig, fname = None, title = None, directory = wkly_dir, **kwargs):
    if fname:
        # Remove extension
        fname = os.path.splitext(fname)[0]

    if title:
        fig.suptitle(title)
        if not fname:
            fname = slugify(title)
    
    if not fname:
        raise Exception("File name must be specified")
    
    # Save Binary
    fname_full = os.path.join(directory, fname)
    pickle.dump(fig, open(fname_full + ".fig.pickle", 'wb'))

    # Save Image
    fig.savefig(fname_full + ".png", **kwargs)

    return fname_full