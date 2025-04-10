import numpy as np
import pandas as pd

# Step 1: Student names
students = ['Ali', 'Ben', 'Chloe', 'Dina', 'Eshan', 'Farah']

# Step 2: Generate random attendance (1 = present, 0 = absent) for 5 days
attendance_data = np.random.randint(0, 2, size=(6, 5))

# Step 3: Create DataFrame with days as column names
df = pd.DataFrame(attendance_data, columns=['Mon', 'Tue', 'Wed', 'Thu', 'Fri'])

# Step 4: Add names to the DataFrame
df.insert(0, 'Name', students)

# Step 5: Calculate total days present
df['Total'] = df[['Mon', 'Tue', 'Wed', 'Thu', 'Fri']].sum(axis=1)

# Step 6: Calculate attendance percentage
df['Percentage'] = (df['Total'] / 5) * 100

# Step 7: Filter students with less than 60% attendance
low_attendance = df[df['Percentage'] < 60]

# Output all
print("📋 Full Attendance Sheet:\n", df)
print("\n❌ Students Below 60% Attendance:\n", low_attendance)
