import json

class HarmonyApp:

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

  def __init__(self):
    pass

  def get_index(self, curr_index):
    if curr_index + 1 >= len(self.scale):
      curr_index = 0
    else:
      curr_index += 1
    return curr_index

  def get_interval_start(self, first_note, interval_offset):
    start_index = self.scale.index(first_note)
    curr_index = start_index
    for i in range(interval_offset):
      curr_index = self.get_index(curr_index)
    return curr_index

  def get_scale_notes(self, first_note, interval_start_index, total_notes):
    scale_notes = []
    curr_index = interval_start_index
    for i in range(total_notes):
      scale_notes.append(self.scale[curr_index])
      curr_index = self.get_index(curr_index)
    return scale_notes

  def calculate_harmony_notes(self, input_json):
    harmony_notes = None
    interval_offset = self.intervals[input_json['interval']]
    input_notes = input_json['notes']
    scale_type = input_json['scale']
    total_notes = len(input_notes)
    first_note = input_notes[0]
    harmony_notes = None
    interval_start_index = self.get_interval_start(first_note, interval_offset)
    harmony_notes = self.get_scale_notes(first_note, interval_start_index, total_notes)
    return harmony_notes

  def print_notes(self, input_notes, harmony_notes):
    print(f"Riff Notes: {input_notes}")
    print(f"Harmony Notes: {harmony_notes}")

  def main(self):
    with open("input.json", "r") as input:
      input_data = json.loads(input.read())
    for phrase in input_data['phrases']:
      harmony_notes = self.calculate_harmony_notes(phrase)
      self.print_notes(phrase['notes'], harmony_notes)

if __name__ == '__main__':
  HarmonyApp().main()
