import json
import sys
import os

#Version 0.1 by XMTech
def convert_nn_to_vcsp(nn_file_path, vcsp_file_path=None):
    with open(nn_file_path, 'r', encoding='utf-8') as nn_file:
        lines = nn_file.readlines()

    bpm = float(lines[0].split()[0])
    num_notes = int(lines[1])
    notes = []
    for i in range(2, num_notes + 2):
        line = lines[i].split()
        note = {
            "lyrics": line[0],
            "phonemes": {},
            "start": int(line[2]) * 100/16,
            "end": (int(line[2]) + int(line[3])) * 100/16,
            "pitch": 23-int(line[4])
        }
        notes.append(note)

    vcsp = {
        "vcsp_version": 4,
        "project_name": "Untitled Project",
        "base_bpm": bpm,
        "changes_bpm": [],
        "beat_per_bar": 4,
        "beat_unit": 4,
        "tracks": [
            {
                "track_name": "Test",
                "track_type": "synth",
                "mute": False,
                "solo": False,
                "voice": {
                    "singer": "Norelln Lite",
                    "singerversion": "v4.0_3",
                    "default_language": "chinese_mandarin",
                    "default_mult_speakers_settings": {
                        "default": 100
                    }
                },
                "track_default_settings": {
                    "volume": 0,
                    "channel": 0,
                    "gender": 0,
                    "power": 0,
                    "breath": 0
                },
                "notes": notes,
                "curves": {
                    "pitch": [],
                    "dynamic": [],
                    "gender": [],
                    "power": [],
                    "breath": []
                }
            }
        ]
    }

    if vcsp_file_path is None:
        vcsp_file_path = os.path.splitext(nn_file_path)[0] + '.vcsp'
    with open(vcsp_file_path, 'w') as vcsp_file:
        json.dump(vcsp, vcsp_file, indent=4)

if __name__ == '__main__':
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python", sys.argv[0], "<input.nn> [<output.vcsp>]")
    else:
        nn_file_path = sys.argv[1]
        if len(sys.argv) == 3:
            vcsp_file_path = sys.argv[2]
        else:
            vcsp_file_path = None
        convert_nn_to_vcsp(nn_file_path, vcsp_file_path)