import pathlib
import subprocess
import unittest


class NativeWorkflowBehaviorTests(unittest.TestCase):
    def test_native_behavior_script(self):
        script = pathlib.Path(__file__).with_suffix('.sh')
        subprocess.run(['bash', str(script)], check=True)


if __name__ == '__main__':
    unittest.main()
