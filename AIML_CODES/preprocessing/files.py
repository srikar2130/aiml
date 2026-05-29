import os
import cv2
import numpy as np

data = []
labels = []

dataset_path = "dataset_folder_path"   # change this

for label in range(10):
    folder = os.path.join(dataset_path, str(label))
    
    for file in os.listdir(folder):
        img_path = os.path.join(folder, file)
        
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, (28, 28))  # ensure size
        
        data.append(img.flatten())  # convert 28x28 → 784 vector
        labels.append(label)

X = np.array(data)
y = np.array(labels)

print(X.shape)  # (num_samples, 784)




import pandas as pd
import glob

# path to folder
files = glob.glob("folder_path/*.csv")

# read and combine
df = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)

print(df.shape)





import os
import pandas as pd

folder = "folder_path"

dfs = []

for file in os.listdir(folder):
    if file.endswith(".csv"):
        path = os.path.join(folder, file)
        dfs.append(pd.read_csv(path))

df = pd.concat(dfs, ignore_index=True)