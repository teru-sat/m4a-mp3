import subprocess
from pathlib import Path

def convert_m4a_to_mp3(input_path, output_path):
    cmd = [
        "ffmpeg",
        "-loglevel", "error",      # ログ抑制（エラーのみ）
        "-i", input_path,
        "-codec:a", "libmp3lame",  # mp3 エンコーダ
        "-qscale:a", "2",          # 音質（2は高音質・ファイルサイズそこそこ）
        output_path,
    ]
    subprocess.run(cmd, check=True)




BASE_DIR = Path(__file__).resolve().parent
input_path = BASE_DIR / "m4a"/"協議意見取得.m4a"
output_path = BASE_DIR / "mp3"/"協議意見取得.mp3"

print(input_path)

# 使い方
convert_m4a_to_mp3(input_path, output_path)
