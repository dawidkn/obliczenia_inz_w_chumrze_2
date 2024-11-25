import subprocess
import csv
import time
from concurrent.futures import ThreadPoolExecutor

def run_python():
    """Uruchamia program w Pythonie i zwraca wynik"""
    start_time = time.time()
    subprocess.run(["python", "prime_numbers_python.py"])
    elapsed_time = time.time() - start_time

    with open("python_output.txt", "r") as file:
        result = file.read().strip()

    return {"program": "Python", "calculation": result, "time": elapsed_time}

def run_cpp():
    """Uruchamia program w C++ i zwraca wynik"""
    start_time = time.time()
    subprocess.run(["./prime_numbers_c"])
    elapsed_time = time.time() - start_time

    with open("cpp_output.txt", "r") as file:
        result = file.read().strip()

    return {"program": "C++", "calculation": result, "time": elapsed_time}

def save_results_to_csv(results, filename="results.csv"):
    """Zapisuje wyniki do pliku CSV"""
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        # Nagłówki
        writer.writerow(["Program", "Calculation", "Execution Time (s)"])
        # Dane
        for result in results:
            writer.writerow([result["program"], result["calculation"], f"{result['time']:.2f}"])

def main():
    with ThreadPoolExecutor(max_workers=2) as executor:
        # Uruchomienie obu programów jednocześnie
        futures = [
            executor.submit(run_python),
            executor.submit(run_cpp),
        ]
        # Pobranie wyników
        results = [future.result() for future in futures]

    # Zapisanie wyników do CSV
    save_results_to_csv(results)

    print("Wyniki zapisane do pliku 'results.csv'.")

if __name__ == "__main__":
    main()
