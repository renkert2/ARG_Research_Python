from .slugify import slugify
import matplotlib.pyplot as plt
import os
import pickle

plt.style.use(os.path.join(os.path.dirname(__file__), 'research_default.mplstyle'))

if "WEEKLY_REPORTS" in os.environ:
    from . import weekly_reports
    default_dir = os.path.join(weekly_reports.WEEKLY_REPORTS, weekly_reports.LATEST_WEEKLY_REPORT)
else:
    default_dir = os.getcwd()
    
def export(fig, fname = None, title = None, directory = default_dir, **kwargs):
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