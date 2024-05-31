from pathlib import Path

from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup

emoji_translator = Pybind11Extension(
    'emojiTranslator_pythonBinding',
    [str(fname) for fname in Path('src').glob('*.cpp')]
)

setup(
    name='emojiTranslator',
    version=0.1,
    author='Rabeeqa',
    author_email='rabeeqatahir76@email.com',
    description='Python binding project for emoji translator',
    ext_modules=[emoji_translator],
    cmdclass={"build_ext": build_ext},
)
