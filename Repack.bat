@echo off
rem 進入 Kuroko 資料夾
cd Kuroko

rem 執行程式
echo.
echo [INFO] Running Kuroko.exe...
Kuroko.exe -v Japan -m Dump

rem 回到上一層目錄
cd ..

rem 檢查 output 資料夾是否存在
if not exist "output" (
    echo [ERROR] 'output' directory not found. The program might have failed.
    pause
    exit /b
)

echo.
echo [INFO] Copying dumped files...

rem 使用 xcopy 複製整個資料夾和其內容
rem /E - 複製所有子目錄 (包含空的)
rem /I - 如果目標不存在，則假設目標是資料夾
rem /Y - 覆寫已存在的檔案而不提示
xcopy "output\Excel_Dumped" "Kuroko\Resources\Japan\Dumped\Excel_Dumped\" /E /I /Y
xcopy "output\ExcelDB_Dumped" "Kuroko\Resources\Japan\Dumped\ExcelDB_Dumped\" /E /I /Y

cd Kuroko
Kuroko.exe -v Japan -m Repack
echo.
echo [SUCCESS] Script finished.
pause