import pathlib
import setuptools

HERE = pathlib.Path(__file__).parent

README = (HERE/"README.md").read_text()

setuptools.setup(
    name="google-photos-takeout-helper",
    version="1.0.0",
    description="Script that helps you export your photos from Google Photos to one, nice folder",
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/TheLastGimbus/GooglePhotosTakeoutHelper/',
    author='TheLastGimbus',
    author_email='mateusz.soszynski@tuta.io',
    license='Apache',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        'License :: OSI Approved :: Apache Software License',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Multimedia :: Graphics'
    ],
    install_requires=(HERE/'requirements.txt').read_text().split('\n'),
    entry_points={
        'console_scripts': [
            'google-photos-takeout-helper=google_photos_takeout_helper.__main__:main'
        ]
    }
)
