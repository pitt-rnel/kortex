ECHO OFF

set build_type="release" 
set build_folder=build-msvc-%build_type%
set msvc_runtime="static" 

mkdir %build_folder%
: Give write permission to everyone in build folder
ICACLS %build_folder% /grant Everyone:F /t

SET /A errno=0
cmake -S ./ -B ./%build_folder% -G "Visual Studio 16 2019" -DUSE_CONAN=OFF -DDOWNLOAD_API=OFF -DCMAKE_BUILD_TYPE=release -DMSVC_RUNTIME=static
SET /A errno=%ERRORLEVEL% 
popd

EXIT /B %errno%

