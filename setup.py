

from distutils.core import setup
import py2exe

setup(console=['finda.py'],
      packages=['finda'],

      # single executable
      options={'py2exe': {'bundle_files': 1}},
      zipfile=None,
      )

if False:
    from cx_Freeze import setup, Executable

    product_family = 'abel'
    base = "Console"

    bdist_msi_options = {
        'upgrade_code': '{C67E0B0A-F8FF-42B2-9717-E12442A513AC}',
        'add_to_path': True,
        'initial_target_dir': r'[ProgramFilesFolder]\%s' % (product_family),
        }

    setup(
        name="finda",
        version="0.0",
        author='James Abel',
        author_email='j@abel.co',
        url='www.abel.co',
        license='LICENSE',
        description="finder program",
        long_description="searches 1 or more paths for 1 or more strings",
        py_modules=['*'],
        platforms=['windows'],
        options={'bdist_msi': bdist_msi_options},
        executables=[Executable("finda.py", base=base)]
    )