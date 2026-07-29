import json

def generate_c_header(json_filepath):
    # 1. Load the JSON Register Map
    with open(json_filepath, 'r') as f:
        data = json.load(f)

    device_name = data.get("device", "PERIPHERAL").upper()
    base_addr = data.get("base_address", "0x00000000")

    header_lines = []
    
    # 2. Add Header Guards and Base Address
    header_lines.append(f"/* Auto-generated Hardware-Software Interface Header for {device_name} */")
    header_lines.append(f"#ifndef {device_name}_H")
    header_lines.append(f"#define {device_name}_H\n")
    header_lines.append("#include <stdint.h>\n")
    header_lines.append(f"/* Base Address */")
    header_lines.append(f"#define {device_name}_BASE_ADDR ({base_addr}UL)\n")

    # 3. Parse Registers and Bitfields
    for reg in data.get("registers", []):
        reg_name = reg["name"].upper()
        offset = reg["offset"]
        desc = reg.get("description", "Register")
        
        header_lines.append(f"/* --- {reg_name}: {desc} --- */")
        header_lines.append(f"#define {device_name}_{reg_name}_OFFSET ({offset})")
        header_lines.append(f"#define {device_name}_{reg_name}_ADDR ({device_name}_BASE_ADDR + {device_name}_{reg_name}_OFFSET)\n")

        # Calculate bit position and masks for each field
        for field in reg.get("fields", []):
            field_name = field["name"].upper()
            bit_offset = field["bit_offset"]
            bit_width = field["bit_width"]
            
            # Compute bitmask
            mask_val = ((1 << bit_width) - 1) << bit_offset
            
            header_lines.append(f"#define {device_name}_{reg_name}_{field_name}_POS ({bit_offset})")
            header_lines.append(f"#define {device_name}_{reg_name}_{field_name}_MASK (0x{mask_val:08X}UL)")
        
        header_lines.append("")  # Blank line separator

    header_lines.append(f"#endif /* {device_name}_H */")
    
    return "\n".join(header_lines)


if __name__ == "__main__":
    c_header_code = generate_c_header("register_map.json")
    print(c_header_code)
    
    # Optionally save to disk
    with open("uart0_driver.h", "w") as f:
        f.write(c_header_code)
    print("\n[SUCCESS] Generated 'uart0_driver.h' successfully!")