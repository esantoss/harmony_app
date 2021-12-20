import unittest
from harmony_app import HarmonyApp

class HarmonyAppTester(unittest.TestCase):

  def test_major_third(self):
    input = { "scale": "Major", "key": "A", "interval": "Major Third", "notes": ["D", "E", "F#"] }
    harmony_notes = HarmonyApp().calculate_harmony_notes(input)
    self.assertEqual(harmony_notes, ['F#', 'G#', 'A'])

  def test_perfect_fifth(self):
    input = { "scale": "Major", "key": "A", "interval": "Perfect Fifth", "notes": ["B", "C#", "D"] }
    harmony_notes = HarmonyApp().calculate_harmony_notes(input)
    self.assertEqual(harmony_notes, ['F#', 'G#', 'A'])

  def test_major_third_again(self):
    input = {"scale": "Major", "key": "A", "interval": "Major Third", "notes": ["C#", "D", "E"] }
    harmony_notes = HarmonyApp().calculate_harmony_notes(input)
    self.assertEqual(harmony_notes, ['E', 'F#', 'G#'])

if __name__ == '__main__':
  unittest.main()