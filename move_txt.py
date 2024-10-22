import os
import shutil

# 원본 폴더 경로
source_dir = r"C:/Users/han/Desktop/snack_data_original/5th_mix_data_all_rabeled_resize_x"
# 대상 폴더 경로
target_dir = r"C:/Users/han/Desktop/snack_data_original/5th_mix_data_all_rabeled_resize_x/txt"

# 대상 폴더가 없으면 생성
if not os.path.exists(target_dir):
    os.makedirs(target_dir)

# 원본 폴더의 파일 목록 순회
for filename in os.listdir(source_dir):
    # 파일의 전체 경로
    source_path = os.path.join(source_dir, filename)
    # 대상 파일 경로
    target_path = os.path.join(target_dir, filename)

    # 파일이 .txt 확장자인 경우에만 이동
    if filename.endswith(".txt"):
        try:
            shutil.move(source_path, target_path)
            print(f"'{filename}' 파일이 '{target_dir}' 폴더로 이동되었습니다.")
        except Exception as e:
            print(f"'{filename}' 파일 이동 중 오류 발생: {e}")