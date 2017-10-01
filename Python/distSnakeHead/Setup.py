import cx_Freeze

executables = [cx_Freeze.Executable("SnakeGame.py")]

cx_Freeze.setup(
    name='Slithering Snake',
    options={"build_exe":{"packages":['pygame'], "include_files":['SnakeHead.png', 'Apple.png', 'Highscore.dat', 'Icon.png']}},

    description = "Slithering snake: eat apples and grow longer!",
    executables = executables

)