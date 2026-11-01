
import os
import shutil

source = input("Enter source folder path: ")
destination = input("Enter destination folder path: ")

# Create destination folder if it does not exist
if not os.path.exists(destination):
    os.makedirs(destination)

count = 0

# Check all files in the source folder
for file in os.listdir(source):

    if file.lower().endswith(".jpg"):
        shutil.move(
            os.path.join(source, file),
            os.path.join(destination, file)
        )

        count += 1
        print("Moved:", file)

print("\nTotal JPG files moved:", count)
print("Task completed successfully!")