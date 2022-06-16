import pandas as pd
import os

path = os.path.join('trainer', 'all_data', 'ko_train_filtered')
df = pd.DataFrame({'filename': [],
                   'words': []})
imgs = os.listdir(path)
i = 0
for img in imgs:
    filename, ext = os.path.splitext(img)
    if ext == '.jpg':
        fname = str(i) + ext
        df = df.append({'filename': fname, 'words': filename}, ignore_index=True)
        i = i + 1

df.to_csv(os.path.join('trainer', 'all_data', 'ko_val', 'labels.csv'), index=False)