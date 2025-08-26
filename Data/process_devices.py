import os
import re

def extract_device_info(input_folder, output_folder):
    """
    Scans all .md files in an input folder, extracts device info blocks,
    and saves each block to a separate .txt file in the output folder.

    A device info block is identified by a line starting with '### 📘', '### ', or '📘 **'.
    """
    # Create the output directory if it doesn't already exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"✅ Created output folder: {output_folder}")

    # --- UPDATED PATTERN ---
    # Regex to find the start of a device info block.
    # It now looks for lines starting with '### 📘', '### ', OR '📘 **'.
    # The order is important: '### 📘' is checked before the more general '### '
    # to ensure correct matching.
    split_pattern = r'^(?=(?:### 📘|### |📘 \*\*))'

    # Process each file in the input directory
    for filename in os.listdir(input_folder):
        # We also check for and skip the main documentation heading file if it exists
        if filename.endswith('.md'):
            md_file_path = os.path.join(input_folder, filename)
            print(f"\nProcessing file: {filename}...")

            with open(md_file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Split the file content into blocks based on the pattern
            # The re.MULTILINE flag allows '^' to match the start of each line
            blocks = re.split(split_pattern, content, flags=re.MULTILINE)

            for block in blocks:
                # Skip any empty blocks or headers that are not device info
                block_content = block.strip()
                if not block_content or block_content.startswith("## UEFN Verse Device Documentation"):
                    continue

                # The first line of the block will be used for the filename
                first_line = block_content.split('\n')[0]

                # --- UPDATED FILENAME CLEANING ---
                # 1. Remove the markdown markers ('### 📘', '### ', '📘 **')
                clean_name = re.sub(r'^(?:### 📘|### |📘 \*\*)', '', first_line).strip()
                # 2. Remove backticks and asterisks
                clean_name = clean_name.replace('`', '').replace('*', '')
                # 3. Replace spaces and multiple hyphens with a single underscore
                clean_name = re.sub(r'[\s-]+', '_', clean_name)
                # 4. Remove any other characters that are not safe for filenames
                clean_name = re.sub(r'[^\w_]', '', clean_name)

                if not clean_name:
                    print("⚠️  Could not determine a valid filename for a block. Skipping.")
                    continue

                # Define the full path for the new .txt file
                output_filename = f"{clean_name}.txt"
                output_filepath = os.path.join(output_folder, output_filename)

                # Write the entire block content to the new .txt file
                with open(output_filepath, 'w', encoding='utf-8') as out_file:
                    out_file.write(block_content)

                print(f"  -> Saved device info to: {output_filename}")

    print("\n🎉 All files processed successfully!")


# --- HOW TO USE ---
if __name__ == "__main__":
    # 1. Set the path to the folder containing your .md files
    #    Example for Windows: 'C:\\Users\\YourUser\\Documents\\MyMDFiles'
    #    Example for macOS/Linux: '/home/user/documents/my_md_files'
    md_files_folder = 'Devices\input'

    # 2. Set the path where you want to save the new .txt files
    #    The script will create this folder if it doesn't exist.
    output_txt_folder = 'Devices\output'

    # Run the function with your specified paths
    extract_device_info(md_files_folder, output_txt_folder)