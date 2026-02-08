import os

input_file = 'Assets/DunkelBlau Weapons Pack ExportVersion.obj'
output_dir = 'Assets'

def split_obj():
    with open(input_file, 'r') as f:
        lines = f.readlines()

    header_lines = [] # v, vt, vn, mtllib, usemtl
    objects = {}
    current_object = None

    for line in lines:
        if line.startswith('v ') or line.startswith('vt ') or line.startswith('vn ') or line.startswith('mtllib '):
            header_lines.append(line)
        elif line.startswith('o '):
            current_object = line.strip().split()[1]
            if current_object not in objects:
                objects[current_object] = []
        elif line.startswith('f ') or line.startswith('usemtl ') or line.startswith('s '):
            if current_object:
                objects[current_object].append(line)
        # Ignore comments or empty lines for now or add to header?
        # Better to add unknown lines to current object if it exists, or header if not.

    # Write files
    created_files = []
    for obj_name, obj_lines in objects.items():
        # Clean filename
        safe_name = "".join([c for c in obj_name if c.isalpha() or c.isdigit() or c=='_']).strip()
        out_name = f"{output_dir}/{safe_name}.obj"
        
        with open(out_name, 'w') as f:
            f.writelines(header_lines)
            f.write(f"o {safe_name}\n")
            f.writelines(obj_lines)
        
        created_files.append(safe_name)
        print(f"Created: {out_name}")

    return created_files

if __name__ == '__main__':
    files = split_obj()
    print("Files created:", files)