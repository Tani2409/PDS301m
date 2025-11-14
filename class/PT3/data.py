import os
import pandas as pd

os.chdir(r"C:\Users\ADMIN\Documents\GitHub\PDS301m\archive")
df = pd.read_csv("StudentsPerformance.csv")
print("\n#1. How many rows and columns the dataset has.")
print("Dataset dimensions (rows, columns):", df.shape)

print("\n#2. Display unique values in gender and race/ethnicity")
columns = ['gender', 'race/ethnicity'] 
for col_name in columns:
    if col_name in df.columns:
        unique_vals = df[col_name].unique()
        
        print(f"\nColumn: '{col_name}'")
        print(f"Unique values: ")
        print(unique_vals)
    else:
        print(f"\nCảnh báo: Không tìm thấy cột '{col_name}' trong DataFrame.")

print("\n#3. Find which column has the highest average value")
avg_scores = df[['math score', 'reading score', 'writing score']].mean()
print("Max Average Scores of 3 subject is: ")
print(avg_scores.max())

print("\n#4. Check for missing values.")
print(df.isnull().sum())

print("\n#5. Replace any missing test scores with the mean.")
columns = ['math score', 'reading score', 'writing score']
    
for col in columns:
    if col in df.columns:
        col_mean = avg_scores[col]
        df[col] = df[col].fillna(col_mean)
        
        print(f"Đã cập nhật cột '{col}', các giá trị null (nếu có) đã được thay bằng: {col_mean:.2f}")
    else:
        print(f"Cảnh báo: Không tìm thấy cột '{col}' để điền giá trị null.")

print("\nKiểm tra lại giá trị null sau khi điền:")
print(df.isnull().sum())

print("\n#6. Rename columns to simpler names (e.g., math instead of math score)")
new_column_names = {
        'race/ethnicity': 'ethnic_group'
    }
df.rename(columns=new_column_names, inplace=True)
print("Cột đã được đổi tên: ")
print(df.columns)

print("\n#7. Find average scores grouped by gender.")
gender_grouped_scores = df.groupby('gender')[['math score', 'reading score', 'writing score']].mean()
print(gender_grouped_scores)

print("\n#8. Find which race/ethnicity group performs best in reading.")
ethnic_reading_avg = df.groupby('ethnic_group')['reading score'].mean()      
ethnic_reading_avg_sorted = ethnic_reading_avg.sort_values(ascending=False)

print("Điểm đọc trung bình theo từng nhóm (đã sắp xếp):")
print(ethnic_reading_avg_sorted)

best_group_name = ethnic_reading_avg.idxmax()
best_group_score = ethnic_reading_avg.max()
print(f"\nNhóm có thành tích đọc tốt nhất là: '{best_group_name}' với điểm trung bình là {best_group_score:.2f}")

print("\n#9. Find the student(s) with the highest total score")
df['total score'] = df['math score'] + df['reading score'] + df['writing score']
top_1_students = df.nlargest(1, 'total score')
print("học sinh có tổng điểm cao nhất:")
print(top_1_students)

print("\n#10")
df['total score'] = df['math score'] + df['reading score'] + df['writing score']
df['average score'] = df['total score'] / 3
print("Đã thêm cột 'total score' và 'average score'.")
print(df.head(2))

print("\n11")
passing_score = 50
df['passed_math'] = df['math score'] >= passing_score
print(df.head(2))

print("\n12")
passed_all_mask = (df['math score'] >= passing_score) & \
                    (df['reading score'] >= passing_score) & \
                    (df['writing score'] >= passing_score)
num_passed_all = passed_all_mask.sum()
print(f"Số học sinh vượt qua cả 3 môn là: {num_passed_all}")
passing_students_df = df[passed_all_mask]
print("\nThông tin 5 học sinh đầu tiên đã vượt qua cả 3 môn:")
print(passing_students_df.head(5).round(2))

print("\n13")
df.to_csv("StudentsPerformanceV2.csv", index=False)
