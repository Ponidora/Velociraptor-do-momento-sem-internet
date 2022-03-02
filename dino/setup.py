import cx_Freeze

executables = [cx_Freeze.Executable('dino.py')]

cx_Freeze.setup(
    name="Jogo do pior dinossauro do mundo",
    options={'build_exe':{'packages':['pygame'],
    'include_files':['sons','sprites dino']
    
    }},

)