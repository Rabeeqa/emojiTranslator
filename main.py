import unittest
import emojiTranslator_pythonBinding as emtr

class TestAdd(unittest.TestCase):

  def test_football_emoji(self):
    result = emtr.emojiTrans(":football:")
    self.assertEqual(result, "\U0001F3C8")

  def test_angry_emoji(self):
    result = emtr.emojiTrans(":angry:")
    self.assertEqual(result, "\U0001F620")
    
  def test_ant_emoji(self):
    result = emtr.emojiTrans(":ant:")
    self.assertEqual(result, "\U0001F41C")

  def test_eyes_emoji(self):
    result = emtr.emojiTrans(":eyes:")
    self.assertEqual(result, "\U0001F440")
    
  def test_lips_emoji(self):
    result = emtr.emojiTrans(":lips:")
    self.assertEqual(result, "\U0001F444")
  
  def test_rose_emoji(self):
    result = emtr.emojiTrans(":rose:")
    self.assertEqual(result, "\U0001F339")
   
  def test_pizza_emoji(self):
    result = emtr.emojiTrans(":pizza:")
    self.assertEqual(result, "\U0001F355")
  
  def test_smile_emoji(self):
    result = emtr.emojiTrans(":smile:")
    self.assertEqual(result, "\U0001F604")

  def test_smirk_emoji(self):
    result = emtr.emojiTrans(":smirk:")
    self.assertEqual(result, "\U0001F60F")

  def test_tulip_emoji(self):
    result = emtr.emojiTrans(":tulip:")
    self.assertEqual(result, "\U0001F337")
    
  def test_violin_emoji(self):
    result = emtr.emojiTrans(":violin:")
    self.assertEqual(result, "\U0001F3BB")

  def test_watch_emoji(self):
    result = emtr.emojiTrans(":watch:")
    self.assertEqual(result, "\U0000231A")

  def test_ocean_emoji(self):
    result = emtr.emojiTrans(":ocean:")
    self.assertEqual(result, "\U0001F30A")

  def test_moon_emoji(self):
    result = emtr.emojiTrans(":moon:")
    self.assertEqual(result, "\U0001F314")
    
  def test_wheelchair_emoji(self):
    result = emtr.emojiTrans(":wheelchair:")
    self.assertEqual(result, "\U0000267F")

  def test_wineGlass_emoji(self):
    result = emtr.emojiTrans(":wineGlass:")
    self.assertEqual(result, "\U0001F377")

  def test_boot_emoji(self):
    result = emtr.emojiTrans(":boot:")
    self.assertEqual(result, "\U0001F462")

  def test_womens_emoji(self):
    result = emtr.emojiTrans(":womens:")
    self.assertEqual(result, "\U0001F6BA")
    
  def test_world_map_emoji(self):
    result = emtr.emojiTrans(":world_map:")
    self.assertEqual(result, "\U0001F5FA")

  def test_gift_emoji(self):
    result = emtr.emojiTrans(":gift:")
    self.assertEqual(result, "\U0001F381")
    
  def test_error(self):
    result = emtr.emojiTrans(":sun:")
    self.assertEqual(result, "Not Found!")
    
if __name__ == '__main__':
  unittest.main()
