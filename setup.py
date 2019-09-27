from distutils.core import setup

if __name__== '__main__':
    setup(include_package_data=True,
          description='Functions for studying interactions with neural networks',
          url='https://github.com/kundajelab/mfinkels_work',
          version='0.1.0.0',
          packages=['interactiondetection'],
          setup_requires=[],
          install_requires=['numpy>=1.9',
                            'scikit-learn>=0.20.0',
                            'scipy>=1.1.0'],
          scripts=[],
          name='interactiondetection')
