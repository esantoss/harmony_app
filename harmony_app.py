import json
with open("input.json", "r") as input:
  input_data = json.loads(input.read())

def get_scale_notes(start, total_notes):
  scale_notes = []
  start_index = scale.index(start)
  curr_index = start_index
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
  'Minor Second': 1,
  'Major Second': 2,
  'Minor Third': 3,
  'Major Third': 4, 
  'Perfect Fourth': 5,
  'Tri-Tone': 6,
  'Perfect Fifth': 7,
  'Minor Sixth': 8,
  'Major Sixth': 9,
  'Minor Seventh': 10,
  'Major Seventh': 11,
  'Perfect Octave': 12
}

interval_offset = intervals[input_data['Interval']]
input_notes = input_data['Notes']
total_notes = len(input_notes)

first_note = input_notes[0]
scale_note = notes[notes.index(first_note) + interval_offset]
harmony_notes = get_scale_notes(scale_note, total_notes)

print(f"Riff Notes: {input_notes}")
print(f"Harmony Notes: {harmony_notes}")