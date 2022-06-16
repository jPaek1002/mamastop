import pandas as pd
import os

path = 'data/stuff'
df = pd.DataFrame({'filename': [],
                   'words': []})
imgs = os.listdir(path)
for img in imgs:
    filename, _ = os.path.splitext(img)
    df = df.append({'filename': img, 'words': filename}, ignore_index=True)

df.to_csv(os.path.join('data', 'ko_train_filtered', "labels.csv"), index=False)