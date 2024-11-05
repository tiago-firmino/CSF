import hashlib
import zipfile

def read_lines_from_file(filename):
    with open(filename, 'r') as f:
        return f.read().splitlines()

def generate_hash(seed, timestamp):
    return hashlib.sha256(str(seed + timestamp).encode("utf-8")).hexdigest() 

def attempt_unzip(zip_filename, password):
    try:
        target_folder = "backup_1727368201"
        with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
            zip_ref.extractall(target_folder, pwd=password.encode('utf-8'))
            print(f"Successfully extracted {zip_filename}")
            return True
    except RuntimeError as e:
        return False
    except zipfile.BadZipFile:
        return False
    except Exception as e:
        return False

def main(seeds_file, zip_path):
    seeds = read_lines_from_file(seeds_file)

    for seed in seeds:
        timestamp = "1727368201"
        password_hash = generate_hash(seed, timestamp)

        if attempt_unzip(zip_path, password_hash):
            print(f"Unzipped '{zip_path}' successfully!")
        else:
            continue;

if __name__ == "__main__":
    seeds_file = 'all_seeds.txt'  # Input seed file
    zip_path = 'backup_1727368201.zip'  # Zip file path

    main(seeds_file, zip_path)