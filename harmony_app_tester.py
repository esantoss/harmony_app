import unittest
from harmony_app import HarmonyApp

class HarmonyAppTester(unittest.TestCase):

  def test_major_third_defsharp(self):
    input = { "scale": "Major", "key": "A", "interval": "Major Third", "notes": ["D", "E", "F#"] }
    harmony_notes = HarmonyApp().calculate_harmony_notes(input)
    self.assertEqual(harmony_notes, ['F#', 'G#', 'A'])

  def test_perfect_fifth_bcsharpd(self):
    input = { "scale": "Major", "key": "A", "interval": "Perfect Fifth", "notes": ["B", "C#", "D"] }
    harmony_notes = HarmonyApp().calculate_harmony_notes(input)
    self.assertEqual(harmony_notes, ['F#', 'G#', 'A'])

  def test_major_third_csharpde(self):
    input = {"scale": "Major", "key": "A", "interval": "Major Third", "notes": ["C#", "D", "E"] }
    harmony_notes = HarmonyApp().calculate_harmony_notes(input)
    self.assertEqual(harmony_notes, ['E', 'F#', 'G#'])

  def test_major_third_fsharpgsharpa(self):
    input = {"scale": "Major", "key": "A", "interval": "Major Third", "notes": ["F#", "G#", "A"] }
    harmony_notes = HarmonyApp().calculate_harmony_notes(input)
    self.assertEqual(harmony_notes, ['A', 'B', 'C#'])

  def test_perfect_fourth_fsharpgsharpa(self):
    input = {"scale": "Major", "key": "A", "interval": "Perfect Fourth", "notes": ["F#", "G#", "A"] }
    harmony_notes = HarmonyApp().calculate_harmony_notes(input)
    self.assertEqual(harmony_notes, ['B', 'C#', 'D'])

  def test_perfect_fifth_fsharpgsharpa(self):
    input = {"scale": "Major", "key": "A", "interval": "Perfect Fifth", "notes": ["F#", "G#", "A"] }
    harmony_notes = HarmonyApp().calculate_harmony_notes(input)
    self.assertEqual(harmony_notes, ['C#', 'D', 'E'])

  def test_major_sixth_fsharpgsharpa(self):
    input = {"scale": "Major", "key": "A", "interval": "Major Sixth", "notes": ["F#", "G#", "A"] }
    harmony_notes = HarmonyApp().calculate_harmony_notes(input)
    self.assertEqual(harmony_notes, ['D', 'E', 'F#'])

if __name__ == '__main__':
  unittest.main()