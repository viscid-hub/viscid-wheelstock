set PATH=%MINGW_DIR%;%PY_DIR%;%PY_DIR%\Scripts;%PATH%
set PATH=%PATH:C:\Program Files\Git\usr\bin;=%
set FC=%MINGW_DIR%\gfortran
set F90=%MINGW_DIR%\gfortran
set F95=%MINGW_DIR%\gfortran

echo where link.exe
where link.exe
echo where gfortran.exe
where gfortran.exe

python numpy_version.py > _npy_version.txt
set /p npy_version=<_npy_version.txt
pip install numpy==%npy_version%

set CIBW_BUILD_VERBOSITY=3
