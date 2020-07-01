import json
import os
import sys
import unittest

from check_state import get_response
from compress_txt import gzip_write, gzip_read


class GetJSONTest(unittest.TestCase):
    """Testy dla funkcji get_response()"""

    def setUp(self):
        x = {
            "name": "John",
            "age": 30,
            "city": "New York"
        }
        with open('test.json', 'w') as outfile:
            json.dump(x, outfile)
        basedir = os.path.dirname(os.path.abspath('test.json'))
        self.local_file = 'file:///' + basedir.replace('\\', '/') + '/test.json'

    def test_get_response_localy(self):
        self.assertIsNone(get_response(url=self.local_file))

    def test_get_response_github(self):
        a = get_response(url='https://api.github.com/users/lioheart')
        b = 'Jawor'
        self.assertEqual(a['location'], b)

    def test_get_response_fail_url(self):
        a = get_response(url='https://api.github.co/users/lioheart')
        self.assertFalse(a)

    def tearDown(self) -> None:
        os.remove('test.json')


class CompressTest(unittest.TestCase):
    def setUp(self) -> None:
        self.original_data = '''
            [32] Sed ut perspiciatis, unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, 
            totam rem aperiam eaque ipsa, quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt, 
            explicabo. Nemo enim ipsam voluptatem, quia voluptas sit, aspernatur aut odit aut fugit, sed quia 
            consequuntur magni dolores eos, qui ratione voluptatem sequi nesciunt, neque porro quisquam est, qui 
            dolorem ipsum, quia dolor sit, amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora 
            incidunt, ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum 
            exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem 
            vel eum iure reprehenderit, qui in ea voluptate velit esse, quam nihil molestiae consequatur, vel illum, 
            qui dolorem eum fugiat, quo voluptas nulla pariatur?
            [33] At vero eos et accusamus et iusto odio dignissimos ducimus, qui blanditiis praesentium voluptatum 
            deleniti atque corrupti, quos dolores et quas molestias excepturi sint, obcaecati cupiditate non provident, 
            similique sunt in culpa, qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum 
            quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio, 
            cumque nihil impedit, quo minus id, quod maxime placeat, facere possimus, omnis voluptas assumenda est, 
            omnis dolor repellendus. Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe 
            eveniet, ut et voluptates repudiandae sint et molestiae non recusandae. Itaque earum rerum hic tenetur a 
            sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus 
            asperiores repellat.
        '''

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_write_and_read_lorem_w(self):
        gzip_write(self.original_data)
        x = gzip_read()
        self.assertEqual(x, self.original_data)
        self.assertEqual(os.stat('example.txt.gz').st_size, 933)

    @unittest.skipUnless(sys.platform.startswith("linux"), "requires Linux")
    def test_write_and_read_lorem_l(self):
        gzip_write(self.original_data)
        x = gzip_read()
        self.assertEqual(x, self.original_data)
        self.assertEqual(os.stat('example.txt.gz').st_size, 930)

    def test_read_polish(self):
        gzip_write()
        x = gzip_read()
        self.assertEqual(x, 'Zażółć gęślą jaźń\n')

    def test_write_and_read_filename(self):
        gzip_write(outfilename='Zażółć gęślą jaźń')
        list_dir = os.listdir()
        file = gzip_read(outfilename='Zażółć gęślą jaźń')
        self.assertIn('Zażółć gęślą jaźń', list_dir)
        self.assertEqual(file, 'Zażółć gęślą jaźń\n')

    def test_read_nonexist_file(self):
        x = gzip_read(outfilename='test.txt')
        self.assertEqual(x, 'Nie znaleziono pliku!')

    def tearDown(self) -> None:
        if 'example.txt.gz' in os.listdir():
            os.remove('example.txt.gz')
        if 'Zażółć gęślą jaźń' in os.listdir():
            os.remove('Zażółć gęślą jaźń')


if __name__ == '__main__':
    unittest.main()
