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

  def main(self):
    with open("input.json", "r") as input:
      input_data = json.loads(input.read())

    phrases = input_data['phrases']
    for phrase in phrases:
      interval_offset = self.intervals[phrase['interval']]
      input_notes = phrase['notes']
      scale_type = phrase['scale']
      total_notes = len(input_notes)
      first_note = input_notes[0]
      harmony_notes = None
      try:
        interval_start_index = self.get_interval_start(first_note, interval_offset)
        harmony_notes = self.get_scale_notes(first_note, interval_start_index, total_notes)
      except Exception as e:
        print(f"ERROR!! with input -> {input_notes}")
        print(f"ERROR is: {e}")

      print(f"Riff Notes: {input_notes}")
      print(f"Harmony Notes: {harmony_notes}")

if __name__ == '__main__':
  HarmonyApp().main()
