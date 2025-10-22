cd Kuroko

Kuroko.exe dump Japan 
Kuroko.exe dump Global

cd ..
xcopy "Kuroko\Resources\Japan\Dumped\Excel_Dumped\" "JP_excels\Excel_Dumped" /E /I /Y
xcopy "Kuroko\Resources\Japan\Dumped\ExcelDB_Dumped\" "JP_excels\ExcelDB_Dumped" /E /I /Y
xcopy "Kuroko\Resources\Global\Dumped\Excel_Dumped\" "TW_excels\Excel_Dumped" /E /I /Y
xcopy "Kuroko\Resources\Global\Dumped\ExcelDB_Dumped\" "TW_excels\ExcelDB_Dumped" /E /I /Y
py dumper.py
py patcher.py
