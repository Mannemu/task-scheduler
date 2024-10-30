#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys

# Add the path to the module you want to import
sys.path.append(r"C:\Users\Manna\OneDrive\Documents\ec_utbildning\python\csv_viewer (1)\csv_viewer_without_data_and_filter 1")

import unittest
from main_script import process_data



# In[ ]:


class TestMainScript(unittest.TestCase):
    def test_process_data(self):
        try:
            data = process_data()
            self.assertFalse(data.empty, "The data should not be empty.")
        except Exception as e:
            self.fail(f"process_data() raised an exception: {e}")


# In[ ]:


if __name__ == '__main__':
    unittest.main()


# In[ ]:





# In[ ]:




