/* Auto-generated HSI Driver Implementation for UART0 */
#include "uart0_driver.h"
#include <stdint.h>

/* Helper macro for memory-mapped I/O register access */
#define HW_REG_WRITE32(addr, val) (*((volatile uint32_t *)(addr)) = (val))
#define HW_REG_READ32(addr)        (*((volatile uint32_t *)(addr)))

void uart0_init(void) {
    /* Initialize base registers */
    /* Enable TXEN in CTRL */
    uint32_t reg_val = HW_REG_READ32(UART0_CTRL_ADDR);
    reg_val |= UART0_CTRL_TXEN_MASK;
    HW_REG_WRITE32(UART0_CTRL_ADDR, reg_val);
    /* Enable ENABLE in CTRL */
    uint32_t reg_val = HW_REG_READ32(UART0_CTRL_ADDR);
    reg_val |= UART0_CTRL_ENABLE_MASK;
    HW_REG_WRITE32(UART0_CTRL_ADDR, reg_val);
}
