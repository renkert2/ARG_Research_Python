#%%
import os
import re
import datetime

WEEKLY_REPORTS = os.getenv("WEEKLY_REPORTS")
DATE_FORMAT = "%m%d%Y"

# Get All Weekly Report Directories

def get_directories(directory=WEEKLY_REPORTS, date_format=DATE_FORMAT):
    def dir_filter(name):
        d = os.path.join(directory, name)
        return os.path.isdir(d)

    dirs = list(filter(dir_filter, os.listdir(directory)))

    today = datetime.date.today()
    today_str = today.strftime(date_format)
    patt = re.compile(r"\d{" + str(len(today_str)) + "}")

    date_dirs = []
    for d in dirs:
        date_str = patt.findall(d)
        if date_str and len(date_str) == 1:
            date_str = date_str[0]
            date = datetime.datetime.strptime(date_str, date_format)
            d_full = os.path.join(directory, d)
            date_dirs.append((date, d, d_full))
    
    date_dirs.sort(key=lambda x: x[0])
    
    # Get most recent date
    latest = date_dirs[-1]
    latest_dir = latest[1]

    return latest_dir, date_dirs

LATEST_WEEKLY_REPORT = get_directories()[0]

def find_dir(search_str):
    dir_dates = get_directories()[1]
    for e in dir_dates:
        name_str = e[1]
        if search_str.lower() in name_str.lower():
            return e
        


if __name__=="__main__":
    dir,dir_dates = get_directories()
# %%
