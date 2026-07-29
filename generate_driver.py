import json

def generate_c_driver(json_filepath):
    with open(json_filepath, 'r') as f:
        data = json.load(f)

    device = data.get("device", "PERIPHERAL").upper()
    header_name = f"{device.lower()}_driver.h"

    c_lines = [
        f'/* Auto-generated HSI Driver Implementation for {device} */',
        f'#include "{header_name}"',
        '#include <stdint.h>\n',
        '/* Helper macro for memory-mapped I/O register access */',
        '#define HW_REG_WRITE32(addr, val) (*((volatile uint32_t *)(addr)) = (val))',
        '#define HW_REG_READ32(addr)        (*((volatile uint32_t *)(addr)))\n'
    ]

    # Generate initialization function
    c_lines.append(f'void {device.lower()}_init(void) {{')
    c_lines.append(f'    /* Initialize base registers */')
    
    for reg in data.get("registers", []):
        reg_name = reg["name"].upper()
        for field in reg.get("fields", []):
            field_name = field["name"].upper()
            c_lines.append(
                f'    /* Enable {field_name} in {reg_name} */\n'
                f'    uint32_t reg_val = HW_REG_READ32({device}_{reg_name}_ADDR);\n'
                f'    reg_val |= {device}_{reg_name}_{field_name}_MASK;\n'
                f'    HW_REG_WRITE32({device}_{reg_name}_ADDR, reg_val);'
            )

    c_lines.append('}\n')

    return "\n".join(c_lines)

if __name__ == "__main__":
    driver_code = generate_c_driver("register_map.json")
    print(driver_code)
    
    with open("uart0_driver.c", "w") as f:
        f.write(driver_code)
    print("\n[SUCCESS] Generated 'uart0_driver.c' successfully!")