import os
import subprocess
import ctypes
import platform

class WinOptimizer:
    def __init__(self):
        if platform.system() != "Windows":
            raise EnvironmentError("WinOptimizer is designed to run on Windows systems only.")

    def disable_startup_programs(self):
        print("Disabling unnecessary startup programs...")
        try:
            subprocess.call(['powershell', '-Command', 'Get-CimInstance Win32_StartupCommand | Remove-CimInstance'])
            print("Startup programs disabled.")
        except Exception as e:
            print(f"Failed to disable startup programs: {e}")

    def clear_temp_files(self):
        print("Clearing temporary files...")
        try:
            temp_folder = os.environ['TEMP']
            for root, dirs, files in os.walk(temp_folder):
                for file in files:
                    file_path = os.path.join(root, file)
                    os.remove(file_path)
            print("Temporary files cleared.")
        except Exception as e:
            print(f"Failed to clear temporary files: {e}")

    def adjust_visual_effects(self):
        print("Adjusting visual effects for best performance...")
        try:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, None, 0)  # SPI_SETDESKWALLPAPER
            print("Visual effects adjusted.")
        except Exception as e:
            print(f"Failed to adjust visual effects: {e}")

    def optimize(self):
        print("Starting system optimization...")
        self.disable_startup_programs()
        self.clear_temp_files()
        self.adjust_visual_effects()
        print("System optimization complete.")

if __name__ == "__main__":
    optimizer = WinOptimizer()
    optimizer.optimize()