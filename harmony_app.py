import json
def get_interval_start(first_note, interval_offset):
  start_index = scale.index(first_note)
  curr_index = start_index
  for i in range(interval_offset):

    if curr_index + 1 >= len(scale):
      curr_index = 0
    else:
      curr_index += 1
  return curr_index

def get_scale_notes(first_note, interval_start_index, total_notes):
  scale_notes = []

  curr_index = interval_start_index
  for i in range(total_notes):
    scale_notes.append(scale[curr_index])
    if curr_index + 1 >= len(scale):
      curr_index = 0
    else:
      curr_index += 1
  return scale_notes

scale = ["A", "B", "C#", "D", "E", "F#", "G#"]
notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]

intervals = {
  'Major Second': 1,
  'Major Third': 2, 
  'Perfect Fourth': 3,
  'Perfect Fifth': 4,
  'Major Sixth': 5,
  'Major Seventh': 6
}

with open("input.json", "r") as input:
  input_data = json.loads(input.read())

phrases = input_data['phrases']
for phrase in phrases:
  try:
    interval_offset = intervals[phrase['interval']]
    input_notes = phrase['notes']
    scale_type = phrase['scale']
    total_notes = len(input_notes)
    first_note = input_notes[0]
    interval_start_index = get_interval_start(first_note, interval_offset)
    harmony_notes = get_scale_notes(first_note, interval_start_index, total_notes)
  except Exception:
    print(f"ERROR!! with input -> {input_notes}")

  print(f"Riff Notes: {input_notes}")
  print(f"Harmony Notes: {harmony_notes}")
