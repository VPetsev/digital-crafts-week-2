import unittest
import main
import logic
import view
import tables


class PoolTableTests(unittest.TestCase):

    def test_if_tables_load_from_json_file(self):
        

    def test_is_table_object_created(self):
        new_table = Table()
        new_table.assign_table_num(2)
        self.assertEqual(1, new_table.table_number)



unittest.main()


# create a certain amount of table objects (12)
# populate the pool hall instance with table objects, 
# making a pool hall object

# all tables are occupied
# how would the application revive itself from the crash
